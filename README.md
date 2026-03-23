# Conversational Evaluation API

Analyzes emotional state, topics, self-efficacy, and goals from conversations.

## Setup

1. Create venv:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Set API key (or use parent .env):
```bash
export ANTHROPIC_API_KEY=your_key
```

3. Run:
```bash
cd src && python api.py
```

API runs on `http://localhost:5000`

## Endpoints

**POST /evaluate** - Submit conversations for analysis
**GET /health** - Health check

## Visualization

Generate graphs from API output:
```bash
python src/visualize.py results/output.md
```

Produces:
- Line chart: emotion/efficacy over time
- Bar chart: topic frequency
- Text report: timeline

## Tests

Individual conversations in sequence (3 separate API calls):
```bash
cd src && python test_individual_in_sequence.py
```

Multi-conversation analysis (synthetic elderly app data):
```bash
cd src && python test_multi_conversation.py
```

Generic test (any synthetic data file):
```bash
cd src && python test_generic.py ../synthetic_data/cluster3_running_comeback.json
```

Visualize results:
```bash
cd src && python visualize.py ../results/synthetic_elderly_app_health.md
```

Outputs to `results/` folder.

## Docs

- `5_response_shape.md` - Full API response structure
- `4_implementation_decisions.md` - Model choices and prompts
- `6_output_readability.md` - Report/graph options
- `7_design_improvement_thoughts.md` - Future optimizations
