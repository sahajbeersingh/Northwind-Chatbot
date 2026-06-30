def validate_query(query):
    for path in query["expand"]:
        if path.count("/") >= 2:
            entities = path.split("/")

            return {
                "valid": False,
                "message":
                    f"I can't retrieve {' → '.join(entities)} in a single query because it requires navigating through multiple related entities. Try a simpler query."
            }
    return {"valid": True}