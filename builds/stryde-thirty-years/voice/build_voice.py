#!/usr/bin/env python3
"""§22U steps 1-2 for the maker (stryde-thirty-years), assembled from Appendix A by ID."""
import re, json, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()

# Locked in BUILD_SHEET.md (step 3); goes verbatim first in every take's delivery.
VOICE_MAKER = ("A man of sixty-two from the Black Country, Walsall, a dry, flat, slightly nasal voice, level and unhurried but never slow. "
 "Statements fall and stop dead, no lift at the end; Black Country vowels, \"I\" close to \"oi\", dropped h's, glottal t's. "
 "A short dry sniff of a laugh before a put-down. Stress: slower and flatter on the turn, never louder.")

AGE = "deep vertical lines between the brows, crow's feet cut deep at both eyes, hollows under the cheekbones, deep horizontal forehead creases, sun spots on the temples"
LIGHT = (S("LIGHT-SHOT").replace("[SOURCE from the light plan — the window on the room's WALL, or the named practical]", "the low morning sun through the east factory windows along the bench wall")
         .replace("[SUBJECT]", "his face").replace("[SCREEN SIDE]", "left").replace("[TIME-OF-DAY QUALITY and the act's light state]", "pale, clean early-morning light")
         .replace("[SIDE]", "the left"))
STEP1 = "\n\n".join([
 S("CAM-FRONT"),
 S("FRAME-SCALE").replace("[SCALE]", "about half") + " " + S("FRAME-SELFIE"),
 "THE SAME MAN exactly as in the attached reference sheet — narrow hollow-cheeked face, long jaw, deep-set pale grey eyes, long hooked nose, thick grey moustache, thin grey hair combed straight back with the scalp showing, short and wiry — unchanged in face, age and build. "
 "He sits on the tall stool at the vice end of his workbench, turned a little towards the bench, holding the phone himself at arm's length slightly above eye level, eyes on the lens, mouth closed, about to speak. "
 "Wearing his green-and-brown check flannel shirt with the sleeves rolled to the elbow under the faded navy canvas work apron, in earth tones. "
 "Behind him, THE SAME WORKSHOP as the attached location plate: the whitewashed pale grey brick, the blue cast-iron vice on the scarred beech bench just behind his shoulder, the pegboard of shears and punches, one of the tall iron-framed factory windows blowing to white, the timber roof trusses above.",
 LIGHT,
 S("SKIN-B1"),
 S("SKIN-B3").replace("[FOREHEAD-LINES]", "deep horizontal creases").replace("[AGE-FEATURES]", AGE),
 S("SKIN-B4"), S("EYES-A"),
 S("HAIR-A").replace("[HAIR-SPEC]", "thin grey hair combed straight back, the scalp showing through at the crown, a thick grey moustache"),
 S("NECK-A"), S("TEETH-A"),
 S("CAP-A"), S("CAP-FILE"),
 "AVOID: " + ", ".join([S("NEG-FRAME"), S("NEG-SKIN"), S("NEG-TEX"), S("NEG-FINISH"), S("NEG-M1"), S("NEG-LIGHT")]),
])
assert "[" not in STEP1, re.findall(r"\[[^\]]*\]", STEP1)[:5]
pathlib.Path("C1_step1_image.prompt.txt").write_text(STEP1)
print("step1", len(STEP1))

# ---- step 2: Kling voice-source takes (§36 JSON, minified, <= 2,500) — sent only after the step-1 image is confirmed
TAKES = [
 ("G1", "And if you do not believe me, I have spent thirty years making knee braces. Load is my job.", "job", "thirty years", "daring them, dry"),
 ("G2", "I have made knee braces for thirty years. I am about to talk you out of buying one.", "one", "talk you out", "a straight confession, level"),
 ("G3", "Seventeen times your bodyweight goes through one spot below your kneecap. Every step.", "step", "Seventeen", "a plain fact, said often"),
]
def take(tid, line, closure, stress, intent):
    mouth = S("MOUTH-C").replace("[CLOSURE-WORD]", closure).replace("[MOUTH-CORNER]", "right")
    mouth = mouth.replace(" Small conversational amplitude matched to the voice, teeth mostly hidden.", "").replace(" Cheeks and throat move with speech.", "").replace(" Mouth fully closed between sentences.", "")
    d = {
     "shot": f"{tid}.",
     "dialogue": line,
     "delivery": VOICE_MAKER + f" To camera, {intent}; stress on '{stress}'. " + S("AUD-A"),
     "subject": "As in the start frame.",
     "camera": {"movement": S("RIG-R2"), "framing": "SELFIE as in the start frame."},
     "motion": S("BREATH-A") + f" Eyes on lens. " + mouth + " " + S("HOLD-C"),
     "lighting": S("INHERIT-CAP"),
     "style": "As in the start frame.",
     "negatives": ", ".join([S("NEG-WARP-C"), S("NEG-CAM-TH"), "no music, no second voice"]),
    }
    return json.dumps(d, ensure_ascii=False, separators=(",", ":"))
out = {}
for t in TAKES:
    s = take(*t); out[t[0]] = s
    assert len(s) <= 2500, (t[0], len(s))
    pathlib.Path(f"C1_{t[0]}.kling.json").write_text(s)
    print(t[0], len(s), len(t[1].split()), "words")
json.dump({"VOICE_MAKER": VOICE_MAKER, "takes": out}, open("voice.json", "w"), indent=1, ensure_ascii=False)
