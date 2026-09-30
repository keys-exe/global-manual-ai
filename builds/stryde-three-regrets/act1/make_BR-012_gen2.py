"""BR-012 clip gen 2 (§22X): new start frame v4 (front view at knee height, finger on the patellar tendon) after the user's image Fixes; sound off (user standing rule 2026-09-29)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
old = json.load(open(D + "BR-012.call.json"))
json.dump(old, open(D + "BR-012_g1.call.json", "w"), ensure_ascii=False, indent=1)
p = json.loads(old["prompt"])
p["subject"] = "THE SAME KNEE, HANDS AND DRESSING-GOWN SLEEVE as in the start frame; unchanged in every respect."
p["camera"]["framing"] = "CU as in the start frame: knee height, in front of the bent knee. FOCUS: the fingertip on the tendon under the kneecap is sharp; the quilt and carpet fall soft."
mo = p["motion"]; i = mo.index("Everything in frame")
p["motion"] = ("CONTINUING: her right forefinger already rests on the patellar tendon just under the kneecap. "
               "COMPLETING: one press, about two seconds — the fingertip pushes straight in, the skin dimpling round it, the finger bending at the first knuckle with the pressure; "
               "a small flinch runs through her hand and the knee twitches slightly, then she holds the press. "
               "UNRESOLVED: the finger stays pressed in under the kneecap. " + mo[i:])
p["motion"] = p["motion"].replace("Mass and momentum in all movement: heavy starts and settles slow, nothing at uniform speed, nothing stops instantly — motions decelerate into a settle or small overshoot; actions travel through the body, weight transferring first, hands arriving last; hair, fabric and straps lag and keep moving after the body stops; objects drag with friction, never glide.", "Mass and momentum: nothing at uniform speed, motions settle slowly, fabric lags.")
p["negatives"] = p["negatives"].replace("no face turning to the lens,", "no face, no finger sliding onto the kneecap, no finger moving to the side,") + ", no sound"
prompt = json.dumps(p, ensure_ascii=False, separators=(",", ":"))
call = dict(old, prompt=prompt, generation=2, audio=False,
            start_image="https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_214018_d8d65386-01e9-468a-a6ab-778acb4eee12.png",
            fix_note="frame fault: v1-v3 showed the hand gripping the side of the knee from over her shoulder, never on the tendon (user Fixes) → new start frame v4 in front of the knee, finger on the patellar tendon under the kneecap, confirmed by the user; motion rewritten as one straight press, sound off")
call["risks"] = [{"risk": "the finger slides off the tendon onto the kneecap", "prevented_by": "one straight press; no finger sliding onto the kneecap"},
                 {"risk": "fingers fuse with the knee", "prevented_by": "HOLD-HC; five separate fingers"},
                 {"risk": "the camera moves to show her face", "prevented_by": "framing as in the start frame; no face"}]
json.dump(call, open(D + "BR-012.call.json", "w"), ensure_ascii=False, indent=1)
open(D + "BR-012.kie_prompt.txt", "w").write(prompt)
print(len(prompt))
