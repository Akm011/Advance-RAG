# 🚀 Advanced RAG Policy Engine (Production-Ready)

## 📌 Overview

This project implements a **production-grade Retrieval-Augmented Generation (RAG)** system for querying enterprise policy documents with high accuracy.

It goes beyond basic RAG by incorporating:

* ✅ Semantic + structured ingestion
* ✅ Metadata-aware retrieval
* ✅ Query transformation (HyDE + Multi-query)
* ✅ Pre & post filtering
* ✅ Cross-encoder reranking
* ✅ FastAPI-based API layer

---

## 🧠 System Architecture

```text
User Query
   ↓
Query Transformation (Multi-query + HyDE)
   ↓
Metadata Routing (Pre-filter)
   ↓
Vector Search (Pinecone)
   ↓
Post-filter (latest version)
   ↓
Reranker (Cross-Encoder)
   ↓
LLM Answer Generation
```

---

## 📂 Project Structure

```text
project/
│
├── app/                        # API Layer (FastAPI)
│   ├── api/
│   │   ├── routes.py
│   │   └── dependencies.py
│   ├── core/
│   │   ├── config.py
│   │   └── logging.py
│   ├── models/
│   │   ├── request_models.py
│   │   └── response_models.py
│   ├── services/
│   │   ├── llm_service.py
│   │   ├── query_service.py
│   │   ├── rerank_service.py
│   │   └── retrieval_service.py
│   └── main.py
│
├── ingestion/                 # Data ingestion pipeline
│   ├── chunking/
│   │   ├── semantic_chunker.py
│   │   ├── markdown_chunker.py
│   │   ├── table_handler.py
│   │   └── chunk_docs.py
│   ├── loaders/
│   │   ├── pdf_loader.py
│   │   ├── text_loader.py
│   │   └── docx_loader.py
│   ├── metadata/
│   │   ├── extractor.py
│   │   └── schema.py
│   ├── embeddings/
│   │   └── embedding_model.py
│   ├── pipelines/
│   │   └── ingest_pipeline.py
│   └── run_ingestion.py
│
├── retrieval/                 # Retrieval pipeline
│   ├── filtering/
│   │   ├── pre_filter.py
│   │   └── post_filter.py
│   ├── query_transform/
│   │   ├── hyde.py
│   │   └── multi_query.py
│   ├── reranker/
│   │   └── cross_encoder.py
│   └── orchestrator.py
│
├── vectorstore/
│   └── pinecone_client.py
│
├── get_llm.py
└── README.md
```

---

## 🔄 Pipeline Breakdown

### 1. 📥 Ingestion Pipeline

* Supports: PDF, TXT, DOCX
* Performs:

  * Markdown-aware chunking
  * Table preservation
  * Semantic chunking
* Extracts metadata:

  * `document_id`
  * `policy_category`
  * `effective_date`
  * headers (H1, H2)

---

### 2. 🔍 Query Transformation

#### ✅ Multi-Query Expansion

Generates multiple semantic variations:

```text
"Taxi reimbursement?"
→ "Ground transport policy"
→ "Uber reimbursement rules"
```

---

#### ✅ HyDE (Hypothetical Document Embeddings)

* LLM generates a synthetic answer
* Improves retrieval by matching document structure

---

### 3. 🧭 Metadata Filtering

#### 🔹 Pre-Filtering

```sql
WHERE policy_category = 'security'
```

Prevents irrelevant domain retrieval.

---

#### 🔹 Post-Filtering

* Keeps only latest policy version
* Based on `effective_date`

---

### 4. 📊 Vector Retrieval

* Uses Pinecone similarity search
* `k = 20–30` per query
* Multi-query + HyDE → high recall

---

### 5. 🎯 Reranking

* Uses Cross-Encoder (BGE reranker)
* Evaluates query + chunk jointly
* Selects Top 5 chunks

---

### 6. 🤖 Answer Generation

* Uses OpenAI LLM
* Strictly grounded in retrieved context
* Minimizes hallucination

---

## ⚙️ Tech Stack

* **LLM**: OpenAI
* **Vector DB**: Pinecone
* **Reranker**: BGE
* **Framework**: LangChain
* **API**: FastAPI

---

## 🛠️ Setup

### 1. Create Virtual Environment

```bash
python -m venv .ragenv
.ragenv\Scripts\activate
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Environment Variables

Create `.env`:

```env
OPENAI_API_KEY=your_key
PINECONE_API_KEY=your_key
HF_TOKEN=your_token
```

---

## 🚀 Run Ingestion

```bash
python -m ingestion.run_ingestion
```

---

## 🚀 Run API

```bash
uvicorn app.main:app --reload
```

---

## 🔍 Test API

```text
http://localhost:8000/docs
```

---

## ⚠️ Important Notes

### 🔸 Pinecone Index Limit

* Free tier → max 5 indexes
* Use **check-before-create logic**

---

### 🔸 Embedding Dimension

| Model                  | Dimension |
| ---------------------- | --------- |
| text-embedding-3-small | 1536      |
| text-embedding-3-large | 3072      |

---

### 🔸 Metadata Consistency

```python
policy_category = "security"  # must match filter exactly
```

---

### 🔸 Date Parsing

```python
datetime.strptime(date, "%B %d, %Y")
```

---

## 🧪 Debug Checklist

If retrieval fails:

* [ ] Disable metadata filter
* [ ] Check Pinecone index exists
* [ ] Validate embeddings dimension
* [ ] Print metadata from stored docs
* [ ] Verify ingestion ran successfully

---

## 📈 Future Enhancements

* Hybrid search (BM25 + vector)
* Query decomposition
* LangGraph orchestration
* RAG evaluation (RAGAS)
* Streaming responses
* Chat memory

---

## 🧠 Key Learnings

* Retrieval quality > LLM quality
* Metadata filtering reduces hallucination
* Reranking is critical for precision
* HyDE improves semantic alignment

---

## 📌 One-line Summary

> A production-ready RAG system combining semantic search, metadata filtering, and reranking for accurate policy intelligence.

---