#!/usr/bin/env python3
"""§22U steps 1-2 for the host (stryde-what-changed), assembled from Appendix A by ID."""
import re, json, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()

# VOICE-HOST (§22D) — locked in the Build Sheet; compressed for the Kling ceiling (§37).
VOICE_HOST_FULL = ("A British woman of forty-one from the south-east of England, a clear mid-range voice with a little warmth underneath, "
 "plain and confiding, as if explaining something to a friend across a table. Soft modern southern English vowels, never RP, never estuary "
 "caricature, never American. Statements fall at the end; the turn lines slower and lower, never louder. Brisk and even, about one hundred "
 "and seventy words a minute.")
VOICE_HOST = ("A British woman of forty-one from the south-east of England, a clear mid-range voice, a little warmth underneath, plain and confiding. "
 "Soft modern southern English vowels, never RP, never American. Statements fall at the end; brisk and even.")

AGE = "fine laugh lines at the outer eyes, faint soft folds from the nose to the corners of the mouth, a faint crease across the forehead, a light scatter of freckles across the nose and cheeks, one small dark beauty mark high on the left cheekbone"
STEP1 = "\n\n".join([
 S("CAM-LOCK"),
 S("FRAME-SCALE").replace("[SCALE]", "about three quarters") + " " +
 "Podcast framing: the phone on a small tripod in front of the sofa at her seated eye height, about a metre and a half away, pointing straight at her, locked off. "
 "She is framed from the middle of her thighs up, sitting in the middle of the frame with a clear band of brick wall above her head, the sofa's buttoned back and rolled arm readable on both sides of her. "
 "Her face takes about a sixth of the frame height and both eyes sit level in the upper third.",
 "THE SAME WOMAN exactly as in the attached reference sheet — the FACE CLOSE-UP panel of the sheet is how her face must look here: shoulder-length honey-blonde waves with darker roots tucked behind the right ear, "
 "a soft heart-shaped face with round apple cheeks, hazel-green eyes, freckles across the nose and cheeks, the small dark beauty mark high on her left cheekbone — unchanged in face, age and build. "
 "She sits on the worn cognac leather chesterfield sofa of the attached studio reference image, relaxed, one knee crossed over the other, her hands resting loosely together in her lap, "
 "FULL FACE TO THE CAMERA: her nose pointing straight at the lens, both eyes looking directly into the lens, shoulders square and level. Mouth closed, about to speak, a warm open look with the corners of her mouth turned very slightly up — "
 "a friendly host about to tell a guest something they'll be glad to know. Wearing the oatmeal-cream chunky cable-knit jumper and mid-blue jeans from her sheet. "
 "The black podcast microphone on its black boom arm reaches in from the right side of the frame and stops beside her chin on her left side, about a hand's width from her face, never in front of her mouth. "
 "The studio behind her exactly as in the attached studio reference: the exposed London stock brick wall, the tall black steel-framed window on the left, the tripod floor lamp with its globe bulb behind the sofa's right end, switched off.",
 S("SKIN-B1"),
 S("SKIN-B3").replace("[FOREHEAD-LINES]", "a faint line or two").replace("[AGE-FEATURES]", AGE),
 S("SKIN-B4"), S("EYES-A"),
 S("HAIR-A").replace("[HAIR-SPEC]", "shoulder-length honey-blonde hair with darker roots in loose natural waves, tucked behind the right ear"),
 S("NECK-A"), S("TEETH-A"),
 "Daylight from the tall window on the left, at about forty-five degrees off the camera axis — soft, overcast, slightly cool, lighting both sides of her face with the left side brighter, a small catchlight in each eye; "
 "the brick behind her a stop darker, shadows open. No studio lights, the floor lamp off.",
 S("CAP-A"), S("CAP-FILE"),
 "AVOID: " + ", ".join([S("NEG-FRAME"), S("NEG-SKIN"), S("NEG-TEX"), S("NEG-FINISH"), S("NEG-M1"),
   "no microphone in front of the mouth, no headphones, no product in frame, no text, no different woman from the reference sheet, no three-quarter view, no head turned, no eyes looking off-camera"]),
])

TAKES = [
 ("G1", "Your knees have been taking seventeen times your bodyweight on every step for forty years, and you never felt a thing.", "thing", "never",
  "letting a guest in on something surprising"),
 ("G2", "That band is the patellar tendon. It sits two centimetres below your kneecap, on the front of the joint.", "joint", "tendon",
  "a plain fact, explained kindly"),
]
def take(tid, line, closure, stress, intent):
    mouth = S("MOUTH-C").replace("[CLOSURE-WORD]", closure).replace("[MOUTH-CORNER]", "right")
    mouth = mouth.replace(" Small conversational amplitude matched to the voice, teeth mostly hidden.", "").replace(" Cheeks and throat move with speech.", "").replace(" Mouth fully closed between sentences.", "")
    d = {
     "shot": f"Voice take {tid}.",
     "dialogue": line,
     "delivery": VOICE_HOST + f" To one guest on a podcast, {intent}; stress on '{stress}'. Not a narrator, not an advert. " + S("AUD-A") + " Small studio room.",
     "subject": "As in the start frame.",
     "camera": {"movement": S("RIG-R3C"), "framing": "As in the start frame."},
     "motion": S("BREATH-A") + f" Hands lift slightly from her lap on '{stress}', settle; eyes on lens. " + mouth + " " + S("HOLD-C"),
     "lighting": S("INHERIT-CAP"),
     "style": "As in the start frame.",
     "negatives": ", ".join([S("NEG-WARP-C"), S("NEG-CAM-TH"), "no music, no second voice"]),
    }
    return json.dumps(d, ensure_ascii=False, separators=(",", ":"))

pathlib.Path("H_step1_image.prompt.txt").write_text(STEP1)
print("step1", len(STEP1))
out = {}
for t in TAKES:
    s = take(*t); out[t[0]] = s
    pathlib.Path(f"H_{t[0]}.kling.json").write_text(s)
    print(t[0], len(s), len(t[1].split()), "words")
json.dump({"VOICE_HOST": VOICE_HOST, "VOICE_HOST_FULL": VOICE_HOST_FULL, "takes": out}, open("voice.json", "w"), indent=1, ensure_ascii=False)
