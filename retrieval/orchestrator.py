from retrieval.query_transform.hyde import generate_hypothetical_answer
from retrieval.reranker.cross_encoder import rerank
from retrieval.filtering.pre_filter import detect_category
from retrieval.filtering.post_filter import filter_latest_versions
from retrieval.query_transform.multi_query import generate_queries
from vectorstore.pinecone_client import vectorstore


def retrieve_chunks(search_queries, retriever):
    all_docs = []

    for q in search_queries:
        docs = retriever.invoke(q)
        all_docs.extend(docs)

    # remove duplicates
    unique_docs = {doc.page_content: doc for doc in all_docs}
    return list(unique_docs.values())

def retrieve_context(query: str):

    # Step 0: Detect Category
    category = detect_category(query)
    print(f"Detected category: {category}")

    retriever = vectorstore.as_retriever(
        search_kwargs={
            "k": 15,
            "filter": {
                "policy_category": category
            }
        }
    )

    # Step 1: HyDE
    hyde_doc = generate_hypothetical_answer(query)
    print(f"HyDE generated document: {hyde_doc}...")
    print("--------------------------------------")

    # Step 2: Generate multiple query variations
    queries = generate_queries(query)
    print(f"Generated query variations: {queries}")
    print("--------------------------------------")

    search_queries = [query] + queries + [hyde_doc]
    print(f"All search queries (original + variations + HyDE): {search_queries}")

    # Step 3: Retrieve Top K
    docs = retrieve_chunks(search_queries, retriever)
    print(f"Retrieved {len(docs)} unique documents before reranking.")
    print(f"Sample retrieved document: {docs[:5]}...")
    print("--------------------------------------")

    # docs = filter_latest_versions(docs)
    # print(f"After post-filter (latest versions): {len(docs)} docs")

    # Step 4: Rerank
    top_chunks = rerank(query, docs)
    print(f"Top chunks after reranking: {len(top_chunks)}")
    print(f"Sample top chunk: {top_chunks}...")
    print("--------------------------------------")

    # Return combined context
    return "\n\n".join([chunk.page_content for chunk in top_chunks])
    # return "DONE"

# res = retrieve_context("What are baggage allowances for travel policy?")
# print("--------------------------------------")
# print("final retrieved context:")
# print(res)