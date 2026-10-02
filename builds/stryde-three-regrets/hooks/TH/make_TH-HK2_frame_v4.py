"""TH-HK2 frame v4 (§6A, user Fix "place the laptop farther from the camera", 2026-10-01): v3 had the laptop right at the lens, cropped by the right edge, filling the lower right → an edit of v3: the laptop pushed back across the desk, smaller, whole in frame, screen still turned a little toward the lens; woman, room, light, face to the lens kept."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "Twenty five thousand people have written to us about their knees. Three things come up more than anything else, and none of them are what you would expect."
prompt = (f'For the line "{LINE}": keep this photo exactly as it is — the same woman, her face, hair, rust-orange needlecord overshirt and cream T-shirt, the wooden chair, the brick wall, the pinboard, the window, the grey post trays, the desk, the light and the camera. Image 1 is that photo.\n'
    "Change only where the laptop is: slide it away from the camera, back across the desk until it sits just in front of her so it looks smaller and the whole laptop fits in the frame, desk around it, nothing cut off by the right edge. Its screen still faces her, turned a little toward the lens so we see the pale inbox at an angle: rows of messages as soft grey lines too small to read. A plain silver laptop, its lid and keys blank and unmarked. Both her hands rest on its keyboard.\n"
    "In frame: one woman, both hands on the keyboard; on the desk only the laptop and the grey post trays, every other surface bare. Her face square to the lens above the screen, both eyes on it, mouth closed.\n"
    "No readable text or logos, no app names, no extra fingers.")
call = {"beat": "TH-HK2", "kind": "image", "mode": 1, "prompt": prompt, "script_line": LINE,
        "face": True, "room": True, "product": False, "body": True,
        "refs": [{"label": "TH-HK2 frame v3", "kind": "frame"}],
        "match": "frame", "edit_of": "d243ddcc-0086-4af0-aab7-ad270b961d77", "taste": ["HT12", "HT17", "HT18", "HT19", "HT20"], "anatomy": False,
        "pair": ["nano_banana_pro"], "alt_reason": "existing build keeps its step-2 image lock (nano_banana_pro on Higgsfield, one render per call)",
        "fix_note": "place the laptop farther from the camera: edit of v3"}
json.dump(call, open(D + "TH-HK2_frame.image.json", "w"), ensure_ascii=False, indent=1)
open(D + "TH-HK2_frame.txt", "w").write(prompt)
print(len(prompt))
