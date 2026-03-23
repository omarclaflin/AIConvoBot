"""
Conversational Evaluation API
Evaluates user beliefs, emotional states, goals, and topics from conversation data.
"""

from flask import Flask, request, jsonify
from transformers import pipeline
import anthropic
import os
from collections import Counter
from datetime import datetime
import numpy as np
import ssl
import urllib.request

# TEMPORARY: Disable SSL verification for HuggingFace downloads
# Only needed if behind corporate proxy/firewall with SSL interception
# WARNING: This is insecure and should only be used for development
import warnings
import httpx
warnings.filterwarnings('ignore', message='Unverified HTTPS request')

# Monkey patch httpx to disable SSL verification
original_client = httpx.Client
class InsecureClient(httpx.Client):
    def __init__(self, *args, **kwargs):
        kwargs['verify'] = False
        super().__init__(*args, **kwargs)

httpx.Client = InsecureClient

# Also patch for async client
original_async_client = httpx.AsyncClient
class InsecureAsyncClient(httpx.AsyncClient):
    def __init__(self, *args, **kwargs):
        kwargs['verify'] = False
        super().__init__(*args, **kwargs)

httpx.AsyncClient = InsecureAsyncClient

ssl._create_default_https_context = ssl._create_unverified_context

app = Flask(__name__)

# Initialize models (lazy loading to avoid startup issues)
sentiment_analyzer = None
topic_classifier = None
anthropic_client = None

def get_sentiment_analyzer():
    """Lazy load sentiment analyzer."""
    global sentiment_analyzer
    if sentiment_analyzer is None:
        sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    return sentiment_analyzer

def get_topic_classifier():
    """Lazy load topic classifier."""
    global topic_classifier
    if topic_classifier is None:
        topic_classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    return topic_classifier

def get_anthropic_client():
    """Lazy load Anthropic client."""
    global anthropic_client
    if anthropic_client is None:
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable not set")
        anthropic_client = anthropic.Anthropic(api_key=api_key)
    return anthropic_client

# Topic categories for zero-shot classification
TOPIC_CATEGORIES = [
    "health", "fitness", "relationships", "family", "work", "stress",
    "anxiety", "loneliness", "hobbies", "technology", "mental_health"
]


def extract_user_messages(conversation):
    """Filter out StoryBot messages, return only user messages."""
    return [
        msg for msg in conversation.get("messages_list", [])
        if msg.get("ref_user_id") != 1
    ]


def analyze_sentiment(messages):
    """Run sentiment analysis on user messages."""
    analyzer = get_sentiment_analyzer()
    results = []
    for msg in messages:
        text = msg.get("message", "")
        if text:
            sentiment = analyzer(text[:512])[0]  # Truncate for model limits
            results.append({
                "label": sentiment["label"],
                "score": sentiment["score"],
                "timestamp": msg.get("transaction_datetime_utc")
            })
    return results


def extract_topics(messages):
    """Extract topics from user messages using zero-shot classification."""
    classifier = get_topic_classifier()
    topics = []
    for msg in messages:
        text = msg.get("message", "")
        if text:
            result = classifier(text[:512], TOPIC_CATEGORIES, multi_label=True)
            # Keep topics with score > 0.5
            msg_topics = [
                label for label, score in zip(result["labels"], result["scores"])
                if score > 0.5
            ]
            topics.append({
                "topics": msg_topics[:3],  # Top 3 topics
                "timestamp": msg.get("transaction_datetime_utc")
            })
    return topics


def extract_self_efficacy_per_message(conversation):
    """Use Anthropic API to extract self-efficacy per message."""
    user_messages = extract_user_messages(conversation)

    if not user_messages:
        return []

    results = []
    client = get_anthropic_client()

    for msg in user_messages:
        text = msg.get('message', '')
        if not text:
            continue

        prompt = f"""Rate the user's self-efficacy (their confidence and belief in their ability to achieve their goals) based on this message.

Message: {text}

Respond with only one word: Low, Medium, or High"""

        try:
            message = client.messages.create(
                model="claude-3-haiku-20240307",
                max_tokens=50,
                messages=[{"role": "user", "content": prompt}]
            )

            response = message.content[0].text.strip()
            if response in ["Low", "Medium", "High"]:
                results.append({
                    "self_efficacy": response,
                    "timestamp": msg.get("transaction_datetime_utc")
                })
        except Exception as e:
            continue

    return results


