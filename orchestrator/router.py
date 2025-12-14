OLLAMA_PATH= r"C:\Users\achyu\AppData\Local\Programs\Ollama\ollama.exe"
import subprocess
import json


ROUTER_PROMPT = """
You are a STRICT router.
Your job is to choose ONE tool.

Available tools:
- inventory_agent
- sales_agent
- offer_agent
- notification_agent

Rules:
- Return ONLY JSON
- Format: {"tool": "<tool_name>"}
- No explanations
- If unclear, return {"tool": "unknown"}

User query:
"""

def route_intent(user_query: str) -> str:
    prompt = ROUTER_PROMPT + user_query

    result = subprocess.run(
        [OLLAMA_PATH, "run", "phi"],
        input=prompt,
        text=True,
        capture_output=True
    )

    output = result.stdout.strip()

    try:
        response = json.loads(output)
        return response.get("tool", "unknown")
    except Exception:
        return "unknown"
