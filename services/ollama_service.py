# backend/services/ollama_service.py

import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "mistral"


def generate_tutorial_script(topic: str):
    """
    Sends the user topic to Ollama and gets back
    a beginner-friendly coding tutorial explanation.

    Example input:
    topic = "Teach me Python for loops"
    """

    prompt = f"""
    Explain {topic} in 4 short beginner-friendly steps.

    Rules:
    - Keep explanation simple
    - Include one short Python code example
    - Keep response clean and structured
    - Do not make it too long
    """

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()

        result = response.json()
        return result.get("response", "No response from Ollama")

    except requests.exceptions.RequestException as e:
        return f"Ollama connection error: {str(e)}"