#!/usr/bin/env python3
"""§22U steps 1-2 for the narrator (stryde-three-regrets), assembled from Appendix A by ID."""
import re, json, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()

VOICE_NARR = ("A woman of fifty-seven from West Yorkshire, a low dry alto, level and unhurried but brisk. "
 "Flat Yorkshire vowels, short \"u\", t's clipped; statements land and stop, no lift. A small breath before a number. "
 "Stress: slower and quieter on the turn word, never louder.")
assert VOICE_NARR == open("../BUILD_SHEET.md").read().split("**`VOICE-NARR`**")[1].split("```")[1].strip()

# ---- step 1: talking-head image (voice-source start frame; also the HeyGen avatar image) ----
AGE = "fine crow's feet at both eyes, two vertical lines between the brows, a soft fold from the nose to each corner of the mouth, faint freckling across the cheekbones"
STEP1 = "\n\n".join([
 S("CAM-LOCK"),
 S("FRAME-SCALE").replace("[SCALE]", "about three quarters") + " " + S("FRAME-PROPPED"),
 "THE SAME WOMAN exactly as in the attached reference sheet — long narrow face, deep-set grey-green eyes, a long nose with a small hook, straight hair grown out from a dark chestnut dye with steel grey through the top, pulled back into a low loose knot, tall and wiry — unchanged in face, age and build. "
 "IN THE SAME ROOM as the attached workroom photograph: the red-brick wall and the cork pinboard of printed messages behind her, soft and out of focus. "
 "She sits at the long worktop desk, turned three-quarters towards the phone propped against a grey post tray in front of her, forearms on the desk, one printed letter loose under her left hand, eyes on the lens, about to speak. "
 "Wearing a rust-orange needlecord overshirt open over a plain cream crew-neck T-shirt, in rust and cream.",
 S("LIGHT-SHOT").replace("[SOURCE from the light plan — the window on the room's WALL, or the named practical]", "The sash window on the room's east wall")
   .replace("[SUBJECT]", "her").replace("[SCREEN SIDE]", "left").replace("[TIME-OF-DAY QUALITY and the act's light state]", "soft ordinary morning daylight").replace("[SIDE]", "the left"),
 S("SKIN-B1"),
 S("SKIN-B3").replace("[FOREHEAD-LINES]", "fine horizontal lines").replace("[AGE-FEATURES]", AGE),
 S("SKIN-B4"), S("EYES-A"),
 S("HAIR-A").replace("[HAIR-SPEC]", "straight hair grown out from a dark chestnut dye, steel grey through the top four centimetres, in a low loose knot"),
 S("NECK-A"), S("TEETH-A"),
 S("CAP-A"), S("CAP-FILE"),
 "AVOID: " + ", ".join([S("NEG-FRAME"), S("NEG-SKIN"), S("NEG-TEX"), S("NEG-FINISH"), S("NEG-M1"), S("NEG-LIGHT")]),
])
assert "[" not in STEP1, STEP1[STEP1.index("["):][:80]

# ---- step 2: Kling voice-source takes (§36 JSON, minified, <= 2,500) --------------------------
TAKES = [
 ("G1", "Three things people tell us they wish they had known about their knees.", "people", "Three", "plain and direct"),
 ("G2", "Not one of them is that they should have gone to the doctor sooner.", "them", "Not one", "a quiet correction"),
]
def sel(neg, *drop):
    return ", ".join(c for c in neg.split(", ") if c not in drop)

def take(tid, line, closure, stress, intent):
    mouth = S("MOUTH-C").replace("[CLOSURE-WORD]", closure).replace("[MOUTH-CORNER]", "left")
    mouth = mouth.replace(" Small conversational amplitude matched to the voice, teeth mostly hidden.", "").replace(" Cheeks and throat move with speech.", "").replace(" Mouth fully closed between sentences.", "")
    d = {
     "shot": f"Voice take {tid}.",
     "dialogue": line,
     "delivery": VOICE_NARR + f" To one person across the desk, {intent}; stress on '{stress}'. Not a narrator, not an advert. " + S("AUD-A") + " Small brick room, phone a metre away.",
     "subject": "As in the start frame.",
     "camera": {"movement": S("RIG-R3C"), "framing": "As in the start frame."},
     "motion": S("BREATH-A") + f" Right hand lifts off the desk on '{stress}', settles; eyes on lens. " + mouth + " " + S("HOLD-C"),
     "lighting": S("INHERIT-CAP"),
     "style": "As in the start frame.",
     "negatives": ", ".join([sel(S("NEG-WARP-C"), "no parts detaching", "no duplicate objects", "no flickering geometry"), S("NEG-CAM-TH"),
                             sel(S("NEG-LIGHT-C"), "no sun patch moving"), "no music, no second voice"]),  # §37 TH ladder step 1: selected negatives
    }
    return json.dumps(d, ensure_ascii=False, separators=(",", ":"))

pathlib.Path("N_step1_image.prompt.txt").write_text(STEP1)
print("step1", len(STEP1))
out = {}
for t in TAKES:
    s = take(*t); out[t[0]] = s
    assert len(s) <= 2500, (t[0], len(s))
    pathlib.Path(f"N_{t[0]}.kling.json").write_text(s)
    print(t[0], len(s), len(t[1].split()), "words")
json.dump({"VOICE_NARR": VOICE_NARR, "takes": out}, open("voice.json", "w"), indent=1, ensure_ascii=False)
