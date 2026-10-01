#!/usr/bin/env python3
"""stryde-71-stairs — Act 7 videos (close: six weeks, the church ladies, the name, the surgeons, the knock-offs, the offer, the guarantee, her sister).
Same §35 shape as video_act3–6. Motion is written from the confirmed image (C-07a's image is her on the porch steps, not the box of the old act-map note).
Lengths: work/lengths_T2.json (E6)."""
import json, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import video_act1 as V
from video_act2 import LOCKED, build
from video_act3 import RIGID, PNEG
from video_act4 import STILL, ANEG

S = "/tmp/claude-0/-home-user-global-manual-ai/8f10ea69-fe4e-5541-9214-2e22280bbf9c/scratchpad"
START = json.load(open(S + "/act7_cur.json"))
RIGID2 = RIGID.replace("The black strap is one rigid moulded piece", "Each black strap is one rigid moulded piece")

B7 = {
 "C-01a": dict(framing="MEDIUM-CLOSE as in the start frame, her sitting on the bed edge, the strap on her right knee.", cam=LOCKED,
   motion="Looking down at her knee, she pats it once with her right hand just above the strap in about a second, a small satisfied nod, then her hand rests on her thigh.",
   extra=PNEG + ", no standing up, no hand on the strap", pace="unhurried", smot="in_place", rigid=True,
   risks=[("hand fuses with the knee","finger clause"),("strap moves under the pat","RIGID + pat above the strap"),("face warps looking down","same person clause")]),
 "C-02a": dict(framing="MEDIUM as in the start frame, from the sidewalk below the brick church steps, the three ladies in Sunday hats to the side.", cam=LOCKED,
   motion="She comes down ONE brick step facing forwards in about a second, her hand free of the rail, steady and upright, while the three ladies watch her and one leans to whisper to the next; then she pauses on that step.",
   extra=PNEG + ", no hand on the handrail, no second step, no stumbling, no hats changing, no ladies merging, no faces changing", pace="unhurried", smot="in_place", rigid=True,
   risks=[("legs blend on the step","one step only, locked camera (§27G stairs)"),("the ladies merge or morph","no ladies merging + same person clause"),("she reaches for the rail","no hand on the handrail")]),
 "C-03a": dict(framing="The anatomical knee with the strap as in the start frame, three-quarter view.", cam=STILL,
   motion="A slow, soft blue glow breathes at the strap's pad just below the kneecap — brightening over about two seconds and settling to a calm steady blue. Nothing else moves.",
   extra=PNEG + ", no red glow" + ANEG, pace="unhurried", smot="still", rigid=True,
   risks=[("strap deforms","RIGID clause"),("glow spills onto the kneecap","'just below the kneecap'"),("anatomy morphs","HOLD")]),
 "C-04a": dict(framing="MEDIUM-CLOSE as in the start frame, over the surgeon's shoulder, his hands at the patient's right knee.", cam=LOCKED,
   motion="The surgeon presses the strap flat just below the patient's kneecap with both thumbs in one firm press over about a second, then checks it with a light touch.",
   extra=PNEG + ", no fingers passing through the strap, no strap going over the kneecap, no face turning to camera", pace="unhurried", smot="in_place", rigid=True,
   risks=[("strap bends under the press","RIGID clause"),("hands fuse with the leg","finger clause"),("strap slides onto the kneecap","'just below the kneecap'")]),
 "C-05a": dict(framing="CLOSE as in the start frame, her hand holding up the cheap frayed strap over the kitchen table.", cam=LOCKED,
   motion="She gives the cheap, frayed strap one small dismissive shake in about a second, the loose velcro tab flapping, then lets it hang limp from her fingers.",
   extra=", no brand, no logo, no readable text on the packaging, no stryde strap, no strap changing into another, no hand merging with the strap", pace="unhurried", smot="in_place",
   risks=[("strap turns into the real product","no stryde strap + no strap changing into another"),("fingers fuse with the fabric","finger clause"),("packaging shows text","no readable text")]),
 "C-06a": dict(framing="MCU as in the start frame, her on the landing holding up two straps toward the phone.", cam=LOCKED,
   motion="Smiling at the lens, she lifts both straps a little higher toward the camera in one easy movement over about a second and holds them there.",
   extra=PNEG.replace(", no second strap", "") + ", no straps changing shape, no more than two straps, no straps merging", pace="unhurried", smot="in_place", rigid=False,
   risks=[("the two straps merge or multiply","no more than two straps + HOLD count"),("straps deform","each strap one rigid piece"),("face warps","same person clause")]),
 "C-07a": dict(framing="MEDIUM as in the start frame, from the front walk looking up at her on the porch steps.", cam=LOCKED,
   motion="She steps down ONE porch step facing forwards in about a second, easy and steady, her hands free of any rail, her bag on her shoulder; then she pauses on that step, a calm look ahead.",
   extra=PNEG + ", no hand on the rail, no second step, no stumbling, no hat changing, no bag changing", pace="unhurried", smot="in_place", rigid=True,
   risks=[("legs blend on the step","one step only, locked camera (§27G stairs)"),("strap moves with the knee bend","RIGID clause"),("bag or hat morphs","HOLD")]),
 "C-09a": dict(framing="CLOSE as in the start frame, her hands at the kitchen table, the pen on the small card lying on the closed box.", cam=LOCKED,
   motion="Her hand writes a few short pen strokes on the small card over about two seconds, then lifts the pen away; her other hand rests on the box.",
   extra=", no readable writing, no letters forming words, no box changing shape, no box opening, no pen changing, no hand merging with the pen", pace="unhurried", smot="in_place",
   risks=[("writing becomes readable text","no readable writing"),("pen fuses with the fingers","finger clause"),("box morphs","HOLD")]),
}

