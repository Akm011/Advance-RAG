import os
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("PINECONE_API_KEY")
if not api_key:
    raise ValueError("PINECONE_API_KEY not found")

pc = Pinecone(api_key=api_key)

index_name = "test-index"

# ✅ Create index ONLY if not exists
if index_name not in [i.name for i in pc.list_indexes()]:
    pc.create_index(
        name=index_name,
        dimension=3072,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

# ✅ Get index
index = pc.Index(index_name)

# ✅ Embeddings
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    api_key=os.getenv("OPENAI_API_KEY")
)


# ✅ Vectorstore
vectorstore = PineconeVectorStore(
    index=index,
    embedding=embeddings
)