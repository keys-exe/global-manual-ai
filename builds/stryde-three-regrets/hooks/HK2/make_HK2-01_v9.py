"""HK2-01 v9 (§6A, user Fix 2026-10-01: "use close package of stryde"): v8 (the user's nano_banana_2 edit) put a box beside the laptop but with invented side text, and the screen drifted → an edit of v6 (Image 1, the screen untouched) with a tight crop of the real closed box (Image 2 = `ref/stryde_box_closed_crop.png`, cut from TH-HK2 v15), placed where v8 put it: on the desk to the right of the laptop."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "Twenty five thousand people have written to us about their knees. Three things come up more than anything else, and none of them are what you would expect."
prompt = (f'For the line "{LINE}": keep this photo exactly as it is — the camera over her shoulder, the laptop and the stryde review page on its screen exactly as it is, her two hands, her rust-orange cuff and grey hair, the desk, brick wall, pinboard and the light. Image 1 is that photo.\n'
    "Add only one thing: the closed box in Image 2, copied exactly — same shape, same parts, same markings, nothing redesigned — lying flat on the desk to the right of the laptop, between the laptop and her right arm, near the brick wall, turned to the same angle as the laptop. A matte black lid over a base, about 28 cm wide, 16 cm deep and 8 cm tall, about a quarter of the frame wide; the only print is the lowercase grey stryde wordmark on the lid; the sides plain black.\n"
    "In frame: the laptop, the one closed box, her two hands, the desk; every other surface bare. Clothing, walls and papers plain — no other lettering or logos; no extra fingers.")
call = {"beat": "HK2-01", "kind": "image", "mode": 1, "prompt": prompt, "script_line": LINE,
        "face": False, "room": True, "product": True, "body": True,
        "refs": [{"label": "HK2-01 v6 (confirmed frame)", "kind": "frame"}, {"label": "closed stryde box (crop of TH-HK2 v15)", "kind": "product"}],
        "match": "frame", "edit_of": "ae40b51c-fe63-4bcf-9030-82287f93594a", "taste": ["HT12", "HT17", "HT18", "HT19", "HT20", "FP02"], "anatomy": False,
        "pair": ["nano_banana_pro"], "alt_reason": "existing build keeps its step-2 image lock (nano_banana_pro on Higgsfield, one render per call)",
        "motion_plan": "From this frame: her right fingers flick the trackpad and the page scrolls fast upward through the reviews; the camera holds.",
        "fix_note": "use close package of stryde"}
json.dump(call, open(D + "HK2-01.image.json", "w"), ensure_ascii=False, indent=1)
open(D + "HK2-01_v9.txt", "w").write(prompt)
print(len(prompt))
