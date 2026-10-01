"""HK3-03 image v3 (§6A, user Fix "make her look that she is in pain", 2026-09-30): an edit of the v2 frame (room, angle, her place by the armchair kept): a real wince, left hand gripping her right knee, right hand braced on the armchair seat. HT02: problem lines show real struggle."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "The most common regret I read is not about surgery. It is not about painkillers. It is not about waiting too long. It is about two centimetres."
prompt = (f'For the line "{LINE}": keep this photo exactly as it is — the lounge, the armchair, the side table with the telephone, the carpet, the window light, the high three-quarter camera, and the woman sitting on the carpet beside the armchair in her heather-purple twinset and grey pleated skirt. Image 1 is that photo.\n'
    "Change only her pain: she is clearly hurting. Her face screws up in a real wince — brows drawn together, eyes squeezed half shut, mouth pulled tight at one corner. Her left hand grips her right knee, fingers pressed round it; her right hand stays braced flat on the armchair seat. Her shoulders hunch forward over the knee. She is looking down at the knee.\n"
    "In frame: one woman, two hands placed as said; one beige slipper on her left foot, the other slipper on the carpet; the side table holds only the telephone, every other surface bare.\n"
    "No blood or injury marks, no crying, no second person, no readable text or logos, no extra fingers.")
call = {"beat": "HK3-03", "kind": "image", "mode": 1, "prompt": prompt, "script_line": LINE,
        "face": True, "room": True, "product": False, "body": True,
        "refs": [{"label": "HK3-03 v2 frame", "kind": "frame"}],
        "match": "frame", "edit_of": "174dbc06-cd8f-4c84-aedb-4603c3926497", "taste": ["HT02", "HT09", "HT12", "HT17", "HT18"], "anatomy": False,
        "pair": ["nano_banana_pro"], "alt_reason": "existing build keeps its step-2 image lock (nano_banana_pro on Higgsfield, one render per call)",
        "fix_note": "make her look that she is in pain: v2 read patient and frightened → edit of v2: a real wince, left hand gripping her right knee, shoulders hunched"}
json.dump(call, open(D + "HK3-03.image.json", "w"), ensure_ascii=False, indent=1)
open(D + "HK3-03.txt", "w").write(prompt)
print(len(prompt))
