import requests
from config import OPENROUTER_KEY

def llm(messages):
    payload = {
        "model": "meta-llama/llama-4-maverick",
        "messages": messages,
        "temperature": 0.3,
        "max_tokens": 300
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_KEY}",
            "HTTP-Referer": "https://openrouter.ai"
        },
        json=payload
    ).json()

    return response["choices"][0]["message"]["content"]