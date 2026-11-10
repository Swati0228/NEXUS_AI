# NexusAI — Autonomous Multi-Agent Research Copilot

An agentic RAG platform architected with **LangGraph**, where a supervisor agent plans and delegates to specialized agents (retriever, web-researcher, code-executor, critic) to produce cited, verified research reports from PDFs, documents, and live web sources.

---

## 🌟 Key Features & Architecture

- **Agentic Orchestration (LangGraph):**
  - **Supervisor Agent:** Plans research workflows and routes tasks to specialized workers.
  - **Specialized Agents:**
    - `retriever`: Knowledge base and document lookup.
    - `web-researcher`: Real-time web queries and fact extraction.
    - `code-executor`: Python REPL / sandbox for computation and data analysis.
    - `critic`: Verification, self-reflection loops, and citation checking.
  - **Human-in-the-Loop:** Checkpoints for review and steering.

- **Advanced RAG Pipeline:**
  - **Hybrid Search:** Dense embeddings (Pinecone) + Sparse lexical search (BM25).
  - **Query Transformation:** Query expansion & rewriting.
  - **Reranking:** Cross-encoder re-ranking for top precision.
  - **Corrective-RAG (CRAG):** Evaluates retrieved document relevance and falls back to web search when necessary.
  - **Evaluation:** Evaluated on faithfulness, answer relevance, and context precision with RAGAS.
  - **MCP Integration:** Model Context Protocol tools for modular agent capabilities.

- **Production-Ready Backend & Serving:**
  - **FastAPI:** Server-Sent Events (SSE) streaming responses.
  - **Redis Semantic Caching:** Reduce latency and LLM API costs.
  - **Guardrails:** Prompt injection detection and input safety sanitization.
  - **Observability:** LangSmith tracing for full agent execution visibility.

- **Modern Frontend & Deployment:**
  - **React Chat UI:** Interactive conversation interface with source citation previews and agent status tracking.
  - **Docker Compose:** One-command orchestration for backend, frontend, Redis, and dependencies.

---

## 📁 Project Structure

```text
Nexus AI/
├── backend/                  # FastAPI & LangGraph backend
│   ├── app/
│   │   ├── agents/           # Supervisor, retriever, web-researcher, etc.
│   │   ├── rag/              # Hybrid search, reranking, Pinecone integration
│   │   ├── api/              # FastAPI routes and SSE streaming
│   │   ├── core/             # Configuration, Redis caching, guardrails
│   │   └── main.py           # Application entrypoint
│   ├── requirements.txt      # Python dependencies
│   └── Dockerfile
├── frontend/                 # React chat interface
│   └── ...
├── docker-compose.yml        # Multi-service local deployment
├── .env.example              # Environment variables template
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

*(Step-by-step setup guides will be populated as each component is implemented)*
