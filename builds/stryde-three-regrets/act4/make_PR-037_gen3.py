"""PR-037 clip gen 3 (§22X): user Fix "change the hand motion" on v2 (the quarter turn in the fingers twisted and flexed the shell) + new confirmed start frame v3 (brand-new strap) → the whole hand lifts the strap a little toward the lens and holds, fingers and wrist locked, no turning; sound off."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
old = json.load(open(D + "PR-037.call.json"))
json.dump(old, open(D + "PR-037_g2.call.json", "w"), ensure_ascii=False, indent=1)
p = json.loads(old["prompt"])
p["subject"] = "THE SAME HAND and brand-new strap as in the start frame; unchanged in every respect."
mo = p["motion"]; i = mo.index("The product keeps")
p["motion"] = ("CONTINUING: her hand already holds the strap up by the window in a bottom-edge pinch, the wordmark facing the lens. "
               "COMPLETING: one gentle presenting move, about two seconds — forearm and hand move as one piece, lifting the strap a few centimetres toward the lens as if showing it to someone, then settle; fingers and wrist locked, the strap square to the lens, never turning. "
               "UNRESOLVED: held up, still, facing the lens. " + mo[i:])
p["negatives"] = p["negatives"].replace("no strap swinging,", "no strap swinging, no turning, no rotating, no wrist twist, no finger movement, no squeezing, no regripping, no strap tilting away,")
prompt = json.dumps(p, ensure_ascii=False, separators=(",", ":"))
call = dict(old, prompt=prompt, generation=3, audio=False, user_go="fix PR-037 (user in chat, 2026-09-30, on the v2 clip, card note: change the hand motion)",
            start_image="https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_091516_8727cd8f-db44-41d0-9395-682529abac7f.png",
            fix_note="motion + frame fault: v2 turned the strap in her fingers, twisting and flexing the shell, and the old frame looked used (user Fixes: brand new product; change the hand motion) → new confirmed frame v3 (brand-new strap); motion is now one gentle lift toward the lens with fingers and wrist locked, no turning; sound off")
call["risks"] = [{"risk": "the shell twists or flexes", "prevented_by": "no turning, no wrist twist; rigid shell never bends"},
                 {"risk": "the fingers regrip and fuse with the shell", "prevented_by": "no finger movement, no regripping; HOLD-HC"},
                 {"risk": "the strap changes size as it nears the lens", "prevented_by": "a few centimetres only; no strap growing or shrinking"}]
json.dump(call, open(D + "PR-037.call.json", "w"), ensure_ascii=False, indent=1)
open(D + "PR-037.kie_prompt.txt", "w").write(prompt)
print(len(prompt), call["duration"])
