import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.query_understanding import understand_query
from agents.synthesizer import synthesize_knowledge
from agents.advisor import generate_advice

def run_pipeline(user_query: str) -> dict:
    # 1. Understand query
    query_info = understand_query(user_query)

    # 2. Retrieve evidence
    knowledge = synthesize_knowledge(query_info)

    # 3. Generate final guidance
    advice = generate_advice(knowledge)

    return {
        "query": user_query,
        "category": advice["category"],
        "summary": advice["summary"],
        "advice_steps": advice["advice_steps"]
    }

if __name__ == "__main__":
    user_input = input("Enter your question for RuralAssist: ")
    result = run_pipeline(user_input)

    print("\n=== RuralAssist Response ===")
    print(f"Category: {result['category']}")
    print("\nSummary of retrieved evidence:")
    print(result["summary"])
    print("\nRecommended steps:")
    for i, step in enumerate(result["advice_steps"], start=1):
        print(f"{i}. {step}")
