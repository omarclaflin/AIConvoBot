# Design Improvements

## API Optimization: Avoid Re-Evaluation
- Separate endpoints: `/evaluate/single` and `/evaluate/aggregate`
- Database-backed caching by conversation_id
- Result ID system with client-side caching
- Client stores individual results, only submits new conversations

## Cross-Conversation Message Windowing
- Sliding window of last N messages across all conversations (ignoring conversation boundaries)
- Actionable for detecting recent trends that span multiple conversations

## Self-Hosted LLM
- Host open-source LLM (Llama, Mistral) to avoid API costs
- Worth it for high volume or data privacy requirements

## Sentiment Model Upgrade
- Current: binary (POSITIVE/NEGATIVE)
- If binary sufficient: keep it
- If need spectrum: upgrade to emotion detection model (joy, sadness, anger, fear, surprise, disgust, neutral)
