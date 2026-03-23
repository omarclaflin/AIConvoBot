# Technical Approach

## Extract Identified Intermediates

Per conversation, extract from user messages (filter out StoryBot):
- Emotional state (sentiment polarity + label)
- Self-efficacy (possibly per detected domain)
- Topics
- Goals

Each of these four has a within-convo trajectory (how it changes across messages in one conversation) and a cross-convo trajectory (how it changes across conversations for a user over time).

## Scoring Per Consumer Team

- **Conversation value team:** belief shift deltas (before/after within convo, and across convos)
- **StoryBot team:** current user state (latest emotional state, self-efficacy, active goals)
- **Recommendation team:** topic tags + extracted goals (for matching to discussion threads)

## Aggregation

Each intermediate produces a score per conversation. Aggregates returned:
- Range (min, max)
- Last value
- Most common (mode)
- Recency-weighted average

Applies both within-convo (across messages) and across-convo (across conversations for a user).

## Modeling Options

| Option | Pros | Cons |
|---|---|---|
| Industry LLM API (OpenAI, Anthropic) | Best quality, handles self-efficacy/goals natively via prompting | Cost per call, latency, external dependency |
| Small LLM self-hosted (Llama, Mistral) | No API cost, data stays local | GPU infra, still slow vs classifiers |
| Non-LLM NLP (HuggingFace classifiers, VADER) | Fast, free, no GPU needed | Weaker on nuanced tasks (self-efficacy, goal extraction) |
| Fine-tuned classifier | Task-specific accuracy | Needs labeled data we don't have |

Chosen path: HuggingFace classifiers for emotional state and topics; LLM API call for self-efficacy and goal extraction. Reasoning: (1) demonstrates both local model and LLM API approaches, (2) these reflect best-guess fit for each category — sentiment/topics have good off-the-shelf classifiers, self-efficacy/goals are too nuanced for them.

## Cross-Conversation Design

API is stateless. Caller provides all conversations to score. For single-convo evaluation, pass one. For cross-convo trajectory, pass multiple (ordered by time). API returns per-conversation scores + cross-conversation aggregates/deltas.

We'll build a test caller script that looks up conversations by user and passes them to the API, to validate cross-convo functionality.



## Input Chunks Per Model

- **Emotional state & Topics (HuggingFace):** single user message → score per message → aggregate
- **Self-efficacy & Goals (LLM API):** full conversation (needs multi-message context) → conversation-level scores → aggregate
   -- possibly sliding window if team was interested in self-efficacy trajectories within conversation

The things that need context are the things going to the LLM. The things that work message-by-message use local classifiers.
