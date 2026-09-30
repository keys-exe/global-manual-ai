"""BR-065 clip gen 2 (§22X): new confirmed start frame v4 (real Stryde below her right kneecap, hands clear of the railing) after the user's Fixes ("don't hold the railings"; "change the product into a Stryde product") → two easy steps down, hands free; sound off."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
old = json.load(open(D + "BR-065.call.json"))
json.dump(old, open(D + "BR-065_g1.call.json", "w"), ensure_ascii=False, indent=1)
p = json.loads(old["prompt"])
p["subject"] = "THE SAME WOMAN as in the start frame, coral cardigan, navy polka-dot dress, white flats, straw basket, one Stryde strap on the bare skin below her right kneecap; unchanged in every respect."
p["camera"]["framing"] = "FULL as in the start frame: low at the foot of the steps, her whole body, the red door behind. FOCUS: her strapped knee and face are sharp."
mo = p["motion"]; i = mo.index("The product keeps")
p["motion"] = ("CONTINUING: she is already stepping down, her right foot lowering onto the next step, both hands clear of the railing, the basket in her hand. "
               "COMPLETING: two easy steps down towards the lens, about three seconds — each foot lands and takes her weight, the strapped knee bending freely over it, the strap staying exactly in place below the kneecap, her smile holding; her hands never reach for the railing. "
               "UNRESOLVED: she keeps coming down, still on the steps, whole body in frame. " + mo[i:])
p["motion"] = p["motion"].replace("Mass and momentum in all movement: heavy starts and settles slow, nothing at uniform speed, nothing stops instantly — motions decelerate into a settle or small overshoot; actions travel through the body, weight transferring first, hands arriving last; hair, fabric and straps lag and keep moving after the body stops; objects drag with friction, never glide.",
                                  "Mass and momentum: nothing at uniform speed, weight transferring first, the dress and basket lag.")
p["negatives"] = p["negatives"].replace("no gripping the rail hard,", "no hand on the railing, no reaching for the railing, no knee sleeve, no strap moving onto the kneecap,") + ", no sound"
prompt = json.dumps(p, ensure_ascii=False, separators=(",", ":"))
call = dict(old, prompt=prompt, generation=2, audio=False,
            start_image="https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_122036_4b1d9919-0697-4dd5-90e1-7f37d79b7e25.png",
            fix_note="frame fault: v1 clip held the railing and later frames showed a generic knee sleeve (user Fixes: don't hold the railings; change the product into a Stryde product) → new start frame v4 with the real Stryde and hands free, confirmed by the user; motion rewritten with no hand on the railing, sound off")
call["risks"] = [{"risk": "her hand goes to the railing", "prevented_by": "hands never reach for the railing; no hand on the railing"},
                 {"risk": "the strap slides or turns into a sleeve", "prevented_by": "strap stays in place; no knee sleeve, no strap moving onto the kneecap"},
                 {"risk": "she walks out of frame", "prevented_by": "two steps, still on the steps; no walking past the camera"}]
json.dump(call, open(D + "BR-065.call.json", "w"), ensure_ascii=False, indent=1)
open(D + "BR-065.kie_prompt.txt", "w").write(prompt)
print(len(prompt), call["duration"])
