from langchain_community.document_loaders import PyPDFLoader


def load_pdf(path):
    print(f"Loading PDF from {path}...")
    loader = PyPDFLoader(path)
    return loader.load()

# doc = load_pdf("data/security/Interview Question on resume.pdf")
# print(doc[0].page_content[:500])