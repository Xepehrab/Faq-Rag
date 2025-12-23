from cleaning import clean_text
from config import EMBEDDING_KEY
import requests
def embed_passages(text):
    payload={
        "model": "intfloat/multilingual-e5-large",
        "input": [f"passages:{t}" for t in text]

    }
    response=requests.post(
        "https://openrouter.ai/api/v1/embeddings",
        headers={"Authorization": f"Bearer {EMBEDDING_KEY}"},
        json=payload

    ).json()

    return [item["embedding"] for item in response['data']]


def embed_query(text):
        payload = {
        "model": "intfloat/multilingual-e5-large",
        "input": [f"query: {text}"]
    }

        response = requests.post(
        "https://openrouter.ai/api/v1/embeddings",
        headers={"Authorization": f"Bearer {EMBEDDING_KEY}"},
        json=payload
    ).json()

        return response["data"][0]["embedding"]
