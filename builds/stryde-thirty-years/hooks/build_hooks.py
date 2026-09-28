#!/usr/bin/env python3
"""Step 6 hook start images (HK1, HK2, HK3-BR, HK3-BR2, HK3-TH) for stryde-thirty-years, from Appendix A by ID. No selfie (user 2026-09-28)."""
import re, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()
ID = ("THE SAME MAN exactly as in the attached reference sheet — narrow hollow-cheeked face, long jaw, deep-set pale grey eyes, long hooked nose, "
      "thick grey moustache, thin grey hair combed straight back with the scalp showing, short and wiry — unchanged in face, age and build. "
      "Wearing his green-and-brown check flannel shirt with the sleeves rolled to the elbow under the faded navy canvas work apron, grey work trousers and brown leather work boots.")
COLOUR = (S("COLOUR-KEY").replace("[LIGHT COLOUR]", "pale east morning daylight, clean and slightly cool")
          .replace("[SET COLOURS]", "whitewashed grey-white brick, grey concrete floor, dark oiled beech, the blue cast-iron vice, black and beige neoprene braces on the steel rail")
          .replace("[WHO]", "he").replace("[WARDROBE COLOURS]", "a green-and-brown check shirt, a faded navy apron and grey trousers")
          .replace("[ACCENT]", "the blue vice").replace("[SATURATION AND CONTRAST IN CAMERA]", "natural, slightly muted"))
HK1 = "\n\n".join([
 S("CAM-LOCK"),
 S("FRAME-SCALE").replace("[SCALE]", "about three fifths") + " " + S("FRAME-WIDE"),
 S("ANGLE-LINE").replace("[HEIGHT CLAUSE from §30I]", "a low, waist-height camera").replace("[SIDE]", "the front, slightly to one side,").replace("[SUBJECT]", "him")
   .replace("[, looking past FOREGROUND, soft in the near foreground | , seen in REFLECTION]", ", looking past the corner of the cutting table, soft in the near foreground"),
 S("FOCUS-LINE").replace("[PLANE — the nearest eye of NAME / the hands and what they hold / the product and its wordmark / the foreground / everything]", "the nearest eye of the man")
   .replace("[DEPTH — the room behind falls to a soft, recognisable shape | everything from near to far stays sharp]", "everything from near to far stays sharp"),
 ID + " Nobody is holding the phone: it is propped on the end of the wide cutting table at the near end of the aisle, facing up the room towards him. "
 "He is walking slowly down the aisle towards it, caught mid-stride — his left foot forward and planted, the right heel just lifting — his right hand trailing loosely along the hangers of the steel rail of finished knee braces that runs down the left-hand side of the frame, "
 "looking straight at the phone and already talking, mouth slightly open. The whole of him is in the frame, floor below his boots, the rail of braces running away behind him, "
 "the long beech workbench, the blue vice and the three tall factory windows on the right-hand side, the timber trusses above. THE SAME WORKSHOP as the attached location plate, seen from the same end.",
 S("LIGHT-SHOT").replace("[SOURCE from the light plan — the window on the room's WALL, or the named practical]", "the low morning sun through the east factory windows along the bench wall")
   .replace("[SUBJECT]", "him").replace("[SCREEN SIDE]", "right").replace("[TIME-OF-DAY QUALITY and the act's light state]", "pale, clean early-morning light").replace("[SIDE]", "the right"),
 COLOUR,
 S("CAP-A"), S("CAP-FILE"),
 "AVOID: " + ", ".join([S("NEG-FRAME"), S("NEG-M1"), S("NEG-FILE"), S("NEG-LIGHT"), S("NEG-SCENE")]) + ", no selfie, no phone in his hand, no arm reaching towards the camera, no readable text, labels or logos, no brand names on the braces",
])

LIGHT_L = lambda subj: (S("LIGHT-SHOT").replace("[SOURCE from the light plan — the window on the room's WALL, or the named practical]", "the low morning sun through the east factory windows along the bench wall")
   .replace("[SUBJECT]", subj).replace("[SCREEN SIDE]", "left").replace("[TIME-OF-DAY QUALITY and the act's light state]", "pale, clean early-morning light").replace("[SIDE]", "the left"))
def ANG(h, side, fg):
    return (S("ANGLE-LINE").replace("[HEIGHT CLAUSE from §30I]", h).replace("[SIDE]", side).replace("[SUBJECT]", "him")
            .replace("[, looking past FOREGROUND, soft in the near foreground | , seen in REFLECTION]", fg))
def FOC(plane, depth):
    return (S("FOCUS-LINE").replace("[PLANE — the nearest eye of NAME / the hands and what they hold / the product and its wordmark / the foreground / everything]", plane)
            .replace("[DEPTH — the room behind falls to a soft, recognisable shape | everything from near to far stays sharp]", depth))
BENCH = ("THE SAME WORKSHOP as the attached location plate: the long scarred beech workbench, the blue cast-iron vice bolted to its end, the pegboard of shears, punches and rivet setters on the whitewashed brick, "
         "one of the tall iron-framed factory windows to the left blowing to white, rolls of neoprene on the shelf under the bench, the timber trusses above.")
NEGS = lambda extra: "AVOID: " + ", ".join([S("NEG-FRAME"), S("NEG-M1"), S("NEG-FILE"), S("NEG-LIGHT"), S("NEG-SCENE")] + extra) + ", no selfie, no phone in his hand, no arm reaching towards the camera, no readable text, labels or logos, no brand names on the braces"
SLEEVE = "a plain unbranded beige neoprene knee sleeve cut clean in half across its middle with shears, the two halves curling slightly at the cut edge, the cut showing the neoprene's layered cross-section"

