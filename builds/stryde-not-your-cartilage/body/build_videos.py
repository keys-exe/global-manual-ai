#!/usr/bin/env python3
"""Step 7 body B-roll video calls (§35 JSON, §27G natural motion, §22X preflight) for the confirmed start images.
Writes body/<BEAT>.kling.json and body/<BEAT>.call.json; lengths from edit/call_lengths.json (E6)."""
import json, re, sys, pathlib
H = pathlib.Path(__file__).resolve().parent; B = H.parent; ROOT = B.parents[1]
T = (ROOT / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S); return m.group(1).strip()
L = json.loads((B / "edit/call_lengths.json").read_text())
RIGID = " The strap keeps its exact shape, size and wordmark in every frame and moves only with the leg or hand that carries it; its rigid shell never bends, flexes or changes proportion."
NEG_PROD = "no bending, no curling, no folding, no melting, no flipping of the product, no wordmark changing, no second strap"
NEG_WORN = NEG_PROD + ", no strap sliding up or down the leg, no strap turning into a narrow band"
NEG_PPL = "no second person appearing, no camera travelling with the subject, no zoom, no music, no speech"
# beat: (subject, motion, moving_subject, product: worn|held|object|absent, extra negatives, risks)
V = {
 "B-01a": ("An older man's big weathered hands, the top joint of the left index finger missing, holding the lid of a matte-black box on his knees; two straps in the insert.",
           "One slow action at an unhurried pace: his left hand lifts the lid a little higher and sets it down against the side of the box, his right hand steadying the box; the two straps stay still in their wells.",
           "in_place", "object", "no strap leaving the box, no box opening further, no third strap",
           [("the straps moving or deforming in the box", "motion keeps them still in their wells; rigid-product clause"), ("his hand or the missing fingertip warping", "one slow lift, HOLD-C + NEG-WARP-C"), ("the box lid text changing", "negatives name the wordmark; no text")]),
 "B-02b": ("Hassan, a very tall thin Black British man of seventy-two in a white shirt and navy cardigan, sitting across a desk from a consultant, looking down at a plastic knee model.",
           "One small action at a slow, heavy pace: he lowers his eyes to the knee model and lets out a slow breath, his shoulders dropping a little; the consultant stays still in the soft foreground.",
           "in_place", "absent", "no knee strap, no brace, no smile, no speaking",
           [("his face drifting from the sheet's identity", "the start frame carries it; one small movement, HOLD-C"), ("the consultant turning to camera", "she stays still, face unseen; negatives"), ("hands warping on his knees", "hands stay where they are; NEG-WARP-C")]),
 "B-03a": ("Derek, a big-framed white British man of seventy-four with a white beard, in an olive waxed jacket, jeans and a tweed cap, on a canal towpath, one hand pressed to his right knee.",
           "One action at a slow, sore pace: already stopped, he leans onto his right knee, winces, and straightens a little as he breathes out; he does not walk on.",
           "in_place", "absent", "no knee strap, no brace, no walking stick, no walking away",
           [("his legs warping as he leans", "he stays on the spot, one lean; PHYS-MOTION-C"), ("the camera following him", "RIG-R1 lags, never moves with the subject"), ("a second action (walking on)", "motion says he does not walk on; negatives")]),
 "B-03b": ("Hassan, very tall and thin, in a white shirt, navy cardigan and grey trousers, standing halfway up his steep patterned-carpet staircase, gripping the dark handrail.",
           "One small action at a slow, tired pace: standing on the same step, he tightens his grip on the handrail, closes his eyes for a moment and breathes out; he takes no step.",
           "in_place", "absent", "no knee strap, no brace, no stepping, no stairs warping",
           [("feet and stairs warping", "no step taken (§27G safe staging), HOLD-C"), ("the handrail bending under his hand", "rigid set; NEG-WARP-C"), ("his face changing", "start frame carries identity; one breath")]),
 "B-03c": ("Folake, a slim Black British woman of sixty-six with long grey-and-black box braids tied back, in a long burnt-orange cardigan, half-way up out of her burgundy armchair, hands on its arms.",
           "One action at a slow, effortful pace: pushing down on the chair arms she rises the rest of the way to standing, a wince on the way up, and steadies herself.",
           "in_place", "absent", "no knee strap, no brace, no walking away, no mug",
           [("arms and hands warping as she pushes up", "one rise at a slow pace, start frame mid-action (§27G), PHYS-MOTION-C"), ("the armchair deforming", "rigid set; NEG-WARP-C"), ("a second action (walking off)", "she only rises and steadies; negatives")]),
 "B-04": ("An older man's big weathered hand holding a matte-black strap in his open palm by a canal, the front of the shell and its grey stryde wordmark facing the phone.",
          "One small action at a slow pace: his palm tilts the strap a little towards the light and back, so the chrome slides catch a glint; the strap stays in his palm.",
          "in_place", "held", "no strap falling, no fingers covering the wordmark",
          [("the shell bending in his hand", "rigid-product clause, one small tilt"), ("the wordmark smearing as it turns", "a small tilt only; negatives name the wordmark"), ("the hand warping", "HOLD-C + NEG-WARP-C")]),
 "B-06": ("Hassan, very tall and thin, in a maroon polo and charcoal shorts, sitting on the bottom stair, his right leg out straight, the strap on his right knee.",
          "One action at a slow, careful pace: he straightens his right leg the last little way and holds it, his face easing, a small relieved breath out.",
          "in_place", "worn", "",
          [("the strap sliding as the leg moves", "rigid-product clause; 'no strap sliding'"), ("the leg or foot warping", "one small straighten, PHYS-MOTION-C"), ("his face drifting", "start frame carries identity")]),
 "B-07": ("Folake, in a yellow-and-green wax-print blouse and a navy skirt above the knee, coming down her red-carpeted staircase, a hand on the white rail, the strap on her right knee.",
          "One action at a steady, easy pace: she takes two steps down towards the camera, one foot per step, her hand sliding lightly along the rail.",
          "travels", "worn", "no stumbling, no stairs changing",
          [("feet and stairs warping on the steps", "two steps only at a countable pace; camera at the foot, never travelling (§27G)"), ("the strap sliding as she steps", "rigid-product clause; 'no strap sliding'"), ("the camera moving with her", "RIG-R1 lags, never moves with the subject")]),
 "B-09a": ("A woman's slim hands flat on both sides of a closed matte-black strap at mid-shin on her straight right leg.",
           "One action at a slow, unhurried pace: her hands slide the strap up the shin in one movement until the shell seats just below the kneecap, the notch cupping its lower edge, and her hands come to rest.",
           "in_place", "worn", "no strap being opened, no strap going over the kneecap",
           [("the strap going over the kneecap or ending too low", "SEAT-LOCK: only ever up, seats by contact"), ("the shell bending as it slides", "rigid-product clause"), ("fingers passing through the strap", "hands flat on the shell's sides; NEG-WARP-C")]),
 "B-09b": ("A woman's slim hands holding a strap turned round so the mid-grey pad inside the shell faces the phone, above a striped duvet.",
           "One small action at a slow pace: her hands tilt the strap a little so the light moves across the grooved pad and its raised ridge, then hold still.",
           "in_place", "held", "no strap turning back round, no pad changing pattern",
           [("the pad's pattern swimming", "a small tilt only; HOLD-C"), ("the shell bending", "rigid-product clause"), ("fingers warping", "NEG-WARP-C")]),
 "B-10": ("Hassan, in a maroon polo and charcoal shorts, crouched at a low kitchen cupboard reaching in, the strap on his bent right knee.",
          "One action at a steady pace: he lifts a saucepan out of the cupboard and stands back up to full height, easy, the strap staying put on his knee.",
          "in_place", "worn", "no strap sliding as the knee straightens, no saucepan warping",
          [("the strap sliding as the knee straightens", "rigid-product clause; 'no strap sliding'"), ("his body warping on the rise", "one stand at a countable pace, start frame mid-crouch (§27G), PHYS-MOTION-C"), ("the saucepan changing shape", "NEG-WARP-C")]),
 "B-11a": ("A woman's right leg from the thigh down beside a bed, an olive trouser leg rolled above the knee, the strap worn on the knee.",
           "One action at a natural pace: she lets go of the rolled cuff and the olive trouser leg unrolls and falls down over the knee and the strap, hanging flat to the ankle.",
           "in_place", "worn", "no strap showing through the fabric as a bulge, no trousers bunching",
           [("the fabric warping as it falls", "one drop, PHYS-MOTION-C: fabric lags and settles"), ("the strap moving under the fabric", "rigid-product clause"), ("the leg changing shape", "HOLD-C")]),
 "B-11b": ("Elaine, a petite white British woman of sixty-three with an ash-grey pixie cut, in a striped top, olive trousers and a yellow raincoat, at a street-market fruit stall.",
           "One action at an easy pace: she picks up one red apple from the crate and drops it into her paper bag, relaxed.",
           "in_place", "absent", "no strap visible, no knee visible, no readable signs",
           [("her hand or the apple warping", "one small reach at an easy pace, NEG-WARP-C"), ("readable text appearing on the stall", "negatives"), ("her face drifting", "start frame carries identity")]),
 "B-13a": ("The open matte-black box on a glass coffee table seen from above, two straps side by side in the insert, a woman's hand at the lid beside it.",
           "One small action at a slow pace: her hand settles the lid flat on the table beside the box and withdraws out of frame; the straps stay still.",
           "in_place", "object", "no strap leaving the box, no third strap, no text appearing",
           [("the straps moving in the box", "motion keeps them still"), ("the hand warping", "one small settle, NEG-WARP-C"), ("the box wordmark changing", "negatives")]),
 "B-14": ("Derek, a big-framed white British man of seventy-four with a white beard, in a navy fleece and khaki shorts, walking a towpath towards the camera, strap on his right knee.",
          "One action at a steady, easy walking pace: he takes three or four steps towards the camera along the path, arms swinging naturally, and the camera does not move back.",
          "travels", "worn", "no running, no stumbling",
          [("legs warping as he walks at the camera", "3–4 steps at a countable pace, waist-height phone (§27G)"), ("the strap sliding as he walks", "rigid-product clause"), ("the camera travelling with him", "RIG-R1 lags, never moves with the subject")]),
 "MECH-02": ("A translucent anatomical model of a knee: muscles semi-transparent, bones ivory-gold, one tight hot red point on the patellar tendon just below the kneecap, the strap just below it.",
             "One action at a steady pace: the strap slides up the last short way and seats on the tendon just below the kneecap, and the instant it seats the red point cools to calm blue.",
             "in_place", "worn", "no glow spreading onto the shin, no glow on the kneecap, no pause, no freeze",
             [("the red glow spreading instead of cooling", "motion names the cool on seating; negatives"), ("the anatomy warping", "RIG-RVD small drift, HOLD-C + NEG-WARP-C"), ("the strap climbing the kneecap", "seats just below the kneecap, rigid-product clause")]),
 "B-08": ("Hassan, a very tall thin Black British man of seventy-two in a white shirt and navy cardigan at his kitchen sink, the strap on his right knee.",
          "One small action at an easy pace: standing on the spot, he holds the kettle under the running tap as it fills, then turns the tap off; his legs stay planted.",
          "in_place", "worn", "no stepping, no kettle changing shape",
          [("the strap turning into a narrow band", "rigid-product clause, negatives name it"), ("the water or his hands warping", "one fill at an easy pace, PHYS-MOTION-C + NEG-WARP-C"), ("his legs moving and the strap sliding", "legs planted, rigid-product clause")]),
 "B-12": ("Derek, a big-framed white British man of seventy-four, on the couch edge, strap on his right knee; a surgeon crouched in the soft foreground.",
          "One small action at a slow pace: the surgeon taps the top edge of the strap's shell once with one finger and nods; Derek stays still.",
          "in_place", "worn", "no strap being pressed out of shape, no surgeon turning to camera",
          [("the shell denting under the tap", "rigid-product clause; one light tap"), ("the surgeon's hand warping", "one tap, NEG-WARP-C"), ("the strap turning into a narrow band", "negatives name it")]),
 "MECH-S1": ("A translucent anatomical model of a right knee in X-ray blue, the strap seated on the patellar tendon just below the kneecap.",
             "One action at a slow pace: a soft electric-blue glow rises in the strap and the tendon under it, holds, and eases a little; nothing else moves.",
             "in_place", "worn", "no strap moving, no glow on the kneecap, no pause, no freeze",
             [("the glow spreading over the whole knee", "motion keeps it to the strap and tendon; negatives"), ("the anatomy warping", "RIG-RVD small drift, HOLD-C + NEG-WARP-C"), ("the strap shifting", "rigid-product clause")]),
 "MECH-S2": ("A translucent anatomical model of a knee in a big blank wraparound brace, the joint under it glowing hot red-orange.",
             "One action at a slow pace: the red-orange glow under the brace pulses once, brighter and back; the brace does not move.",
             "in_place", "absent", "no brace moving, no text or logo appearing, no pause, no freeze",
             [("the red glow spreading off the joint", "motion names one pulse; negatives"), ("the brace deforming", "brace does not move, NEG-WARP-C"), ("text appearing on the brace", "negatives")]),
 "MECH-01": ("A translucent ghost limb, the knee seen low in profile: bone on bone, the worn joint surfaces glowing hot red.",
             "One action at a slow pace: the red on the worn joint surfaces pulses once, brighter and back, as if with each heartbeat; the bones do not move.",
             "in_place", "absent", "no bones moving, no glow spreading up the thigh, no pause, no freeze",
             [("the bones moving apart or merging", "bones do not move, HOLD-C + NEG-WARP-C"), ("the glow spreading", "one pulse on the joint; negatives"), ("the anatomy warping", "RIG-RVD small drift")]),
}
MECH = {"MECH-02", "MECH-S1", "MECH-S2", "MECH-01"}
def url_of(b):
    f = sorted(H.glob(f"{b}_v*.json"), key=lambda p: int(p.stem.rsplit("_v", 1)[1]))[-1]
    raw = f.read_text(); r = json.loads(raw[raw.rindex("\n{") + 1:]) if "\n{" in raw else json.loads(raw)
    return r["urls"][0]
