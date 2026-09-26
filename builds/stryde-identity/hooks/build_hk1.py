#!/usr/bin/env python3
"""HK1 (step 6, Manual): two split-band start frames (§22T seeds) + Kling I2V JSON (§35), assembled by ID."""
import re, json, pathlib, importlib.util
ROOT = pathlib.Path(__file__).resolve().parents[3]
T = (ROOT / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S); return m.group(1).strip()
sp = importlib.util.spec_from_file_location("ps", ROOT / "products/stryde/stryde_product_sheet.py")
P = importlib.util.module_from_spec(sp); sp.loader.exec_module(P)
side = lambda s: s.replace("[SIDE]", "right").replace("[OTHER_SIDE]", "left")
NEGS = lambda *xs: ", ".join(xs)
SPLIT_T2I = ("Composed for a split screen: everything that matters — the hands, the strap and the action — sits in the middle band "
             "of the tall frame, with nothing important in the top quarter or the bottom quarter.")
PROP = dict(l.split("=", 1) for l in [])
CARRIED = ("faded magnolia walls, yellowed white gloss ogee skirting and architraves, white four-panel doors with dull brass knobs, "
           "worn beige carpet with brass stair rods")
PROP_FILL = {
 "[WALL FINISH AND COLOUR]": "slightly uneven painted plaster walls in a faded magnolia",
 "[SKIRTING — profile, height, colour]": "deep ogee-profile wooden skirting painted in yellowed white gloss",
 "[ARCHITRAVE]": "matching moulded architraves in the same yellowed gloss",
 "[INTERNAL DOOR — style, colour, handle]": "four-panel white doors with round brass knobs worn dull",
 "[CEILING]": "a plain white ceiling with a faint Artex swirl",
 "[FLOOR, AND WHAT IT CHANGES TO AT THE THRESHOLD]": "worn beige carpet on the hall and stairs held by brass stair rods",
 "[RADIATOR TYPE]": "white single-panel steel radiators",
 "[SWITCHES AND SOCKETS]": "slightly yellowed white plastic switches"}
def fill(s, d):
    for k, v in d.items(): s = s.replace(k, v)
    assert "[" not in s, s[:160]; return s

# ------------------------------------------------------------------ HK1-T  (C4, consulting room, held)
grip = "two-hand presentation: " + dict(P.HELD_GRIPS)["two-hand presentation"].split(" -- ")[0]
HK1T = "\n\n".join([
  S("CAM-LOCK"),
  "A snapshot from a phone propped against the pen pot on his desk, about sixty centimetres from him, leaning back a little and not quite level, nobody looking at its screen. "
  "A tight chest-level shot of an older man, an orthopaedic surgeon, sitting at the desk and holding the strap out towards the camera in both hands: "
  "his upper body fills the frame from just under his chin down to the desk — the frame's top edge passes across the underside of his chin and the knot of his shirt collar, "
  "so the shot is his collar, jumper, forearms and big square hands with age spots and clean short nails, with the strap held out in front of his chest. "
  "Beside his shoulder, a knee X-ray glows cool white on the lightbox on the back wall, soft and out of focus. "
  "Nothing of anyone holding the phone is in frame. " + SPLIT_T2I,
  fill(S("SUBJ-REF"), {"[two or three named markers: hair, build, one distinctive feature]":
       "tall and slightly stooped, broad square jaw, close white hair at the sides"}) + " "
  + fill(S("WARD-LINE"), {"[BASE]": "a blue-and-white fine-check button-down shirt", "[MID if present], ": "a navy v-neck jumper, ",
       "[OUTER if present], ": "", "[LOWER], ": "", "[FOOT], ": "", "[ACCENT if present]": "a steel watch on the left wrist", "[colour family]": "navy and denim blue"}),
  fill(S("SCENE-REF"), {"[LOCATION]": "CONSULTING ROOM",
       "[the location's named anchors, stated in one clause]": "the X-ray lightbox with two knee X-rays on the back wall, the tall bookshelf of worn textbooks beside it, the desk under the left-hand window, the anatomical knee model on the desk",
       "[where the camera now sits, what it looks across, and how that differs from the reference view]": "on the desk itself at chest height, looking across the desk at the surgeon with the back wall and its lightbox directly behind him, where the reference was taken from the door"}),
  P.REF_PROD + " held in a " + grip + ". " + P.SIZE_HELD + " The front face and the wordmark are square to the lens and readable; the hands are on the pad and the shell's lower edge only. Each chrome slide carries exactly three small engraved dotted chevrons stacked vertically and pointing up — no other marks, icons or symbols on the slides. His fingertips press on the pad behind the shell and his thumbs rest on the shell's lower edge near each end, well inside the chrome slides; both slides are fully visible and untouched.",
  "Light: cool daylight from the window on his left, the lightbox behind him glowing white and rimming the hands and the strap's peaks, the front of the hands a stop darker with soft sensor noise.",
  S("CAP-FILE"),
  "AVOID: " + NEGS(S("NEG-FILE"), S("NEG-NOFACE"), S("NEG-SCENE"), S("NEG-SUBJ"), S("NEG-M1"), P.NEG_HELD_P, P.NEG_OBSERVED, "no second strap, no text on screen, no readable writing on the X-rays, no mouth, no nose, no erased or cut-away head, no head fragment, no ceiling in frame, no icons or symbols on the chrome slides, no fingers on or over the chrome slides"),
])

