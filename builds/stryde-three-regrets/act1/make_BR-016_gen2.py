"""BR-016 clip gen 2 (§22X): new start frame v3 (P1 bedroom from the doorway, no hanging strap) after the user's image Fixes; sound off (user standing rule 2026-09-29)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
old = json.load(open(D + "BR-016.call.json"))
json.dump(old, open(D + "BR-016_g1.call.json", "w"), ensure_ascii=False, indent=1)
p = json.loads(old["prompt"])
p["subject"] = "THE SAME WOMAN, CHEST OF DRAWERS AND BEDROOM as in the start frame; unchanged in every respect."
p["camera"]["framing"] = "MEDIUM as in the start frame: from the doorway, three-quarter behind her at the chest, the bed and window beyond. FOCUS: her hands and the jammed drawer are sharp."
mo = p["motion"]; i = mo.index("Everything in frame")
p["motion"] = ("CONTINUING: both her hands are already on the front of the overfilled top drawer. "
               "COMPLETING: one push, about two seconds — the drawer slides in a few centimetres and jams on the stuffed supports; it will not shut. "
               "UNRESOLVED: her hands stay on it, her head dropping slightly. " + mo[i:])
p["motion"] = p["motion"].replace("Mass and momentum in all movement: heavy starts and settles slow, nothing at uniform speed, nothing stops instantly — motions decelerate into a settle or small overshoot; actions travel through the body, weight transferring first, hands arriving last; hair, fabric and straps lag and keep moving after the body stops; objects drag with friction, never glide.", "Mass and momentum: nothing at uniform speed, motions settle slowly, the drawer drags with friction, fabric lags.")
if "no strap hanging out" not in p["negatives"]:
    p["negatives"] = p["negatives"] + ", no strap hanging out"
p["negatives"] = p["negatives"] + ", no furniture moving, no sound"
prompt = json.dumps(p, ensure_ascii=False, separators=(",", ":"))
call = dict(old, prompt=prompt, generation=2, audio=False,
            start_image="https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_214414_2a86affa-7eb4-4e78-ac82-d654b368ed07.png",
            fix_note="frame fault: v1 was not in the P1 bedroom and v2 had a strap hanging out (user Fixes) → new start frame v3 in the P1 room from the doorway, no strap out, confirmed by the user; same single push, sound off")
call["risks"] = [{"risk": "the drawer closes fully", "prevented_by": "it jams a few centimetres in; no drawer closing fully"},
                 {"risk": "a strap appears hanging out", "prevented_by": "no strap hanging out"},
                 {"risk": "the room warps or furniture moves", "prevented_by": "HOLD-C; no furniture moving"}]
json.dump(call, open(D + "BR-016.call.json", "w"), ensure_ascii=False, indent=1)
open(D + "BR-016.kie_prompt.txt", "w").write(prompt)
print(len(prompt), call.get("duration"))
