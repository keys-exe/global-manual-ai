#!/usr/bin/env python3
"""stryde-71-stairs — Act 4 videos + second video generations for P-01a, T-03a (new confirmed images), R-03a, R-05a (Fix notes 2026-09-30).
Same §35 shape as video_act2.py / video_act3.py. Lengths: work/lengths_T2.json (E6)."""
import json, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import video_act1 as V
from video_act2 import LOCKED, build
from video_act3 import B3, RIGID, PNEG

STILL = "Camera completely still. The frame does not move."
ANEG = ", no bones moving, no leg bending, no anatomy changing shape, no text, no labels"
START = {"P-01a": "P-01a_img_v6.png", "T-03a": "T-03a_img_v2.png", "R-03a": "R-03a_img_v1.png", "R-05a": "R-05a_img_v1.png",
         "M-01a": "M-01a_img_v2.png", "M-01b": "M-01b_img_v1.png", "M-02a": "M-02a_img_v1.png", "M-03a": "M-03a_img_v1.png",
         "M-04a": "M-04a_img_v1.png", "M-04b": "M-04b_img_v1.png", "M-05a": "M-05a_img_v2.png", "M-05b": "M-05b_img_v1.png", "M-06a": "M-06a_img_v7.png"}
DUR = {"M-03a": 8}   # anatomy pulse (no human motion, §27G cap is for people); E6 needs 7.6s for the line — one still-camera clip instead of a split

