import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "phi"

def explain_inventory_result(result: dict) -> str:
    """
    Uses LLM only to explain ML output.
    No decisions, no tools, no actions.
    """

    prompt = f"""
You are a retail analytics assistant.
Explain the inventory risk to the store owner.

Data:
- Store ID: {result['store_id']}
- Predicted Weekly Sales: {result['predicted_weekly_sales']}
- Risk Level: {result['risk_level']}

Rules:
- Do NOT suggest actions
- Only explain the meaning
- Keep it simple
"""

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    return response.json()["response"]
