import json
import sys
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np

def load_json(path):
    with open(path, 'r') as f:
        content = f.read()

    # Try to parse as JSON first
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        # Extract JSON from markdown code block
        import re
        json_match = re.search(r'```json\n(.*?)\n```', content, re.DOTALL)
        if json_match:
            return json.loads(json_match.group(1))
        raise ValueError("Could not find JSON in file")

def generate_line_chart(data, output_path):
    """Emotion and self-efficacy over time."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    # Collect all messages across conversations
    emotion_data = []
    efficacy_data = []

    for conv in data['per_conversation']:
        for msg in conv['emotional_state']['per_message']:
            ts = datetime.fromisoformat(msg['timestamp'].replace('Z', '+00:00'))
            emotion_val = 1 if msg['label'] == 'POSITIVE' else -1
            emotion_data.append((ts, emotion_val))

        if conv['self_efficacy']['per_message']:
            for msg in conv['self_efficacy']['per_message']:
                ts = datetime.fromisoformat(msg['timestamp'].replace('Z', '+00:00'))
                efficacy_map = {'Low': 1, 'Medium': 2, 'High': 3}
                efficacy_data.append((ts, efficacy_map.get(msg['self_efficacy'], 2)))

    # Sort by timestamp
    emotion_data.sort(key=lambda x: x[0])
    efficacy_data.sort(key=lambda x: x[0])

    times = [x[0] for x in emotion_data]
    emotions = [x[1] for x in emotion_data]

    # Plot emotions
    ax1.plot(times, emotions, marker='o', linestyle='-', color='blue')
    ax1.axhline(y=0, color='gray', linestyle='--', alpha=0.5)
    ax1.set_ylabel('Emotion')
    ax1.set_yticks([-1, 0, 1])
    ax1.set_yticklabels(['NEGATIVE', '', 'POSITIVE'])
    ax1.grid(True, alpha=0.3)
    ax1.set_title('Emotional State Over Time')

    # Plot self-efficacy
    if efficacy_data:
        eff_times, eff_values = zip(*efficacy_data)
        ax2.plot(eff_times, eff_values, marker='s', linestyle='-', color='green')
        ax2.set_ylabel('Self-Efficacy')
        ax2.set_yticks([1, 2, 3])
        ax2.set_yticklabels(['Low', 'Medium', 'High'])
        ax2.grid(True, alpha=0.3)
        ax2.set_title('Self-Efficacy Over Time')

    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()

def generate_topic_bar_chart(data, output_path):
    """Topic frequency per conversation."""
    conv_labels = []
    topic_data = {}

    for i, conv in enumerate(data['per_conversation'], 1):
        conv_labels.append(f"Conv {i}")

        # Track which topics appear in this conversation
        conv_topics = set()
        if conv['topics']['aggregates']:
            for topic, count in conv['topics']['aggregates']['topic_counts'].items():
                if topic not in topic_data:
                    topic_data[topic] = [0] * (i - 1)  # Pad previous conversations
                topic_data[topic].append(count)
                conv_topics.add(topic)

        # Pad topics that don't appear in this conversation
        for topic in topic_data:
            if topic not in conv_topics:
                topic_data[topic].append(0)

    fig, ax = plt.subplots(figsize=(10, 6))

    x = np.arange(len(conv_labels))
    width = 0.8 / len(topic_data) if topic_data else 0.8

    for i, (topic, counts) in enumerate(topic_data.items()):
        offset = (i - len(topic_data)/2) * width
        ax.bar(x + offset, counts, width, label=topic)

    ax.set_xlabel('Conversation')
    ax.set_ylabel('Topic Frequency')
    ax.set_title('Topics per Conversation')
    ax.set_xticks(x)
    ax.set_xticklabels(conv_labels)
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')

    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()

def generate_text_report(data, output_path):
    """Timeline text report."""
    lines = []
    lines.append("# Timeline Report\n")

    for i, conv in enumerate(data['per_conversation'], 1):
        conv_id = conv['conversation_id']
        user_id = conv['user_id']
        lines.append(f"\n## Conversation {i} (ID: {conv_id}, User: {user_id})\n")

        # Merge messages by timestamp
        messages = []
        for msg in conv['emotional_state']['per_message']:
            messages.append({
                'time': msg['timestamp'],
                'emotion': msg['label'],
                'topics': None,
                'efficacy': None
            })

        # Add topics
        for msg in conv['topics']['per_message']:
            for m in messages:
                if m['time'] == msg['timestamp']:
                    m['topics'] = ', '.join(msg['topics'])

        # Add efficacy
        for msg in conv['self_efficacy']['per_message']:
            for m in messages:
                if m['time'] == msg['timestamp']:
                    m['efficacy'] = msg['self_efficacy']

        for msg in messages:
            lines.append(f"{msg['time']}: {msg['emotion']}")
            if msg['efficacy']:
                lines.append(f" | Efficacy: {msg['efficacy']}")
            if msg['topics']:
                lines.append(f" | Topics: {msg['topics']}")
            lines.append("\n")

        # Aggregates
        if conv['goals']:
            lines.append(f"\nGoals: {', '.join(conv['goals'])}\n")

    # Cross-conversation
    if 'cross_conversation' in data:
        cross = data['cross_conversation']
        lines.append(f"\n## Cross-Conversation Summary\n")
        lines.append(f"Total conversations: {cross['conversation_count']}\n")
        lines.append(f"Emotional trajectory: {' → '.join(cross['emotional_trajectory'])}\n")
        lines.append(f"Self-efficacy trajectory: {' → '.join(cross['self_efficacy_trajectory'])}\n")

        if cross.get('goal_aggregates'):
            lines.append(f"Total goals: {cross['goal_aggregates']['total_count']}\n")

    with open(output_path, 'w') as f:
        f.writelines(lines)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python visualize.py <json_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    base_name = input_file.replace('.md', '').replace('.json', '')

    data = load_json(input_file)

    generate_line_chart(data, f"{base_name}_line_chart.png")
    generate_topic_bar_chart(data, f"{base_name}_topic_bars.png")
    generate_text_report(data, f"{base_name}_report.txt")

    print(f"Generated: {base_name}_line_chart.png")
    print(f"Generated: {base_name}_topic_bars.png")
    print(f"Generated: {base_name}_report.txt")
