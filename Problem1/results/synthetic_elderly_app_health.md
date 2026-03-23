# Elderly App Health - Synthetic Data

## Conversations

### Conversation 98696 (User 782)

**[2023-10-01T10:15:00Z]** Hello StoryBot, I’m having a tough time with this app. My fingers aren’t what they used to be. Can you help me?

**[2023-10-01T10:25:00Z]** It's just so complicated! I keep hitting the wrong buttons. And sometimes it logs me out unexpectedly.

**[2023-10-01T10:35:00Z]** I’d appreciate that. My grandson usually helps, but he’s busy with school lately. I feel so helpless.

**[2023-10-01T10:45:00Z]** I’d like to read the daily stories! They used to lift my spirits.

**[2023-10-02T11:15:00Z]** I managed to get to the stories! But I’m feeling a bit down today. My health has been off, and I’m worried about my family.

**[2023-10-02T11:25:00Z]** Well, I had a fall last week, and it shook me up. I remember back in the day, I slipped in the kitchen while baking. I thought I broke my hip then, but I learned to always be careful and mindful. That taught me to value my health and strength.

**[2023-10-03T12:00:00Z]** I talked to my daughter about it. She said I should consider moving into assisted living, but I don’t want to leave my home.

**[2023-10-03T12:10:00Z]** My garden is beautiful, and I love my cozy chair by the window. But, I guess I worry about being safe alone.

**[2023-10-03T12:20:00Z]** Yes, please! I want to stay here for as long as I can.

**[2023-10-04T11:10:00Z]** That sounds manageable! I’ll talk to my daughter about it. Thank you for being so helpful!

### Conversation 38080 (User 782)

**[2023-10-01T09:00:00Z]** Hello, StoryBot. I’m having a tough time with this app. It keeps logging me out, and I can't seem to type very well today.

**[2023-10-01T09:05:00Z]** Not yet! I’ll give that a try. Meanwhile, my knees are acting up again. It’s hard to get up and down.

**[2023-10-01T09:10:00Z]** Yes, but they just tell me to rest. It feels like I’m just sitting around these days, not doing much.

**[2023-10-02T09:20:00Z]** I like reading. Just finished a mystery novel, but I'm feeling a bit restless again.

**[2023-10-02T09:25:00Z]** I used to enjoy painting, but it’s been a long time. Maybe I’ll pick it up again…

**[2023-10-03T09:30:00Z]** Mostly landscapes. I loved capturing the colors of sunsets. Speaking of colors, what do you think about life? What's the point of all this?

**[2023-10-04T09:35:00Z]** I suppose it’s about those connections, but sometimes I feel lonely, even with family nearby.

**[2023-10-05T09:40:00Z]** I did! My granddaughter called me yesterday. We talked for an hour about her new job.

**[2023-10-06T09:45:00Z]** It made me feel happy! Family can be a great comfort. Just wish I could do more things with them.

**[2023-10-08T09:50:00Z]** That’s a good idea! I’ll suggest a picnic in the park next time we chat. Thanks, StoryBot.

### Conversation 45582 (User 782)

**[2023-10-01T10:00:00Z]** Hello! I’m really struggling with this app. It keeps freezing on me!

**[2023-10-02T09:30:00Z]** I did. Still no luck. Also, my knees have been acting up. Makes it hard to get around!

**[2023-10-08T11:15:00Z]** Yes, I have an appointment next week. Hope this app works better by then!

---

## API Output

