"""BR-039 clip gen 2 (§22X): new start frame v3 from the user's photo of the real back (grey ribbed pad, raised ridge), confirmed by the user ("MAKE CLIP FOR BR-039"); sound off (user standing rule 2026-09-29)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
old = json.load(open(D + "BR-039.call.json"))
json.dump(old, open(D + "BR-039_g1.call.json", "w"), ensure_ascii=False, indent=1)
p = json.loads(old["prompt"])
p["subject"] = "THE SAME HANDS and strap as in the start frame, the grey ribbed pad with its raised ridge facing the lens; unchanged in every respect."
p["camera"]["framing"] = "CU as in the start frame: level, front, the strap held up over the bed. FOCUS: the grey pad, its ribs and the ridge are sharp."
mo = p["motion"]; i = mo.index("The product keeps")
p["motion"] = ("CONTINUING: her two hands already hold the strap by its chrome ends, the grey pad facing the lens. "
               "COMPLETING: one small tilt, about two seconds — the shell tips a little back towards the window so the sun rakes across the grey ribs and the raised ridge, then settles. "
               "UNRESOLVED: held still, the pad facing the lens, the band hanging below. " + mo[i:])
p["motion"] = p["motion"].replace("Mass and momentum in all movement: heavy starts and settles slow, nothing at uniform speed, nothing stops instantly — motions decelerate into a settle or small overshoot; actions travel through the body, weight transferring first, hands arriving last; hair, fabric and straps lag and keep moving after the body stops; objects drag with friction, never glide.",
                                  "Mass and momentum: nothing at uniform speed, motions settle slowly, the band lags.")
p["negatives"] = p["negatives"].replace("no glossy pad,", "no glossy pad, no pad changing colour, no ribs changing direction, no ridge flattening,") + ", no sound"
prompt = json.dumps(p, ensure_ascii=False, separators=(",", ":"))
call = dict(old, prompt=prompt, generation=2, audio=False,
            start_image="https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_081425_5c53a554-ec93-4e7e-9394-4717d1247696.png",
            fix_note="frame fault: v1 clip showed a plain black pad, not the real back (user Fix: use this image as reference of the back) → new start frame v3 from the user's photo, grey ribbed pad with a raised ridge, confirmed by the user; same small tilt, sound off")
call["risks"] = [{"risk": "the strap spins and the back changes", "prevented_by": "small tilt only; no turning the strap round"},
                 {"risk": "the pad's ribs or ridge morph", "prevented_by": "no ribs changing direction, no ridge flattening; HOLD-PC"},
                 {"risk": "fingers fuse with the shell", "prevented_by": "no extra or fused fingers"}]
json.dump(call, open(D + "BR-039.call.json", "w"), ensure_ascii=False, indent=1)
open(D + "BR-039.kie_prompt.txt", "w").write(prompt)
print(len(prompt), call["duration"])
