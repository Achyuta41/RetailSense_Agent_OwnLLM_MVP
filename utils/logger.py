import json
from datetime import datetime

LOG_FILE = "logs/decisions.log"

def log_decision(data: dict):
    data["timestamp"] = datetime.utcnow().isoformat()
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(data) + "\n")
