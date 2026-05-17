# Personal Projects — AI / NLP Learning Lab

Hands-on projects across **NLP**, **agent frameworks** (LangChain, LangGraph, AutoGen, CrewAI), and **small language models (SLMs)**.

## Repository layout

```
Personal_projects/
├── nlp/
├── agents/
│   ├── langchain/
│   ├── langgraph/
│   ├── autogen/
│   └── crewai/
└── slms/
```

## Projects index

| Path | Stack | Description |
|------|--------|-------------|
| **NLP** | | |
| `nlp/search-engine-biencoder-crossencoder/` | Bi-encoder, cross-encoder | Semantic search engine |
| **LangChain** | | |
| `agents/langchain/product-recommendation/` | LangChain, SQL memory | Multi-user product recommender |
| `agents/langchain/travel-assistant/` | LangChain | Travel planning agent |
| **LangGraph** | | |
| `agents/langgraph/text2sql-react/` | LangGraph, ReAct | Natural language → SQL |
| `agents/langgraph/financial-stock-openbb/` | LangGraph, OpenBB | US stock analyst agent |
| `agents/langgraph/reflection-pattern/` | LangGraph | Reflection / critique pattern |
| `agents/langgraph/healthcare-customer-support-rag/` | LangGraph, RAG, Chroma | Healthcare support router + RAG |
| **AutoGen** | | |
| `agents/autogen/smart-health-assistant/` | AutoGen | BMI → diet → workout multi-agent |
| **CrewAI** | | |
| `agents/crewai/automated-code-debugging-assistant/` | CrewAI | Code analysis & correction crew |
| `agents/crewai/ai-mock-interviewer/` | CrewAI, Streamlit | Mock technical interview app |
| **SLMs** | | |
| `slms/bert-classification-full-finetune/` | BERT | Full fine-tuning for classification |
| `slms/tinyllama-1b-text2sql-sft/` | TinyLlama 1B | Supervised fine-tuning for Text2SQL |

## Conventions

- **Folder names**: lowercase `kebab-case`, one project per folder.
- **Secrets**: use `.env` locally (never commit API keys).
- **Course PDFs**: stored locally only (gitignored under `Course Handouts/` and `*.pdf`).

## Adding a new project

1. Choose `nlp/`, `agents/<framework>/`, or `slms/`.
2. Create `agents/crewai/my-new-project/` (example).
3. Add notebook/code + a short `README.md`.
4. Update this index table.
