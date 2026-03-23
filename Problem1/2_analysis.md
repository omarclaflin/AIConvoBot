# User-Modeling / Psychographic Extraction (Beliefs, Goals)

## Downstream Scoring & Actionables

- Conversation value scoring (did beliefs shift positively?)
- StoryBot behavior tuning (adjust tone based on user state)
- Community content recommendation (match goals/interests to discussion threads)

-"team assigning value to conversations" — did a conversation move a user from negative self-perception to positive? That conversation has measurable value.
-"team developing StoryBot" — if user is gaining confidence, adjust tone; if regressing, change approach.
-"team recommending content in the community" — user who just set a fitness goal gets recommended fitness-related discussion threads from discussions.json.






## (Possible) Modeled Intermediates

- Emotional state
- Self-efficacy (per domain)
- Topic tagging
- Goals

- Before/after belief states ("evolutions") for each



## What StoryBot is/how its adjustable?

Per the data: 
1. Greets users, 
2. asks open-ended follow-up questions, 
3. validates feelings, 
4. gives gentle suggestions (e.g. "try tapping the Stories section"), 
5. encourages users to take small steps, 
6. and checks back on progress across multi-day conversations. 

It does not fix technical problems directly, does not give medical advice, and does not initiate new topics unprompted — it follows the user's lead.
It "builds resilience" through "everyday conversations."


# Possible adjustment knobs/inputs to StoryBot:

1) Adjusting tone/prompting strategy based on detected emotional trajectory (user is declining → more supportive; user is progressing → more encouraging/challenging)
2) Referencing extracted goals in follow-ups ("How's the 5K training going?")
3) Knowing when to suggest community discussion topics vs. staying in 1-on-1 mode
4) Detecting when a user is stuck or disengaging and changing approach (different prompts/personalities/topics)


