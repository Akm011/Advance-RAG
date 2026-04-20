project-aegis/
│
├── app/                         # Main application (API layer)
│   ├── api/                     # FastAPI routes
│   │   ├── routes.py
│   │   └── dependencies.py
│   │
│   ├── core/                    # Config & settings
│   │   ├── config.py
│   │   └── logging.py
│   │
│   ├── services/                # Business logic
│   │   ├── query_service.py     # Handles query pipeline
│   │   ├── retrieval_service.py # Vector search + filtering
│   │   ├── rerank_service.py    # Cross-encoder reranking
│   │   └── llm_service.py       # LLM calls
│   │
│   ├── models/                  # Pydantic models (request/response)
│   │   ├── request_models.py
│   │   └── response_models.py
│   │
│   └── main.py                  # FastAPI entry point
│
├── ingestion/                   # Data ingestion pipeline (offline jobs)
│   ├── loaders/                 # Document loaders
│   │   ├── pdf_loader.py
│   │   └── docx_loader.py
│   │
│   ├── chunking/                # Chunking logic (VERY IMPORTANT)
│   │   ├── semantic_chunker.py
│   │   ├── markdown_chunker.py  # Header-aware chunking
│   │   └── table_handler.py
│   │
│   ├── metadata/                # Metadata extraction
│   │   ├── extractor.py
│   │   └── schema.py
│   │
│   ├── embeddings/              # Embedding generation
│   │   └── embedding_model.py
│   │
│   ├── pipelines/               # End-to-end ingestion pipeline
│   │   └── ingest_pipeline.py
│   │
│   └── run_ingestion.py         # Entry script
│
├── retrieval/                   # Advanced retrieval logic
│   ├── query_transform/
│   │   ├── multi_query.py       # Query expansion
│   │   └── hyde.py              # Hypothetical answer generation
│   │
│   ├── filtering/
│   │   ├── pre_filter.py        # Metadata filtering
│   │   └── post_filter.py
│   │
│   ├── reranker/
│   │   └── cross_encoder.py
│   │
│   └── orchestrator.py          # Full retrieval pipeline
│
├── vectorstore/                 # Vector DB integration
│   ├── qdrant_client.py
│   ├── pinecone_client.py
│   └── schema.py
│
├── data/                        # Raw data (your folders)
│   ├── security/
│   ├── training/
│   ├── travel/
│   └── work_policies/
│
├── evaluation/                  # Evaluation & testing
│   ├── metrics.py               # Relevance, faithfulness
│   └── eval_pipeline.py
│
├── tests/                       # Unit & integration tests
│   ├── test_ingestion.py
│   ├── test_retrieval.py
│   └── test_api.py
│
├── scripts/                     # Utility scripts
│   ├── reindex.py
│   └── cleanup.py
│
├── infra/                       # DevOps / Deployment
│   ├── docker/
│   │   └── Dockerfile
│   ├── docker-compose.yml
│   └── k8s/                     # (optional)
│
├── .env                         # Environment variables
├── requirements.txt
├── README.md
└── run.py                       # App runner

