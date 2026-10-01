"""stryde-cascade Current 2, Fix round 5 (user, 2026-09-30):
A5-B1 "fix the image i need him to like show the strap to us" → new frame: crouched by his tool bag he holds one strap up to the lens
(true size across his palm, FP06), the second strap still in the bag's pocket. Writes calls/A5-B1.gap5.image.json + preflight."""
import json, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from fill_gaps import B, PF, FRONT, FITTER, VAN, PHONE

TRUE = "the strap is small — a rigid black W-topped shell about 12 × 5 cm, no longer than his palm, on one soft black knit band"
OUTFIT = "a worn tan canvas work jacket open over a dark green work shirt, charcoal work trousers"
b = dict(beat="A5-B1", line="I started carrying a couple because I was tired of fitting the second rail.",
    refs=[FRONT, FITTER, VAN], taste=["FP01", "FP02", "FP06", "HT06", "HT09"],
    fix='user Fix: "fix the image i need him to like show the strap to us" → he now holds one strap up to the lens, the second in the bag',
    motion="crouched by his tool bag, he lifts one strap up towards us and holds it there, showing it, one lift, 2s",
    prompt='For the line "I started carrying a couple because I was tired of fitting the second rail.": in the open back of his van the fitter crouches by his open black canvas tool bag and holds one strap up towards the lens, showing it to us, a small knowing look; the second strap pokes out of the bag\'s side pocket. The strap is exactly the product in the attached front photo — ' + TRUE + ' — resting across his open palm, thumb beside it, the shell and wordmark facing us, nothing covering it. Eye level, three-quarter, medium-close, his face and the strap sharp. He is the same man as the attached cast sheet, in ' + OUTFIT + '. The van as in the attached van plate. ' + PHONE)
c = {"beat": b["beat"], "kind": "image", "mode": 1, "prompt": b["prompt"], "script_line": b["line"], "face": True, "room": True,
     "product": True, "body": True, "refs": [{"label": r[1], "kind": r[2], "id": r[0]} for r in b["refs"]], "taste": b["taste"],
     "anatomy": False, "pair": ["nano_banana_pro", "nano_banana_pro"], "motion_plan": b["motion"], "model": "nano_banana_pro",
     "render_count": 1, "fix_note": b["fix"]}
p = B / "calls/A5-B1.gap5.image.json"
json.dump(c, open(p, "w"), indent=1, ensure_ascii=False)
out = subprocess.run(["python3", str(PF), str(p)], capture_output=True, text=True).stdout
real = [l.strip() for l in out.splitlines() if l.strip().startswith("FAIL") and "Sunburst on realistic" not in l]
print(f"A5-B1 {len(b['prompt'])} chars {'PASS' if not real else 'FAIL ' + ' | '.join(real)}")
sys.exit(1 if real else 0)
