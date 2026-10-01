"""TH-HK2 frame v10 (§6A, user Fix "lock the laptop angle, now place it in front of the woman", 2026-10-01): v9's laptop angle kept exactly (screen toward her, the inbox showing to the lens at an angle); the laptop slid forward along the desk to sit right in front of her, under her hands. An edit of v9, same camera."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "Twenty five thousand people have written to us about their knees. Three things come up more than anything else, and none of them are what you would expect."
prompt = (f'For the line "{LINE}": keep this photo exactly as it is — the same camera angle, distance and framing, the same woman, her face, hair, rust-orange needlecord overshirt and cream T-shirt, the chair, brick wall, pinboard, shelves, window, grey post trays, desk and light. Image 1 is that photo.\n'
    "Change only where the laptop sits, keeping its angle exactly as it is now — the same turn, the screen toward her with the pale inbox showing to the lens at the same angle. Slide it forward along the desk until it sits right in front of her, its keyboard just past her forearms, the whole laptop inside the frame. A plain silver laptop, lid and keys blank, the inbox soft grey lines too small to read. Both her hands rest on its keyboard.\n"
    "In frame: one woman; on the desk only the laptop and the grey post trays, every other surface bare. Her face square to the lens above the screen, both eyes on it, mouth closed.\n"
    "No readable text or logos, no extra fingers.")
call = {"beat": "TH-HK2", "kind": "image", "mode": 1, "prompt": prompt, "script_line": LINE,
        "face": True, "room": True, "product": False, "body": True,
        "refs": [{"label": "TH-HK2 frame v9", "kind": "frame"}],
        "match": "frame", "edit_of": "29464a0d-7f3b-4b34-b695-7a644d933ccc", "taste": ["HT12", "HT17", "HT18", "HT19", "HT20"], "anatomy": False,
        "pair": ["nano_banana_pro"], "alt_reason": "existing build keeps its step-2 image lock (nano_banana_pro on Higgsfield, one render per call)",
        "fix_note": "lock the laptop angle, now place it in front of the woman: edit of v9"}
json.dump(call, open(D + "TH-HK2_frame.image.json", "w"), ensure_ascii=False, indent=1)
open(D + "TH-HK2_frame.txt", "w").write(prompt)
print(len(prompt))
