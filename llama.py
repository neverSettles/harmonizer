from llama_index import Document, GPTListIndex


documents = []
batch_size = 2

documents = SimpleDirectoryReader('data').load_data()
index = GPTVectorStoreIndex.from_documents(documents)

for raw_batch, processed_batch in get_batches_of_rows(csv_file, batch_size):
    document = Document(
        "Raw rows:\n"
        + "\n".join(raw_batch)
        + "\n\nProcessed rows:\n"
        + "\n".join(processed_batch)
    )
    documents.append(document)

index = GPTListIndex(documents)
query = "I have a dataset that has different data schemas and I want to harmonize them so that they use the same one. Can you provide python code that would turn Data Schema B into the same structure as Data Schema A, taking into account the field names, field descriptions and making sure that units and types of values are consistent?"

query_engine = index.as_query_engine(response_mode="default")
result_python_code = query_engine.query(query)

