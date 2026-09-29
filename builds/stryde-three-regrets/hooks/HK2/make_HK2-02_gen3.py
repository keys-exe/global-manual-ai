"""HK2-02 clip gen 3 (§22X, user_go): start image v6, three numbered stacks; strings shared with act6/make_act6_calls.py."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
A6 = D + "../../act6/make_act6_calls.py"
ns = {"__file__": A6}
exec(open(A6).read().split("HPC =")[0], ns)
R1C, HOLD_C, HOLD_HC, PHYS, CAP, NEGW = [ns[k] for k in ("R1C", "HOLD_C", "HOLD_HC", "PHYS", "CAP", "NEGW")]
URL = "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_174126_5aebba75-f61e-4fd5-b42e-5b9c47c355d3.png"
motion = ("CONTINUING: her right hand is laying one more opened letter onto the top of the middle stack. "
          "COMPLETING: one set-down, about two seconds — the letter settles flat on the stack and her hand lifts away and rests on the desk. "
          "UNRESOLVED: she looks at the three stacks, still.")
prompt = json.dumps({"shot": "hk2_three_stacks",
    "subject": "THE SAME WOMAN, DESK AND THREE NUMBERED STACKS OF LETTERS as in the start frame; unchanged in every respect. The three cards read 1, 2 and 3 in every frame.",
    "camera": {"movement": R1C, "framing": "MEDIUM as in the start frame: low, just above the desk, three-quarter front, the stacks towering. FOCUS: the stacks and their numbered cards are sharp."},
    "motion": motion + " " + HOLD_C + " " + HOLD_HC + " " + PHYS, "lighting": CAP,
    "style": "Unremarkable phone clip, soft cool morning window light from the left, no grade.",
    "negatives": NEGW + ", no stacks falling or sliding, no letters scattering, no numbers changing, no fourth stack, no readable words on the letters, no pinboard, no face to the lens, no talking, no music"},
    ensure_ascii=False, separators=(",", ":"))
call = {"beat": "HK2-02", "connector": "kling", "mode": 1, "kind": "broll", "prompt": prompt, "duration": 3, "resolution": "1080p", "aspect_ratio": "9:16",
        "start_image": URL, "start_approved": True, "pinned": False, "subject_motion": "in_place", "prefer_multi_shots": "false", "generation": 3,
        "user_go": "user 2026-09-29: \"MAKE CLIP FOR HK2-02\" (after image v6, told it would be the 3rd generation)",
        "fix_note": "frame fault: v5 (one letter) did not show 'more than anything else' (user Fix 6) → new start image v6, three tall numbered stacks of letters, confirmed by the user; motion rewritten for it: one set-down of a letter on the middle stack, stacks rigid, numbers held",
        "risks": [{"risk": "a stack topples or letters scatter", "prevented_by": "one gentle set-down; HOLD-C; no stacks falling or sliding, no letters scattering"},
                  {"risk": "the numbers morph or the cards rewrite", "prevented_by": "subject: cards read 1, 2 and 3 in every frame; no numbers changing"},
                  {"risk": "fingers fuse with the paper", "prevented_by": "HOLD-HC; the hand lifts away and rests on the desk"}]}
json.dump(call, open(D + "HK2-02.call.json", "w"), ensure_ascii=False, indent=1)
open(D + "HK2-02.kie_prompt.txt", "w").write(prompt)
print("HK2-02", len(prompt))
