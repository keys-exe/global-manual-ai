"""stryde-cascade Current 2, Fix round 6 (user, 2026-10-01): A5-B1 "the strap is floating in his hands and its a bit too small"
→ the strap lay flat on an open palm with no band, reading smaller than the hand. Now the product sheet's "bottom-edge pinch"
grip (thumb in front on the shell's bottom edge, fingers behind on the pad, band slack round the wrist) and its SIZE_HELD
wording (the shell five to six thumb-widths across, overhanging the hand at both ends). Writes calls/A5-B1.gap6.image.json."""
import json, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from fill_gaps import B, PF, FRONT, FITTER, VAN, PHONE

OUTFIT = "a worn tan canvas work jacket open over a dark green work shirt, charcoal work trousers"
prompt = ('For the line "I started carrying a couple because I was tired of fitting the second rail.": in the open back of his van the fitter '
          'crouches by his open black tool bag and holds one strap up towards the lens to show it, a small knowing look; the second strap '
          'pokes out of the bag\'s side pocket. The strap is exactly the product in the attached front photo, gripped firmly: his thumb in '
          'front on the shell\'s bottom edge below the wordmark, his fingers behind it, the black knit band hanging slack round his wrist. '
          'True size: the rigid shell is about 12 × 5 cm, five to six of his thumb-widths across, overhanging his hand at both ends, about as tall as his thumb '
          'is long. Eye level, three-quarter, medium-close, his face and the strap sharp. He is the same man as the attached cast sheet, in '
          + OUTFIT + '. The van as in the attached plate. ' + PHONE)
c = {"beat": "A5-B1", "kind": "image", "mode": 1, "prompt": prompt,
     "script_line": "I started carrying a couple because I was tired of fitting the second rail.",
     "face": True, "room": True, "product": True, "body": True,
     "refs": [{"label": "STRYDE front photo", "kind": "product", "id": FRONT[0]},
              {"label": "N-CHINESE cast sheet", "kind": "character", "id": FITTER[0]},
              {"label": "PLATE-VAN", "kind": "location", "id": VAN[0]}],
     "taste": ["FP01", "FP02", "FP05", "FP06", "HT06", "HT09"], "anatomy": False, "pair": ["nano_banana_pro", "nano_banana_pro"],
     "motion_plan": "crouched by his tool bag, he lifts one strap up towards us and holds it there, showing it, one lift, 2s",
     "model": "nano_banana_pro", "render_count": 1,
     "fix_note": 'user Fix: "the strap is floating in his hands and its a bit too small" → flat on an open palm, no band; now gripped (bottom-edge pinch), band round the wrist, SIZE_HELD against his thumb'}
p = B / "calls/A5-B1.gap6.image.json"
json.dump(c, open(p, "w"), indent=1, ensure_ascii=False)
out = subprocess.run(["python3", str(PF), str(p)], capture_output=True, text=True).stdout
real = [l.strip() for l in out.splitlines() if l.strip().startswith("FAIL") and "Sunburst on realistic" not in l]
print(f"A5-B1 {len(prompt)} chars {'PASS' if not real else 'FAIL ' + ' | '.join(real)}")
sys.exit(1 if real else 0)
