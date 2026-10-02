"""TH-HK2 new frame (§6A, user Fix "instead of in a paper, can we please make it in a laptop where she's reading the messages", 2026-10-01): the talking head's photo avatar came from the confirmed N step-1 frame (job 9378efcb, she holds a printed letter) → an edit of that frame: the letter gone, an open laptop on the desk in front of her showing an inbox of messages, her right hand on its trackpad; face square to the lens (lip-sync). Then a new HeyGen photo avatar + Avatar V render of VO-MASTER-HK2, after the user confirms this frame."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "Twenty five thousand people have written to us about their knees. Three things come up more than anything else, and none of them are what you would expect."
prompt = (f'For the line "{LINE}": keep this photo exactly as it is — the same woman, her face, hair, rust-orange needlecord overshirt and cream T-shirt, the wooden chair, the brick wall, the pinboard, the window, the grey post trays, the desk, the light and the camera. Image 1 is that photo.\n'
    "Change only what is on the desk in front of her: the printed letters are gone. In their place an open silver laptop sits on the desk in front of her, its screen turned a little toward her and toward us, showing a long list of messages in an inbox, each line a grey blur too small to read. Her right hand rests on the laptop's trackpad; her left forearm rests on the desk edge.\n"
    "In frame: one woman, both hands placed as said; on the desk only the laptop and the grey post trays, every other surface bare. Her face square to the lens, both eyes on it, mouth closed, as if she has just looked up from the messages.\n"
    "No readable text or logos on the screen or the laptop, no printed letters, no extra fingers.")
call = {"beat": "TH-HK2", "kind": "image", "mode": 1, "prompt": prompt, "script_line": LINE,
        "face": True, "room": True, "product": False, "body": True,
        "refs": [{"label": "N step-1 frame (the talking head's source)", "kind": "frame"}],
        "match": "frame", "edit_of": "9378efcb-3e27-47ab-99d1-18e9ee05c803", "taste": ["HT12", "HT17", "HT18", "HT19", "HT20"], "anatomy": False,
        "pair": ["nano_banana_pro"], "alt_reason": "existing build keeps its step-2 image lock (nano_banana_pro on Higgsfield, one render per call); a talking-head source frame is one render (§5)",
        "fix_note": "instead of in a paper, make it a laptop where she's reading the messages"}
json.dump(call, open(D + "TH-HK2_frame.image.json", "w"), ensure_ascii=False, indent=1)
open(D + "TH-HK2_frame.txt", "w").write(prompt)
print(len(prompt))
