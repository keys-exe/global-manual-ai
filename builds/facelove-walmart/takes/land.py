#!/usr/bin/env python3
"""Land finished takes: download, music check (clips with sound), clean with unmusic.py, write takes/landed.json.
Usage: land.py '{"SC02-T1": "<result_url>", ...}'"""
import json, pathlib, subprocess, sys
H = pathlib.Path(__file__).parent
S = H.parents[2] / ".claude/skills/ai-prompt-engineer/scripts"
urls = json.loads(sys.argv[1])
L = json.load(open(H / "landed.json")) if (H / "landed.json").exists() else {}
for t, u in urls.items():
    raw = H / f"{t}_v1.mp4"
    subprocess.run(["curl", "-sS", "-o", str(raw), u], check=True)
    dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(raw)]).decode())
    has_a = bool(subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries", "stream=index", "-of", "csv=p=0", str(raw)]).decode().strip())
    rec = {"url": u, "raw": str(raw), "dur": round(dur, 2), "size": raw.stat().st_size, "audio": has_a, "music": None, "clean": None}
    if has_a:
        out = subprocess.run([sys.executable, str(S / "unmusic.py"), "--check", str(raw)], capture_output=True, text=True).stdout.strip().splitlines()[-1]
        rec["music"] = out
        if out.startswith("MUSIC"):
            (H / "clean").mkdir(exist_ok=True)
            subprocess.run([sys.executable, str(S / "unmusic.py"), "--out-dir", str(H / "clean"), str(raw)], capture_output=True, text=True)
            c = H / "clean" / f"{t}_v1.nomusic.mp4"
            chk = subprocess.run([sys.executable, str(S / "unmusic.py"), "--check", str(c)], capture_output=True, text=True).stdout.strip().splitlines()[-1]
            rec["clean"] = str(c); rec["clean_check"] = chk; rec["clean_size"] = c.stat().st_size
    L[t] = rec
    print(t, rec["dur"], rec["music"], rec.get("clean_check"))
json.dump(L, open(H / "landed.json", "w"), indent=1)
