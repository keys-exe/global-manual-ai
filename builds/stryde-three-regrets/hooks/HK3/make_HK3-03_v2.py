"""HK3-03 image v2 (§6A, user Fix "The woman fell down and is waiting for help", 2026-09-30): v1 was Joan in her armchair looking at the clock → she has fallen and sits on the lounge carpet by the armchair, unable to get up, waiting for help. New picture (not an edit): refs P4 plate (room) + R3 sheet v2 (face). High three-quarter = small / overwhelmed (§30I)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "The most common regret I read is not about surgery. It is not about painkillers. It is not about waiting too long. It is about two centimetres."
prompt = (f'For the line "{LINE}": she has fallen in her lounge and sits on the carpet beside her armchair, unable to get up, waiting for help.\n'
    "A high three-quarter shot from standing height, her whole body in frame, small on the carpet with the room around her.\n"
    "Image 1 is her lounge: the same rose-pink wing armchair, net-curtained window, carpet and teak side table, copied exactly. Image 2 is the woman: the same face and white pixie crop, copied exactly.\n"
    "In frame: she sits on the floor with her legs out to one side, her right hand flat on the armchair seat as if she tried to pull herself up, her left hand in her lap; the side table holds only the telephone, out of her reach; every other surface bare. Heather-purple twinset, grey pleated skirt, one beige slipper off on the carpet. She is looking toward the door off to the right, mouth closed, patient and a little frightened, not hurt.\n"
    "Grey afternoon daylight through the nets from the left. An ordinary iPhone photo.\n"
    "No blood or injury, no second person, no readable text or logos, no extra fingers.")
call = {"beat": "HK3-03", "kind": "image", "mode": 1, "prompt": prompt, "script_line": LINE,
        "face": True, "room": True, "product": False, "body": True,
        "refs": [{"label": "P4-J-LOUNGE plate", "kind": "location"}, {"label": "R3-JOAN sheet v2", "kind": "character"}],
        "match": None, "edit_of": None, "taste": ["HT02", "HT08", "HT09", "HT12", "HT18"], "anatomy": False,
        "pair": ["nano_banana_pro"], "alt_reason": "existing build keeps its step-2 image lock (nano_banana_pro on Higgsfield, one render per call)",
        "fix_note": "The woman fell down and is waiting for help: v1 was her seated in the armchair looking at the clock → on the carpet after a fall, the phone out of reach, waiting"}
json.dump(call, open(D + "HK3-03.image.json", "w"), ensure_ascii=False, indent=1)
open(D + "HK3-03.txt", "w").write(prompt)
print(len(prompt))
