"""HK3-02 image v2 (§6A, user Fix "the pill must be under the Blister pack", 2026-09-30): v1 showed the pill lying on top of the card under his thumb → an edit of the v1 frame (angle, hands, bench and pavement kept): card held level above his open palm, bubbles up, thumb pressing one bubble, the pill pushed out through the foil UNDERSIDE, dropping into the palm below. Avoids 'tablet / blister' wording (Higgsfield filter, 2026-09-28)."""
import json, os, shutil
D = os.path.dirname(os.path.abspath(__file__)) + "/"
if not os.path.exists(D + "HK3-02_v1.txt"):
    shutil.copy(D + "HK3-02.txt", D + "HK3-02_v1.txt")
LINE = "The most common regret I read is not about surgery. It is not about painkillers. It is not about waiting too long. It is about two centimetres."
prompt = (f'For the line "{LINE}": keep this photo exactly as it is — his hands, gold ring, tan jacket cuffs, stone shorts, bare knee, pavement, kerb and shelter post, the same high three-quarter angle and grey daylight. Image 1 is that photo.\n'
    "Change only the pill card and the pill: his right hand holds the small silver foil card of headache pills flat and level, a hand's width ABOVE his open left palm, the clear raised bubbles facing up. His right thumb presses down on one full bubble, and one small round white pill has just broken out through the silver foil on the UNDERSIDE of the card and is dropping into the middle of his open palm below. The pill is below the card, between the card and the palm — never on top of the card.\n"
    "In frame: exactly two hands, five fingers each, one card, one falling pill; two empty bubbles, the rest full. The card and palm fill the middle of the frame.\n"
    "No pill on top of the card, no readable text or logos on the foil, no box, no extra fingers.")
call = {"beat": "HK3-02", "kind": "image", "mode": 1, "prompt": prompt, "script_line": LINE,
        "face": False, "room": False, "product": False, "body": True,
        "refs": [{"label": "HK3-02 v1 frame", "kind": "frame"}],
        "match": "frame", "edit_of": "deb72848-6430-493c-aeaa-1e222336f286", "taste": ["HT04", "HT12", "HT17", "HT18", "HT19"], "anatomy": False,
        "pair": ["nano_banana_pro"], "alt_reason": "existing build keeps its step-2 image lock (nano_banana_pro on Higgsfield, one render per call)",
        "fix_note": "the pill must be under the Blister pack: v1's pill lay on top of the card under his thumb → edit of v1: the pill breaks out through the foil underside and drops into his palm below"}
json.dump(call, open(D + "HK3-02.image.json", "w"), ensure_ascii=False, indent=1)
open(D + "HK3-02.txt", "w").write(prompt)
print(len(prompt))
