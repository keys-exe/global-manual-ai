#!/usr/bin/env python3
"""stryde-71-stairs — Act 3 videos (the remedy: Loretta's visit → the strap → down the stairs). Same §35 shape as video_act2.py.
Start images: the confirmed image version on the board (2026-09-30). Lengths: work/lengths_T2.json (E6)."""
import json, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import video_act1 as V
from video_act2 import LOCKED, build

RIGID = ("The black strap is one rigid moulded piece: it keeps its exact shape, size, two small peaks, silver buckle and white wordmark in every frame — "
         "it never bends, stretches, melts, grows or changes where it sits.")
PNEG = ", no strap changing shape, no strap changing size, no strap sliding, no second strap, no wordmark changing, no readable text other than the strap's wordmark"
START = {"R-01a": "R-01a_img_v1.png", "R-02a": "R-02a_img_v1.png", "R-02b": "R-02b_img_v1.png", "R-03a": "R-03a_img_v1.png",
         "R-04a": "R-04a_img_v4.png", "R-05a": "R-05a_img_v1.png", "R-06a": "R-06a_img_v2.png", "R-07a": "R-07a_img_v9.png"}

B3 = {
 "R-01a": dict(framing="MEDIUM-WIDE as in the start frame, from inside the hall toward the open front door.", cam=LOCKED,
   motion="Loretta, just inside the front door with her overnight bag in her right hand, takes ONE step toward the camera over about a second, the bag swinging a little at her side, and smiles; then she stops.",
   extra=", no second step, no walking past the camera, no bag changing, no door moving", pace="unhurried", smot="in_place",
   risks=[("legs blend while walking at camera","one step only, locked camera (§27G walking at camera)"),("bag morphs","HOLD"),("face warps","same person clause")]),
 "R-02a": dict(framing="CLOSE as in the start frame, over the kitchen table, her hands, the tube and the two tablets.", cam=LOCKED,
   motion="Her right hand squeezes the white tube once and a small line of clear gel comes out onto the fingertips of her left hand over about a second; the two tablets and the glass of water stay where they are.",
   extra=", no gel pouring, no tablets moving, no tube changing shape, no readable label", pace="unhurried", smot="in_place",
   risks=[("tube and fingers merge","finger clause + HOLD"),("tablets multiply","HOLD count clause"),("gel floods","'a small line of gel' + no gel pouring")]),
 "R-02b": dict(framing="CLOSE as in the start frame, seated at the kitchen table, her knee in the black hinged brace and the blue ice pack.", cam=LOCKED,
   motion="Both hands press the blue ice pack down onto her right knee once over about a second, the pack flattening a little under her palms, then her hands rest on it.",
   extra=", no brace changing shape, no ice pack changing colour, no strap", pace="unhurried", smot="in_place",
   risks=[("pack and hands merge","finger clause"),("hinged brace deforms","HOLD + no brace changing shape"),("too much motion","one press only")]),
 "R-03a": dict(framing="MEDIUM as in the start frame, Loretta seated across the kitchen table.", cam=LOCKED,
   motion="Loretta gives her rolled khaki trouser cuff one small push higher above her right knee with both hands over about two seconds, then her hands settle on her thighs and she looks across the table with a small smile.",
   extra=PNEG + ", no trousers unrolling, no standing up", pace="unhurried", smot="in_place", rigid=True,
   risks=[("strap slides with the trouser","RIGID clause + no strap sliding"),("fabric morphs","HOLD"),("face warps","same person clause")]),
 "R-04a": dict(framing="EXTREME CLOSE as in the start frame, her right knee and the strap under the kneecap.", cam=LOCKED,
   motion="Her index finger taps the strap once, just below the kneecap, over about a second, then lifts a little away.",
   extra=PNEG + ", no finger passing through the strap", pace="unhurried", smot="in_place", rigid=True,
   risks=[("strap bends at the tap","RIGID clause"),("finger merges with the strap","finger clause + no passing through"),("wordmark warps","no wordmark changing")]),
 "R-05a": dict(framing="CLOSE as in the start frame, the strap lying across her open palms over the kitchen table.", cam=LOCKED,
   motion="She tilts her open hands a little toward herself over about a second, the strap resting on her palms tipping with them, as if taking a closer look; then her hands hold still.",
   extra=PNEG + ", no strap falling, no hands closing, no fingers merging with the strap", pace="unhurried", smot="in_place", rigid=True,
   risks=[("strap drops or floats","'resting on her palms tipping with them' + no strap falling"),("strap changes shape","RIGID clause"),("fingers merge","finger clause")]),
 "R-06a": dict(framing="CLOSE as in the start frame, seated, both hands at her right knee holding the strap.", cam=LOCKED,
   motion="Both hands slide the strap up the last couple of centimetres of her shin in one smooth push over about a second and stop when it seats just below the kneecap; her hands stay on it.",
   extra=PNEG.replace(", no strap sliding", "") + ", no strap going over the kneecap, no strap going above the knee", pace="unhurried", smot="in_place", rigid=True,
   risks=[("strap stretches while sliding","RIGID clause — the whole piece moves as one"),("strap overshoots onto the kneecap","'stop when it seats just below the kneecap' + negatives"),("hands fuse with it","finger clause")]),
 "R-07a": dict(framing="MEDIUM-WIDE as in the start frame, from the hall floor at the foot of the stairs, looking up the flight at her on the landing.", cam=LOCKED,
   motion="She walks DOWN the stairs FACING FORWARDS toward the camera, one step per second, about five steps in the clip, one foot on each step and the other foot to the next step below — "
          "arms loose at her sides, her hands NEVER touching the handrail, her head up and a small smile. She keeps coming down at the same steady pace until the clip ends.",
   extra=PNEG + ", no hand on the handrail, no both feet on one step, no going backwards, no stumbling, no fall, no running",
   pace="brisk", smot="traveling", rigid=True,
   risks=[("legs blend on the stairs","locked camera at the bottom, subject walks toward it (§27G stairs staging), one step per second"),
          ("she reaches for the rail","hands at her sides + no hand on the handrail (user)"),("strap drifts or grows","RIGID clause")]),
}

if __name__ == "__main__":
    for bt, cfg in B3.items():
        cfg = dict(cfg)
        if cfg.pop("rigid", False): cfg["motion"] += " " + RIGID
        print(bt, V.LEN[bt], "s", build(bt, cfg, START[bt]), "chars")
