import os
from ingestion.loaders.pdf_loader import load_pdf
from ingestion.loaders.text_loader import load_text_file
from ingestion.chunking.chunk_docs import split_docs
from vectorstore.pinecone_client import vectorstore

DATA_PATH = "data/"

def run():
    print("🚀 Starting ingestion process...")
    all_docs = []

    for category in os.listdir(DATA_PATH):
        category_path = os.path.join(DATA_PATH, category)

        for file in os.listdir(category_path):
            file_path = os.path.join(category_path, file)
            print(f"Processing {file_path}...Category: {category}")
            if file_path.endswith(".pdf"):
                docs = load_pdf(file_path)
            elif file_path.endswith(".txt"):
                docs = load_text_file(file_path)
            print(f"Loaded {len(docs)} documents from {file_path}")

            for doc in docs:
                doc.metadata["policy_category"] = category

            all_docs.extend(docs)
    print(f"Total documents loaded: {len(all_docs)}")
    chunks = split_docs(all_docs)
    print(f"Total chunks created: {len(chunks)}")
    # print(chunks[0])  # Print the content of the first chunk for verification
    # exit()
    vectorstore.add_documents(chunks)

    print("✅ Ingestion complete!")

if __name__ == "__main__":
    run()