FIX = {
 "P-01a": ("the v1 video was made from the old image (seen from the side, she was on the wrong step); user asked for a new image of her back, halfway up, "
           "coming down backwards with both feet on each step → new confirmed image v6; one step-to only, both feet end together and hold, camera fixed"),
 "T-03a": "the v1 video was made from the ANAT-A (full muscle) image; user: 'should be the ghost limb anatomy here' → new confirmed ANAT-B image v2; same single pulse, camera still",
 "R-03a": ("v1 had her push the trouser cuff higher (motion fault, user: 'make her just showing the stryde strap') → no hand on the trousers; she only presents the knee "
           "with the strap, a small turn of the knee toward the camera, hands resting"),
 "R-05a": ("v1 had her tilt her hands and the strap turned over (motion fault, user: 'dont make her turn it over') → hands hold still, the strap lies flat on her palms, "
           "same face up the whole clip, only a small breath"),
}
G2 = {
 "P-01a": dict(framing="MEDIUM-WIDE as in the start frame, from the hall floor looking up the flight at her back, halfway up the stairs.", cam=LOCKED,
   motion="ONLY ONE STEP IN THE WHOLE CLIP. Facing up the stairs, both hands on the handrail, she lowers her right foot behind her onto the step just below, then her left foot joins it on that SAME step, "
          "the two slippers side by side again after about two seconds — then she stays still there, both feet together on that one step, to the end of the clip.",
   extra=", no second step, no turning around, no facing the camera, no walking forwards, no alternating feet, no feet on different steps at the end, no hand off the handrail, no stumbling, no fall",
   pace="unhurried", smot="in_place",
   risks=[("she walks down several steps","'ONLY ONE STEP IN THE WHOLE CLIP' + no second step / no alternating feet"),
          ("she turns to face down the stairs","'facing up the stairs' + no turning around"),("legs blend on the stairs","locked camera, one step only (§27G stairs staging)")]),
 "T-03a": dict(framing="The ghost-limb knee as in the start frame, side view.", cam=STILL,
   motion="The tight red spot on the patellar tendon just below the kneecap pulses once — brightening over about a second and easing back — while the worn joint surfaces behind it stay pale and rough. Nothing else moves.",
   extra=", no glow spreading over the kneecap, no muscle appearing" + ANEG, pace="unhurried", smot="still",
   risks=[("glow drifts onto the kneecap","'just below the kneecap' + no glow over the kneecap"),("muscle layer appears","no muscle appearing"),("anatomy morphs","HOLD + no anatomy changing shape")]),
 "R-03a": dict(framing="MEDIUM as in the start frame, Loretta seated across the kitchen table, her trouser leg already rolled above her right knee.", cam=LOCKED,
   motion="Loretta just shows the strap: her hands stay resting on her thighs, away from the trousers, and she turns her right knee a little toward the camera over about two seconds so the strap under her kneecap faces us, "
          "a small knowing smile. Her trousers do not move.",
   extra=PNEG + ", no hands on the trousers, no rolling the trousers, no trousers moving, no standing up", pace="unhurried", smot="in_place", rigid=True,
   risks=[("she fiddles with the trousers again","hands stay on her thighs + no hands on the trousers (user)"),("strap slides","RIGID + no strap sliding"),("face warps","same person clause")]),
 "R-05a": dict(framing="CLOSE as in the start frame, the strap lying flat across her open palms over the kitchen table.", cam=LOCKED,
   motion="Her open hands hold still with the strap lying flat across her palms, the same side facing up the whole clip; only a small breath lifts her hands a few millimetres and settles them. The strap never turns, flips or tips.",
   extra=PNEG + ", no turning the strap over, no flipping, no tilting the hands, no strap falling, no hands closing", pace="unhurried", smot="in_place", rigid=True,
   risks=[("strap turns over","'the same side facing up the whole clip' + no turning / flipping (user)"),("strap drops","hands hold still + no strap falling"),("fingers merge","finger clause")]),
}
B4 = {
 "M-01a": dict(framing="MEDIUM as in the start frame, the physical therapy room, her on the treatment table with the heat pad on her knee.", cam=LOCKED,
   motion="Eyes closed, she settles her head back into the headrest once over about a second, her shoulders easing down, then lies still with her hands resting.",
   extra=", no opening eyes, no sitting up, no heat pad moving, no strap", pace="unhurried", smot="in_place",
   risks=[("face warps with eyes closed","same person clause + one small settle"),("heat pad morphs","HOLD"),("she sits up","no sitting up")]),
 "M-01b": dict(framing="The anatomical knee as in the start frame, three-quarter view.", cam=STILL,
   motion="The red glow at the spot just below the kneecap spreads slowly a little further into the tissue around it over about two seconds, then holds. Nothing else moves.",
   extra=", no glow over the kneecap" + ANEG, pace="unhurried", smot="still",
   risks=[("glow floods the whole knee","'a little further' + no glow over the kneecap"),("anatomy morphs","HOLD + no anatomy changing shape"),("leg moves","camera still, nothing else moves")]),
 "M-02a": dict(framing="The anatomical knee with the strap as in the start frame, front view.", cam=STILL,
   motion="A slow, soft blue-white glow settles at the strap's pad, just below the kneecap, over about two seconds, and holds. Nothing else moves.",
   extra=PNEG + ", no red glow" + ANEG, pace="unhurried", smot="still", rigid=True,
   risks=[("strap deforms","RIGID clause"),("glow spills over the kneecap","'just below the kneecap'"),("anatomy morphs","HOLD")]),
 "M-03a": dict(framing="The anatomical knee as in the start frame, side view from low.", cam=STILL,
   motion="The tight red point on the patellar tendon just under the kneecap pulses in a walking rhythm — brightening and easing about once a second, steady through the whole clip. Nothing else moves.",
   extra=", no glow over the kneecap, no glow spreading" + ANEG, pace="countable", smot="still",
   risks=[("pulse drifts onto the kneecap","'just under the kneecap' + no glow over the kneecap"),("anatomy morphs over 8s","HOLD + still camera"),("pulse speeds up","'about once a second, steady'")]),
 "M-04a": dict(framing="OVERHEAD as in the start frame, the kitchen table with the braces, sleeves and pill bottles.", cam=V.SWAY,
   motion="Nothing on the table moves; the phone hovering overhead drifts very slightly, and the soft daylight across the table stays as it is. A held moment.",
   extra=", no objects moving, no items appearing, no items disappearing, no readable labels, no hands entering, no strap", pace="unhurried", smot="still",
   risks=[("items morph or multiply","HOLD count clause + no items appearing"),("labels become text","no readable labels"),("camera drifts too far","sway only, never travels")]),
 "M-04b": dict(framing="The anatomical knee as in the start frame, three-quarter view, the translucent sleeve drawn around it.", cam=STILL,
   motion="Under the translucent sleeve, the tight red point just below the kneecap keeps pulsing about once a second, untouched by the sleeve. Nothing else moves.",
   extra=", no sleeve moving, no sleeve changing shape, no glow over the kneecap" + ANEG, pace="countable", smot="still",
   risks=[("sleeve warps","HOLD + no sleeve changing shape"),("pulse spreads","'tight red point'"),("anatomy morphs","HOLD")]),
 "M-05a": dict(framing="The anatomical leg as in the start frame, side view.", cam=STILL,
   motion="Soft warm pressure pulses travel down the thigh and gather into the tight red point on the patellar tendon just below the kneecap, one pulse about every second. Nothing else moves.",
   extra=", no glow on the kneecap, no red on the kneecap" + ANEG, pace="countable", smot="still",
   risks=[("red lands on the kneecap","'just below the kneecap' + no red on the kneecap"),("muscle deforms with the pulses","HOLD + no anatomy changing shape"),("too many effects","one pulse path only")]),
 "M-05b": dict(framing="The anatomical knee with the strap as in the start frame, three-quarter view from low.", cam=STILL,
   motion="At the strap's pad, just below the kneecap, the last of the red fades into a calm soft blue over about two seconds as the pad takes the load, then holds steady. Nothing else moves.",
   extra=PNEG + ", no red returning" + ANEG, pace="unhurried", smot="still", rigid=True,
   risks=[("strap deforms","RIGID clause"),("colour flickers back","'then holds steady' + no red returning"),("anatomy morphs","HOLD")]),
 "M-06a": dict(framing="CLOSE as in the start frame, her right leg with the strap under the knee, her slipper on the top step.", cam=LOCKED,
   motion="She lowers her other foot past the camera onto the next step down in one easy, steady step over about a second, her hands free and away from the rail, the strapped knee bending naturally; then she pauses.",
   extra=PNEG + ", no hand on the handrail, no stumbling, no second step, no feet merging", pace="unhurried", smot="in_place", rigid=True,
   risks=[("feet blend on the step","one step only, locked camera (§27G stairs)"),("she grabs the rail","hands free + no hand on the handrail (user)"),("strap moves with the knee bend","RIGID clause")]),
}

def go(beat, cfg, gen=1, fix=None):
    cfg = dict(cfg)
    if cfg.pop("rigid", False): cfg["motion"] += " " + RIGID
    n = build(beat, cfg, START[beat], gen=gen, fix=fix, dur=DUR.get(beat))
    print(beat, DUR.get(beat) or V.LEN[beat], "s", n, "chars", "gen", gen)

if __name__ == "__main__":
    for bt, cfg in G2.items(): go(bt, cfg, gen=2, fix=FIX[bt])
    for bt, cfg in B4.items(): go(bt, cfg)
