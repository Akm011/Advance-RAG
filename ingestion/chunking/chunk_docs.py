from langchain_text_splitters import RecursiveCharacterTextSplitter
from ingestion.chunking.semantic_chunker import split_by_headers
from ingestion.chunking.table_handler import preserve_tables


def apply_overlap(chunks):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100  # ~10–15%
    )
    final_chunks = []

    for chunk in chunks:
        splits = splitter.split_documents([chunk])
        final_chunks.extend(splits)

    return final_chunks

def split_docs(docs):
    all_chunks = []

    for doc in docs:
        # Step 1: header-based split
        header_chunks = split_by_headers(doc)
        print(f"Header-based split resulted in {len(header_chunks)} chunks for document: {doc.metadata.get('source', 'unknown')}")
        # print(header_chunks[5])
        print("----------------------")

        # Step 2: preserve tables
        table_safe_chunks = preserve_tables(header_chunks)
        print(f"Table preservation resulted in {len(table_safe_chunks)} chunks for document: {doc.metadata.get('source', 'unknown')}")
        # print(table_safe_chunks[5])
        print("----------------------")

        # Step 3: overlap
        final_chunks = apply_overlap(table_safe_chunks)
        print(f"Overlap applied resulted in {len(final_chunks)} chunks for document: {doc.metadata.get('source', 'unknown')}")
        # print(final_chunks[5])
        print("----------------------")

        all_chunks.extend(final_chunks)

    return all_chunks