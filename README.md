Built a multi-user Product Recommendation assistant using LangChain (end-to-end in a notebook).

Core idea

Take a user’s natural-language request
If it’s a follow-up question, rephrase it into a standalone query using chat history (so filtering stays accurate)
Use an LLM to generate a pandas filter query over a product catalog table
Feed the filtered products into another LLM step to produce recommendations + short reasoning
Support multiple users/sessions with persistent memory in SQLite (each user gets their own history)
What I implemented (LangChain concepts)

✅ Sequential chaining (Pipeline)
✅ Input-preserving pipelines (RunnablePassthrough + mapping)
✅ Parallel/fan-out composition (build inputs + join downstream)
✅ Conditional routing (handle greetings vs recommendation queries)
✅ Safety moderation / guardrails
✅ Persistent memory (SQLite) with SQLChatMessageHistory
✅ Automatic history handling with RunnableWithMessageHistory
✅ Query contextualization: history-aware follow-up → standalone query rephrasing