FIX = {"C-05a": ("THIS SHOULD BE THE LOOK A LIKES → the frame was the cause (v1 animated a generic nylon strap). New start image v5 (confirmed): two cheap look-alike "
                  "copies of the strap lying on the torn mailer, her hand beside them; motion: she pushes them away with the back of her fingers")}
G2 = {
 "C-05a": dict(framing="CLOSE as in the start frame, the kitchen table, two cheap copies of the strap on the torn grey mailer, her hand resting beside them.", cam=LOCKED,
   motion="With the back of her fingers she pushes the two cheap copies a few inches away across the mailer in one small dismissive movement over about a second, then her hand lifts off the table. "
          "Each copy is one rigid moulded piece and keeps its exact shape, both sliding together.",
   extra=", no brand, no logo, no readable text, no chrome, no straps changing shape, no straps bending, no straps merging, no third strap, no hand merging with the straps, no picking them up",
   pace="unhurried", smot="in_place",
   risks=[("copies bend or melt as they slide","'one rigid moulded piece… keeps its exact shape' + no straps bending"),("fingers fuse with the plastic","finger clause"),("copies turn into the real strap","no brand / no chrome")]),
}

FIX3 = {"C-05a": ("two shells on one band in v2 (from image v5) → ONE copy from image v6. Generation 3 on the user's go ('confirm go', 2026-10-01). v2 animated image v5, which had two shells on one band (user: 'IT SHOULD JUST BE ONE PAD NOT 2 IN ONE STRAP'); "
                   "new start image v6 (confirmed): ONE cheap copy, one shell on one band; motion: one small push away with the back of her fingers")}
G3 = {
 "C-05a": dict(framing="CLOSE as in the start frame, the kitchen table, ONE cheap copy of the strap on the torn grey mailer, her hand resting beside it.", cam=LOCKED,
   motion="With the back of her fingers she pushes the one cheap copy a few inches away across the mailer in one small dismissive movement over about a second, then her hand lifts off the table. "
          "The copy is one rigid moulded piece — one shell on one band — and keeps its exact shape as it slides.",
   extra=", no brand, no logo, no readable text, no chrome, no strap changing shape, no strap bending, no second strap, no second shell, no two pads on one band, no hand merging with the strap, no picking it up",
   pace="unhurried", smot="in_place",
   risks=[("a second shell appears","'ONE cheap copy… one shell on one band' + no second shell (user)"),("copy bends as it slides","'one rigid moulded piece… keeps its exact shape'"),("fingers fuse with the plastic","finger clause")]),
}

def go(beat, cfg, gen=1, fix=None):
    cfg = dict(cfg)
    r = cfg.pop("rigid", False)
    if r: cfg["motion"] += " " + RIGID
    elif beat == "C-06a": cfg["motion"] += " " + RIGID2
    print(beat, V.LEN[beat], "s", build(beat, cfg, START[beat], gen=gen, fix=fix), "chars")

if __name__ == "__main__":
    if sys.argv[1:] == ["--g3"]:
        for bt, cfg in G3.items(): go(bt, cfg, gen=3, fix=FIX3[bt])
        sys.exit()
    if sys.argv[1:] == ["--g2"]:
        for bt, cfg in G2.items(): go(bt, cfg, gen=2, fix=FIX[bt])
        sys.exit()
    for bt, cfg in B7.items(): go(bt, cfg)
