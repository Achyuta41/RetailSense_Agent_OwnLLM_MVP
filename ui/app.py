import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(r"B:\RetailSense_Agent_MVP\orchestrator")))

import streamlit as st
from orchestrator.orchestrator import orchestrate

st.set_page_config(page_title="RetailSense Agent", layout="centered")

st.title("🛒 RetailSense Agent – Admin Dashboard")

query = st.text_input("Ask something:", "What is the inventory risk for store 1?")
store_id = st.number_input("Store ID", value=1)
weeks = st.number_input("Weeks", value=3)


if st.button("Run Agent"):
    response = orchestrate(
        user_query=query,
        payload={
            "store_id": store_id,
            "weeks": weeks
        }
    )

    st.subheader("📊 Inventory Result")
    st.json(response["result"])

    st.subheader("🧠 AI Explanation")
    st.write(response["explanation"])
