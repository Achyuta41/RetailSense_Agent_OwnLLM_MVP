def route_query(user_query: str) -> str:
    """
    Rule-based router (MVP).
    Later replace with small LLM.
    """
    query = user_query.lower()

    if "stock" in query or "inventory" in query or "risk" in query:
        return "inventory_agent"

    if "sales" in query or "performance" in query:
        return "sales_agent"

    if "offer" in query or "discount" in query:
        return "offer_agent"

    return "unknown"
