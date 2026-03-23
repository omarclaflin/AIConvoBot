# Possible Deliverables Per Team

## Conversation Value Team
- Belief shift deltas (emotional state + self-efficacy, start vs end)
- Cross-convo trajectory (is user trending better over time?)
- Goal emergence/completion counts

## StoryBot Team
- Current emotional state (last label + score)
- Current self-efficacy (last value)
- Active goals (for contextual follow-ups)
- Topic tags (what the user is talking about right now)

## Recommendation Team
- Topic tags + frequency
- Extracted goals (map to discussion thread topics)
- Cross-convo topic shifts (evolving interests)



# Current Status

## Conversation Value Team
- Belief shift deltas — YES (`emotional_state.aggregates.min/max/last`, `self_efficacy.aggregates.last`)
- Cross-convo trajectory — YES (`emotional_trajectory`, `self_efficacy_trajectory`)
- Goal emergence/completion counts — PARTIAL (listed, not tracked over time)

## StoryBot Team
- Current emotional state — YES (`emotional_state.aggregates.labels.last`, `emotional_state.aggregates.recency_weighted_numeric`)
- Current self-efficacy — YES (`self_efficacy.aggregates.last`)
- Active goals — PARTIAL (listed, not tagged active/completed)
- Topic tags — YES (`topics.all_topics`, `topics.aggregates.last`)

## Recommendation Team
- Topic tags + frequency — YES (`topics.aggregates.topic_counts`, `topics.aggregates.most_common`)
- Goals mapped to discussions — NO
- Cross-convo topic shifts — PARTIAL (per-convo topics exist, no explicit diff)




## Possible follow-ups (to fix possible deficiencies)
1. Ask about goals/obtain goal completion information somehow (without sloppy inference)
2. Discussion topic to forum topic map
3. Possibly a topic diff (for recommendation team; e.g {health, technology, loneliness}, {health, family, fitness} --> -:{technology, loneliness}, +:{family, fitness} )