out = {}
for b, (subj, motion, mv, prod, xneg, risks) in V.items():
    anat = b in MECH
    body = S("HOLD-C") + ("" if anat else " " + S("PHYS-MOTION-C"))
    nw = NEG_WORN.replace("no strap sliding up or down the leg", "no strap sliding down the leg") if b == "B-09a" else NEG_WORN
    negs = [S("NEG-WARP-C"), nw if prod == "worn" else NEG_PROD if prod in ("held", "object") else "", xneg, "no pause, no freeze" if anat else NEG_PPL]
    j = {"shot": b.lower().replace("-", "_"), "subject": subj,
         "camera": {"movement": S("RIG-RVD") if anat else S("RIG-R1"), "framing": "As in the start frame."},
         "motion": motion + (RIGID if prod in ("worn", "held", "object") else "") + " " + body,
         "lighting": "Exactly as in the start frame." if anat else S("INHERIT-CAP"), "style": "As in the start frame.",
         "negatives": ", ".join(n for n in negs if n)}
    s = json.dumps(j, ensure_ascii=False, separators=(",", ":"))
    (H / f"{b}.kling.json").write_text(s)
    c = {"beat": b, "connector": "kling", "mode": 1, "kind": "broll", "prompt": s, "duration": L.get(b, L["MECH-S1"]), "resolution": "1080p", "aspect_ratio": "9:16",
         "start_image": url_of(b), "start_approved": True, "pinned": False, "end_image": None, "end_approved": False, "subject_motion": mv,
         "prefer_multi_shots": "false", "generation": 1, "rack": None, "risks": [{"risk": r, "prevented_by": p} for r, p in risks],
         "route": "Kie AI kling-3.0 (§5 fallback: Kling connector at 3 credits)"}
    (H / f"{b}.call.json").write_text(json.dumps(c, indent=1, ensure_ascii=False))
    out[b] = {"chars": len(s), "duration": c["duration"], "img": c["start_image"][-40:]}
print(json.dumps(out))