def extract_goals(conversation):
    """Use Anthropic API to extract goals from full conversation."""
    user_messages = extract_user_messages(conversation)

    convo_text = "\n".join([
        f"[{msg.get('transaction_datetime_utc')}] User: {msg.get('message')}"
        for msg in user_messages
    ])

    if not convo_text:
        return []

    prompt = f"""Extract all goals, intentions, and aspirations mentioned by the user in this conversation. Include both explicit statements (e.g., "I want to run a 5K") and implicit intentions (e.g., "I need more balance" means a goal of achieving work-life balance).

Conversation:
{convo_text}

List each goal on a separate line with no preamble. If no goals are mentioned, respond with only: None"""

    try:
        client = get_anthropic_client()
        message = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=300,
            messages=[{"role": "user", "content": prompt}]
        )

        response_text = message.content[0].text.strip()

        if response_text.lower() == "none":
            return []

        # Parse goals and strip preamble
        lines = response_text.split("\n")
        goals = []
        for line in lines:
            line = line.strip()
            # Skip preamble lines
            if not line or ":" in line or line.lower().startswith("here"):
                continue
            # Remove list markers
            line = line.lstrip("0123456789.-) ")
            if line:
                goals.append(line)
        return goals

    except Exception as e:
        return []


def aggregate_scores(data, key):
    """Compute aggregates for a list of scored items."""
    if not data:
        return None

    values = []
    for item in data:
        if isinstance(item, dict) and key in item:
            val = item[key]
            if isinstance(val, (int, float)):
                values.append(val)

    if not values:
        return None

    return {
        "min": min(values),
        "max": max(values),
        "last": values[-1],
        "mean": np.mean(values),
        "recency_weighted_avg": np.average(values, weights=range(1, len(values) + 1))
    }


def aggregate_labels(data, key, label_to_numeric=None):
    """Compute mode and last value for categorical data."""
    if not data:
        return None

    labels = [item[key] for item in data if isinstance(item, dict) and key in item]
    if not labels:
        return None

    counter = Counter(labels)

    result = {
        "mode": counter.most_common(1)[0][0] if counter else None,
        "last": labels[-1],
        "distribution": dict(counter)
    }

    # Convert to numeric for recency-weighted average if mapping provided
    if label_to_numeric:
        numeric_values = [label_to_numeric.get(label, 0) for label in labels]
        result["recency_weighted_numeric"] = np.average(numeric_values, weights=range(1, len(numeric_values) + 1)) if numeric_values else None
        if numeric_values:
            result["min"] = min(numeric_values)
            result["max"] = max(numeric_values)

    return result


