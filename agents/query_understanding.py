# agents/query_understanding.py

AGRI_KEYWORDS = [
    "crop", "maize", "rice", "wheat", "plant", "leaves", "soil",
    "fertilizer", "pest", "harvest", "agriculture", "farm", "yield"
]

HEALTH_KEYWORDS = [
    "fever", "cold", "dehydration", "headache", "vomit",
    "health", "pain", "cough"
]

def understand_query(user_query: str) -> dict:
    text = user_query.lower()

    agri_score = sum(1 for k in AGRI_KEYWORDS if k in text)
    health_score = sum(1 for k in HEALTH_KEYWORDS if k in text)

    # *** NEW: Out-of-domain detection ***
    if agri_score == 0 and health_score == 0:
        return {
            "original_query": user_query,
            "category": "out_of_domain",
            "clean_query": user_query.strip()
        }

    category = "agriculture" if agri_score >= health_score else "health"

    return {
        "original_query": user_query,
        "category": category,
        "clean_query": user_query.strip()
    }
