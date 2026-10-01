"""BR-064 clip gen 2 (§22X): new confirmed start frame v4 (brand-new imitation wrapped round the leg) after the user's Fixes ("a brand new imitation, then its band snaps and it falls to the floor"; "make the strap go around the knee") → one action: the band snaps at the buckle and the imitation drops to the floor; sound off."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
old = json.load(open(D + "BR-064.call.json"))
json.dump(old, open(D + "BR-064_g1.call.json", "w"), ensure_ascii=False, indent=1)
p = json.loads(old["prompt"])
p["shot"] = "act6_copy_snaps"
p["subject"] = "THE SAME LEG, KITCHEN CHAIR AND BRAND-NEW CHEAP IMITATION STRAP as in the start frame, the thin band wrapped round the leg below the knee; unchanged in every respect."
p["camera"]["framing"] = "CU as in the start frame: low, shin height, profile, the knee, the shin and the tiled floor below. FOCUS: the imitation is sharp."
mo = p["motion"]; i = mo.index("One small movement")
p["motion"] = ("CONTINUING: the imitation sits tight on the leg, the thin band stretched beside one buckle. "
               "COMPLETING: one snap and fall, about three seconds — the thin nylon band snaps apart right beside the buckle with a small flick, its two loose ends springing back; "
               "the imitation loosens, slides down the shin and drops to the tiled floor in frame, landing with one small bounce and settling there. "
               "UNRESOLVED: the imitation lies on the floor, the leg bare and still. "
               "Apart from the band snapping at the buckle, everything in frame keeps its exact form, proportion and count first frame to last — nothing melts, merges, grows or becomes something else. "
               + mo[i:].replace("One small movement, completing inside the clip, subject fully in frame throughout, nothing leaving frame and returning.", "One action, completing inside the clip, the imitation in frame throughout, landing in frame.")
               ).replace("Mass and momentum in all movement: heavy starts and settles slow, nothing at uniform speed, nothing stops instantly — motions decelerate into a settle or small overshoot; actions travel through the body, weight transferring first, hands arriving last; hair, fabric and straps lag and keep moving after the body stops; objects drag with friction, never glide.",
                         "Mass and momentum: the band snaps suddenly, the imitation falls under its own weight and settles, nothing at uniform speed.")
p["negatives"] = p["negatives"].replace("no strap falling off the leg, ", "").replace("no splitting, no parts detaching, ", "") + ", no shell breaking into pieces, no band snapping anywhere but beside the buckle, no imitation leaving frame, no second strap, no leg kicking, no slow motion, no sound"
prompt = json.dumps(p, ensure_ascii=False, separators=(",", ":"))
call = dict(old, prompt=prompt, generation=2, audio=False, duration=5,
            start_image="https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_120149_ced2e2c5-0418-4c52-87a4-4ebdcc9d851f.png",
            fix_note="frame fault: v1 clip was a worn copy sagging down the shin (user Fixes: a brand-new imitation, the band round the knee, then it snaps and falls to the floor) → new start frame v4 confirmed by the user; motion rewritten as one snap at the buckle and the fall to the floor, sound off")
call["risks"] = [{"risk": "the shell shatters or splits", "prevented_by": "only the band snaps, beside the buckle; no shell breaking into pieces"},
                 {"risk": "the imitation falls out of frame", "prevented_by": "lands on the tiled floor in frame; no imitation leaving frame"},
                 {"risk": "the leg moves or kicks", "prevented_by": "the leg stays still; no leg kicking"}]
json.dump(call, open(D + "BR-064.call.json", "w"), ensure_ascii=False, indent=1)
open(D + "BR-064.kie_prompt.txt", "w").write(prompt)
print(len(prompt))
