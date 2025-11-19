# eval/evaluate_retrieval.py
import json
from agents.synthesizer import synthesize_knowledge
from agents.query_understanding import understand_query

TEST_QUERIES = [
    {"q": "My maize leaves are turning yellow", "expected": "nitrogen"},
    {"q": "What is the right dose of urea for maize?", "expected": "fertilizer"},
    # add more labeled examples
]

def evaluate():
    results = []
    for t in TEST_QUERIES:
        qi = understand_query(t["q"])
        res = synthesize_knowledge(qi)
        # crude metric: check expected keyword in retrieved evidence text
        evidence_text = " ".join(res.get("evidence_chunks", []))
        hit = 1 if t["expected"].lower() in evidence_text.lower() else 0
        results.append({"query": t["q"], "expected": t["expected"], "hit": hit})
    score = sum(r["hit"] for r in results) / len(results)
    print("Retrieval accuracy:", score)
    with open("eval/results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    return score

if __name__ == "__main__":
    evaluate()

