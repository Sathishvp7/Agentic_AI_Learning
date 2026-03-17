# LangChain Product Recommendation (Multi-user + SQL Memory)

An end-to-end **product recommendation assistant** built with **LangChain**.  
It turns natural-language requests into **pandas filters** over a product catalog and then generates **recommendations with rationale**. It also supports **multi-user conversations** with **persistent chat history (SQLite)** and **history-aware query rephrasing** for follow-up questions.

## What this project does

Given a user query like:
- “Looking for a tablet with > 10 inch display and at least 64GB storage”
- “Make it cheaper” (follow-up)

The system:
- **(1) Rephrases** follow-up queries into a standalone query using past conversation history.
- **(2) Generates a pandas query** (LLM → code) to filter the product catalog (`Ecommerce_Product_List.csv` loaded into a dataframe).
- **(3) Recommends products** from the filtered table (no hallucinated products), including a brief “why”.
- **(4) Persists chat history** per user/session in **SQLite** (`memory.db`) so the assistant can continue across runs.

## Key LangChain concepts covered

- **Sequential chaining (pipeline)**: filter → recommend
- **Input-preserving pipelines**: mapping + `RunnablePassthrough.assign(...)`
- **Parallel/fan-out composition**: build structured inputs for downstream steps
- **Conditional handling**: respond to greetings/generic queries without recommending products
- **Safety/guardrails**: constrain the LLM to schema-safe pandas expressions and avoid inventing products
- **Persistent memory (SQL / SQLite)**: `SQLChatMessageHistory`
- **Automatic history handling**: `RunnableWithMessageHistory`
- **Contextual query rephrasing**: history-aware follow-up → standalone query

## Project structure

- `Product_recommendation.ipynb` — complete notebook implementation
- `Ecommerce_Product_List.csv` — sample product catalog used in the notebook
- `memory.db` — created at runtime (SQLite chat history; **not committed**)

## How it works (pipeline)

1. **Catalog filter chain**
   - Prompt instructs the model to output **only a pandas query** using known columns:
     `Category`, `Price_USD`, `Rating` (plus identifier/name/description columns in the table).
   - The query is executed against the dataframe to produce a filtered markdown table.

2. **Recommendation chain**
   - Takes `product_table` + `user_query`
   - Produces a concise recommendation list (name, price, rating, description) + rationale
   - Explicitly constrained to **recommend only from the provided table**

3. **Conversation + multi-user memory**
   - Each user/session is identified by a `session_id`
   - `SQLChatMessageHistory(session_id, "sqlite:///memory.db")` stores history per session
   - A windowed history function keeps only the last *K* turns for context
   - `RunnableWithMessageHistory` automatically loads and updates history on every call

## Setup

### Prerequisites
- Python 3.10+ (recommended: 3.11/3.12)
- Jupyter Notebook / JupyterLab

### Install dependencies

If you’re running exactly like the notebook:

```bash
pip install langchain==0.3.21 langchain-openai==0.3.9 langchain-community==0.3.19
```

You’ll also need typical notebook utilities used in the notebook (examples):

```bash
pip install pandas rich colorama
```

### Configure API key

This notebook uses **OpenAI** via `langchain-openai`.

- Set environment variable:

```bash
setx OPENAI_API_KEY "YOUR_KEY_HERE"
```

Or enter it interactively when prompted in the notebook (if you keep that cell).

## Run

1. Open `Product_recommendation.ipynb`
2. Run all cells
3. Try the chat helper with a user id/session id, for example:
   - `user_id = "AI001"`
   - `chat_with_llm("looking for a tablet", user_id)`
   - Follow up: `chat_with_llm("cheaper options", user_id)`

## Notes on safety

This project intentionally constrains the LLM to:
- Use only known dataframe columns (schema-based prompting)
- Output **only** a pandas query string for filtering
- Recommend only items present in the filtered product table

## Roadmap / possible improvements

- Add stricter parsing/validation for generated pandas queries (avoid `eval`)
- Convert to a small Streamlit/Gradio app
- Add unit tests for routing, filtering, and recommendation formatting
- Add richer metadata filtering (brand, specs, etc.) with a larger catalog

## License

Choose a license (MIT is common for learning projects). Add a `LICENSE` file if you plan to open source it.

