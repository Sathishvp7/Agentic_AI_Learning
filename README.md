# Personal Projects — AI / NLP Learning Lab

A structured collection of hands-on projects across **NLP**, **agent frameworks**, and **small language models (SLMs)**.

## Repository layout

```
Personal_projects/
├── nlp/                          # Classical / retrieval NLP (non-agent)
│   └── search-engine-biencoder-crossencoder/
│
├── agents/                       # Agentic AI frameworks
│   ├── langchain/                # Chains, runnables, memory, tools
│   ├── langgraph/                # Graph-based agents (ReAct, state machines)
│   ├── autogen/                  # Microsoft AutoGen (upcoming)
│   └── crewai/                   # CrewAI multi-agent (upcoming)
│
└── slms/                         # Small language models (upcoming)
```

## Projects index

| Path | Topic |
|------|--------|
| `nlp/search-engine-biencoder-crossencoder/` | Bi-encoder + cross-encoder search |
| `agents/langchain/product-recommendation/` | Multi-user product recommender (SQL memory) |
| `agents/langchain/travel-assistant/` | Travel AI agent |
| `agents/langgraph/text2sql-react/` | Text-to-SQL ReAct agent |
| `agents/langgraph/financial-stock-openbb/` | US stock analyst (OpenBB + ReAct) |
| `agents/langgraph/reflection-pattern/` | LangChain vs LangGraph reflection pattern |

## Adding a new project

1. Pick the right top-level folder (`nlp/`, `agents/<framework>/`, or `slms/`).
2. Create a **kebab-case** project folder, e.g. `agents/crewai/research-crew/`.
3. Add a short `README.md` inside the project (goal, stack, how to run).
4. Keep notebooks + data together in that project folder.

## Conventions

- **Folder names**: lowercase `kebab-case` (e.g. `product-recommendation`).
- **One project per folder**: notebook(s), data, and project `README.md` live together.
- **Secrets**: never commit API keys; use environment variables or local `.env` (gitignored).
