from langchain_text_splitters import MarkdownHeaderTextSplitter
from ingestion.chunking.helper.metadata_extractor import extract_global_metadata
from langchain_core.documents import Document

def split_by_headers(doc: Document):
    headers = [
        ("#", "h1"),
        ("##", "h2"),
        ("###", "h3"),
    ]
    # Extract global metadata ONCE per doc
    global_meta = extract_global_metadata(doc.page_content)
    splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers)

    chunks = splitter.split_text(doc.page_content)

    # Attach original metadata
    for chunk in chunks:
        chunk.metadata.update(doc.metadata)
        chunk.metadata.update(global_meta)

    return chunks








# from langchain_text_splitters import RecursiveCharacterTextSplitter

# def split_docs(documents):
#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=1000,
#         chunk_overlap=200
#     )
#     return splitter.split_documents(documents)