"""HK2-01 v6 (§6A, user Fix 2026-10-01: "fix HK2-01 use this as reference in screen" + a screenshot of the STRYDE product page's review carousel): an edit of v5 (Image 1) — only the laptop screen changes, to show that page (Image 2 = `ref/HK2-01_screen_ref.png`, rebuilt from the screenshot by `make_HK2-01_screen_ref.py`). The user asked for this page, so its own text and the stryde wordmark show on screen."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "Twenty five thousand people have written to us about their knees. Three things come up more than anything else, and none of them are what you would expect."
prompt = (f'For the line "{LINE}": keep this photo exactly as it is — the same camera over her shoulder, the laptop, her two hands, her rust-orange cuff and grey hair, the desk, brick wall, pinboard and the light. Image 1 is that photo.\n'
    "Change only what is on the laptop screen: it shows the web page in Image 2, copied exactly — same shape, same parts, same markings, nothing redesigned — the black stryde wordmark and menu across the top, the row of small product photos, the black Add to Cart bar, and in the middle the customer review: the round photo, the name, the orange Verified Purchase tick, five gold stars and the short quote under them, the small dots below. The page fills the screen edge to edge, lit by the screen itself, seen at the same angle as the screen in Image 1.\n"
    "In frame: the laptop, her two hands, the desk; every other surface bare. Clothing, walls and papers plain — no other lettering or logos; no extra fingers.")
call = {"beat": "HK2-01", "kind": "image", "mode": 1, "prompt": prompt, "script_line": LINE,
        "face": False, "room": True, "product": False, "body": True,
        "refs": [{"label": "HK2-01 v5", "kind": "frame"}, {"label": "STRYDE review page (user's screenshot, rebuilt)", "kind": "screen"}],
        "match": "frame", "edit_of": "255b37d2-4cce-4d41-909b-c2550cfd6e82", "taste": ["HT12", "HT17", "HT18", "HT19", "HT20"], "anatomy": False,
        "pair": ["nano_banana_pro"], "alt_reason": "existing build keeps its step-2 image lock (nano_banana_pro on Higgsfield, one render per call)",
        "motion_plan": "From this frame: her right fingers flick the trackpad and the page scrolls fast upward through the reviews; the camera holds.",
        "fix_note": "use this as reference in screen (user's screenshot of the STRYDE review carousel)"}
json.dump(call, open(D + "HK2-01.image.json", "w"), ensure_ascii=False, indent=1)
open(D + "HK2-01_v6.txt", "w").write(prompt)
print(len(prompt))
