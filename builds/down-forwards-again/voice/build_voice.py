#!/usr/bin/env python3
"""§22U steps 1-2 for the doctor D (down-forwards-again), assembled from Appendix A by ID (never retyped)."""
import re, json, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()
SHEET = (pathlib.Path(__file__).resolve().parents[1] / "BUILD_SHEET.md").read_text()
VOICE_DOC = SHEET.split("**`VOICE-DOC`**")[1].split("```")[1].strip()

# ---- step 1: talking-head frame (voice-source start frame; also the HeyGen avatar image) ----
AGE = "soft creases fanning from the outer eyes, two fine horizontal forehead lines, slightly puffy skin under the eyes, a few faded freckles on the cheekbones, a little softening along the jawline and under the chin"
STEP1 = "\n\n".join([
 S("CAM-LOCK"),
 S("FRAME-SCALE").replace("[SCALE]", "about three quarters") + " " + S("FRAME-PROPPED"),
 "THE SAME MAN exactly as in the attached reference sheet — a white British man of fifty-four, broad square face, light blue-grey eyes set wide apart, a short snub nose, fair ruddy freckled skin, "
 "short sandy-red hair going grey at the sides with a left side parting, clean-shaven, a small flat brown mole high on his right cheekbone, stocky and broad through the chest — unchanged in face, age and build. "
 "HE IS DRESSED AS A DOCTOR AT WORK, and this is the most important thing in the picture after his face: a crisp white knee-length doctor's lab coat worn ON, open at the front, its white lapels and shoulders clearly visible over a pale blue button-down shirt with the top button undone and no tie, and a black stethoscope hung round his neck over the coat collar, its two tubes and silver chest-piece resting on the front of the coat. "
 "IN THE SAME ROOM as the attached consulting-room photograph: the pale grey wall, the cork noticeboard of leaflets and the blood-pressure unit behind him, soft and out of focus, the examination couch at the right edge. "
 "He sits in his black swivel chair square to the phone, which is propped on the light-wood desk in front of him, forearms resting on the desk edge, hands loosely together, the white knee model at the left edge of the desk, eyes on the lens, about to speak. " +
 S("APPROACH-PRO") + " "
 "In white and pale blue: the white coat and the stethoscope are in frame.",
 S("LIGHT-SHOT").replace("[SOURCE from the light plan — the window on the room's WALL, or the named practical]", "The consulting-room window on the room's north wall")
   .replace("[SUBJECT]", "him").replace("[SCREEN SIDE]", "left").replace("[TIME-OF-DAY QUALITY and the act's light state]", "steady overcast morning daylight").replace("[SIDE]", "the left"),
 S("SKIN-B1"),
 S("SKIN-B3").replace("[FOREHEAD-LINES]", "two fine horizontal lines").replace("[AGE-FEATURES]", AGE),
 S("SKIN-B4"), S("EYES-A"),
 S("HAIR-A").replace("[HAIR-SPEC]", "short sandy-red hair going grey through the sides, the ginger still showing on top, side-parted on the left"),
 S("NECK-A"), S("TEETH-A"),
 S("CAP-A"), S("CAP-FILE"),
 "AVOID: no doctor in a shirt only, no missing white coat, no coat taken off or hung on the chair, no missing stethoscope, no scrubs, no suit jacket, no jumper over the shirt, " + ", ".join([S("NEG-FRAME"), S("NEG-SKIN"), S("NEG-TEX"), S("NEG-FINISH"), S("NEG-M1"), S("NEG-LIGHT")]),
])
assert "[" not in STEP1, STEP1[STEP1.index("["):][:80]

# ---- step 2: Kling voice-source takes (§36 JSON, minified, <= 2,500) -- the script's opening lines, in order
TAKES = [
 ("G1", "In six weeks, this woman stopped coming down her own stairs backwards.", "woman", "six weeks", "a plain fact, quietly pleased"),
 ("G2", "Without an operation. Without another course of physio. Without one more brace going in the drawer.", "operation", "Without", "counting them off"),
 ("G3", "And here is how you can do that too.", "here", "you", "warm"),
]
def sel(neg, *drop):
    return ", ".join(c for c in neg.split(", ") if c not in drop)
def take(tid, line, closure, stress, intent):
    mouth = S("MOUTH-C").replace("[CLOSURE-WORD]", closure).replace("[MOUTH-CORNER]", "right")
    mouth = mouth.replace(" Small conversational amplitude matched to the voice, teeth mostly hidden.", "").replace(" Cheeks and throat move with speech.", "").replace(" Mouth fully closed between sentences.", "")
    d = {
     "shot": f"Voice take {tid}.",
     "dialogue": line,
     "delivery": VOICE_DOC + f" Across the desk, {intent}; stress on '{stress}'. " + S("AUD-A") + " Phone a metre away.",
     "subject": "As in the start frame.",
     "camera": {"movement": S("RIG-R3C"), "framing": "As in the start frame."},
     "motion": S("BREATH-A") + f" Right hand lifts off the desk on '{stress}', settles; eyes on lens. " + mouth + " " + S("HOLD-C"),
     "lighting": S("INHERIT-CAP"),
     "style": "As in the start frame.",
     "negatives": ", ".join([sel(S("NEG-WARP-C"), "no parts detaching", "no duplicate objects", "no flickering geometry", "no shape shifting", "no merging", "no splitting", "no texture swimming", "no smearing"), S("NEG-CAM-TH"),
                             sel(S("NEG-LIGHT-C"), "no sun patch moving", "no shadows sliding", "no light following the subject"), "no music, no second voice"]),  # §37 TH ladder step 1
    }
    return json.dumps(d, ensure_ascii=False, separators=(",", ":"))

pathlib.Path("D_step1_image.prompt.txt").write_text(STEP1); print("step1", len(STEP1))
out = {}
for t in TAKES:
    s = take(*t); out[t[0]] = s
    pathlib.Path(f"D_{t[0]}.kling.json").write_text(s)
    print(t[0], len(s), len(t[1].split()), "words", "OVER" if len(s) > 2500 else "ok")
json.dump({"VOICE_DOC": VOICE_DOC, "takes": out}, open("voice.json", "w"), indent=1, ensure_ascii=False)
