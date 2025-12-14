
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(r"B:\RetailSense_Agent_MVP")))

from orchestrator.router import route_query
from orchestrator.schemas import InventoryRequest
from agents.inventory_agent import inventory_agent
from utils.logger import log_decision

def orchestrate(user_query: str, payload: dict):
    tool = route_query(user_query)

    if tool == "inventory_agent":
        validated = InventoryRequest(**payload)
        result = inventory_agent(
            store_id=validated.store_id,
            weeks=validated.weeks
        )

    else:
        result = {"error": "Unsupported request"}

    log_decision({
        "query": user_query,
        "tool": tool,
        "payload": payload,
        "result": result
    })

    return result
