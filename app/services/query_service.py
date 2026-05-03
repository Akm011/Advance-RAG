from app.services.retrieval_service import get_context
from app.services.llm_service import generate_answer

def handle_query(query: str):
    # Step 1: Retrieve context
    context = get_context(query)

    # Step 2: Generate answer
    answer = generate_answer(query, context)

    return {
        "answer": answer,
        "sources": []  # you can enhance later
    }