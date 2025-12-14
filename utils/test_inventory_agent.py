import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(r"B:\RetailSense_Agent_MVP\agents")))
from agents.inventory_agent import inventory_agent

result = inventory_agent(store_id=1)
print(result)