# ------------------------------------------------------------------ HK1-B  (C1, hall stairs, worn, bent)
HK1B = "\n\n".join([
  S("CAM-LOCK"),
  "A snapshot from a phone held low by someone standing two steps below her on the stairs, very close to her right knee and pointed at it, tilted, not looking at the screen. "
  "AN EXTREME CLOSE-UP OF AN OLDER WOMAN'S RIGHT KNEE WEARING THE STRAP as she steps down the carpeted staircase at home: the knee and the strap fill the width of the frame, "
  "from just above the kneecap to the top of the shin, the knee bent mid-step as her right foot reaches down to the next stair below the bottom edge. "
  "Only the hem of her teal skirt shows at the very top edge. Her hands, the handrail and the rest of her are out of frame. "
  "Behind the knee, soft and out of focus, the worn beige stair carpet with a brass stair rod and a strip of magnolia wall. "
  + SPLIT_T2I.replace("the hands, the strap and the action", "the knee and the strap"),
  fill(S("SUBJ-REF"), {"[two or three named markers: hair, build, one distinctive feature]":
       "short and heavyset, heavy bare knees and calves, age-spotted hands"}) + " "
  + fill(S("WARD-LINE"), {"[BASE]": "a mustard-and-teal paisley blouse", "[MID if present], ": "", "[OUTER if present], ": "",
       "[LOWER]": "a teal A-line skirt ending a hand above the knee", "[FOOT]": "tartan slippers", ", [ACCENT if present]": "", "[colour family]": "a pattern-led mustard and teal"}),
  fill(S("SCENE-REF"), {"[LOCATION]": "HALL AND STAIRS",
       "[the location's named anchors, stated in one clause]": "the staircase rising on the left with its white banister and mahogany-stained handrail, worn beige carpet with brass stair rods, magnolia walls and yellowed gloss skirting",
       "[where the camera now sits, what it looks across, and how that differs from the reference view]": "low on the stairs two steps below her, looking up the flight at her knee, where the reference looks down the hall from the front door"})
  + " " + fill(S("PROP-SHELL"), PROP_FILL),
  P.REF_PROD + " " + side(P.PLACE_BENT) + " " + P.FIT_SNUG + " " + P.SIZE_WORN + " " + S("IFACE-C"),
  P.LEG_SKIN.replace("about sixty", "about seventy-four"),
  "Light: morning daylight from the front-door glass below throws a pale wash up the stair carpet and across the knee from the front and below; the wall behind falls a stop darker with soft sensor noise.",
  S("CAP-FILE"),
  "AVOID: " + NEGS(S("NEG-FILE"), S("NEG-NOFACE"), S("NEG-SCENE"), S("NEG-PROP"), S("NEG-SUBJ"), S("NEG-M1"), side(P.NEG_PLACE), P.NEG_BENT, P.NEG_ORIENT, P.NEG_OBSERVED, "no trousers, no tights, no strap over clothing, no text on screen, no hands in frame, no handrail in frame, no full leg, no feet in frame, no wide shot"),
])
out = {"HK1-T": HK1T, "HK1-B": HK1B}
for k, v in out.items():
    (pathlib.Path(__file__).parent / f"{k}.t2i.txt").write_text(v); print(k, len(v), "chars")

# ------------------------------------------------------------------ Kling I2V (§35), ≤ 2,500 chars minified
SPLIT_I2V = "split: the action stays in the middle band of the frame, nothing that matters in the top or bottom quarter"
I2V = {}
I2V["HK1-T"] = {
  "shot": "hk1_top_surgeon_presents_strap",
  "subject": S("INHERIT-SUBJ") + " The strap is held up in both of his hands; his head stays where it is at the very top edge of the frame, leaning over the strap.",
  "camera": {"movement": S("RIG-R3C"),
             "framing": "PROPPED as in the start frame, hands and strap in the middle of frame, his head staying at the top edge; " + SPLIT_I2V + "."},
  "motion": "Already holding the strap out to the lens, he turns it once, slowly, a half turn so the plain matte-black pad faces the camera, the band swinging behind; as the clip ends he starts turning it back, not yet there. " + S("HOLD-C") + " " + P.HOLD_PC + " " + S("PHYS-MOTION-C"),
  "lighting": S("INHERIT-CAP"),
  "style": "As in the start frame.",
  "negatives": NEGS(S("NEG-WARP-C"), "no shell bending, no peaks becoming uneven, no wordmark changing, no second strap, no hand gripping the band, no fingers across the wordmark, no head moving down into the middle of frame, no face turning to camera, no text on screen, no music"),
}
I2V["HK1-B"] = {
  "shot": "hk1_bottom_knee_steps_down",
  "subject": S("INHERIT-SUBJ") + " " + fill(S("PLACE-LOCK"), {"[SIDE] [REGION]": "right knee",
       "[ITS CONTACT RELATIONSHIP TO [LANDMARK] — the geometry that sets its height, stated as contact rather than as a measurement]": "its notch cups the kneecap's lower border, no gap, the equal peaks flanking it",
       "[LANDMARK]": "The kneecap"}) + " " + P.ORIENT_C.split(" Only the black")[0],
  "camera": {"movement": S("RIG-R1C") + " Eases back and up to show her hand on the rail.",
             "framing": "OTS as in the start frame; split: knee and strap in the middle band, nothing in the top or bottom quarter."},
  "motion": "Mid-step, her right foot lands on the next stair, the knee taking her weight; her hand slides down the rail; her other foot starts to lift at the cut. " + S("IFACE-C") + " " + S("HOLD-C") + " " + P.HOLD_PC,
  "lighting": S("INHERIT-CAP"),
  "style": "As in the start frame.",
  "negatives": NEGS(S("NEG-WARP-C"), "no strap sliding, no face, no stumble, no text, no music"),
}
for k, v in I2V.items():
    s = json.dumps(v, ensure_ascii=False, separators=(",", ":"))
    (pathlib.Path(__file__).parent / f"{k}.i2v.json").write_text(s); print(k, "i2v", len(s), "chars")
