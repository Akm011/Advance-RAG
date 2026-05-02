from langchain_core.documents import Document

def load_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    return [Document(page_content=text, metadata={"source": file_path})]

# to test the text-loader
# doc = load_text_file("data/security/it security and data privacy.txt")
# print(doc[0].page_content)