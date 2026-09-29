"""HK1-01 / HK1-02 clip gen 2 (§22X): new start frames after the user's image Fixes; strings shared with act6/make_act6_calls.py."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
A6 = D + "../../act6/make_act6_calls.py"
ns = {"__file__": A6}
exec(open(A6).read().split("HPC =")[0], ns)
R1C, LOCK, HOLD_C, HOLD_HC, PHYS, CAP, NEGW = [ns[k] for k in ("R1C", "LOCK", "HOLD_C", "HOLD_HC", "PHYS", "CAP", "NEGW")]
HF = "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/"
B = [
 dict(beat="HK1-01", dur=3, url=HF + "hf_20260929_193752_d163c373-a8fe-4578-87ab-64f020c880ea.png", cam=R1C, sm="in_place",
  subject="THE SAME WOMAN AND BEDROOM as in the start frame; unchanged in every respect.",
  framing="MEDIUM as in the start frame: eye height from the doorway, three-quarter, the room around her. FOCUS: her face and hands on the knee are sharp.",
  motion="CONTINUING: she sits on the bed edge, both hands clamped round her right knee, wincing. COMPLETING: one slow painful rock forward, about two seconds — she leans over the knee, the wince tightening, then eases a little back. UNRESOLVED: she stays bent over the knee, still hurting.",
  style="Unremarkable phone clip, grey flat late-morning window light from the right, no grade.",
  negs="no standing up, no letting go of the knee, no crying, no talking, no face to the lens, no furniture moving, no music",
  fix="frame fault: v1 did not look like struggling, then the room drifted from P1 (user Fixes 1-2) → new start frame v3 in the P1 bedroom, wincing, confirmed by the user; motion kept to one slow painful rock",
  risks=[{"risk":"she stands up or lets go","prevented_by":"one rock, stays seated; no standing up, no letting go of the knee"},
         {"risk":"the room warps or furniture moves","prevented_by":"HOLD-C; no furniture moving"},
         {"risk":"hands fuse with the knee","prevented_by":"HOLD-HC"}]),
 dict(beat="HK1-02", dur=4, url=HF + "hf_20260929_194359_c572bebd-0eae-4091-a315-134173c88c69.png", cam=LOCK, sm="in_place",
  subject="THE SAME MAN AND BUS SHELTER as in the start frame; unchanged in every respect.",
  framing="FULL as in the start frame: low at his knee height, three-quarter front, the bench and the street around. FOCUS: deep.",
  motion="CONTINUING: he is half up off the red bench, hands pushing hard on his knees, grimacing. COMPLETING: one slow hard push, about three seconds — he pushes on his knees and straightens part way, the right knee stiff and slow, his face strained, a small wobble as his weight comes over his feet. UNRESOLVED: he is nearly upright, still bent a little, catching his breath.",
  style="Unremarkable phone clip, flat grey overcast late-morning daylight from the street on the left, no grade.",
  negs="no sitting back down, no falling, no walking away, no stepping off the kerb, no quick easy stand, no talking, no face to the lens, no music",
  fix="frame fault: v1 was a kerb step, then half-perched through glass, then a calm face (user Fixes 1-3) → new start frame v4, half up off the bench, grimacing, confirmed by the user; motion rewritten as one slow hard push toward standing, camera locked",
  risks=[{"risk":"he stands up too easily","prevented_by":"one slow hard push, nearly upright; no quick easy stand"},
         {"risk":"he falls or sits back","prevented_by":"no falling, no sitting back down"},
         {"risk":"the camera travels with him","prevented_by":"locked-off camera"}]),
]
for b in B:
    prompt = json.dumps({"shot": b["beat"].lower().replace("-", "_") + "_struggle", "subject": b["subject"],
        "camera": {"movement": b["cam"], "framing": b["framing"]},
        "motion": b["motion"] + " " + HOLD_C + " " + HOLD_HC + " " + PHYS, "lighting": CAP, "style": b["style"],
        "negatives": NEGW + ", " + b["negs"]}, ensure_ascii=False, separators=(",", ":"))
    call = {"beat": b["beat"], "connector": "kling", "mode": 1, "kind": "broll", "prompt": prompt, "duration": b["dur"], "resolution": "1080p",
            "aspect_ratio": "9:16", "start_image": b["url"], "start_approved": True, "pinned": False, "subject_motion": b["sm"],
            "prefer_multi_shots": "false", "generation": 2, "fix_note": b["fix"], "risks": b["risks"]}
    json.dump(call, open(D + b["beat"] + ".call.json", "w"), ensure_ascii=False, indent=1)
    open(D + b["beat"] + ".kie_prompt.txt", "w").write(prompt)
    print(b["beat"], len(prompt))
