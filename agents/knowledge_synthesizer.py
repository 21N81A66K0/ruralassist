# agents/knowledge_synthesizer.py

def synthesize_knowledge(query_info: dict) -> dict:
    """
    Mock synthesizer.
    Later: will call FAISS + embeddings.
    Now: returns a fake 'evidence summary' based on category.
    """
    category = query_info["category"]
    user_query = query_info["original_query"]

    if category == "agriculture":
        summary = (
            "This looks like an agriculture-related question. "
            "Common factors: soil nutrients, water management, pests, and local climate."
        )
    else:
        summary = (
            "This looks like a basic health-related question. "
            "General guidance: hygiene, nutrition, and seeking professional help when serious."
        )

    return {
        "original_query": user_query,
        "category": category,
        "evidence_summary": summary
    }
