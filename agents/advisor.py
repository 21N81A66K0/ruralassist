def generate_advice(knowledge: dict) -> dict:
    category = knowledge["category"]
    evidence = knowledge["evidence_chunks"]

    # If no evidence, fallback safe response
    if not evidence:
        return {
            "category": category,
            "summary": "No strong evidence was found in local documents.",
            "advice_steps": [
                "Re-check symptoms or provide more details.",
                "Try another query with a specific crop, symptom, or health condition.",
            ]
        }

    # Simple summarization logic (offline)
    summary = " ".join(evidence)[:600] + "..."

    # Agriculture-specific template
    if category == "agriculture":
        advice = [
            "Inspect the affected crop section carefully for pests, discoloration, or rot.",
            "Compare symptoms with the recommended practices found in the retrieved evidence.",
            "Check soil fertility, moisture, and drainage as these commonly influence the symptoms.",
            "Apply corrective fertilizer or treatment only if evidence supports it.",
            "Avoid pesticide overuse; follow safe dosage guidelines.",
        ]
    else:
        # Health template
        advice = [
            "Avoid unverified home remedies that may worsen the condition.",
            "Follow general safety guidelines mentioned in the evidence.",
            "Monitor symptoms closely for 24 hours.",
            "Seek medical support if symptoms escalate or persist.",
        ]

    return {
        "category": category,
        "summary": summary,
        "advice_steps": advice
    }

def generate_advice(knowledge: dict) -> dict:
    category = knowledge["category"]

    # NEW: Safe fallback for irrelevant queries
    if category == "out_of_domain":
        return {
            "category": "out_of_domain",
            "summary": "Your query does not match agriculture or basic health topics.",
            "advice_steps": [
                "RuralAssist specializes only in crop and rural health guidance.",
                "Please ask a question about crops, soil, pests, fertilizers, or simple health queries.",
                "Example: 'My maize leaves are turning yellow' or 'How to treat dehydration?'"
            ]
        }
