"""HK3-02 image v4 (§6A, user Fix "make the bottle look like real pain killer", 2026-09-30): v3's bottle read as a blank white supplement tub → an edit of the v3 frame: a real chemist's painkiller bottle — translucent amber plastic, white wrap-round label with a red band, fine print too small to read (HT18: no readable text), white pills visible through it. Same pose, pill in palm."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "The most common regret I read is not about surgery. It is not about painkillers. It is not about waiting too long. It is about two centimetres."
prompt = (f'For the line "{LINE}": keep this photo exactly as it is — his hands, gold ring, tan jacket cuffs, stone shorts, bare knee, pavement, the pill in his palm, the same high three-quarter angle and grey daylight. Image 1 is that photo.\n'
    "Change only the bottle: make it a real painkiller bottle from a chemist — translucent amber-brown plastic, a few round white pills visible through it, a plain white paper label wrapped round it with one red band across the top, printed with nothing. Same size, same tilt, same open mouth over his palm, cap off.\n"
    "In frame: exactly two hands, five fingers each, one bottle, one pill in the palm. The bottle and palm fill the middle of the frame.\n"
    "No lettering, logos or words anywhere, no plain white tub, no other pills, no extra fingers.")
call = {"beat": "HK3-02", "kind": "image", "mode": 1, "prompt": prompt, "script_line": LINE,
        "face": False, "room": False, "product": False, "body": True,
        "refs": [{"label": "HK3-02 v3 frame", "kind": "frame"}],
        "match": "frame", "edit_of": "5f6c4299-1bd8-4356-88c4-a7f9127c3514", "taste": ["HT12", "HT17", "HT18", "HT19"], "anatomy": False,
        "pair": ["nano_banana_pro"], "alt_reason": "existing build keeps its step-2 image lock (nano_banana_pro on Higgsfield, one render per call)",
        "fix_note": "make the bottle look like real pain killer: v3 was a blank white tub → edit of v3: amber chemist's bottle, white label with a red band, no printing (§6A rule 5)"}
json.dump(call, open(D + "HK3-02.image.json", "w"), ensure_ascii=False, indent=1)
open(D + "HK3-02.txt", "w").write(prompt)
print(len(prompt))
