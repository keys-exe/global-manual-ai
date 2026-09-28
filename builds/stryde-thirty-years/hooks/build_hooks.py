#!/usr/bin/env python3
"""Step 6 hook start images for stryde-thirty-years, from Appendix A by ID. No selfie (user 2026-09-28)."""
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
for k, v in {"HK1": HK1}.items():
    assert "[" not in v, re.findall(r"\[[^\]]*\]", v)[:3]
    pathlib.Path(f"{k}_start.prompt.txt").write_text(v); print(k, len(v))
