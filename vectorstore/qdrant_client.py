# from langchain_community.vectorstores import Qdrant
from langchain_qdrant import Qdrant
from langchain_openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Load existing collection
vectorstore = Qdrant(
    collection_name="policy_docs",
    embeddings=embeddings,
    url="http://qdrant:6333"
)

def search_vectors(query, top_k=10):
    return vectorstore.similarity_search(query, k=top_k)