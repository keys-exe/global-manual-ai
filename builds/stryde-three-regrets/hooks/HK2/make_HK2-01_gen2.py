"""HK2-01 clip gen 2 (§22X): new confirmed start frame v4 (formal typed letters of different lengths) after the user's Fixes; same single lift; sound off (user standing rule 2026-09-29)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
old = json.load(open(D + "HK2-01.call.json"))
json.dump(old, open(D + "HK2-01_g1.call.json", "w"), ensure_ascii=False, indent=1)
p = json.loads(old["prompt"])
p["subject"] = "THE SAME WOMAN'S HANDS as in the start frame, 57, long knuckly fingers, rust needlecord cuffs; the desk buried in formal typed letters of different lengths; exactly as in the start frame, unchanged in every respect."
p["motion"] = p["motion"].replace("two loose envelopes sliding off the top back onto the pile", "one loose envelope sliding off the top back onto the pile").replace(
    "Mass and momentum in all movement: heavy starts and settles slow, nothing at uniform speed, nothing stops instantly — motions decelerate into a settle or small overshoot; actions travel through the body, weight transferring first, hands arriving last; hair, fabric and straps lag and keep moving after the body stops; objects drag with friction, never glide.",
    "Mass and momentum: heavy start, nothing at uniform speed, the paper sags and lags.")
p["negatives"] = p["negatives"] + ", no handwriting appearing, no letters changing, no sound"
prompt = json.dumps(p, ensure_ascii=False, separators=(",", ":"))
call = dict(old, prompt=prompt, generation=2, audio=False,
            start_image="https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_140635_9af1fe41-210a-41b0-a2a6-ed02d6068d6d.png",
            fix_note="frame fault: v1 clip was made from handwritten letters (user Fixes: formal letters, then different lengths) → new start frame v4 confirmed by the user; same single lift of the stack, sound off")
call["risks"] = [{"risk": "the typed letters morph into handwriting", "prevented_by": "no handwriting appearing, no letters changing"},
                 {"risk": "fingers fuse into the paper", "prevented_by": "no extra fingers, no fused fingers"},
                 {"risk": "papers fly off", "prevented_by": "one envelope slides back onto the pile; no letters flying"}]
json.dump(call, open(D + "HK2-01.call.json", "w"), ensure_ascii=False, indent=1)
open(D + "HK2-01.kie_prompt.txt", "w").write(prompt)
print(len(prompt))