```json
{
  "cross_conversation": {
    "conversation_count": 3,
    "emotional_aggregates": {
      "distribution": {
        "NEGATIVE": 1,
        "POSITIVE": 2
      },
      "last": "NEGATIVE",
      "mode": "POSITIVE"
    },
    "emotional_trajectory": [
      "POSITIVE",
      "POSITIVE",
      "NEGATIVE"
    ],
    "goal_aggregates": {
      "all_goals": [
        "Achieve work-life balance",
        "Improve dexterity for app usage",
        "Run a 5K",
        "Maintain health and strength",
        "Receive assistance to enable independent living",
        "Pick up painting again",
        "Capture the colors of sunsets",
        "Spend more time with family",
        "Make more meaningful connections",
        "Remain living independently in current home",
        "Read daily stories to lift spirits"
      ],
      "total_count": 11,
      "unique_count": 11
    },
    "goal_trajectory": [
      [
        "Improve dexterity for app usage",
        "Read daily stories to lift spirits",
        "Maintain health and strength",
        "Remain living independently in current home",
        "Receive assistance to enable independent living"
      ],
      [
        "Run a 5K",
        "Achieve work-life balance",
        "Pick up painting again",
        "Capture the colors of sunsets",
        "Make more meaningful connections",
        "Spend more time with family"
      ],
      []
    ],
    "self_efficacy_aggregates": {
      "distribution": {
        "High": 2,
        "Medium": 1
      },
      "last": "Medium",
      "max": 3,
      "min": 2,
      "mode": "High",
      "recency_weighted_numeric": 2.5
    },
    "self_efficacy_trajectory": [
      "High",
      "High",
      "Medium"
    ],
    "topic_aggregates": {
      "all_topics": [
        "health",
        "stress",
        "relationships",
        "anxiety",
        "work",
        "fitness",
        "family",
        "hobbies",
        "technology",
        "loneliness",
        "mental_health"
      ],
      "most_common": [
        [
          "stress",
          3
        ],
        [
          "health",
          3
        ],
        [
          "work",
          3
        ],
        [
          "family",
          3
        ],
        [
          "technology",
          3
        ]
      ],
      "topic_counts": {
        "anxiety": 1,
        "family": 3,
        "fitness": 2,
        "health": 3,
        "hobbies": 1,
        "loneliness": 2,
        "mental_health": 2,
        "relationships": 2,
        "stress": 3,
        "technology": 3,
        "work": 3
      }
    },
    "topic_trajectory": [
      [
        "stress",
        "health",
        "relationships",
        "anxiety",
        "work",
        "fitness",
        "family",
        "technology",
        "loneliness"
      ],
      [
        "health",
        "stress",
        "relationships",
        "work",
        "fitness",
        "family",
        "hobbies",
        "technology",
        "loneliness",
        "mental_health"
      ],
      [
        "health",
        "stress",
        "work",
        "family",
        "technology",
        "mental_health"
      ]
    ]
  },
  "per_conversation": [
    {
      "conversation_id": 98696,
      "emotional_state": {
        "aggregates": {
          "labels": {
            "distribution": {
              "NEGATIVE": 4,
              "POSITIVE": 6
            },
            "last": "POSITIVE",
            "max": 1,
            "min": -1,
            "mode": "POSITIVE",
            "recency_weighted_numeric": 0.41818181818181815
          }
        },
        "per_message": [
          {
            "label": "NEGATIVE",
            "score": 0.9988638162612915,
            "timestamp": "2023-10-01T10:15:00Z"
          },
          {
            "label": "POSITIVE",
            "score": 0.5709629058837891,
            "timestamp": "2023-10-01T10:25:00Z"
          },
          {
            "label": "NEGATIVE",
            "score": 0.9960058331489563,
            "timestamp": "2023-10-01T10:35:00Z"
          },
          {
            "label": "POSITIVE",
            "score": 0.9997628331184387,
            "timestamp": "2023-10-01T10:45:00Z"
          },
          {
            "label": "NEGATIVE",
            "score": 0.9988980293273926,
            "timestamp": "2023-10-02T11:15:00Z"
          },
          {
            "label": "POSITIVE",
            "score": 0.9994993209838867,
            "timestamp": "2023-10-02T11:25:00Z"
          },
          {
            "label": "NEGATIVE",
            "score": 0.7846354842185974,
            "timestamp": "2023-10-03T12:00:00Z"
          },
          {
            "label": "POSITIVE",
            "score": 0.9928299784660339,
            "timestamp": "2023-10-03T12:10:00Z"
          },
          {
            "label": "POSITIVE",
            "score": 0.9972808361053467,
            "timestamp": "2023-10-03T12:20:00Z"
          },
          {
            "label": "POSITIVE",
            "score": 0.9998477697372437,
            "timestamp": "2023-10-04T11:10:00Z"
          }
        ]
      },
      "goal_aggregates": {
        "count": 5
      },
      "goals": [
        "Improve dexterity for app usage",
        "Read daily stories to lift spirits",
        "Maintain health and strength",
        "Remain living independently in current home",
        "Receive assistance to enable independent living"
      ],
      "message_count": 10,
      "self_efficacy": {
        "aggregates": {
          "distribution": {
            "High": 2,
            "Low": 7,
            "Medium": 1
          },
          "last": "High",
          "max": 3,
          "min": 1,
          "mode": "Low",
          "recency_weighted_numeric": 1.8
        },
        "per_message": [
          {
            "self_efficacy": "Low",
            "timestamp": "2023-10-01T10:15:00Z"
          },
          {
            "self_efficacy": "Low",
            "timestamp": "2023-10-01T10:25:00Z"
          },
          {
            "self_efficacy": "Low",
            "timestamp": "2023-10-01T10:35:00Z"
          },
          {
            "self_efficacy": "Low",
            "timestamp": "2023-10-01T10:45:00Z"
          },
          {
            "self_efficacy": "Low",
            "timestamp": "2023-10-02T11:15:00Z"
          },
          {
            "self_efficacy": "Medium",
            "timestamp": "2023-10-02T11:25:00Z"
          },
          {
            "self_efficacy": "Low",
            "timestamp": "2023-10-03T12:00:00Z"
          },
          {
            "self_efficacy": "Low",
            "timestamp": "2023-10-03T12:10:00Z"
          },
          {
            "self_efficacy": "High",
            "timestamp": "2023-10-03T12:20:00Z"
          },
          {
            "self_efficacy": "High",
            "timestamp": "2023-10-04T11:10:00Z"
          }
        ]
      },
      "topics": {
        "aggregates": {
          "last": [
            "family",
            "health",
            "relationships"
          ],
          "most_common": [
            [
              "health",
              7
            ],
            [
              "family",
              5
            ],
            [
              "relationships",
              4
            ]
          ],
          "recency_weighted_counts": {
            "anxiety": 8,
            "family": 34,
            "health": 44,
            "relationships": 29,
            "stress": 15
          },
          "topic_counts": {
            "anxiety": 1,
            "family": 5,
            "fitness": 1,
            "health": 7,
            "loneliness": 1,
            "relationships": 4,
            "stress": 3,
            "technology": 2,
            "work": 1
          }
        },
        "all_topics": [
          "stress",
          "health",
          "relationships",
          "anxiety",
          "work",
          "fitness",
          "family",
          "technology",
          "loneliness"
        ],
        "per_message": [
          {
            "timestamp": "2023-10-01T10:15:00Z",
            "topics": [
              "technology"
            ]
          },
          {
            "timestamp": "2023-10-01T10:25:00Z",
            "topics": [
              "technology",
              "work",
              "stress"
            ]
          },
          {
            "timestamp": "2023-10-01T10:35:00Z",
            "topics": [
              "family",
              "relationships",
              "health"
            ]
          },
          {
            "timestamp": "2023-10-01T10:45:00Z",
            "topics": [
              "health"
            ]
          },
          {
            "timestamp": "2023-10-02T11:15:00Z",
            "topics": [
              "health",
              "family",
              "stress"
            ]
          },
          {
            "timestamp": "2023-10-02T11:25:00Z",
            "topics": [
              "health",
              "fitness"
            ]
          },
          {
            "timestamp": "2023-10-03T12:00:00Z",
            "topics": [
              "family",
              "relationships",
              "health"
            ]
          },
          {
            "timestamp": "2023-10-03T12:10:00Z",
            "topics": [
              "anxiety",
              "loneliness",
              "stress"
            ]
          },
          {
            "timestamp": "2023-10-03T12:20:00Z",
            "topics": [
              "family",
              "relationships",
              "health"
            ]
          },
          {
            "timestamp": "2023-10-04T11:10:00Z",
            "topics": [
              "family",
              "health",
              "relationships"
            ]
          }
        ]
      },
      "user_id": 782
    },
    {
      "conversation_id": 38080,
      "emotional_state": {
        "aggregates": {
          "labels": {
            "distribution": {
              "NEGATIVE": 6,
              "POSITIVE": 4
            },
            "last": "POSITIVE",
            "max": 1,
            "min": -1,
            "mode": "NEGATIVE",
            "recency_weighted_numeric": 0.2
          }
        },
        "per_message": [
          {
            "label": "NEGATIVE",
            "score": 0.9925481677055359,
            "timestamp": "2023-10-01T09:00:00Z"
          },
          {
            "label": "NEGATIVE",
            "score": 0.9989132881164551,
            "timestamp": "2023-10-01T09:05:00Z"
          },
          {
            "label": "NEGATIVE",
            "score": 0.9996885061264038,
            "timestamp": "2023-10-01T09:10:00Z"
          },
          {
            "label": "NEGATIVE",
            "score": 0.9528188109397888,
            "timestamp": "2023-10-02T09:20:00Z"
          },
          {
            "label": "NEGATIVE",
            "score": 0.9125702977180481,
            "timestamp": "2023-10-02T09:25:00Z"
          },
          {
            "label": "POSITIVE",
            "score": 0.9974472522735596,
            "timestamp": "2023-10-03T09:30:00Z"
          },
          {
            "label": "NEGATIVE",
            "score": 0.9934060573577881,
            "timestamp": "2023-10-04T09:35:00Z"
          },
          {
            "label": "POSITIVE",
            "score": 0.9892237186431885,
            "timestamp": "2023-10-05T09:40:00Z"
          },
          {
            "label": "POSITIVE",
            "score": 0.9997867941856384,
            "timestamp": "2023-10-06T09:45:00Z"
          },
          {
            "label": "POSITIVE",
            "score": 0.9997380375862122,
            "timestamp": "2023-10-08T09:50:00Z"
          }
        ]
      },
      "goal_aggregates": {
        "count": 6
      },
      "goals": [
        "Run a 5K",
        "Achieve work-life balance",
        "Pick up painting again",
        "Capture the colors of sunsets",
        "Make more meaningful connections",
        "Spend more time with family"
      ],
      "message_count": 10,
      "self_efficacy": {
        "aggregates": {
          "distribution": {
            "High": 1,
            "Low": 6,
            "Medium": 2
          },
          "last": "High",
          "max": 3,
          "min": 1,
          "mode": "Low",
          "recency_weighted_numeric": 1.7333333333333334
        },
        "per_message": [
          {
            "self_efficacy": "Low",
            "timestamp": "2023-10-01T09:00:00Z"
          },
          {
            "self_efficacy": "Low",
            "timestamp": "2023-10-01T09:05:00Z"
          },
          {
            "self_efficacy": "Low",
            "timestamp": "2023-10-01T09:10:00Z"
          },
          {
            "self_efficacy": "Low",
            "timestamp": "2023-10-02T09:25:00Z"
          },
          {
            "self_efficacy": "Low",
            "timestamp": "2023-10-03T09:30:00Z"
          },
          {
            "self_efficacy": "Low",
            "timestamp": "2023-10-04T09:35:00Z"
          },
          {
            "self_efficacy": "Medium",
            "timestamp": "2023-10-05T09:40:00Z"
          },
          {
            "self_efficacy": "Medium",
            "timestamp": "2023-10-06T09:45:00Z"
          },
          {
            "self_efficacy": "High",
            "timestamp": "2023-10-08T09:50:00Z"
          }
        ]
      },
      "topics": {
        "aggregates": {
          "last": [
            "relationships",
            "technology"
          ],
          "most_common": [
            [
              "family",
              4
            ],
            [
              "relationships",
              4
            ],
            [
              "technology",
              2
            ]
          ],
          "recency_weighted_counts": {
            "family": 27,
            "hobbies": 9,
            "relationships": 34,
            "technology": 11,
            "work": 10
          },
          "topic_counts": {
            "family": 4,
            "fitness": 1,
            "health": 2,
            "hobbies": 2,
            "loneliness": 1,
            "mental_health": 1,
            "relationships": 4,
            "stress": 1,
            "technology": 2,
            "work": 2
          }
        },
        "all_topics": [
          "health",
          "stress",
          "relationships",
          "work",
          "fitness",
          "family",
          "hobbies",
          "technology",
          "loneliness",
          "mental_health"
        ],
        "per_message": [
          {
            "timestamp": "2023-10-01T09:00:00Z",
            "topics": [
              "technology",
              "stress"
            ]
          },
          {
            "timestamp": "2023-10-01T09:05:00Z",
            "topics": [
              "work",
              "health",
              "fitness"
            ]
          },
          {
            "timestamp": "2023-10-01T09:10:00Z",
            "topics": [
              "health",
              "family",
              "mental_health"
            ]
          },
          {
            "timestamp": "2023-10-02T09:20:00Z",
            "topics": [
              "hobbies"
            ]
          },
          {
            "timestamp": "2023-10-02T09:25:00Z",
            "topics": [
              "hobbies"
            ]
          },
          {
            "timestamp": "2023-10-03T09:30:00Z",
            "topics": []
          },
          {
            "timestamp": "2023-10-04T09:35:00Z",
            "topics": [
              "relationships",
              "loneliness",
              "family"
            ]
          },
          {
            "timestamp": "2023-10-05T09:40:00Z",
            "topics": [
              "family",
              "relationships",
              "work"
            ]
          },
          {
            "timestamp": "2023-10-06T09:45:00Z",
            "topics": [
              "family",
              "relationships"
            ]
          },
          {
            "timestamp": "2023-10-08T09:50:00Z",
            "topics": [
              "relationships",
              "technology"
            ]
          }
        ]
      },
      "user_id": 782
    },
    {
      "conversation_id": 45582,
      "emotional_state": {
        "aggregates": {
          "labels": {
            "distribution": {
              "NEGATIVE": 3
            },
            "last": "NEGATIVE",
            "max": -1,
            "min": -1,
            "mode": "NEGATIVE",
            "recency_weighted_numeric": -1.0
          }
        },
        "per_message": [
          {
            "label": "NEGATIVE",
            "score": 0.9678887724876404,
            "timestamp": "2023-10-01T10:00:00Z"
          },
          {
            "label": "NEGATIVE",
            "score": 0.9990504384040833,
            "timestamp": "2023-10-02T09:30:00Z"
          },
          {
            "label": "NEGATIVE",
            "score": 0.9313342571258545,
            "timestamp": "2023-10-08T11:15:00Z"
          }
        ]
      },
      "goal_aggregates": null,
      "goals": [],
      "message_count": 3,
      "self_efficacy": {
        "aggregates": {
          "distribution": {
            "Low": 2,
            "Medium": 1
          },
          "last": "Medium",
          "max": 2,
          "min": 1,
          "mode": "Low",
          "recency_weighted_numeric": 1.5
        },
        "per_message": [
          {
            "self_efficacy": "Low",
            "timestamp": "2023-10-01T10:00:00Z"
          },
          {
            "self_efficacy": "Low",
            "timestamp": "2023-10-02T09:30:00Z"
          },
          {
            "self_efficacy": "Medium",
            "timestamp": "2023-10-08T11:15:00Z"
          }
        ]
      },
      "topics": {
        "aggregates": {
          "last": [
            "technology",
            "health",
            "mental_health"
          ],
          "most_common": [
            [
              "technology",
              2
            ],
            [
              "work",
              2
            ],
            [
              "health",
              2
            ]
          ],
          "recency_weighted_counts": {
            "family": 2,
            "health": 5,
            "mental_health": 3,
            "technology": 4,
            "work": 3
          },
          "topic_counts": {
            "family": 1,
            "health": 2,
            "mental_health": 1,
            "stress": 1,
            "technology": 2,
            "work": 2
          }
        },
        "all_topics": [
          "health",
          "stress",
          "work",
          "family",
          "technology",
          "mental_health"
        ],
        "per_message": [
          {
            "timestamp": "2023-10-01T10:00:00Z",
            "topics": [
              "technology",
              "work",
              "stress"
            ]
          },
          {
            "timestamp": "2023-10-02T09:30:00Z",
            "topics": [
              "health",
              "work",
              "family"
            ]
          },
          {
            "timestamp": "2023-10-08T11:15:00Z",
            "topics": [
              "technology",
              "health",
              "mental_health"
            ]
          }
        ]
      },
      "user_id": 782
    }
  ]
}
```
