"""HK1-01 clip gen 3 (§22X, user_go): start image v4, the hook's own outfit; strings shared with act6/make_act6_calls.py."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
A6 = D + "../../act6/make_act6_calls.py"
ns = {"__file__": A6}
exec(open(A6).read().split("HPC =")[0], ns)
R1C, HOLD_C, HOLD_HC, PHYS, CAP, NEGW = [ns[k] for k in ("R1C", "HOLD_C", "HOLD_HC", "PHYS", "CAP", "NEGW")]
URL = "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_204225_69bf0596-516f-4829-863b-d86a399b3dc0.png"
motion = ("CONTINUING: she sits on the bed edge, both hands clamped round her right knee, wincing. "
          "COMPLETING: one slow painful rock forward, about two seconds — she leans over the knee, the wince tightening, then eases a little back. "
          "UNRESOLVED: she stays bent over the knee, still hurting.")
prompt = json.dumps({"shot": "hk1_01_struggle",
    "subject": "THE SAME WOMAN, CLOTHES AND BEDROOM as in the start frame; unchanged in every respect.",
    "camera": {"movement": R1C, "framing": "MEDIUM as in the start frame: eye height from the doorway, three-quarter, the room around her. FOCUS: her face and hands on the knee are sharp."},
    "motion": motion + " " + HOLD_C + " " + HOLD_HC + " " + PHYS, "lighting": CAP,
    "style": "Unremarkable phone clip, grey flat late-morning window light from the right, no grade.",
    "negatives": NEGW + ", no standing up, no letting go of the knee, no clothes changing, no crying, no talking, no face to the lens, no furniture moving, no music"},
    ensure_ascii=False, separators=(",", ":"))
call = {"beat": "HK1-01", "connector": "kling", "mode": 1, "kind": "broll", "prompt": prompt, "duration": 3, "resolution": "1080p", "aspect_ratio": "9:16",
        "start_image": URL, "start_approved": True, "pinned": False, "subject_motion": "in_place", "prefer_multi_shots": "false", "generation": 3,
        "user_go": "user 2026-09-29: \"MAKE CLIP FOR HK1-01\" (after image v4, told it would be the 3rd generation)",
        "fix_note": "frame fault: gen 2 was from v3 in the dressing gown (user Fix: CHANGE CLOTHES) → new start image v4, the hook's own outfit, confirmed by the user; same single painful rock",
        "risks": [{"risk": "she stands up or lets go", "prevented_by": "one rock, stays seated; no standing up, no letting go of the knee"},
                  {"risk": "the outfit changes mid-clip", "prevented_by": "subject unchanged; no clothes changing"},
                  {"risk": "hands fuse with the knee", "prevented_by": "HOLD-HC"}]}
json.dump(call, open(D + "HK1-01.call.json", "w"), ensure_ascii=False, indent=1)
open(D + "HK1-01.kie_prompt.txt", "w").write(prompt)
print("HK1-01", len(prompt))
