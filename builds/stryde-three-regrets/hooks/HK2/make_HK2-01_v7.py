"""HK2-01 v7 (§6A, user Fix 2026-10-01: "add package stryde next to laptop"): an edit of v6 (Image 1) — one closed STRYDE box added on the desk beside the laptop, the same box as on her desk in TH-HK2 v15 (Image 2; Product Sheet §16 PACKAGE: rigid two-piece, matte black, ~28 × 16 × 8 cm, lowercase grey stryde wordmark centred on the lid)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "Twenty five thousand people have written to us about their knees. Three things come up more than anything else, and none of them are what you would expect."
prompt = (f'For the line "{LINE}": keep this photo exactly as it is — the camera over her shoulder, the laptop and the stryde review page on its screen, her two hands, her rust-orange cuff and grey hair, the desk, brick wall, pinboard and the light. Image 1 is that photo.\n'
    "Add only one thing: one closed stryde box lying flat on the desk just to the left of the laptop, its long side parallel to the laptop's edge — the closed box on the desk in Image 2, copied exactly — same shape, same parts, same markings, nothing redesigned. A rigid two-piece box, a lid over a base, matte black all over, about 28 cm wide, 16 cm deep and 8 cm tall, about a quarter of the frame wide; the only print is the lowercase grey stryde wordmark centred on the lid.\n"
    "In frame: the laptop, the closed box, her two hands, the desk; every other surface bare. Clothing, walls and papers plain — no other lettering or logos; no extra fingers.")
call = {"beat": "HK2-01", "kind": "image", "mode": 1, "prompt": prompt, "script_line": LINE,
        "face": False, "room": True, "product": True, "body": True,
        "refs": [{"label": "HK2-01 v6 (confirmed frame)", "kind": "frame"}, {"label": "TH-HK2 v15 — the closed stryde box", "kind": "product"}],
        "match": "frame", "edit_of": "ae40b51c-fe63-4bcf-9030-82287f93594a", "taste": ["HT12", "HT17", "HT18", "HT19", "HT20", "FP02"], "anatomy": False,
        "pair": ["nano_banana_pro"], "alt_reason": "existing build keeps its step-2 image lock (nano_banana_pro on Higgsfield, one render per call)",
        "motion_plan": "From this frame: her right fingers flick the trackpad and the page scrolls fast upward through the reviews; the camera holds.",
        "fix_note": "add package stryde next to laptop"}
json.dump(call, open(D + "HK2-01.image.json", "w"), ensure_ascii=False, indent=1)
open(D + "HK2-01_v7.txt", "w").write(prompt)
print(len(prompt))
