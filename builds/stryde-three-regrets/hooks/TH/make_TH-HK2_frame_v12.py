"""TH-HK2 frame v12 (§6A, user Fix "move the laptop close to her", 2026-10-01): v11 had the laptop by her hands but mostly past the right edge → an edit of v11, same camera: the laptop slid left along the desk, close to her, so the whole laptop and its screen are in frame."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "Twenty five thousand people have written to us about their knees. Three things come up more than anything else, and none of them are what you would expect."
prompt = (f'For the line "{LINE}": keep this photo exactly as it is — the same camera angle, distance and framing, the same woman, her face, hair, rust-orange needlecord overshirt and cream T-shirt, the chair, brick wall, pinboard, shelves, window, grey post trays, desk and light. Image 1 is that photo.\n'
    "Change only the laptop: slide it left along the desk, close to her, so it sits right by her body under her hands and the whole laptop is inside the frame, screen open and facing her, turned a little toward the lens so the pale inbox shows at an angle — soft grey lines too small to read. A plain silver laptop, lid and keys blank. Both her hands rest on its keyboard.\n"
    "In frame: one woman; on the desk only the laptop and the grey post trays, every other surface bare. Her face square to the lens, both eyes on it, mouth closed.\n"
    "No readable text or logos, no extra fingers.")
call = {"beat": "TH-HK2", "kind": "image", "mode": 1, "prompt": prompt, "script_line": LINE,
        "face": True, "room": True, "product": False, "body": True,
        "refs": [{"label": "TH-HK2 frame v11", "kind": "frame"}],
        "match": "frame", "edit_of": "b7bf3ada-d471-439d-98a0-7e18bc2aaf54", "taste": ["HT12", "HT17", "HT18", "HT19", "HT20"], "anatomy": False,
        "pair": ["nano_banana_pro"], "alt_reason": "existing build keeps its step-2 image lock (nano_banana_pro on Higgsfield, one render per call)",
        "fix_note": "move the laptop close to her: edit of v11"}
json.dump(call, open(D + "TH-HK2_frame.image.json", "w"), ensure_ascii=False, indent=1)
open(D + "TH-HK2_frame.txt", "w").write(prompt)
print(len(prompt))
