"""TH-HK2 frame v6 (§6A, user Fix "use previous camera angle, the laptop place farther to the frame", 2026-10-01): v5 pulled the camera back (outpaint) → the user wants v3's close camera back, with the laptop kept whole inside the frame as in v5. An edit of v3 (Image 1: camera, framing, woman) with v5 as Image 2 (where the laptop sits: whole, back on the desk, desk around it)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "Twenty five thousand people have written to us about their knees. Three things come up more than anything else, and none of them are what you would expect."
prompt = (f'For the line "{LINE}": keep this photo exactly as it is — the same camera, distance and framing, the same woman, her face, hair, rust-orange needlecord overshirt and cream T-shirt, the chair, brick wall, pinboard, window, grey post trays, desk and light. Image 1 is that photo.\n'
    "Change only the laptop: place it as in Image 2 — farther back on the desk, toward the grey post trays, smaller, the whole laptop inside the frame with bare desk showing between it and the right and bottom edges. Its screen faces her, turned a little toward the lens, a pale inbox of soft grey lines too small to read. A plain silver laptop, lid and keys blank. Her right hand rests on its keyboard, her left forearm on the desk edge.\n"
    "In frame: one woman; on the desk only the laptop and the grey post trays, every other surface bare. Her face square to the lens, both eyes on it, mouth closed.\n"
    "No readable text or logos, no extra fingers.")
call = {"beat": "TH-HK2", "kind": "image", "mode": 1, "prompt": prompt, "script_line": LINE,
        "face": True, "room": True, "product": False, "body": True,
        "refs": [{"label": "TH-HK2 frame v3", "kind": "frame"}, {"label": "TH-HK2 frame v5 (laptop placement)", "kind": "frame"}],
        "match": "frame", "edit_of": "d243ddcc-0086-4af0-aab7-ad270b961d77", "taste": ["HT12", "HT17", "HT18", "HT19", "HT20"], "anatomy": False,
        "pair": ["nano_banana_pro"], "alt_reason": "existing build keeps its step-2 image lock (nano_banana_pro on Higgsfield, one render per call)",
        "fix_note": "use previous camera angle, the laptop place farther to the frame: edit of v3, laptop placed as in v5"}
json.dump(call, open(D + "TH-HK2_frame.image.json", "w"), ensure_ascii=False, indent=1)
open(D + "TH-HK2_frame.txt", "w").write(prompt)
print(len(prompt))
