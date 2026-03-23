# Design Decisions (Summary)

1. **Sentiment model:** `distilbert-base-uncased-finetuned-sst-2-english` — binary POSITIVE/NEGATIVE with confidence score
   > Standard pretrained sentiment classifier, small/fast, from 2018 BERT family
   > Alternatives: `cardiffnlp/twitter-roberta-base-sentiment` (positive/neutral/negative), `j-hartmann/emotion-english-distilroberta-base` (joy/sadness/anger/fear/surprise/disgust/neutral)

2. **Topic model:** `facebook/bart-large-mnli` — zero-shot, 11 hardcoded categories (health, fitness, relationships, family, work, stress, anxiety, loneliness, hobbies, technology, mental_health), threshold >0.5, top 3 per message
   > Standard zero-shot classifier; categories derived from observed data themes

3. **Self-efficacy + goals:** Anthropic Claude 3.5 Sonnet API call, structured prompt, Low/Medium/High scale for self-efficacy, comma-separated goals list
   > Too nuanced for classifiers; L/M/H scale keeps LLM output consistent vs asking for floats

4. **Stateless API** — no DB, caller passes everything
   > Caller is NOT stateless — it does user lookup and gathers conversations upstream

5. **Filter out StoryBot messages** (user_id == 1) before analysis
   > Bot responses don't reflect user beliefs, would pollute scores

6. **Truncate to 512 chars** for local models
   > BERT max input is 512 tokens; no message in this data comes close anyway

7. **Recency weighting:** linear weights (1, 2, 3...) via numpy
   > Later messages weighted higher — current state matters more than early state

8. **Aggregation for numeric scores:** min, max, mean, last, recency-weighted avg
9. **Aggregation for categorical:** mode, last, distribution
   > Different teams need different views; range shows volatility, last shows current state

10. **Cross-convo:** last-label-per-conversation trajectory, self-efficacy trajectory, union of all goals
    > Tracks evolution across separate sessions

11. **Framework:** Flask on port 5000

12. **Topic list is static** — not derived dynamically
    > Tradeoff: less flexible, but predictable output schema for consumers
