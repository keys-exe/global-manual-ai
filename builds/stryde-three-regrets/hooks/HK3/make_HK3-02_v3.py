"""HK3-02 image v3 (§6A, user Fix "change it pain killer into a bottle one", 2026-09-30): v2 had a foil card → an edit of the v2 frame (hands, angle, bench, pavement kept): a small plain white plastic pill bottle, cap off, tipped over his open palm, one white pill dropping out. 'Headache pills' wording, no 'tablet/blister' (Higgsfield filter, 2026-09-28)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "The most common regret I read is not about surgery. It is not about painkillers. It is not about waiting too long. It is about two centimetres."
prompt = (f'For the line "{LINE}": keep this photo exactly as it is — his hands, gold ring, tan jacket cuffs, stone shorts, bare knee, pavement, kerb and shelter post, the same high three-quarter angle and grey daylight. Image 1 is that photo.\n'
    "Change only what he holds: the foil card is gone. In his right hand is a small plain white plastic bottle from the chemist, about the size of his thumb, its white cap off. He tilts it over his open left palm, and one small round white headache pill has just rolled out onto the middle of the palm.\n"
    "In frame: exactly two hands, five fingers each, one bottle, one pill. The bottle and palm fill the middle of the frame.\n"
    "No foil card, no label text or logos on the bottle, no box, no other pills, no extra fingers.")
call = {"beat": "HK3-02", "kind": "image", "mode": 1, "prompt": prompt, "script_line": LINE,
        "face": False, "room": False, "product": False, "body": True,
        "refs": [{"label": "HK3-02 v2 frame", "kind": "frame"}],
        "match": "frame", "edit_of": "bedec169-1c5c-4083-af2f-c4cfa925830d", "taste": ["HT04", "HT12", "HT17", "HT18", "HT19"], "anatomy": False,
        "pair": ["nano_banana_pro"], "alt_reason": "existing build keeps its step-2 image lock (nano_banana_pro on Higgsfield, one render per call)",
        "fix_note": "change it pain killer into a bottle one: v2 was a foil card → edit of v2: a small plain pill bottle tipped over his palm, one pill rolled out into his palm (retry wording after job 35731d3c failed without a reason)"}
json.dump(call, open(D + "HK3-02.image.json", "w"), ensure_ascii=False, indent=1)
open(D + "HK3-02.txt", "w").write(prompt)
print(len(prompt))
