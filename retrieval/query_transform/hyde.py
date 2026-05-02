from get_llm import get_llm

# LLM writes fake answer → better semantic match
llm = get_llm()

def generate_hypothetical_answer(query):
    prompt = f"""
    Generate a hypothetical policy answer to help retrieve relevant documents.

    Guidelines:
    - Use enterprise policy language (BYOD, MDM, compliance, access control)
    - Do NOT introduce unrelated concepts
    - Focus on likely requirements, not detailed procedures
    - Keep it concise and factual

    Query: {query}
    """
    response = llm.invoke(prompt)
    return response.content