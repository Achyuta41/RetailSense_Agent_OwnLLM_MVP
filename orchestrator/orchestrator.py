
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(r"B:\RetailSense_Agent_MVP")))
from agents.inventory_agent import inventory_agent
from orchestrator.schemas import InventorySchema
from orchestrator.llm_explainer import explain_inventory_result
from utils.logger import log_decision

def orchestrate(user_query, payload):
    # Validate input
    validated = InventorySchema(**payload)

    # Call deterministic agent
    result = inventory_agent(
        store_id=validated.store_id,
        weeks=validated.weeks
    )

    # LLM explanation (read-only)
    explanation = explain_inventory_result(result)

    # Log everything
    log_decision(
        query=user_query,
        tool="inventory_agent",
        payload=payload,
        result=result
    )

    return {
        "result": result,
        "explanation": explanation
    }
