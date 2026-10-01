"""stryde-cascade: the fitter's B-roll wardrobe differs from the talking head (user, 2026-09-30:
"the avatar broll clothes should not be the same as the th"). One work outfit across his B-roll beats;
face from the cast sheet only, the TH frame is no longer attached. Writes calls/<BEAT>.gap2.image.json + preflight."""
import json, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from fill_gaps import BEATS, B, PF, THF

OUTFIT = ("in his B-roll work clothes, not the talking-head outfit: a worn tan canvas work jacket open over a "
          "dark green work shirt, charcoal work trousers, no fleece")
OLD = "in the navy fleece from the attached talking-head frame"
NOTE = 'user Fix 2026-09-30: "the avatar broll clothes should not be the same as the th" → TH frame dropped, new work outfit'
FIX = ["HK2-B0", "HK2-B3", "A5-B1", "A5-B1b"]

bad = 0
for b in BEATS:
    if b["beat"] not in FIX:
        continue
    assert OLD in b["prompt"], b["beat"]
    prompt = b["prompt"].replace(OLD, OUTFIT)
    refs = [r for r in b["refs"] if r != THF]
    c = {"beat": b["beat"], "kind": "image", "mode": 1, "prompt": prompt, "script_line": b["line"],
         "face": b["face"], "room": b["room"], "product": b["product"], "body": True,
         "refs": [{"label": r[1], "kind": r[2], "id": r[0]} for r in refs], "taste": b["taste"] + ["HT09"],
         "anatomy": False, "pair": ["nano_banana_pro", "nano_banana_pro"], "motion_plan": b["motion"],
         "model": "nano_banana_pro", "render_count": 1, "fix_note": NOTE,
         "note": "build keeps its step-2 image lock (nano_banana_pro); one render"}
    p = B / f"calls/{b['beat']}.gap2.image.json"
    json.dump(c, open(p, "w"), indent=1, ensure_ascii=False)
    out = subprocess.run(["python3", str(PF), str(p)], capture_output=True, text=True).stdout
    real = [l.strip() for l in out.splitlines() if l.strip().startswith("FAIL") and "Sunburst on realistic" not in l]
    bad += bool(real)
    print(f"{b['beat']:7} {len(prompt):5} chars  {'PASS/LOCK-ONLY' if not real else 'FAIL ' + ' | '.join(real)}")
sys.exit(1 if bad else 0)
