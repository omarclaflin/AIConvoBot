import json
import requests

API_URL = "http://localhost:5000"

with open('../../data/conversations.json', 'r') as f:
    all_conversations = json.load(f)

all_conversations.sort(key=lambda c: c.get('messages_list', [{}])[0].get('transaction_datetime_utc', ''))
conversations = all_conversations[:3]

md = []
md.append("# Individual Conversation Evaluations\n\n")

for i, conv in enumerate(conversations, 1):
    response = requests.post(
        f"{API_URL}/evaluate",
        json={"conversations": conv}
    )

    if response.status_code != 200:
        continue

    result = response.json()
    conv_id = conv['ref_conversation_id']
    user_id = conv['ref_user_id']
    messages = conv.get('messages_list', [])

    md.append(f"## Conversation {i}: ID {conv_id} (User {user_id})\n\n")

    for msg in messages:
        if msg.get('ref_user_id') != 1:
            ts = msg.get('transaction_datetime_utc', '')
            text = msg.get('message', '')
            md.append(f"**[{ts}]** {text}\n\n")

    md.append("### Analysis\n\n")

    conv_result = result.get('per_conversation', [{}])[0]

    emo = conv_result.get('emotional_state', {}).get('aggregates', {})
    if emo:
        labels = emo.get('labels', {})

        md.append(f"**Emotional State:**\n")
        if labels:
            md.append(f"- Last: {labels.get('last')}\n")
            md.append(f"- Mode: {labels.get('mode')}\n")
            if labels.get('recency_weighted_numeric') is not None:
                md.append(f"- Recency-weighted: {labels.get('recency_weighted_numeric'):.3f}\n")
            if labels.get('distribution'):
                dist = ', '.join([f"{k}: {v}" for k, v in labels['distribution'].items()])
                md.append(f"- Distribution: {dist}\n")
        md.append("\n")

    if conv_result.get('topics', {}).get('all_topics'):
        md.append(f"**Topics:** {', '.join(conv_result['topics']['all_topics'])}\n\n")

    if conv_result.get('self_efficacy'):
        md.append(f"**Self-efficacy:** {conv_result['self_efficacy']}\n\n")

    if conv_result.get('goals'):
        md.append(f"**Goals:**\n")
        for g in conv_result['goals']:
            md.append(f"- {g}\n")
        md.append("\n")

    md.append("---\n\n")

with open('../results/individual_evaluations.md', 'w') as f:
    f.write(''.join(md))
