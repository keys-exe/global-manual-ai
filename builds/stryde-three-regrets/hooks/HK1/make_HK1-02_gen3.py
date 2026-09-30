"""HK1-02 clip gen 3 (§22X, user_go): start image v7, seated on the bench; strings shared with act6/make_act6_calls.py."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
A6 = D + "../../act6/make_act6_calls.py"
ns = {"__file__": A6}
exec(open(A6).read().split("HPC =")[0], ns)
LOCK, HOLD_C, HOLD_HC, PHYS, CAP, NEGW = [ns[k] for k in ("LOCK", "HOLD_C", "HOLD_HC", "PHYS", "CAP", "NEGW")]
URL = "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_200407_4aa6d8d9-4817-4752-8c52-ed96cedc8edf.png"
motion = ("CONTINUING: he sits on the red bench, hands gripping the seat edge, grimacing, gathering himself. "
          "COMPLETING: one slow hard push up, about three seconds — he leans forward, pushes down on the seat edge and rises part way off the bench, the right knee stiff and slow, his face strained, a small wobble as his weight comes over his feet. "
          "UNRESOLVED: he is half up, still bent forward, one hand still on the seat edge, catching his breath.")
prompt = json.dumps({"shot": "hk1_02_bench_push",
    "subject": "THE SAME MAN, BENCH AND BUS STOP as in the start frame; unchanged in every respect.",
    "camera": {"movement": LOCK, "framing": "MEDIUM-FULL as in the start frame: low at his knee height, three-quarter, him on the left, the street running away on the right. FOCUS: his face and hands are sharp."},
    "motion": motion + " " + HOLD_C + " " + HOLD_HC + " " + PHYS, "lighting": CAP,
    "style": "Unremarkable phone clip, flat grey overcast daylight, no grade.",
    "negatives": NEGW + ", no quick easy stand, no standing fully upright, no sitting back down, no falling, no walking away, no talking, no face to the lens, no music"},
    ensure_ascii=False, separators=(",", ":"))
call = {"beat": "HK1-02", "connector": "kling", "mode": 1, "kind": "broll", "prompt": prompt, "duration": 4, "resolution": "1080p", "aspect_ratio": "9:16",
        "start_image": URL, "start_approved": True, "pinned": False, "subject_motion": "in_place", "prefer_multi_shots": "false", "generation": 3,
        "user_go": "user 2026-09-29: \"MAKE CLIP FOR HK1-02\" (after image v7, told it would be the 3rd generation)",
        "fix_note": "frame fault: gen 2 started half-standing and the user asked for him seated, the P3 street and a new angle (image Fixes 4-6) → new start image v7, seated on the bench, low and close, confirmed by the user; motion is one slow hard push to half up, camera locked",
        "risks": [{"risk": "he stands too easily", "prevented_by": "one slow hard push to half up; no quick easy stand, no standing fully upright"},
                  {"risk": "he falls or sits back", "prevented_by": "no falling, no sitting back down"},
                  {"risk": "the camera follows him up", "prevented_by": "locked-off camera"}]}
json.dump(call, open(D + "HK1-02.call.json", "w"), ensure_ascii=False, indent=1)
open(D + "HK1-02.kie_prompt.txt", "w").write(prompt)
print("HK1-02", len(prompt))
