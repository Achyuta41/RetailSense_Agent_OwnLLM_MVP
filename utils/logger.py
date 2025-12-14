import json
from datetime import datetime

def log_decision(query, tool,payload,result):
    log = {
        "timestamp": datetime.utcnow().isoformat(),
        "query": query,
        "tool": tool,
        "payload":payload,
        "result": result
    }

    with open("logs/decisions.log", "a") as f:
        f.write(json.dumps(log) + "\n")
