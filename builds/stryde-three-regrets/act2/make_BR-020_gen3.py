"""BR-020 clip gen 3 (§22X): user Fix on v2 "must not jump, act natural, face struggling" — motion fault (the 'pushes up / leg swings up' wording read as a hop from the wide lunge) → slow grounded step, one foot always down, strain on the face from frame one; sound off."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
old = json.load(open(D + "BR-020.call.json"))
json.dump(old, open(D + "BR-020_g2.call.json", "w"), ensure_ascii=False, indent=1)
p = json.loads(old["prompt"])
p["subject"] = ("THE SAME MAN as in the start frame, flat cap, tan golf jacket, stone shorts, navy socks, brown brogues; unchanged in every respect. "
                "His face STRAINED first frame to last: brow knotted, jaw clenched, wincing — struggling, never smiling.")
mo = p["motion"]; i = mo.index("Everything in frame")
p["motion"] = ("CONTINUING: left brogue already flat on top of the kerb, right hand gripping the lamp post, stiff right leg down on the road. "
               "COMPLETING: one slow laboured step up at walking pace, about four seconds, ONE FOOT ON THE GROUND AT EVERY MOMENT — he leans over the left foot, pulls on the post, "
               "the left knee straightens slowly and shakily, then the stiff right foot drags up onto the kerb and settles beside the left. "
               "UNRESOLVED: he stands hunched, gripping the post, catching his breath. " + mo[i:])
p["motion"] = p["motion"].replace("Mass and momentum in all movement: heavy starts and settles slow, nothing at uniform speed, nothing stops instantly — motions decelerate into a settle or small overshoot; actions travel through the body, weight transferring first, hands arriving last; hair, fabric and straps lag and keep moving after the body stops; objects drag with friction, never glide.",
                                  "Mass and momentum: heavy and slow, nothing at uniform speed, weight transferring first, fabric lags.")
p["negatives"] = p["negatives"].replace("no jump, no both feet in the air, no stumbling,", "no jump, no hop, no spring, no bounce, no both feet in the air, no leap, no athletic step, no quick step, no smile, no relaxed face, no fall,")
prompt = json.dumps(p, ensure_ascii=False, separators=(",", ":"))
call = dict(old, prompt=prompt, generation=3, audio=False, user_go="FIX BR-020 (user in chat, 2026-09-30, on the v2 clip)",
            fix_note="motion fault: v2 hopped up onto the kerb with a neutral face (user Fix: must not jump, act natural, face struggling) → slow laboured step at walking pace with one foot always on the ground, the trailing foot dragging up, strain on his face from frame one; the confirmed start frame kept; sound off")
call["risks"] = [{"risk": "he hops or springs up", "prevented_by": "one foot on the ground at every moment; no jump, no hop, no spring"},
                 {"risk": "his face relaxes or smiles", "prevented_by": "subject: strained face first to last; no smile"},
                 {"risk": "the right knee bends normally", "prevented_by": "stiff right foot drags up; HOLD-HC"}]
json.dump(call, open(D + "BR-020.call.json", "w"), ensure_ascii=False, indent=1)
open(D + "BR-020.kie_prompt.txt", "w").write(prompt)
print(len(prompt), call["duration"])
