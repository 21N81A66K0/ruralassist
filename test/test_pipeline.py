# tests/test_pipeline.py
from app.orchestrator import run_pipeline

def test_basic_agri_query():
    out = run_pipeline("My maize leaves are turning yellow")
    assert "advice_steps" in out
    assert isinstance(out["advice_steps"], list)
