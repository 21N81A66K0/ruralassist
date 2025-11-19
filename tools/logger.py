# tools/logger.py
import datetime
import json
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "ruralassist.log")
FEEDBACK_FILE = os.path.join(LOG_DIR, "feedback.jsonl")

def _now():
    return datetime.datetime.utcnow().isoformat() + "Z"

def log(msg: str, meta: dict = None):
    entry = {"ts": _now(), "msg": msg}
    if meta:
        entry["meta"] = meta
    line = json.dumps(entry, ensure_ascii=False)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"[RuralAssist][{entry['ts']}] {msg}")

def record_feedback(query: str, rating: str, comment: str = ""):
    """rating: helpful / unclear / unsafe"""
    entry = {"ts": _now(), "query": query, "rating": rating, "comment": comment}
    with open(FEEDBACK_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    log(f"Feedback recorded: {rating}", {"query": query})
