from retrieval.query_transform.hyde import generate_hypothetical_answer
from vectorstore.qdrant_client import search_vectors
from retrieval.reranker.cross_encoder import rerank

def retrieve_context(query: str):
    # Step 1: HyDE
    hyde_doc = generate_hypothetical_answer(query)

    # Step 2: Retrieve Top K
    results = search_vectors(hyde_doc, top_k=20)

    # Step 3: Rerank
    top_chunks = rerank(query, results)

    # Return combined context
    return "\n\n".join([chunk.page_content for chunk in top_chunks])