"""BR-042 clip gen 4 (user go: "MAKE CLIP FOR BR-042", 2026-09-30) on the confirmed v11 frame (jogging, strap under the kneecap), and BR-058 clip gen 2 on the confirmed v3 frame (finger under a line of the letter); sound off."""
import json, os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/"
MM = "Mass and momentum in all movement: heavy starts and settles slow, nothing at uniform speed, nothing stops instantly — motions decelerate into a settle or small overshoot; actions travel through the body, weight transferring first, hands arriving last; hair, fabric and straps lag and keep moving after the body stops; objects drag with friction, never glide."
def build(path, gen, subject, framing, motion, marker, neg_add, img, fix, risks, style=None, go=None, neg_drop=()):
    old = json.load(open(R + path + ".call.json"))
    json.dump(old, open(R + path + f"_g{gen-1}.call.json", "w"), ensure_ascii=False, indent=1)
    p = json.loads(old["prompt"])
    p["subject"] = subject; p["camera"]["framing"] = framing
    mo = p["motion"]; i = mo.index(marker)
    p["motion"] = (motion + " " + mo[i:]).replace(MM, "Mass and momentum: nothing at uniform speed, motions settle slowly, fabric lags.")
    if style: p["style"] = style
    n = p["negatives"]
    for x in neg_drop: n = n.replace(x, "")
    p["negatives"] = n.rstrip(", ") + ", " + neg_add + ", no sound"
    prompt = json.dumps(p, ensure_ascii=False, separators=(",", ":"))
    call = dict(old, prompt=prompt, generation=gen, audio=False, start_image=img, fix_note=fix, risks=risks)
    if go: call["user_go"] = go
    json.dump(call, open(R + path + ".call.json", "w"), ensure_ascii=False, indent=1)
    open(R + path + ".kie_prompt.txt", "w").write(prompt)
    print(path, len(prompt), call["duration"])

build("act4/BR-042", 4,
      "THE SAME WOMAN'S LEGS, SHORTS, T-SHIRT AND STRAP as in the start frame, the strap on the bare skin just below her right kneecap; unchanged in every respect.",
      "MEDIUM as in the start frame: knee height, three-quarter front on the gravel park path, waist down. FOCUS: the strapped knee is sharp.",
      "CONTINUING: she is already jogging towards the lens at an easy pace, mid-stride. "
      "COMPLETING: two easy jogging strides, about three seconds, at a gentle recreational pace; the strapped knee bends and straightens with each stride and the strap stays exactly in place just below the kneecap, the rigid shell never bending. "
      "UNRESOLVED: still jogging, mid-stride.",
      "The product keeps",
      "no sprinting, no running out of frame, no strap sliding, no strap moving onto the kneecap, no shell bending, no feet leaving the frame, no camera following her",
      "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_225543_7d1c9132-322f-46f6-97ba-4231cb34c401.png",
      "frame fault: v3 clip tapped the notch on the v10 bedroom frame (user Fix: the person is running while using the Stryde product) → new start frame v11 jogging on a park path, confirmed by the user; motion rewritten as two easy jogging strides with the strap staying put, sound off",
      [{"risk": "the strap slides or morphs as the knee bends", "prevented_by": "strap stays exactly in place; no strap sliding, no shell bending"},
       {"risk": "she runs out of frame", "prevented_by": "two strides toward the lens; no running out of frame"},
       {"risk": "the legs warp mid-stride", "prevented_by": "HOLD-C; limbs keep their length"}],
      style="Unremarkable phone clip, warm late-morning sun, no grade.",
      go="MAKE CLIP FOR BR-042 (user in chat, 2026-09-30) — go for gen 4, §22X",
      neg_drop=("no trousers over the strap, ", "no finger pressing the kneecap, "))

build("act6/BR-058", 2,
      "THE SAME WOMAN, HANDS AND TYPED LETTER as in the start frame, rust shirt, at the wooden table; unchanged in every respect.",
      "MEDIUM CLOSE as in the start frame: eye height across the table, her hands and the letter, her face cut at the eyes. FOCUS: her fingertip and the typed line are sharp.",
      "CONTINUING: her right forefinger rests under one typed line near the bottom of the letter. "
      "COMPLETING: one slow small trace, about two seconds — the fingertip moves a finger's width along under the line and stops; her left hand stays still on the table. "
      "UNRESOLVED: her finger rests there, still, her head bowed slightly over the page.",
      "Everything in frame",
      "no readable text, no letters forming words, no page turning, no paper sliding, no hand lifting off the page, no crying",
      "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_231115_e695a1bd-1826-4f19-8a32-eb095650cd1a.png",
      "frame fault: v1 clip traced a handwritten card on a pinboard (user Fixes: a typed letter, then change camera angle) → new start frame v3 at the table, finger under a typed line, confirmed by the user; same small trace, sound off",
      [{"risk": "the text turns readable or changes", "prevented_by": "no readable text, no letters forming words"},
       {"risk": "the page slides or turns", "prevented_by": "no page turning, no paper sliding"},
       {"risk": "the finger fuses into the page", "prevented_by": "HOLD-HC; five separate fingers"}],
      style="Unremarkable phone clip, soft daylight from the window on the left, no grade.",
      neg_drop=("no readable words, ", "no words forming, ", "no card falling, ", "no pins moving, ", "no face, "))
