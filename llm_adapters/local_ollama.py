import requests

def local_llm_chat(prompt: str) -> str:
    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    })
    return response.json().get("response", "")
