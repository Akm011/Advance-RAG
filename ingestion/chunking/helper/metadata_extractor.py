import re

def extract_global_metadata(text: str):
    metadata = {}

    # Document ID
    doc_id = re.search(r"Document ID:\s*(.*)", text)
    if doc_id:
        metadata["document_id"] = doc_id.group(1).strip()

    # Effective Date
    eff_date = re.search(r"Effective Date:\s*(.*)", text)
    if eff_date:
        metadata["effective_date"] = eff_date.group(1).strip()

    # Policy Owner
    owner = re.search(r"Policy Owner:\s*(.*)", text)
    if owner:
        metadata["policy_owner"] = owner.group(1).strip()

    return metadata