# API Response Structure

## Per-Conversation Fields

- conversation_id
- user_id
- message_count
- emotional_state
  - per_message
    - label
    - score
    - timestamp
  - aggregates
    - labels
      - mode
      - last
      - distribution
      - recency_weighted_numeric
      - min
      - max
- topics
  - per_message
    - timestamp
    - topics
  - all_topics
  - aggregates
    - topic_counts
    - most_common
    - last
    - recency_weighted_counts
- self_efficacy
  - per_message
    - self_efficacy
    - timestamp
  - aggregates
    - mode
    - last
    - distribution
    - recency_weighted_numeric
    - min
    - max
- goals
- goal_aggregates
  - count

## Cross-Conversation Fields

- conversation_count
- emotional_trajectory
- emotional_aggregates
  - mode
  - last
  - distribution
  - recency_weighted_numeric
  - min
  - max
- self_efficacy_trajectory
- self_efficacy_aggregates
  - mode
  - last
  - distribution
  - min
  - max
  - recency_weighted_numeric
- topic_trajectory
- topic_aggregates
  - all_topics
  - topic_counts
  - most_common
- goal_trajectory
- goal_aggregates
  - all_goals
  - total_count
  - unique_count

## Template API Output

```json
{
  "per_conversation": [
    {
      "conversation_id": 12345,
      "user_id": 782,
      "message_count": 5,
      "emotional_state": {
        "per_message": [
          {
            "label": "NEGATIVE",
            "score": 0.95,
            "timestamp": "2023-10-01T10:00:00Z"
          },
          {
            "label": "NEGATIVE",
            "score": 0.98,
            "timestamp": "2023-10-01T11:00:00Z"
          },
          {
            "label": "POSITIVE",
            "score": 0.92,
            "timestamp": "2023-10-01T12:00:00Z"
          }
        ],
        "aggregates": {
          "labels": {
            "mode": "NEGATIVE",
            "last": "POSITIVE",
            "distribution": {
              "NEGATIVE": 2,
              "POSITIVE": 1
            },
            "recency_weighted_numeric": 0.33,
            "min": -1,
            "max": 1
          }
        }
      },
      "topics": {
        "per_message": [
          {
            "timestamp": "2023-10-01T10:00:00Z",
            "topics": ["health", "anxiety"]
          },
          {
            "timestamp": "2023-10-01T11:00:00Z",
            "topics": ["health", "fitness"]
          },
          {
            "timestamp": "2023-10-01T12:00:00Z",
            "topics": ["fitness", "work"]
          }
        ],
        "all_topics": ["health", "anxiety", "fitness", "work"],
        "aggregates": {
          "topic_counts": {
            "health": 2,
            "fitness": 2,
            "anxiety": 1,
            "work": 1
          },
          "most_common": [
            ["health", 2],
            ["fitness", 2],
            ["anxiety", 1]
          ],
          "last": ["fitness", "work"],
          "recency_weighted_counts": {
            "fitness": 5,
            "health": 3,
            "work": 3,
            "anxiety": 1
          }
        }
      },
      "self_efficacy": {
        "per_message": [
          {
            "self_efficacy": "Low",
            "timestamp": "2023-10-01T10:00:00Z"
          },
          {
            "self_efficacy": "Medium",
            "timestamp": "2023-10-01T11:00:00Z"
          },
          {
            "self_efficacy": "High",
            "timestamp": "2023-10-01T12:00:00Z"
          }
        ],
        "aggregates": {
          "mode": "Low",
          "last": "High",
          "distribution": {
            "Low": 1,
            "Medium": 1,
            "High": 1
          },
          "recency_weighted_numeric": 2.33,
          "min": 1,
          "max": 3
        }
      },
      "goals": [
        "start exercising",
        "eat healthier",
        "reduce stress"
      ],
      "goal_aggregates": {
        "count": 3
      }
    },
    {
      "conversation_id": 12346,
      "user_id": 782,
      "message_count": 4,
      "emotional_state": {
        "per_message": [
          {
            "label": "POSITIVE",
            "score": 0.97,
            "timestamp": "2023-10-05T10:00:00Z"
          },
          {
            "label": "POSITIVE",
            "score": 0.99,
            "timestamp": "2023-10-05T11:00:00Z"
          }
        ],
        "aggregates": {
          "labels": {
            "mode": "POSITIVE",
            "last": "POSITIVE",
            "distribution": {
              "POSITIVE": 2
            },
            "recency_weighted_numeric": 1.0,
            "min": 1,
            "max": 1
          }
        }
      },
      "topics": {
        "per_message": [
          {
            "timestamp": "2023-10-05T10:00:00Z",
            "topics": ["fitness", "hobbies"]
          },
          {
            "timestamp": "2023-10-05T11:00:00Z",
            "topics": ["fitness", "health"]
          }
        ],
        "all_topics": ["fitness", "hobbies", "health"],
        "aggregates": {
          "topic_counts": {
            "fitness": 2,
            "hobbies": 1,
            "health": 1
          },
          "most_common": [
            ["fitness", 2],
            ["hobbies", 1],
            ["health", 1]
          ],
          "last": ["fitness", "health"],
          "recency_weighted_counts": {
            "fitness": 3,
            "health": 2,
            "hobbies": 1
          }
        }
      },
      "self_efficacy": {
        "per_message": [
          {
            "self_efficacy": "High",
            "timestamp": "2023-10-05T10:00:00Z"
          },
          {
            "self_efficacy": "High",
            "timestamp": "2023-10-05T11:00:00Z"
          }
        ],
        "aggregates": {
          "mode": "High",
          "last": "High",
          "distribution": {
            "High": 2
          },
          "recency_weighted_numeric": 3.0,
          "min": 3,
          "max": 3
        }
      },
      "goals": [
        "run 5K",
        "maintain routine"
      ],
      "goal_aggregates": {
        "count": 2
      }
    }
  ],
  "cross_conversation": {
    "conversation_count": 2,
    "emotional_trajectory": ["POSITIVE", "POSITIVE"],
    "emotional_aggregates": {
      "mode": "POSITIVE",
      "last": "POSITIVE",
      "distribution": {
        "POSITIVE": 2
      },
      "recency_weighted_numeric": 1.0,
      "min": 1,
      "max": 1
    },
    "self_efficacy_trajectory": ["High", "High"],
    "self_efficacy_aggregates": {
      "mode": "High",
      "last": "High",
      "distribution": {
        "High": 2
      },
      "min": 3,
      "max": 3,
      "recency_weighted_numeric": 3.0
    },
    "topic_trajectory": [
      ["health", "anxiety", "fitness", "work"],
      ["fitness", "hobbies", "health"]
    ],
    "topic_aggregates": {
      "all_topics": ["health", "anxiety", "fitness", "work", "hobbies"],
      "topic_counts": {
        "health": 2,
        "fitness": 2,
        "anxiety": 1,
        "work": 1,
        "hobbies": 1
      },
      "most_common": [
        ["health", 2],
        ["fitness", 2],
        ["anxiety", 1],
        ["work", 1],
        ["hobbies", 1]
      ]
    },
    "goal_trajectory": [
      ["start exercising", "eat healthier", "reduce stress"],
      ["run 5K", "maintain routine"]
    ],
    "goal_aggregates": {
      "all_goals": ["start exercising", "eat healthier", "reduce stress", "run 5K", "maintain routine"],
      "total_count": 5,
      "unique_count": 5
    }
  }
}
```
