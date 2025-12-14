import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(r"B:\RetailSense_Agent_MVP\orchestrator")))



from orchestrator.orchestrator import orchestrate


response = orchestrate(
    user_query="What is the inventory risk for store 1?",
    payload={"store_id": 1, "weeks": 3}
)

print(response)