def process_conversations(conversations):
    """Process one or more conversations and return analysis."""
    if not isinstance(conversations, list):
        conversations = [conversations]

    all_results = []

    for conv in conversations:
        conv_id = conv.get("ref_conversation_id")
        user_id = conv.get("ref_user_id")
        user_messages = extract_user_messages(conv)

        # Extract features
        sentiments = analyze_sentiment(user_messages)
        topics = extract_topics(user_messages)
        self_efficacy_per_msg = extract_self_efficacy_per_message(conv)
        goals = extract_goals(conv)

        # Topic aggregates within conversation
        all_topics_in_conv = [t for msg in topics for t in msg.get("topics", [])]
        topic_counts_in_conv = Counter(all_topics_in_conv)

        # Recency-weighted topic counts
        topic_recency_weights = {}
        for idx, msg_topics in enumerate(topics, 1):
            weight = idx
            for topic in msg_topics.get("topics", []):
                topic_recency_weights[topic] = topic_recency_weights.get(topic, 0) + weight

        # Per-conversation result
        result = {
            "conversation_id": conv_id,
            "user_id": user_id,
            "message_count": len(user_messages),
            "emotional_state": {
                "per_message": sentiments,
                "aggregates": {
                    "labels": aggregate_labels(sentiments, "label", {"POSITIVE": 1, "NEGATIVE": -1})
                }
            },
            "topics": {
                "per_message": topics,
                "all_topics": list(set(all_topics_in_conv)),
                "aggregates": {
                    "topic_counts": dict(topic_counts_in_conv),
                    "most_common": topic_counts_in_conv.most_common(3),
                    "last": topics[-1].get("topics", []) if topics else [],
                    "recency_weighted_counts": dict(sorted(topic_recency_weights.items(), key=lambda x: x[1], reverse=True)[:5])
                } if all_topics_in_conv else None
            },
            "self_efficacy": {
                "per_message": self_efficacy_per_msg,
                "aggregates": aggregate_labels(self_efficacy_per_msg, "self_efficacy", {"Low": 1, "Medium": 2, "High": 3})
            },
            "goals": goals,
            "goal_aggregates": {
                "count": len(goals)
            } if goals else None
        }

        all_results.append(result)

    # Cross-conversation analysis
    if len(all_results) > 1:
        # Emotional trajectory
        emotional_traj = [r["emotional_state"]["aggregates"]["labels"]["last"] for r in all_results if r["emotional_state"]["aggregates"]["labels"]]

        # Self-efficacy trajectory (last value from each conversation)
        self_efficacy_traj = []
        for r in all_results:
            if r["self_efficacy"] and r["self_efficacy"]["aggregates"]:
                self_efficacy_traj.append(r["self_efficacy"]["aggregates"]["last"])

        self_efficacy_values = {"Low": 1, "Medium": 2, "High": 3}
        self_efficacy_numeric = [self_efficacy_values.get(s, 0) for s in self_efficacy_traj]

        # Topic trajectory
        topic_traj = [r["topics"]["all_topics"] for r in all_results]
        all_topics_flat = [t for topics in topic_traj for t in topics]
        topic_counts = Counter(all_topics_flat)

        # Goal trajectory
        goal_traj = [r["goals"] for r in all_results]
        all_goals_flat = [g for goals in goal_traj for g in goals]

        cross_convo = {
            "conversation_count": len(all_results),
            "emotional_trajectory": emotional_traj,
            "emotional_aggregates": aggregate_labels(
                [{"label": l} for l in emotional_traj], "label"
            ) if emotional_traj else None,
            "self_efficacy_trajectory": self_efficacy_traj,
            "self_efficacy_aggregates": {
                "mode": Counter(self_efficacy_traj).most_common(1)[0][0] if self_efficacy_traj else None,
                "last": self_efficacy_traj[-1] if self_efficacy_traj else None,
                "distribution": dict(Counter(self_efficacy_traj)),
                "min": min(self_efficacy_numeric) if self_efficacy_numeric else None,
                "max": max(self_efficacy_numeric) if self_efficacy_numeric else None,
                "recency_weighted_numeric": np.average(self_efficacy_numeric, weights=range(1, len(self_efficacy_numeric) + 1)) if self_efficacy_numeric else None
            } if self_efficacy_traj else None,
            "topic_trajectory": topic_traj,
            "topic_aggregates": {
                "all_topics": list(set(all_topics_flat)),
                "topic_counts": dict(topic_counts),
                "most_common": topic_counts.most_common(5)
            } if all_topics_flat else None,
            "goal_trajectory": goal_traj,
            "goal_aggregates": {
                "all_goals": list(set(all_goals_flat)),
                "total_count": len(all_goals_flat),
                "unique_count": len(set(all_goals_flat))
            } if all_goals_flat else None
        }
        return {"per_conversation": all_results, "cross_conversation": cross_convo}

    return {"per_conversation": all_results}


@app.route("/evaluate", methods=["POST"])
def evaluate():
    """
    Main API endpoint to evaluate conversation(s).

    Request body:
    {
        "conversations": [ ... ]  // Single conversation object or array of conversations
    }

    Returns analysis with per-conversation and cross-conversation insights.
    """
    try:
        data = request.json
        if not data or "conversations" not in data:
            return jsonify({"error": "Missing 'conversations' field"}), 400

        conversations = data["conversations"]
        result = process_conversations(conversations)

        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint."""
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    # Load environment variables from .env file if present
    from dotenv import load_dotenv
    load_dotenv("../../.env")

    if not os.getenv("ANTHROPIC_API_KEY"):
        print("WARNING: ANTHROPIC_API_KEY not found in environment")

    print("Starting Conversational Evaluation API on http://localhost:5000")
    print("Models will be downloaded on first use.")
    app.run(host="0.0.0.0", port=5000, debug=True)
