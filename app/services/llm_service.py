from get_llm import get_llm

llm = get_llm()

def generate_answer(query: str, context: str):
    prompt = f"""
    Answer the question using ONLY the context below.

    Context:
    {context}

    Question:
    {query}
    """

    response = llm.invoke(prompt)
    return response.content