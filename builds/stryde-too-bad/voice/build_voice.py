#!/usr/bin/env python3
"""§22U steps 1-2 for the narrator (stryde-too-bad), assembled from Appendix A by ID."""
import re, json, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()

VOICE_NARR = open("../BUILD_SHEET.md").read().split("**`VOICE-NARR`**")[1].split("```")[1].strip()
assert VOICE_NARR.startswith("A British woman of fifty-seven")

# ---- step 1: talking-head image (voice-source start frame; also the HeyGen avatar image) ----
AGE = "fine lines at the outer eyes and across the forehead, a deep vertical line between the brows, soft folds from the nose to the mouth, faint sun spots on the cheekbones"
STEP1 = "\n\n".join([
 S("CAM-LOCK"),
 S("FRAME-SCALE").replace("[SCALE]", "about three quarters") + " " + S("FRAME-PROPPED"),
 "THE SAME WOMAN as in the two attached reference images — the face close-up (image 2) is her face exactly, and the five-panel sheet (image 1) is her body and clothes; copy that face, do not invent a new one. A white British woman of fifty-seven — long narrow face with high flat cheekbones, hooded grey-green eyes, a slightly hooked narrow nose, a thin mouth that turns down a little at the corners, the small white scar breaking the outer end of her right eyebrow, silver-ash blunt chin-length bob with a straight fringe, tall and narrow — her real age showing, unchanged in face, age, hair colour and build. "
 "In her own small study at home: a white-painted wall behind her with a crowded bookshelf and a framed map, soft and out of focus. "
 "She sits at a wooden desk, turned three-quarters towards the camera, forearms resting on the bare desk top, hands loosely together, eyes on the lens, about to speak. An ordinary photograph of the room: no phone, camera screen, on-screen buttons or device appears anywhere, and nothing stands on the desk between her and the lens. "
 "Wearing a charcoal-grey merino V-neck jumper over a white T-shirt, in charcoal and white.",
 S("LIGHT-SHOT").replace("[SOURCE from the light plan — the window on the room's WALL, or the named practical]", "The window on the study's west wall")
   .replace("[SUBJECT]", "her").replace("[SCREEN SIDE]", "left").replace("[TIME-OF-DAY QUALITY and the act's light state]", "soft ordinary afternoon daylight").replace("[SIDE]", "the left"),
 S("SKIN-B1"),
 S("SKIN-B3").replace("[FOREHEAD-LINES]", "fine horizontal lines").replace("[AGE-FEATURES]", AGE),
 S("SKIN-B4"), S("EYES-A"),
 S("HAIR-A").replace("[HAIR-SPEC]", "ash-blonde hair gone mostly silver, cut in a blunt chin-length bob with a straight fringe"),
 S("NECK-A"), S("TEETH-A"),
 S("CAP-A"), S("CAP-FILE"),
 "AVOID: " + ", ".join([S("NEG-FRAME"), S("NEG-SKIN"), S("NEG-TEX"), S("NEG-FINISH"), S("NEG-M1"), S("NEG-LIGHT"), "no phone in frame, no phone in her hand, no second phone, no screen or device, no object between her and the camera, no mug or pens in the foreground, no newspaper, no readable text, no camera app interface, no on-screen buttons or labels, no shutter button, no viewfinder overlay, no screenshot, no younger woman, no brown or dark hair, no hair tied back, no different face from the reference"]),
])
assert "[" not in STEP1, STEP1[STEP1.index("["):][:80]

# ---- step 2: Kling voice-source takes (§36 JSON, minified, <= 2,500) --------------------------
TAKES = [
 ("G1", "Too bad these knee straps look too small to work.", "bad", "small", "dry, almost amused"),
 ("G2", "Built over three years with orthopaedic surgeons, to do what sleeves and braces never could.", "Built", "three", "plain and sure"),
 ("G3", "They're small on purpose. Because the pain comes from one small spot.", "purpose", "one", "setting a friend straight"),
]
def sel(neg, *drop):
    return ", ".join(c for c in neg.split(", ") if c not in drop)

def take(tid, line, closure, stress, intent):
    mouth = S("MOUTH-C").replace("[CLOSURE-WORD]", closure).replace("[MOUTH-CORNER]", "left")
    mouth = mouth.replace(" Small conversational amplitude matched to the voice, teeth mostly hidden.", "").replace(" Cheeks and throat move with speech.", "").replace(" Mouth fully closed between sentences.", "")
    d = {
     "shot": f"Voice take {tid}.",
     "dialogue": line,
     "delivery": VOICE_NARR + f" To one person, {intent}; stress on '{stress}'. Not a narrator, not an advert. " + S("AUD-A") + "",
     "subject": "As in the start frame.",
     "camera": {"movement": S("RIG-R3C"), "framing": "As in the start frame."},
     "motion": S("BREATH-A") + f" Right hand lifts off the desk on '{stress}', settles; eyes on lens. " + mouth + " " + S("HOLD-C"),
     "lighting": S("INHERIT-CAP"),
     "style": "As in the start frame.",
     "negatives": ", ".join([sel(S("NEG-WARP-C"), "no parts detaching", "no duplicate objects", "no flickering geometry", "no background bending", "no texture swimming", "no smearing"), S("NEG-CAM-TH"),
                             sel(S("NEG-LIGHT-C"), "no sun patch moving", "no shadows sliding", "no light following the subject", "no flickering light"), "no music, no second voice"]),  # §37 TH ladder step 1: selected negatives
    }
    return json.dumps(d, ensure_ascii=False, separators=(",", ":"))

pathlib.Path("N_step1_image.prompt.txt").write_text(STEP1)  # v3 (Fix "USE MY AVATAR NARRATOR": v2 ignored the sheet — younger woman, brown hair — and drew a camera-app screen; face crop attached as image 2, identity restated, UI negatives) · v2 (Fix "fix this": v1 drew a second phone, pen mug and newspaper in front of her)
print("step1", len(STEP1))
out = {}
for t in TAKES:
    s = take(*t); out[t[0]] = s
    assert len(s) <= 2500, (t[0], len(s))
    pathlib.Path(f"N_{t[0]}.kling.json").write_text(s)
    print(t[0], len(s), len(t[1].split()), "words")
json.dump({"VOICE_NARR": VOICE_NARR, "takes": out}, open("voice.json", "w"), indent=1, ensure_ascii=False)
