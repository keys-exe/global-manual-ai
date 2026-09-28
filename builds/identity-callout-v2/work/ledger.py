import json, sys, time
from pathlib import Path
L = Path(__file__).resolve().parents[1] / "run_ledger.json"
def load():
    return json.loads(L.read_text()) if L.exists() else {"build":"identity-callout-v2","version_built_against":"7.60.7","run_mode":"AUTOMATIC","beats":{},"spend":{},"events":[]}
def save(d): L.write_text(json.dumps(d, indent=1))
def beat(bid, **kw):
    d = load(); b = d["beats"].setdefault(bid, {"beat_id": bid, "retries": []}); b.update(kw); save(d)
def event(msg):
    d = load(); d["events"].append({"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "msg": msg}); save(d)
if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "beat": beat(sys.argv[2], **json.loads(sys.argv[3]))
    elif cmd == "event": event(sys.argv[2])
