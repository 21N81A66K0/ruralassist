# tools/feedback_cli.py
from tools.logger import record_feedback

def feedback_prompt(query: str, summary: str):
    print("\n--- FEEDBACK ---")
    print("Summary shown: ", summary[:400])
    rating = input("Was this helpful? (helpful / unclear / unsafe) ").strip().lower()
    comment = input("Optional comment: ").strip()
    record_feedback(query, rating, comment)
    print("Thank you — feedback saved.")

