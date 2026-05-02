from sentence_transformers import CrossEncoder
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("HF_TOKEN")

model = CrossEncoder(
    "BAAI/bge-reranker-large",
    token=token
    )

def rerank(query, documents):
    pairs = [(query, doc.page_content) for doc in documents]
    scores = model.predict(pairs)

    ranked = sorted(zip(documents, scores), key=lambda x: x[1], reverse=True)

    return [doc for doc, _ in ranked[:5]]