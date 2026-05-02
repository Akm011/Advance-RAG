from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_core.documents import Document

def split_by_headers(doc: Document):
    headers = [
        ("#", "h1"),
        ("##", "h2"),
        ("###", "h3"),
    ]

    splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers)

    chunks = splitter.split_text(doc.page_content)

    # Attach original metadata
    for chunk in chunks:
        chunk.metadata.update(doc.metadata)

    return chunks








# from langchain_text_splitters import RecursiveCharacterTextSplitter

# def split_docs(documents):
#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=1000,
#         chunk_overlap=200
#     )
#     return splitter.split_documents(documents)