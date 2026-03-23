import json
import requests
import sys

if len(sys.argv) < 2:
    print("Usage: python test_generic.py <input_json_file>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = input_file.replace('.json', '.md').replace('../synthetic_data/', '../results/')

with open(input_file, 'r') as f:
    conversations = json.load(f)

response = requests.post('http://localhost:5000/evaluate', json={'conversations': conversations})
result = response.json()

with open(output_file, 'w') as f:
    f.write('```json\n')
    f.write(json.dumps(result, indent=2))
    f.write('\n```\n')

print(f"Results saved to {output_file}")
