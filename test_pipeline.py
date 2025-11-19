"""
Test script for RuralAssist pipeline
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.orchestrator import run_pipeline

# Test queries
test_queries = [
    "My maize leaves are turning yellow",
    "How to treat dehydration",
    "Tell me about politics"
]

print("=" * 60)
print("RuralAssist - Pipeline Test")
print("=" * 60)

for query in test_queries:
    print(f"\n📝 Query: {query}")
    print("-" * 60)
    try:
        result = run_pipeline(query)
        print(f"✅ Category: {result['category']}")
        print(f"\n📚 Summary:\n{result['summary']}\n")
        print("📋 Recommended Steps:")
        for i, step in enumerate(result["advice_steps"], 1):
            print(f"   {i}. {step}")
    except Exception as e:
        print(f"❌ Error: {e}")
    print()

print("=" * 60)
print("Test Complete!")
print("=" * 60)
