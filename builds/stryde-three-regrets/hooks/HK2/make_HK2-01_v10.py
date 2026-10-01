"""HK2-01 v10 (§6A, user Fix 2026-10-01: "change camera angle, show the laptop and the package"): in v9 her head hid the box. New angle — over her LEFT shoulder, a little higher — so the laptop (review page on screen) and the closed stryde box to its right are both in clear view. Image 1 = the closed-box crop (product first), Image 2 = v9 (the scene). The screen text is put back by warp afterwards (as v9)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "Twenty five thousand people have written to us about their knees. Three things come up more than anything else, and none of them are what you would expect."
prompt = (f'For the line "{LINE}": the same desk, laptop, review page and room as Image 2 — her rust-orange needlecord cuffs, the wooden desk, brick wall, pinboard, soft window light. Image 2 is that scene; Image 1 is the box.\n'
    "New camera angle: over her LEFT shoulder, a little higher, looking down at the desk at about 45 degrees. In frame, left to right: her left shoulder soft at the left edge; the open laptop in the middle, its screen facing the lens at a slight angle, the white stryde review page on it; and on the desk to the right of the laptop, fully in view and nothing in front of it, the closed box in Image 1, copied exactly — same shape, same parts, same markings, nothing redesigned: matte black, about 28 × 16 × 8 cm, the lowercase grey stryde wordmark on the lid facing up, about a quarter of the frame wide. Both her hands on the keyboard, her right fingers on the trackpad.\n"
    "In frame: the laptop, the one closed box, her two hands; every other surface bare. Clothing, walls and papers plain — no other lettering or logos; no extra fingers.")
call = {"beat": "HK2-01", "kind": "image", "mode": 1, "prompt": prompt, "script_line": LINE,
        "face": False, "room": True, "product": True, "body": True,
        "refs": [{"label": "closed stryde box (crop of TH-HK2 v15)", "kind": "product"}, {"label": "HK2-01 v9 (the scene)", "kind": "plate"}],
        "taste": ["HT12", "HT17", "HT18", "HT19", "HT20", "FP02"], "anatomy": False,
        "pair": ["nano_banana_pro"], "alt_reason": "existing build keeps its step-2 image lock (nano_banana_pro on Higgsfield, one render per call)",
        "motion_plan": "From this frame: her right fingers flick the trackpad and the page scrolls fast upward through the reviews; the camera holds.",
        "fix_note": "change camera angle, show the laptop and the package"}
json.dump(call, open(D + "HK2-01.image.json", "w"), ensure_ascii=False, indent=1)
open(D + "HK2-01_v10.txt", "w").write(prompt)
print(len(prompt))