HK2 = "\n\n".join([
 S("CAM-LOCK"),
 S("FRAME-SCALE").replace("[SCALE]", "about three quarters") + " " + S("FRAME-PROPPED"),
 ANG("an eye-level camera", "three-quarter, from his right,", ", looking past the jaws of the vice and the brace held in it, soft in the near foreground"),
 FOC("the nearest eye of the man", "everything from near to far stays sharp"),
 ID + " Nobody is holding the phone: it is propped against the tin of rivets at the vice end of the bench, a metre in front of him at chest height. "
 "He sits on the tall stool at the vice, turned towards the phone, one forearm resting on the bench top, the other hand loose on his knee below the bench edge, eyes on the lens, mouth slightly open, already talking. "
 "Clamped in the vice beside him, between him and the lens and to one side so it never covers his face, a half-built generic hinged knee brace: two steel side bars with a round hinge at the knee, one black strap riveted on, the other strap loose and unriveted, the pad not yet fitted — plain, unbranded, unfinished. He does not touch it. "
 "Chest-up, the bench edge across the bottom of the frame, a clear band of brick above his head. " + BENCH,
 LIGHT_L("his face"),
 COLOUR,
 S("CAP-A"), S("CAP-FILE"),
 NEGS([S("NEG-HAND")]),
])

HK3_BR = "\n\n".join([
 S("CAM-LOCK"),
 ANG("an overhead camera looking straight down", "directly above,", "").replace("of him", "of his hands on the bench"),
 FOC("the hands and what they hold", "the room behind falls to a soft, recognisable shape"),
 "Nobody else is in the frame and no face is seen. He holds the phone flat above the bench in his left hand, looking straight down at the scarred dark beech bench top. On the wood lie " + SLEEVE + ". "
 "His right hand — an old maker's hand, weathered, knuckles thick, nails short with glue under them, the rolled cuff of a green-and-brown check flannel shirt at the wrist — is already lifting one half a few centimetres off the wood, caught mid-lift, thumb and two fingers pinching the cut edge, the half sagging softly under its own weight; the other half still lies on the wood. "
 "Around them on the bench, loose and unarranged: a pair of heavy shears lying open, a few neoprene offcuts, a pencil, the edge of the blue cast-iron vice just in one corner. " + BENCH.replace("THE SAME WORKSHOP as the attached location plate: ", "THE SAME BENCH as the attached location plate — ").split(", the pegboard")[0] + ".",
 LIGHT_L("the bench top and his hand").replace(", so the face has a lit side toward the left and a softer shadow side, with a small catchlight in the eyes", ", so the hand and the sleeve halves have a lit side toward the left and a softer shadow side"),
 COLOUR.replace("he wears a green-and-brown check shirt, a faded navy apron and grey trousers", "his shirt cuff is green-and-brown check"),
 S("CAP-A"), S("CAP-FILE"),
 NEGS([S("NEG-HAND"), S("NEG-POV")]).replace(", no phone in his hand", "").replace("no hand entering or leaving frame, ", ""),
])

HK3_BR2 = "\n\n".join([
 S("CAM-LOCK"),
 S("FRAME-SCALE").replace("[SCALE]", "about three quarters") + " " + S("FRAME-PROPPED"),
 ANG("an eye-level camera", "three-quarter, from his left,", ", looking past the half of the knee sleeve he holds up close to the lens, soft in the near foreground"),
 FOC("the foreground", "the room behind falls to a soft, recognisable shape"),
 ID + " Nobody is holding the phone: it is propped against the tin of rivets on the bench, a metre in front of him at chest height. "
 "He sits on the tall stool at the bench, angled to it, and holds up in his right hand, close to the phone, one half of " + SLEEVE + ". The half fills the lower left of the frame and is the sharpest thing in it, the cut edge towards the lens; "
 "behind it his face is soft but recognisable, eyes on the lens, mouth closed, still. The other half lies on the bench in front of him beside the shears. Chest-up, the bench edge across the bottom of the frame. " + BENCH,
 LIGHT_L("his face"),
 COLOUR,
 S("CAP-A"), S("CAP-FILE"),
 NEGS([S("NEG-HAND")]),
])

HK3_TH = "\n\n".join([
 S("CAM-LOCK"),
 S("FRAME-SCALE").replace("[SCALE]", "about three quarters") + " " + S("FRAME-PROPPED"),
 ANG("an eye-level camera", "three-quarter, from his left,", ""),
 FOC("the nearest eye of the man", "everything from near to far stays sharp"),
 ID + " Nobody is holding the phone: it is propped against the tin of rivets on the bench, a metre in front of him at chest height. "
 "He sits on the tall stool at the bench, angled to it, turned to the phone, and holds loosely in his right hand, low in the frame and resting on the bench edge, one half of " + SLEEVE + "; the other half lies on the bench beside the shears. "
 "Eyes on the lens, mouth slightly open, about to speak. Chest-up, the bench edge across the bottom of the frame, a clear band of brick above his head. " + BENCH,
 LIGHT_L("his face"),
 COLOUR,
 S("CAP-A"), S("CAP-FILE"),
 NEGS([S("NEG-HAND")]),
])

for k, v in {"HK1": HK1, "HK2": HK2, "HK3-BR": HK3_BR, "HK3-BR2": HK3_BR2, "HK3-TH": HK3_TH}.items():
    assert "[" not in v, re.findall(r"\[[^\]]*\]", v)[:3]
    pathlib.Path(f"{k}_start.prompt.txt").write_text(v); print(k, len(v))
