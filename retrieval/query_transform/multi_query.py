from get_llm import get_llm

llm = get_llm()

def generate_queries(query: str): 
    prompt = f"""
    Generate 4 concise query variations for semantic search.

    Guidelines:
    - Use short, keyword-rich phrases
    - Focus on policy / compliance language
    - Avoid long sentences

    Query: {query}
    """

    response = llm.invoke(prompt)
    queries = response.content.split("\n")
    return [q.strip("- ") for q in queries if q.strip()]