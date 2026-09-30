"""BR-038 clip gen 2 (new confirmed v3 frame: walking outside in sage shorts, strap on the picture-right knee) and BR-041 clip gen 3 (user go "make clip for BR-041", new confirmed v11 frame: cycling in sage shorts); sound off."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
MM = "Mass and momentum in all movement: heavy starts and settles slow, nothing at uniform speed, nothing stops instantly — motions decelerate into a settle or small overshoot; actions travel through the body, weight transferring first, hands arriving last; hair, fabric and straps lag and keep moving after the body stops; objects drag with friction, never glide."
def build(beat, gen, subject, framing, motion, neg_add, neg_drop, img, fix, risks, style, go=None, duration=None):
    old = json.load(open(D + beat + ".call.json"))
    json.dump(old, open(D + beat + f"_g{gen-1}.call.json", "w"), ensure_ascii=False, indent=1)
    p = json.loads(old["prompt"])
    p["subject"] = subject; p["camera"]["framing"] = framing
    mo = p["motion"]; i = mo.index("The product keeps")
    p["motion"] = (motion + " " + mo[i:]).replace(MM, "Mass and momentum: nothing at uniform speed, motions settle slowly, fabric lags.")
    p["style"] = style
    n = p["negatives"]
    for x in neg_drop: n = n.replace(x, "")
    p["negatives"] = n.rstrip(", ") + ", " + neg_add + ", no sound"
    prompt = json.dumps(p, ensure_ascii=False, separators=(",", ":"))
    call = dict(old, prompt=prompt, generation=gen, audio=False, start_image=img, fix_note=fix, risks=risks)
    if duration: call["duration"] = duration
    if go: call["user_go"] = go
    json.dump(call, open(D + beat + ".call.json", "w"), ensure_ascii=False, indent=1)
    open(D + beat + ".kie_prompt.txt", "w").write(prompt)
    print(beat, len(prompt), call["duration"])

build("BR-038", 2,
      "THE SAME WOMAN'S LEGS, SAGE LINEN SHORTS, SANDALS AND STRAP as in the start frame, the strap on the bare skin below the kneecap of the leg on the right of the picture; unchanged in every respect.",
      "MEDIUM CLOSE as in the start frame: knee height, three-quarter front on the sunny pavement, waist down. FOCUS: the strapped knee is sharp.",
      "CONTINUING: she is already walking towards the lens at an easy pace, mid-stride. "
      "COMPLETING: two easy, natural walking steps, about three seconds; the strapped knee bends and straightens with each step and the strap stays exactly in place just below the kneecap, the rigid shell never bending; her hands swing loosely. "
      "UNRESOLVED: still walking, mid-stride.",
      "no walking out of frame, no running, no strap moving onto the kneecap, no strap on the other knee, no trousers, no camera following her",
      ("no hands on the strap, ",),
      "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_081226_3c5f61ea-f5d2-434c-bb9d-7c19dd3d8288.png",
      "frame fault: v1 clip was a seated breath in the bedroom (user Fixes: walk outside; shorts in the same colour and texture; strap on the right knee) → new start frame v3 walking on the pavement in sage shorts, confirmed by the user; motion rewritten as two easy steps with the strap staying put, sound off",
      [{"risk": "the strap slides or morphs as the knee bends", "prevented_by": "strap stays exactly in place; no strap sliding, no shell bending"},
       {"risk": "she walks out of frame", "prevented_by": "two steps toward the lens; no walking out of frame"},
       {"risk": "the strap jumps to the other knee", "prevented_by": "no strap on the other knee; HOLD-PC"}],
      "Unremarkable phone clip, warm late-morning sun from the right, no grade.", duration=4)

build("BR-041", 3,
      "THE SAME WOMAN, BICYCLE, SAGE LINEN SHORTS AND STRAP as in the start frame, the strap on the bare skin below her right kneecap; unchanged in every respect.",
      "MEDIUM as in the start frame: knee height, side view of the whole bicycle on the park path. FOCUS: she, the bike and the strap are sharp.",
      "CONTINUING: she is already riding slowly along the path, left to right, right foot on the pedal near the top. "
      "COMPLETING: one slow pedal stroke, about three seconds — the right pedal goes down, the left comes up, chain and wheels turning with them, the bike moving a little right; the strap stays in place below the kneecap. "
      "UNRESOLVED: still pedalling gently, the whole bike in frame.",
      "no bike leaving frame, no broken bike geometry, no extra pedal, no feet off the pedals, no strap moving onto the kneecap, no trousers, no fast pedalling",
      ("no band pulled, ",),
      "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_091533_2bdec7ac-72eb-47a8-8e0d-1933c36dfef2.png",
      "frame fault: v2 clip was a hand press on the strap indoors (user Fixes: make the person cycle; shorts in the same colour and texture) → new start frame v11 cycling in sage shorts, confirmed by the user; motion rewritten as one slow pedal stroke with the strap staying put, sound off",
      [{"risk": "the bike geometry breaks as the pedals turn", "prevented_by": "chain and wheels turn with the pedals; no broken bike geometry, no extra pedal"},
       {"risk": "the strap slides as the knee bends", "prevented_by": "strap stays exactly in place; no strap moving onto the kneecap"},
       {"risk": "the bike rides out of frame", "prevented_by": "one slow stroke, moving a little; no bike leaving frame"}],
      "Unremarkable phone clip, warm late-morning sun from the right, no grade.",
      go="make clip for BR-041 (user in chat, 2026-09-30) — go for gen 3, §22X", duration=4)
