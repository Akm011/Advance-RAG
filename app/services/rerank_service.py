from retrieval.reranker.cross_encoder import rerank

def rerank_chunks(query, docs):
    return rerank(query, docs)