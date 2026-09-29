#!/usr/bin/env python3
"""Talking-head image v2 (user 2026-09-28: 'don't use the selfie style') — PROPPED (§22F), from Appendix A by ID."""
import re, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()
AGE = "deep vertical lines between the brows, crow's feet cut deep at both eyes, hollows under the cheekbones, deep horizontal forehead creases, sun spots on the temples"
LIGHT = (S("LIGHT-SHOT").replace("[SOURCE from the light plan — the window on the room's WALL, or the named practical]", "the low morning sun through the east factory windows along the bench wall")
         .replace("[SUBJECT]", "his face").replace("[SCREEN SIDE]", "left").replace("[TIME-OF-DAY QUALITY and the act's light state]", "pale, clean early-morning light")
         .replace("[SIDE]", "the left"))
P = "\n\n".join([
 S("CAM-LOCK"),
 S("FRAME-SCALE").replace("[SCALE]", "about half") + " " + S("FRAME-PROPPED"),
 "THE SAME MAN exactly as in the attached reference sheet — narrow hollow-cheeked face, long jaw, deep-set pale grey eyes, long hooked nose, thick grey moustache, thin grey hair combed straight back with the scalp showing, short and wiry — unchanged in face, age and build. "
 "Nobody is holding the phone: it is propped against the tin of rivets on his workbench, a metre in front of him at chest height. He sits on the tall stool at the bench, turned square to the phone, both forearms resting on the scarred beech bench top, hands loose and relaxed in the lower third of the frame, eyes on the lens, mouth closed, about to speak. "
 "Chest-up, the edge of the bench across the bottom of the frame, a clear band of whitewashed brick above his head. "
 "Wearing his green-and-brown check flannel shirt with the sleeves rolled to the elbow under the faded navy canvas work apron, in earth tones. "
 "Around him, THE SAME WORKSHOP as the attached location plate: the blue cast-iron vice on the bench beside him, the pegboard of shears and punches behind his shoulder, one of the tall iron-framed factory windows to the left blowing to white, the timber roof trusses above, rolls of neoprene on the shelf.",
 LIGHT,
 S("SKIN-B1"),
 S("SKIN-B3").replace("[FOREHEAD-LINES]", "deep horizontal creases").replace("[AGE-FEATURES]", AGE),
 S("SKIN-B4"), S("EYES-A"),
 S("HAIR-A").replace("[HAIR-SPEC]", "thin grey hair combed straight back, the scalp showing through at the crown, a thick grey moustache"),
 S("NECK-A"), S("TEETH-A"),
 S("CAP-A"), S("CAP-FILE"),
 "AVOID: " + ", ".join([S("NEG-FRAME"), S("NEG-SKIN"), S("NEG-TEX"), S("NEG-FINISH"), S("NEG-M1"), S("NEG-LIGHT")]) + ", no selfie, no arm reaching towards the camera, no phone in his hand",
])
assert "[" not in P
pathlib.Path("C1_TH_propped.prompt.txt").write_text(P)
print(len(P))
