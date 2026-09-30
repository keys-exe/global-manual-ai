"""BR-026 clip gen 3 (§22X): user Fix on v2 "make them walk not at the same time" — motion fault (one shared stride instruction made the three march in step) → each woman walks at her own pace and rhythm, feet landing at different moments; sound off."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
old = json.load(open(D + "BR-026.call.json"))
json.dump(old, open(D + "BR-026_g2.call.json", "w"), ensure_ascii=False, indent=1)
p = json.loads(old["prompt"])
mo = p["motion"]; i = mo.index("Everything in frame")
p["motion"] = ("CONTINUING: the three women are already walking along the path, left to right, each in her own rhythm. "
               "COMPLETING: about three seconds of ordinary walking, NEVER IN STEP: the woman in red strides out briskly with long steps, "
               "the woman in navy walks a little slower with shorter steps, the woman in teal ambles, half a beat behind; their feet land at different moments, "
               "one heel striking while another foot is lifting, their arms swinging out of time; each strap stays in place below the kneecap, the rigid shell never bending. "
               "UNRESOLVED: still walking, all three fully in frame. " + mo[i:])
p["negatives"] = p["negatives"].replace("no walkers leaving frame,", "no walking in step, no marching, no synchronised legs, no matching strides, no walkers leaving frame,")
prompt = json.dumps(p, ensure_ascii=False, separators=(",", ":"))
call = dict(old, prompt=prompt, generation=3, audio=False, user_go="FIX BR-026 (user in chat, 2026-09-30, on the v2 clip)",
            fix_note="motion fault: v2 had the three women walking in step (user Fix: make them walk not at the same time) → each walks at her own pace and rhythm, feet landing at different moments, arms out of time; the confirmed v4 frame kept; sound off")
call["risks"] = [{"risk": "they walk in step again", "prevented_by": "own pace each; no walking in step, no synchronised legs"},
                 {"risk": "the straps slide or morph", "prevented_by": "each strap stays in place; no strap sliding, no shell bending"},
                 {"risk": "a walker leaves frame", "prevented_by": "about three seconds; no walkers leaving frame"}]
json.dump(call, open(D + "BR-026.call.json", "w"), ensure_ascii=False, indent=1)
open(D + "BR-026.kie_prompt.txt", "w").write(prompt)
print(len(prompt))
