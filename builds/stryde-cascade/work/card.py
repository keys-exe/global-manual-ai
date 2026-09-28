"""Write a board card JSON (generations/<build>__<BEAT>) from local files; upload with ArtifactData file_path."""
import json, sys, time, argparse
from pathlib import Path
B = "stryde-cascade"
OUT = Path(__file__).parent / "board"; OUT.mkdir(exist_ok=True)
def card(beat, **f):
    p = OUT / f"{beat}.json"
    d = json.loads(p.read_text()) if p.exists() else {"build": B, "beat": beat}
    for k in ("imagePrompt", "prompt"):
        if isinstance(f.get(k), str) and f[k].startswith("@"):
            f[k] = Path(f[k][1:]).read_text()
    for k in ("imageVersions", "videoVersions"):
        if k in f and isinstance(f[k], dict):  # append one version
            d.setdefault(k, []).append(f.pop(k))
    d.update(f); d["updatedAt"] = int(time.time() * 1000)
    p.write_text(json.dumps(d, ensure_ascii=False, indent=1)); return p
if __name__ == "__main__":
    beat = sys.argv[1]; kv = {}
    for a in sys.argv[2:]:
        k, v = a.split("=", 1)
        try: v = json.loads(v)
        except Exception: pass
        kv[k] = v
    print(card(beat, **kv))
