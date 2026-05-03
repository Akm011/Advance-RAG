# 🚀 Advanced RAG System – Policy Intelligence Engine

## 📌 Overview

This project implements a **production-grade Retrieval-Augmented Generation (RAG)** system for querying enterprise policy documents.

Unlike naive RAG, this system focuses on:

* Context-aware ingestion
* Metadata-driven filtering
* Query transformation (HyDE + Multi-query)
* High-precision retrieval with reranking

---

## 🧠 Architecture

```text
User Query
   ↓
Query Transformation (Multi-query + HyDE)
   ↓
Metadata Routing (Category Detection)
   ↓
Vector Search (Pinecone)
   ↓
Post-filtering (Latest Policy Version)
   ↓
Reranking (Cross-Encoder)
   ↓
LLM Answer Generation
```

---

## ⚙️ Tech Stack

* **LLM**: OpenAI (gpt-4o-mini)
* **Vector DB**: Pinecone
* **Reranker**: BGE (bge-reranker-large)
* **Framework**: LangChain
* **Embeddings**: OpenAI `text-embedding-3-large`

---

## 📂 Project Structure

```text
project/
│
├── ingestion/
│   ├── loaders/
│   ├── chunking/
│   └── run_ingestion.py
│
├── retrieval/
│   ├── query_transform/
│   │   ├── hyde.py
│   │   └── multi_query.py
│   ├── filtering/
│   │   ├── get_category.py
│   │   └── post_filter.py
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

### 1. 📥 Ingestion Engine

* Parses documents (PDF / TXT)
* Performs **semantic chunking**
* Adds metadata:

  * `document_id`
  * `policy_category`
  * `effective_date`
  * headers (`h1`, `h2`)
* Stores embeddings in Pinecone

---

### 2. 🔍 Query Transformation

#### ✅ Multi-Query Expansion

Generates multiple variations of user query:

```text
"What are taxi rules?"
→ "Ground transportation reimbursement"
→ "Uber policy"
```

#### ✅ HyDE (Hypothetical Document Embeddings)

LLM generates a **fake answer** to improve retrieval relevance.

---

### 3. 🧭 Metadata Filtering

#### 🔹 Pre-Filtering

Before retrieval:

```sql
WHERE policy_category = 'security'
```

Prevents irrelevant domains.

#### 🔹 Post-Filtering

After retrieval:

* Keeps only **latest policy version**
* Uses `effective_date`

---

### 4. 📊 Retrieval

* Uses Pinecone similarity search
* `k = 25` per query
* Multi-query + HyDE → high recall

---

### 5. 🎯 Reranking

* Uses Cross-Encoder (`bge-reranker-large`)
* Scores query + chunk together
* Selects **Top 5 most relevant chunks**

---

### 6. 🤖 Answer Generation

* Final LLM response uses only retrieved context
* Prevents hallucination

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

Create `.env` file:

```env
OPENAI_API_KEY=your_openai_key
PINECONE_API_KEY=your_pinecone_key
HF_TOKEN=your_huggingface_token
```

---

## 🚀 Run Ingestion

```bash
python -m ingestion.run_ingestion
```

---

## 🔍 Run Retrieval

```bash
python -m retrieval.orchestrator
```

---

## ⚠️ Important Notes

### 🔸 Pinecone Index Limit

Free tier allows only **5 indexes**

Fix:

* Reuse index
* Avoid creating index on every run

---

### 🔸 Embedding Dimension

| Model                  | Dimension |
| ---------------------- | --------- |
| text-embedding-3-small | 1536      |
| text-embedding-3-large | 3072      |

👉 Must match Pinecone index

---

### 🔸 Metadata Consistency

Ensure:

```python
policy_category = "security"  # lowercase
```

---

### 🔸 Date Format Handling

Your system uses:

```text
June 1, 2026
```

Use:

```python
datetime.strptime(date, "%B %d, %Y")
```

---

## 🧪 Debug Checklist

If retrieval fails:

* [ ] Check Pinecone index exists
* [ ] Verify metadata stored correctly
* [ ] Disable filter and test retrieval
* [ ] Check embedding dimension
* [ ] Print sample metadata

---

## 📈 Future Improvements

* Hybrid search (BM25 + vector)
* Query decomposition
* LangGraph orchestration
* RAG evaluation (RAGAS)
* Streaming responses

---

## 🧠 Key Learnings

* Retrieval quality > LLM quality
* Metadata filtering prevents hallucination
* Reranking is critical for precision
* HyDE improves semantic recall

---

## 📌 One-line Summary

> A production-grade RAG system with query expansion, metadata filtering, and reranking for accurate policy retrieval.

---