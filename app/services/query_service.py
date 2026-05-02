from retrieval.orchestrator import retrieve_context
from app.services.llm_service import generate_answer

def handle_query(query: str):
    context = retrieve_context(query)
    answer = generate_answer(query, context)
    return answer