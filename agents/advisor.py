def generate_advice(knowledge: dict) -> dict:
    """Generate final advice from synthesized knowledge."""
    if knowledge is None:
        return {
            "category": "error",
            "summary": "Error processing query.",
            "advice_steps": ["Please try again with a clear question."]
        }
    
    category = knowledge.get("category", "unknown")
    evidence = knowledge.get("evidence_chunks", [])

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
    try:
        summary = " ".join(str(e) for e in evidence)[:600] + "..."
    except Exception:
        summary = "Evidence retrieved but could not summarize."

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
