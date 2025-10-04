# LawMind – Legal Document Intelligence Engine
LawMind is a legal AI assistant that helps with legal research and document analysis.


**Built for FutureStack GenAI Hackathon by WeMakeDevs**

## 🚀 Stack
- Cerebras API – Legal clause extraction
- Meta Llama 3 – Summarization + Fairness scoring
- Docker MCP – Multi-service orchestration

lawmind/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── cerebras_client.py
│   ├── clause_extractor.py
│   └── uploads/
│
├── frontend/
│   ├── pages/
│   │   └── upload.js
│   ├── components/
│   │   └── ClauseViewer.jsx
│   └── package.json
│
├── docker/
│   ├── Dockerfile.backend
│   └── Dockerfile.frontend
│
└── README.md


## 🧩 Features
- Upload contracts
- Extract & classify clauses
- Rate fairness (0–100)
- Summarize in plain English

