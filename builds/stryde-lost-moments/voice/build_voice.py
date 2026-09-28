#!/usr/bin/env python3
"""§22U steps 1-2 for the narrator (stryde-lost-moments), assembled from Appendix A by ID."""
import re, json, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()

VOICE_NARR_FULL = ("A woman of sixty-two from South London, a warm mid-low voice with a soft grain, brisk and even. "
 "Placement between chest and mouth, a little warmth in the low end; texture soft grain, clean on held vowels; tempo brisk, about 175 words a minute; "
 "melody: statements fall gently at the end, a small lift on the payoff word; articulation: London vowels, relaxed and unforced, t's lightly dropped mid-word, clear at line ends; "
 "habit: a short in-breath before a number. Age wear: a little breath at long line ends. "
 "Stress: slower and lower on the turn word, never louder.")

# Compressed once for the Kling ceiling (§37) and locked in this form (Build Sheet, VOICE-NARR).
VOICE_NARR = ("A woman of sixty-two from South London, a warm mid-low voice with a soft grain, brisk and even. "
 "London vowels, relaxed and unforced; t's lightly dropped mid-word, clear at line ends. Statements fall gently at the end; "
 "a small smile audible on the payoff lines. Stress: slower and lower on the turn word, never louder.")

# ---- step 1: talking-head image (voice-source start frame) -------------------------
AGE = "soft folds from the nose to the corners of the mouth, fine lines fanning from the outer eyes, slight hollowing under the eyes, a faint crease across the lower forehead, a scatter of small dark raised spots on both cheekbones"
STEP1 = "\n\n".join([
 S("CAM-LOCK"),
 S("FRAME-SCALE").replace("[SCALE]", "about three quarters") + " " + S("FRAME-PROPPED"),
 "THE SAME WOMAN exactly as in the attached reference sheet — short natural hair cropped close, black threaded thickly with grey, a round face with high full cheekbones, deep-set dark brown eyes, the small dark raised spots across both cheekbones, full-figured — unchanged in face, age and build. "
 "She sits at her own kitchen table, forearms resting on it, turned square to the phone propped against a mug in front of her, eyes on the lens, mouth closed, about to speak. "
 "Wearing a mustard-yellow knitted cardigan buttoned over a cream round-neck top. "
 "Her kitchen in a south London flat, untidied: a kettle and a tin of biscuits on the worktop behind her, a spider plant on the windowsill, a calendar with no readable writing, a tea towel over the oven door.",
 S("SKIN-B1"),
 S("SKIN-B3").replace("[FOREHEAD-LINES]", "a few horizontal lines").replace("[AGE-FEATURES]", AGE),
 S("SKIN-B4"), S("EYES-A"),
 S("HAIR-A").replace("[HAIR-SPEC]", "short natural hair cropped close to the head, black threaded thickly with grey, grey heaviest at the temples"),
 S("NECK-A"), S("TEETH-A"),
 S("LOC-KITCHEN-MORN"),
 S("CAP-A"), S("CAP-FILE"),
 "AVOID: " + ", ".join([S("NEG-FRAME"), S("NEG-SKIN"), S("NEG-TEX"), S("NEG-FINISH"), S("NEG-M1")]),
])

# ---- step 2: Kling voice-source takes (§36 JSON, minified, <= 2,500) ----------------
TAKES = [
 ("G1", "Too bad you can't go down the stairs forwards. Thanks to these life-changing knee straps, not for much longer.", "much", "forwards",
  "telling it straight, a little rueful"),
 ("G2", "Built over three years with orthopaedic surgeons, to do what sleeves and braces never could.", "braces", "never",
  "a plain fact, quietly proud"),
]
def take(tid, line, closure, stress, intent):
    mouth = S("MOUTH-C").replace("[CLOSURE-WORD]", closure).replace("[MOUTH-CORNER]", "right")
    mouth = mouth.replace(" Small conversational amplitude matched to the voice, teeth mostly hidden.", "").replace(" Cheeks and throat move with speech.", "").replace(" Mouth fully closed between sentences.", "")
    d = {
     "shot": f"Voice take {tid}.",
     "dialogue": line,
     "delivery": VOICE_NARR + f" To one person across the table, {intent}; stress on '{stress}'. Not a narrator, not an advert. " + S("AUD-A") + " Kitchen.",
     "subject": "As in the start frame.",
     "camera": {"movement": S("RIG-R3C"), "framing": "PROPPED as in the start frame."},
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
