
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(r"B:\RetailSense_Agent_MVP\agents")))

from agents.sales_agent import sales_agent

result = sales_agent(store_id=1)
print(result)
