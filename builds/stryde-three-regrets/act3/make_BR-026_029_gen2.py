"""BR-026 and BR-029 clips gen 2 (§22X): new start frames confirmed by the user (BR-026 v4 three walkers with bare knees; BR-029 v3 whole body, sad) — "MAKE CLIP FOR BR-026 / BR-029"; sound off (user standing rule 2026-09-29)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
MM = "Mass and momentum in all movement: heavy starts and settles slow, nothing at uniform speed, nothing stops instantly — motions decelerate into a settle or small overshoot; actions travel through the body, weight transferring first, hands arriving last; hair, fabric and straps lag and keep moving after the body stops; objects drag with friction, never glide."
def build(beat, subject, framing, motion, neg_add, neg_drop, img, fix, risks, style=None):
    old = json.load(open(D + beat + ".call.json"))
    json.dump(old, open(D + beat + "_g1.call.json", "w"), ensure_ascii=False, indent=1)
    p = json.loads(old["prompt"])
    p["subject"] = subject
    p["camera"]["framing"] = framing
    mo = p["motion"]; i = mo.index("Everything in frame")
    p["motion"] = (motion + " " + mo[i:]).replace(MM, "Mass and momentum: nothing at uniform speed, motions settle slowly, fabric lags.")
    if style: p["style"] = style
    n = p["negatives"]
    for x in neg_drop: n = n.replace(x, "")
    p["negatives"] = n.rstrip(", ") + ", " + neg_add + ", no sound"
    prompt = json.dumps(p, ensure_ascii=False, separators=(",", ":"))
    call = dict(old, prompt=prompt, generation=2, audio=False, start_image=img, fix_note=fix, risks=risks)
    json.dump(call, open(D + beat + ".call.json", "w"), ensure_ascii=False, indent=1)
    open(D + beat + ".kie_prompt.txt", "w").write(prompt)
    print(beat, len(prompt), call["duration"])

build("BR-026",
      "THE SAME THREE WOMEN as in the start frame — red anorak and khaki shorts, navy fleece and denim skirt, teal waterproof and grey shorts — each with ONE Stryde strap on the bare skin just below the near kneecap; unchanged in every respect.",
      "MEDIUM as in the start frame: knee height, side-on to the path, the lawn and brick flats behind. FOCUS: the near knees and straps are sharp.",
      "CONTINUING: the three women are already mid-stride along the path, one behind the other, left to right. "
      "COMPLETING: they walk on at an easy, cheerful pace for about three seconds, two relaxed strides each, arms swinging, moving a little to the right across the frame; "
      "each strap stays exactly in place below the kneecap as the knee bends and straightens, the rigid black shell never bending. "
      "UNRESOLVED: they are still walking, all three fully in frame.",
      "no walkers leaving frame, no fourth person, no strap sliding, no strap moving onto the kneecap, no strap over clothing, no shell bending, no trousers, no running, no faces turning to the lens",
      ["no walkers entering the room, ", "no window opening, ", "no faces of the walkers, ", "no turning to the lens, "],
      "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_080345_e3462dfb-5139-46b8-a63b-3c494dd3aacd.png",
      "frame fault: v1 was Joan watching walkers through a net curtain (user Fixes: show women outside walking with Stryde on the knee, not over the pants) → new start frame v4, three women walking outside with bare knees, one strap each, confirmed by the user; motion rewritten as an easy walk with the straps staying put, sound off",
      [{"risk": "the straps slide or morph as the knees bend", "prevented_by": "each strap stays in place; no strap sliding, no shell bending"},
       {"risk": "the walkers leave frame or a fourth appears", "prevented_by": "two strides, all three in frame; no walkers leaving frame, no fourth person"},
       {"risk": "legs merge between the walkers", "prevented_by": "HOLD-C; exact form and count"}],
      style="Unremarkable phone clip, bright overcast afternoon daylight, no grade.")

build("BR-029",
      "THE SAME WOMAN as in the start frame, seventy-nine, white pixie crop, camel wool coat, heather-purple twinset, grey pleated skirt, black shoes, handbag; unchanged in every respect.",
      "FULL as in the start frame: her whole body from head to shoes, the steps, railing and red door behind. FOCUS: she is sharp head to shoes.",
      "CONTINUING: she stands at the foot of the steps, eyes lowered to the pavement, mouth turned down. "
      "COMPLETING: one slow breath out, about two seconds — her shoulders sink a little further, her head dips slightly, her hand tightens on the handbag strap. "
      "UNRESOLVED: she stays standing there, sad and still, eyes down.",
      "no smile, no happy face, no walking, no climbing the steps, no hand to the face, no crying, no camera moving closer, no crop to a close-up",
      ["no crying, "],
      "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_080354_d2964266-20e3-49d5-8fc9-c511ab9cd940.png",
      "frame fault: v1 was a close-up covering smile (user Fixes: sad and disappointed, then show the whole body) → new start frame v3, her whole body at the foot of the steps, sad, confirmed by the user; motion rewritten as one slow sad breath out, sound off",
      [{"risk": "she smiles", "prevented_by": "motion: sad breath out; no smile, no happy face"},
       {"risk": "the camera pushes in and crops her", "prevented_by": "FULL as in the start frame; no crop to a close-up"},
       {"risk": "she walks off or up the steps", "prevented_by": "UNRESOLVED: stays standing; no walking, no climbing the steps"}])
