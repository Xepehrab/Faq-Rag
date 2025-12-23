import chromadb
client= chromadb.PersistentClient(path="./chroma_db")
collection=client.get_or_create_collection(
    name="faq_rag",
    metadata={"hnsw:space": "cosine"}

)

def add_documents(chunks, embeddings):
    collection.add(
        ids=[f"id_{i}" for i in range(len(chunks))],
        documents=chunks,
        embeddings=embeddings
    )

def retrieve(query_embedding,top_k=3):
    return collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    