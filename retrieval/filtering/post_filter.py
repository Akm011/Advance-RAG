from datetime import datetime

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%B %d, %Y")
    except:
        return None


def filter_latest_versions(chunks):
    latest_docs = {}

    for chunk in chunks:
        doc_id = chunk.metadata.get("document_id")
        date = chunk.metadata.get("effective_date")

        # DEBUG
        print("Checking:", doc_id, date)
        
        if not doc_id or not date:
            continue

        date_obj = parse_date(date)
        if not date_obj:
            continue

        if doc_id not in latest_docs or date_obj > latest_docs[doc_id][1]:
            latest_docs[doc_id] = (chunk, date_obj)

    return [v[0] for v in latest_docs.values()]