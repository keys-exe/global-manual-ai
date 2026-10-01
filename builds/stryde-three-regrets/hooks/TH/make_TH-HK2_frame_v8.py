"""TH-HK2 frame v8 (§6A, user Fix "use the previous camera angle, change the laptop position make it close to the left side of the woman", 2026-10-01): v7's camera kept; the laptop slid left across the desk, close in against her body, so it sits in front of her torso instead of out toward the right of the frame. An edit of v7."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "Twenty five thousand people have written to us about their knees. Three things come up more than anything else, and none of them are what you would expect."
prompt = (f'For the line "{LINE}": keep this photo exactly as it is — the same camera angle, distance and framing, the same woman, her face, hair, rust-orange needlecord overshirt and cream T-shirt, the chair, brick wall, pinboard, shelves, window, grey post trays, desk and light. Image 1 is that photo.\n'
    "Change only the laptop's position: slide it left along the desk, close in to her, so it sits right against her body in front of her chest, its left corner touching her forearm and its screen just below her chin line. The right half of the desk is left bare. Its screen faces her, turned a little toward the lens, a pale inbox of soft grey lines too small to read. A plain silver laptop, lid and keys blank. Both her hands rest on its keyboard, close to her body.\n"
    "In frame: one woman; on the desk only the laptop and the grey post trays, every other surface bare. Her face square to the lens above the screen, both eyes on it, mouth closed.\n"
    "No readable text or logos, no extra fingers.")
call = {"beat": "TH-HK2", "kind": "image", "mode": 1, "prompt": prompt, "script_line": LINE,
        "face": True, "room": True, "product": False, "body": True,
        "refs": [{"label": "TH-HK2 frame v7", "kind": "frame"}],
        "match": "frame", "edit_of": "5409fe10-3362-40e4-8e3d-8d550c04117b", "taste": ["HT12", "HT17", "HT18", "HT19", "HT20"], "anatomy": False,
        "pair": ["nano_banana_pro"], "alt_reason": "existing build keeps its step-2 image lock (nano_banana_pro on Higgsfield, one render per call)",
        "fix_note": "use the previous camera angle, make the laptop close to the left side of the woman: edit of v7"}
json.dump(call, open(D + "TH-HK2_frame.image.json", "w"), ensure_ascii=False, indent=1)
open(D + "TH-HK2_frame.txt", "w").write(prompt)
print(len(prompt))
