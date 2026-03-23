Problem Statement 2: Real-Time Anomaly Detection in Conversational Data
Scenario: Imagine a platform that processes a continuous stream of conversations from a
generative agent (StoryBot). To maintain a safe and engaging environment, you need to
monitor these conversations in real time for anomalies such as sudden shifts in sentiment,
unusual topic spikes, or atypical user behavior that could indicate emerging issues or
opportunities.
Task: Develop a streaming machine learning pipeline in Python that ingests data (message
and metadata), does feature extraction and preprocessing in near real time, applies an
anomaly detection model (your own or from a 3rd party), and returns alerts when anomalies
are detected. For this task, feel free to pick an anomaly you think would be interesting to
track (e.g., changes in mood, change in emoji use, shifts in language, use of the phrase “I
don’t know”, prompt injection attacks, etc.). As part of your solution, provide a brief
README that outlines the architecture, setup instructions, and how to run tests.