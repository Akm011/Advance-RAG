from ingestion.chunking.helper.check_table import is_table

def preserve_tables(chunks):
    final_chunks = []

    for chunk in chunks:
        content = chunk.page_content

        if is_table(content):
            # keep table intact
            final_chunks.append(chunk)
        else:
            final_chunks.append(chunk)

    return final_chunks