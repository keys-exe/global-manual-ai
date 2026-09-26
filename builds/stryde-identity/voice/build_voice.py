#!/usr/bin/env python3
"""§22U steps 1-2 for the narrator (stryde-identity), assembled from Appendix A by ID."""
import re, json, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()

VOICE_NARR_FULL = ("A man of sixty from Tyneside, a low dry chest voice with gravel at its edges, brisk and stop-start. "
 "Placement in the chest, little nasal colour; texture dry with a faint rasp on held vowels; tempo brisk, about 185 words a minute, in short bursts; "
 "melody flat, statements falling at the end, questions barely lifting; articulation: Geordie vowels kept, final t's glottal, every other consonant clear; "
 "habit: a short breath out through the nose before a number. Age wear: breath shortening at long line ends, a thin top to the range. "
 "Stress: quieter and slower on the turn word, never louder.")

# Compressed once for the Kling ceiling (§37) and locked in this form: VOICE-OPEN + melody, articulation, habit, stress register.
VOICE_NARR = ("A man of sixty from Tyneside, a low dry chest voice with gravel at its edges, brisk and stop-start. "
 "Statements land flat and fall at the end; Geordie vowels, glottal t's; a short breath out through the nose before a number. "
 "Stress: quieter and slower on the turn word, never louder.")

# ---- step 1: talking-head image (voice-source start frame) -------------------------
AGE = "laugh lines fanning deep from both eyes, soft folds from the nose to the mouth, a few horizontal lines across the forehead, faint sun freckling on the cheekbones"
STEP1 = "\n\n".join([
 S("CAM-LOCK"),
 S("FRAME-SCALE").replace("[SCALE]", "about three quarters") + " " + S("FRAME-PROPPED"),
 "THE SAME MAN exactly as in the attached reference sheet — wavy dark-grey hair worn a little long over the collar, short salt-and-pepper beard, warm hazel eyes crinkled at the corners, solid build — unchanged in face, age and build. "
 "He sits at his own kitchen table, forearms resting on it, turned square to the phone propped against a mug in front of him, eyes on the lens, mouth closed, about to speak. "
 "Wearing a navy crew-neck knitted jumper with the collar of a blue checked shirt, in navy/denim. "
 "His kitchen, untidied: a kettle and a biscuit tin on the worktop behind him, a radio on the windowsill, a tea towel over the oven door, a wall clock.",
 S("SKIN-B1"),
 S("SKIN-B3").replace("[FOREHEAD-LINES]", "a few horizontal lines").replace("[AGE-FEATURES]", AGE),
 S("SKIN-B4"), S("EYES-A"),
 S("HAIR-A").replace("[HAIR-SPEC]", "wavy dark-grey hair a little long over the collar, a short salt-and-pepper beard"),
 S("NECK-A"), S("TEETH-A"),
 S("LOC-KITCHEN-MORN"),
 S("CAP-A"), S("CAP-FILE"),
 "AVOID: " + ", ".join([S("NEG-FRAME"), S("NEG-SKIN"), S("NEG-TEX"), S("NEG-FINISH"), S("NEG-M1")]),
])

# ---- step 2: Kling voice-source takes (§36 JSON, minified, <= 2,500) ----------------
TAKES = [
 ("G1", "Why these knee straps are a must if you've been told you're bone on bone.", "bone", "must",
  "asking it straight"),
 ("G2", "Because every step puts seventeen times your bodyweight through one small spot below your kneecap.", "bodyweight", "seventeen",
  "a plain fact"),
 ("G3", "These straps took three years to build with orthopaedic surgeons, to sit right on that spot.", "build", "three years",
  "quietly proud"),
]
def take(tid, line, closure, stress, intent):
    mouth = S("MOUTH-C").replace("[CLOSURE-WORD]", closure).replace("[MOUTH-CORNER]", "right")
    mouth = mouth.replace(" Small conversational amplitude matched to the voice, teeth mostly hidden.", "").replace(" Cheeks and throat move with speech.", "").replace(" Mouth fully closed between sentences.", "")
    d = {
     "shot": f"Voice take {tid}.",
     "dialogue": line,
     "delivery": VOICE_NARR + f" To one person across the table, {intent}; stress on '{stress}'. Not a narrator, not an advert. " + S("AUD-A") + " Kitchen, phone a metre away.",
     "subject": "As in the start frame.",
     "camera": {"movement": S("RIG-R3C"), "framing": "PROPPED as in the start frame, hands in the lower frame."},
     "motion": S("BREATH-A") + f" Right hand lifts on '{stress}', settles; eyes on lens. " + mouth + " " + S("HOLD-C"),
     "lighting": S("INHERIT-CAP"),
     "style": "As in the start frame.",
     "negatives": ", ".join([S("NEG-WARP-C"), S("NEG-CAM-TH"), "no music, no second voice"]),
    }
    return json.dumps(d, ensure_ascii=False, separators=(",", ":"))

pathlib.Path("N_step1_image.prompt.txt").write_text(STEP1)
print("step1", len(STEP1))
out = {}
for t in TAKES:
    s = take(*t); out[t[0]] = s
    pathlib.Path(f"N_{t[0]}.kling.json").write_text(s)
    print(t[0], len(s), len(t[1].split()), "words")
json.dump({"VOICE_NARR": VOICE_NARR, "VOICE_NARR_FULL": VOICE_NARR_FULL, "takes": out}, open("voice.json", "w"), indent=1, ensure_ascii=False)
