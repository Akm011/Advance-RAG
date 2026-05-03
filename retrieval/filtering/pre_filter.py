from get_llm import get_llm

llm = get_llm()

def detect_category(query: str):
    prompt = f"""
    Classify the query into one category:
    [travel, security, training, work policy]

    Query: {query}

    Only return category name.
    """

    return llm.invoke(prompt).content.strip().lower()