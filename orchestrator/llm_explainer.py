import subprocess
import json

def explain_inventory_result(result: dict) -> str:
    """
    Uses local LLM (Ollama) ONLY to explain agent output.
    No tools, no decisions, no data access.
    """

    prompt = f"""
You are an AI assistant for a retail store owner.

Given the following inventory analysis result:
{json.dumps(result, indent=2)}

Explain this result in simple business language.
Do NOT suggest actions.
Do NOT invent numbers.
Do NOT call tools.
Just explain what this means.
"""

    response = subprocess.run(
        ["ollama", "run", "phi"],
        input=prompt,
        text=True,
        capture_output=True,
        encoding="utf-8",
    )

    return response.stdout.strip()
