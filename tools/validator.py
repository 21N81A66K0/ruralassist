# tools/validator.py
from typing import List

TRUSTED_SOURCES = ["gov", "who", "faO", "agr", "icAR"]  # use simple tokens matched in metadata

def score_source_trust(metadata: dict) -> float:
    """Return a simple trust score 0..1 based on metadata (filename, domain)."""
    name = (metadata.get("source") or "").lower()
    score = 0.1
    for token in TRUSTED_SOURCES:
        if token.lower() in name:
            score += 0.3
    return min(score, 1.0)

def detect_conflict(evidence: List[str]) -> bool:
    """Very simple conflict detection: checks for contradictory keywords."""
    negatives = ["do not", "avoid", "contraindicat", "not recommended"]
    positives = ["recommended", "use", "apply", "safe"]
    found_neg = any(any(tok in chunk.lower() for tok in negatives) for chunk in evidence)
    found_pos = any(any(tok in chunk.lower() for tok in positives) for chunk in evidence)
    return found_neg and found_pos
