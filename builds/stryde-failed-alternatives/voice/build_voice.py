#!/usr/bin/env python3
"""§22U steps 1-2 for the narrator (stryde-failed-alternatives), assembled from Appendix A by ID."""
import re, json, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()

VOICE_NARR = open("../BUILD_SHEET.md").read().split("**`VOICE-NARR`**")[1].split("```")[1].strip()
assert VOICE_NARR.startswith("A British woman of sixty-one")

# ---- step 1: talking-head image (voice-source start frame; also the HeyGen avatar image) ----
AGE = "fine lines fanning from the outer eyes, soft creases across the forehead, deep folds from the nose to the mouth, a soft double chin, faint thread veins on the cheeks"
STEP1 = "\n\n".join([
 S("CAM-LOCK"),
 S("FRAME-SCALE").replace("[SCALE]", "about three quarters") + " " + S("FRAME-PROPPED"),
 "THE SAME WOMAN as in the two attached reference images — the face close-up (image 2) is her face exactly, and the five-panel sheet (image 1) is her body and clothes; copy that face, do not invent a new one. A white British woman of sixty-one — broad round face with full soft cheeks, heavy-lidded pale blue eyes, a short snub nose, a wide mouth with a fuller lower lip, the small round pitted scar in the middle of her forehead just above the brows, short white hair cut close at the sides and pushed up at the front in a soft spiky crop, short and heavyset — her real age showing, unchanged in face, age, hair colour and build. "
 "In her own small front room at home: a pale buttermilk wall behind her with a pine dresser of blue-and-white plates and a framed seaside print, soft and out of focus. "
 "She sits at a small round pine table, turned three-quarters towards the camera, forearms resting on the bare table top, hands loosely together, eyes on the lens, about to speak. An ordinary photograph of the room: no phone, camera screen, on-screen buttons or device appears anywhere, and nothing stands on the table between her and the lens. "
 "Wearing a bottle-green wool cardigan open over a navy-and-white striped Breton top, in green, navy and white.",
 S("LIGHT-SHOT").replace("[SOURCE from the light plan — the window on the room's WALL, or the named practical]", "The window on the front room's south wall")
   .replace("[SUBJECT]", "her").replace("[SCREEN SIDE]", "right").replace("[TIME-OF-DAY QUALITY and the act's light state]", "soft ordinary late-morning daylight").replace("[SIDE]", "the right"),
 S("SKIN-B1"),
 S("SKIN-B3").replace("[FOREHEAD-LINES]", "fine horizontal lines").replace("[AGE-FEATURES]", AGE),
 S("SKIN-B4"), S("EYES-A"),
 S("HAIR-A").replace("[HAIR-SPEC]", "short white hair cut close at the back and sides and pushed up at the front in a soft spiky crop"),
 S("NECK-A"), S("TEETH-A"),
 S("CAP-A"), S("CAP-FILE"),
 "AVOID: " + ", ".join([S("NEG-FRAME"), S("NEG-SKIN"), S("NEG-TEX"), S("NEG-FINISH"), S("NEG-M1"), S("NEG-LIGHT"), "no phone in frame, no phone in her hand, no second phone, no screen or device, no object between her and the camera, no mug or pens in the foreground, no newspaper, no readable text, no camera app interface, no on-screen buttons or labels, no shutter button, no viewfinder overlay, no screenshot, no younger woman, no long hair, no dark hair, no slim or narrow face, no different face from the reference"]),
])
assert "[" not in STEP1, STEP1[STEP1.index("["):][:80]

# ---- step 2: Kling voice-source takes (§36 JSON, minified, <= 2,500) --------------------------
TAKES = [
 ("G1", "Too bad about all those sleeves and braces you bought.", "bad", "all", "sympathetic, a touch rueful"),
 ("G2", "Thanks to these life-changing knee straps, you won't need another one.", "these", "need", "warm and sure"),
 ("G3", "Built over three years with orthopaedic surgeons, to do what sleeves and braces never could.", "Built", "three", "plain and sure"),
]
def sel(neg, *drop):
    return ", ".join(c for c in neg.split(", ") if c not in drop)

def take(tid, line, closure, stress, intent):
    mouth = S("MOUTH-C").replace("[CLOSURE-WORD]", closure).replace("[MOUTH-CORNER]", "left")
    mouth = mouth.replace(" Small conversational amplitude matched to the voice, teeth mostly hidden.", "").replace(" Cheeks and throat move with speech.", "").replace(" Mouth fully closed between sentences.", "")
    d = {
     "shot": f"Voice take {tid}.",
     "dialogue": line,
     "delivery": VOICE_NARR + f" To one person, {intent}; stress on '{stress}'. " + S("AUD-A") + "",
     "subject": "As in the start frame.",
     "camera": {"movement": S("RIG-R3C"), "framing": "As in the start frame."},
     "motion": S("BREATH-A") + f" Right hand lifts off the table on '{stress}', settles; eyes on lens. " + mouth + " " + S("HOLD-C"),
     "lighting": S("INHERIT-CAP"),
     "style": "As in the start frame.",
     "negatives": ", ".join([sel(S("NEG-WARP-C"), "no parts detaching", "no duplicate objects", "no flickering geometry", "no background bending", "no texture swimming", "no smearing"), S("NEG-CAM-TH"),
                             sel(S("NEG-LIGHT-C"), "no sun patch moving", "no shadows sliding", "no light following the subject", "no flickering light"), "no music, no second voice"]),  # §37 TH ladder step 1: selected negatives
    }
    return json.dumps(d, ensure_ascii=False, separators=(",", ":"))

pathlib.Path("N_step1_image.prompt.txt").write_text(STEP1)  # v1 (face crop attached from the start, as the sibling build learned); sibling notes: v3 (Fix "USE MY AVATAR NARRATOR": v2 ignored the sheet — younger woman, brown hair — and drew a camera-app screen; face crop attached as image 2, identity restated, UI negatives) · v2 (Fix "fix this": v1 drew a second phone, pen mug and newspaper in front of her)
print("step1", len(STEP1))
out = {}
for t in TAKES:
    s = take(*t); out[t[0]] = s
    assert len(s) <= 2500, (t[0], len(s))
    pathlib.Path(f"N_{t[0]}.kling.json").write_text(s)
    print(t[0], len(s), len(t[1].split()), "words")
json.dump({"VOICE_NARR": VOICE_NARR, "takes": out}, open("voice.json", "w"), indent=1, ensure_ascii=False)
