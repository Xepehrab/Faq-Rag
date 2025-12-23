from embeddings import embed_query
from vectorstore import retrieve
from llm import llm
from config import SYSTEM_PROMPT


chat_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

def ask(question):
    query_vec = embed_query(question)
    results = retrieve(query_vec)

    context = "\n\n".join(results["documents"][0])

    chat_history.append({
        "role": "user",
        "content": f"Context:\n{context}\n\nQuestion:\n{question}"
    })

    answer = llm(chat_history)

    chat_history.append({
        "role": "assistant",
        "content": answer
    })

    return answer