"""BR-008 clip gen 2 (§22X): new start frame v2 in the P1 bedroom after the user's image Fix; sound off (user standing rule 2026-09-29)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
old = json.load(open(D + "BR-008.call.json"))
json.dump(old, open(D + "BR-008_g1.call.json", "w"), ensure_ascii=False, indent=1)
p = json.loads(old["prompt"])
p["subject"] = "THE SAME WOMAN AND BEDROOM as in the start frame; unchanged in every respect."
p["camera"]["framing"] = "MEDIUM (waist-up) as in the start frame: eye height from the doorway, three-quarter, standing by the chest and its open drawer, the bed and window behind. FOCUS: her face is sharp; the room stays readable, slightly soft."
p["negatives"] = p["negatives"].replace("no music", "no furniture moving, no music, no sound")
prompt = json.dumps(p, ensure_ascii=False, separators=(",", ":"))
call = dict(old, prompt=prompt, generation=2, audio=False,
            start_image="https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_210543_8f2dab6f-1c92-4e5a-a3f5-b9cae924d743.png",
            fix_note="frame fault: v1 was not in the P1 bedroom (user Fix: USE P1-G-BEDROOM AS BACKGROUND) → new start frame v2 in the P1 room, waist-up, confirmed by the user; same single tired shrug; sound off")
call["risks"] = old["risks"] + [{"risk": "the room warps or furniture moves", "prevented_by": "HOLD-C; no furniture moving"}]
json.dump(call, open(D + "BR-008.call.json", "w"), ensure_ascii=False, indent=1)
open(D + "BR-008.kie_prompt.txt", "w").write(prompt)
print(len(prompt))
