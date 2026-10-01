"""stryde-cascade Current 2, Fix round 7 (user, 2026-10-01): A5-B1 "he is holding the 2 straps showing to us"
→ v5 showed one strap held up and the second in the bag pocket. Now he holds both straps up, one in each hand, the same
bottom-edge pinch grip and SIZE_HELD wording as round 6 on each. Writes calls/A5-B1.gap7.image.json."""
import json, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from fill_gaps import B, PF, FRONT, FITTER, VAN, PHONE

OUTFIT = "a worn tan canvas work jacket open over a dark green work shirt, charcoal work trousers"
prompt = ('For the line "I started carrying a couple because I was tired of fitting the second rail.": in the open back of his van the fitter '
          'crouches by his open black tool bag and holds up two straps towards the lens, one in each hand, showing them, a small knowing look. '
          'Each strap is exactly the product in the attached front photo, gripped firmly: his thumb in front on the shell\'s bottom edge below '
          'the wordmark, fingers behind, its black knit band hanging slack round his wrist. True size: each rigid shell is about 12 × 5 cm, '
          'five to six of his thumb-widths across, overhanging his hand at both ends. Exactly two straps, both identical. Eye level, three-quarter, medium-close, his face and both straps sharp. He is the same man as the attached cast sheet, in '
          + OUTFIT + '. The van as in the attached plate. ' + PHONE)
c = {"beat": "A5-B1", "kind": "image", "mode": 1, "prompt": prompt,
     "script_line": "I started carrying a couple because I was tired of fitting the second rail.",
     "face": True, "room": True, "product": True, "body": True,
     "refs": [{"label": "STRYDE front photo", "kind": "product", "id": FRONT[0]},
              {"label": "N-CHINESE cast sheet", "kind": "character", "id": FITTER[0]},
              {"label": "PLATE-VAN", "kind": "location", "id": VAN[0]}],
     "taste": ["FP01", "FP02", "FP05", "FP06", "HT06", "HT09"], "anatomy": False, "pair": ["nano_banana_pro", "nano_banana_pro"],
     "motion_plan": "crouched by his tool bag, he lifts the two straps, one in each hand, up towards us and holds them there, showing them, one lift, 2s",
     "model": "nano_banana_pro", "render_count": 1,
     "fix_note": 'user Fix: "he is holding the 2 straps showing to us" → v5 held one strap up, the second in the bag pocket; now both straps held up, one in each hand, same grip and true size'}
p = B / "calls/A5-B1.gap7.image.json"
json.dump(c, open(p, "w"), indent=1, ensure_ascii=False)
out = subprocess.run(["python3", str(PF), str(p)], capture_output=True, text=True).stdout
real = [l.strip() for l in out.splitlines() if l.strip().startswith("FAIL") and "Sunburst on realistic" not in l]
print(f"A5-B1 {len(prompt)} chars {'PASS' if not real else 'FAIL ' + ' | '.join(real)}")
sys.exit(1 if real else 0)
