import json
import requests

API_URL = "http://localhost:5000"

with open('../synthetic_data/cluster1_elderly_app_health.json', 'r') as f:
    conversations = json.load(f)

response = requests.post(
    f"{API_URL}/evaluate",
    json={"conversations": conversations}
)

result = response.json()

md = []
md.append("# Elderly App Health - Synthetic Data\n\n")

md.append("## Conversations\n\n")
for conv in conversations:
    conv_id = conv['ref_conversation_id']
    user_id = conv['ref_user_id']
    messages = conv.get('messages_list', [])

    md.append(f"### Conversation {conv_id} (User {user_id})\n\n")

    for msg in messages:
        if msg.get('ref_user_id') != 1:
            ts = msg.get('transaction_datetime_utc', '')
            text = msg.get('message', '')
            md.append(f"**[{ts}]** {text}\n\n")

md.append("---\n\n")
md.append("## API Output\n\n")
md.append("```json\n")
md.append(json.dumps(result, indent=2))
md.append("\n```\n")

with open('../results/synthetic_elderly_app_health.md', 'w') as f:
    f.write(''.join(md))
