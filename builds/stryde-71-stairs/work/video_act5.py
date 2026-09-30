#!/usr/bin/env python3
"""stryde-71-stairs — Act 5 videos (proof: the montage, the doctor, the husband, the niece, her six weeks).
Same §35 shape as video_act3/4. Lengths: work/lengths_T2.json (E6, PR-01a–d split 2026-09-30)."""
import json, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import video_act1 as V
from video_act2 import LOCKED, build
from video_act3 import RIGID, PNEG

S = "/tmp/claude-0/-home-user-global-manual-ai/8f10ea69-fe4e-5541-9214-2e22280bbf9c/scratchpad"
START = json.load(open(S + "/act5_cur.json"))
HID = ", no strap showing, no strap over the trousers, no product"

B5 = {
 "PR-01a": dict(framing="MEDIUM as in the start frame, on the front porch steps, the man with the mulch bag on his shoulder.", cam=LOCKED,
   motion="Carrying the bag on his shoulder, he steps down ONE porch step, his left foot landing on the step below in about a second, the strapped right knee bending easily; then he pauses.",
   extra=PNEG + ", no second step, no dropping the bag, no bag changing shape", pace="unhurried", smot="in_place", rigid=True,
   risks=[("legs blend on the step","one step only, locked camera (§27G stairs)"),("bag morphs","HOLD"),("strap moves with the knee bend","RIGID clause")]),
 "PR-01b": dict(framing="MEDIUM as in the start frame, in the back garden, the woman pushing the wheelbarrow.", cam=LOCKED,
   motion="She leans in and pushes the loaded wheelbarrow forward in one easy push, taking one step with it over about a second, smiling; the soil stays in the barrow. Her trousers cover her knees.",
   extra=HID + ", no soil spilling, no wheelbarrow changing shape, no second push", pace="unhurried", smot="in_place",
   risks=[("wheelbarrow warps","HOLD"),("hands fuse with the handles","finger clause"),("strap appears over the trousers","no strap showing (user: under the trousers)")]),
 "PR-01c": dict(framing="MEDIUM as in the start frame, in the garage, the man on the stepladder hanging the bicycle.", cam=LOCKED,
   motion="Standing on the stepladder, he lifts the bicycle's front wheel the last few centimetres and settles it onto the wall hook in about a second, then lets his hands rest on the frame.",
   extra=PNEG + ", no ladder moving, no bicycle changing shape, no spokes warping, no falling", pace="unhurried", smot="in_place", rigid=True,
   risks=[("bicycle spokes warp","HOLD + no spokes warping"),("hands merge with the frame","finger clause"),("ladder bends","HOLD + no ladder moving")]),
 "PR-01d": dict(framing="CLOSE as in the start frame, her right knee in the gym, both hands on the strap.", cam=LOCKED,
   motion="Both hands press the strap flat onto her leg just below the kneecap in one firm press over about a second, then her fingers lift a little off it.",
   extra=PNEG + ", no strap going over the kneecap, no fingers passing through the strap", pace="unhurried", smot="in_place", rigid=True,
   risks=[("strap bends under the press","RIGID clause"),("fingers merge with it","finger clause"),("strap slides onto the kneecap","'just below the kneecap'")]),
 "PR-02a": dict(framing="MCU as in the start frame, the doctor at his desk holding up the strap, the knee model behind.", cam=LOCKED,
   motion="The doctor turns the strap a little toward the camera in his hand over about a second, as if showing it to a patient across the desk, and holds it there with a slight nod.",
   extra=PNEG + ", no strap twisting, no knee model moving, no readable text on the wall", pace="unhurried", smot="in_place", rigid=True,
   risks=[("strap twists or flops","RIGID clause + no strap twisting"),("hand merges with the strap","finger clause"),("face warps","same person clause")]),
 "PR-03a": dict(framing="MEDIUM-FULL as in the start frame, on the golf course, low from the side, mid follow-through.", cam=LOCKED,
   motion="He finishes the follow-through of his swing, the club coming round over his shoulder in about a second, his weight settling onto the front foot, and holds the finish looking down the fairway.",
   extra=PNEG + ", no second swing, no club bending, no ball, no club changing shape", pace="brisk", smot="in_place", rigid=True,
   risks=[("club bends or duplicates","HOLD + no club changing shape"),("arms blend in the swing","one follow-through only, locked camera"),("strap moves","RIGID clause")]),
 "PR-04a": dict(framing="MEDIUM-FULL as in the start frame, on the red running track, the young woman jogging toward the camera.", cam=LOCKED,
   motion="She jogs steadily toward the camera, about two strides per second, arms swinging loosely, the strapped right knee lifting and landing smoothly; she is still fully in frame, a little closer, at the end.",
   extra=PNEG + ", no sprinting, no running out of frame, no legs crossing wrongly, no people in the background changing", pace="brisk", smot="traveling", rigid=True,
   risks=[("legs tangle while running at camera","steady jog, locked camera, stays in frame (§27G walking at camera)"),("strap moves on the knee","RIGID clause"),("background runners morph","HOLD")]),
 "PR-05a": dict(framing="MEDIUM as in the start frame, in the front garden, her watering the flower bed.", cam=LOCKED,
   motion="She tips the green watering can a little further and water pours steadily onto the flowers for about two seconds, her strapped knee bent as she leans; then she eases the can back up.",
   extra=PNEG + ", no water pouring from anywhere else, no can changing shape, no flowers changing", pace="unhurried", smot="in_place", rigid=True,
   risks=[("water stream turns strange","'pours steadily onto the flowers'"),("can morphs","HOLD"),("strap moves with the bend","RIGID clause")]),
 "PR-05b": dict(framing="CLOSE as in the start frame, from the side in the bedroom, her trouser leg over the knee.", cam=LOCKED,
   motion="Her hand smooths the navy trouser leg down over her knee once in about a second and the fabric settles flat; nothing shows under it. Then her hand rests at her side.",
   extra=HID + ", no bump under the trousers, no trousers lifting", pace="unhurried", smot="in_place",
   risks=[("strap shows through or over the trousers","no strap showing + no bump (user: no product in PR-05b)"),("fabric morphs","HOLD"),("hand distorts","finger clause")]),
 "PR-06a": dict(framing="CLOSE as in the start frame, the cleared kitchen table with the coffee mug and the strap.", cam=V.SWAY,
   motion="Steam rises slowly from the coffee mug and drifts away; nothing else on the table moves. A quiet held moment in the morning light.",
   extra=PNEG + ", no objects moving, no mug changing, no hands entering, no pills, no brace", pace="unhurried", smot="still", rigid=True,
   risks=[("strap deforms on the table","RIGID clause"),("mug morphs","HOLD"),("steam turns to smoke","'steam rises slowly'")]),
}

if __name__ == "__main__":
    for bt, cfg in B5.items():
        cfg = dict(cfg)
        if cfg.pop("rigid", False): cfg["motion"] += " " + RIGID
        print(bt, V.LEN[bt], "s", build(bt, cfg, START[bt]), "chars")
