import pandas as pd
from cleaning import clean_text
from embeddings import embed_passages
from vectorstore import add_documents
from rag import ask

df = pd.read_csv("QA.csv")

chunks = [
    f"Question: {clean_text(q)}\nAnswer: {clean_text(a)}"
    for q, a in zip(df["Questions"], df["Answers"])
    if q and a
]

embeddings = embed_passages(chunks)
add_documents(chunks, embeddings)

print(ask("نحوه ثبت نام چگونه است؟"))