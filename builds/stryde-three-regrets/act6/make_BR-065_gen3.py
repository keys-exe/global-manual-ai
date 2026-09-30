"""BR-065 clip gen 3 (§22X): user Fix on v2 "the woman must not hold the railings at any time" — motion fault (she drifted left toward the railing and her basket hand brushed the post) → she walks straight down and slightly away from the railing, the basket held low in her right hand throughout; sound off."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
old = json.load(open(D + "BR-065.call.json"))
json.dump(old, open(D + "BR-065_g2.call.json", "w"), ensure_ascii=False, indent=1)
p = json.loads(old["prompt"])
mo = p["motion"]; i = mo.index("The product keeps")
p["motion"] = ("CONTINUING: she is stepping down, basket low in her right hand, left arm free. "
               "COMPLETING: two easy steps down, about three seconds, straight down and slightly right, AWAY from the railing; the strap stays below the kneecap, her smile holding. The basket stays low in her right hand; the gap to the railing only grows. "
               "UNRESOLVED: she keeps coming down, whole body in frame. " + mo[i:])
p["negatives"] = p["negatives"].replace("no hand on the railing, no reaching for the railing,", "no hand on the railing, no touching the railing or post, no reaching for the railing, no drifting left, no letting go of the basket,")
prompt = json.dumps(p, ensure_ascii=False, separators=(",", ":"))
call = dict(old, prompt=prompt, generation=3, audio=False, user_go="FIX BR-065 (user in chat, 2026-09-30, card note: THE WOMAN MUST NOT HOLD IN RAILINGS AT ANY TIME)",
            fix_note="motion fault: v2 drifted left toward the railing and her basket hand brushed the post (user Fix: must not hold the railings at any time) → her path goes straight down and away from the railing, the basket held low in her right hand throughout; same confirmed v4 frame; sound off")
call["risks"] = [{"risk": "her hand touches the railing", "prevented_by": "basket held low throughout; path away from the railing; no hand touching the railing or its post"},
                 {"risk": "the strap slides", "prevented_by": "strap stays in place; no strap moving onto the kneecap"},
                 {"risk": "she walks out of frame", "prevented_by": "two steps; whole body in frame"}]
json.dump(call, open(D + "BR-065.call.json", "w"), ensure_ascii=False, indent=1)
open(D + "BR-065.kie_prompt.txt", "w").write(prompt)
print(len(prompt))
