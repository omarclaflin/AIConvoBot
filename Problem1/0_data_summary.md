Here's a field-by-field summary of the data in each file:

---

## `conversations.json`

A JSON array of conversation objects. Each object has:

| Field | Description | Observed Values |
|---|---|---|
| `ref_conversation_id` | Unique ID for the conversation | Integers in the ~42000–98000 range (e.g. 98696, 56808, 76922, 63988, 96530, 97302) |
| `ref_user_id` | The human user's ID (top-level) | Integers, various (e.g. 782, 876, 905, 141, 396, 367) |
| `messages_list` | Ordered array of message objects (see below) | Varies from ~12 to ~30+ messages per conversation |

### Fields inside each message object in `messages_list`:

| Field | Description | Observed Values |
|---|---|---|
| `ref_conversation_id` | Same conversation ID, repeated on every message | Matches the parent object's `ref_conversation_id` |
| `ref_user_id` | Author of this message | `1` for StoryBot; otherwise the human user's ID (e.g. 782, 876, 905) |
| `transaction_datetime_utc` | ISO 8601 timestamp | Dates in Sept–Oct 2023 range (e.g. `"2023-10-01T10:15:00Z"`, `"2023-09-07T08:00:00Z"`). Conversations span multiple days. |
| `screen_name` | Display name of the author | `"StoryBot"` for the AI (always user_id 1). For humans: two-word compound names like `"ChattyPenguin"`, `"ChirpyPenguin"`, `"BubblyPenguin"`, `"JoyfulTiger"`, `"HappyPineapple"`, `"JoyfulExplorer"` |
| `message` | The text content | Natural conversational English. Topics include: app navigation help, loneliness, health concerns, family relationships, personal memories/stories, fitness goals, anxiety, stress management, hobbies. StoryBot asks supportive follow-up questions and gives gentle suggestions. |

**General conversation pattern:** StoryBot initiates or responds to greetings, the user raises a topic (tech help, emotional state, personal goal), and a multi-day back-and-forth follows covering personal wellbeing themes.

---

## `discussions.json`

A JSON array of discussion thread objects. Each object has:

| Field | Description | Observed Values |
|---|---|---|
| `post_id` | Unique ID for the discussion thread | Integers in the ~1000–9900 range (e.g. 1131, 2602, 7601, 8685, 8840, 1086, 7164, 6199, 9521, 7549, 2244) |
| `messages_list` | Ordered array: first element is the original post, remaining elements are comments | Typically 1 post + 4–9 comments per thread |

### Fields inside each message object in `messages_list`:

| Field | Description | Observed Values |
|---|---|---|
| `post_id` | ID of the parent thread, repeated on every message | Matches the parent object's `post_id` |
| `comment_id` | Comment sequence number, or `null` for the original post | `null` for the opening post; integers `1`, `2`, `3`… for comments, sequential |
| `text` | The post or comment content | Multi-sentence text. Topics are almost entirely about **stress management and mental wellness**: meditation, journaling, exercise, yoga, nature walks, sleep, nutrition, therapy, social support, burnout, work-life balance. Mix of agreement, personal anecdotes, mild disagreement, and questions to the group. |
| `author_ref_user_id` | ID of the user who wrote this | Integers — a mix of low-range IDs (10–150) and higher IDs (200–987). Post authors and comment authors are different users. |
| `reported_or_removed` | Moderation flag | Boolean. `false` on most messages. `true` on a small number of comments (observed on scattered comments across threads). |

**General discussion pattern:** A user posts an open-ended question about stress/wellness. 4–9 other users comment with a mix of suggestions (meditation, exercise, journaling, therapy), personal experiences, mild pushback on certain approaches, and meta-discussion about individual differences.

---

## `activity.json`

A JSON array of flat activity records. Each object has:

| Field | Description | Observed Values |
|---|---|---|
| `ref_user_id` | ID of the user who performed the action | Integers. Low-range IDs (10–56, 101, 105, 123, 150) appear in `"created"` records. A wider range of IDs (13–987) appear in `"commented"` and `"read"` records. |
| `activity_type` | What the user did | Exactly one of three string values: `"created"`, `"commented"`, `"read"` |
| `post_id` | Which discussion post the activity relates to | Integers matching `post_id` values from `discussions.json` (e.g. 1131, 2602, 7601, etc.) |

**Data ordering:** The file is grouped by activity type — all `"created"` records first, then all `"commented"` records, then all `"read"` records. The `"read"` activity records make up the bulk of the file (~12,000+ lines out of ~12,748).

---

## Cross-file relationships

- `activity.post_id` and `discussions.post_id` reference the same discussion threads.
- `ref_user_id` values in `activity.json` and `discussions.json` overlap (e.g. user 25 created post 1131, and user 25 also appears as a comment author in discussions).
- `conversations.json` users (700–900 range IDs) are mostly distinct from discussion post authors (10–150 range), but some IDs overlap in the commenter/reader pools.
- StoryBot (`ref_user_id: 1`) only appears in `conversations.json`, never in discussions or activity.
