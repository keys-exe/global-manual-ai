#!/usr/bin/env python3
"""Step 6 hook frames (step-1 images) for down-forwards-again — §22T candid seed order with §30I ANGLE-LINE, §30J FOCUS-LINE,
§30K LIGHT-SHOT, §27G start frame caught in the action, §9D concealed. Appendix A strings by ID (never retyped).
Order: CAM-LOCK → ANGLE-LINE → FOCUS-LINE → PROP-REF/room → SEED-CANDID prose → LIGHT-SHOT → (SKIN-T → CAP-SHARP on MCU faces) → CAP-FILE → AVOID."""
import re, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[3]
T = (ROOT / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()
def pick(i, *keep):  # selected clauses of a negative list, verbatim
    cl = [c.strip() for c in S(i).split(",")]
    out = [c for c in cl if any(k in c for k in keep)]
    assert len(out) >= len(keep), (i, keep, out); return ", ".join(out)

HEIGHT = {"low": "the lens at hip height, looking up at the subject", "eye": "the lens at the subject's eye height, level",
          "high": "the lens above head height, looking down at the subject"}
def angle(h, side, subj, fg=None):
    s = S("ANGLE-LINE").replace("[HEIGHT CLAUSE from §30I]", HEIGHT[h]).replace("[SIDE]", side).replace("[SUBJECT]", subj)
    s = s.replace("[, looking past FOREGROUND, soft in the near foreground | , seen in REFLECTION]", fg or "")
    assert "[" not in s, s; return s
def focus(plane, depth):
    s = S("FOCUS-LINE")
    s = re.sub(r"\[PLANE[^\]]*\]", plane, s); s = re.sub(r"\[DEPTH[^\]]*\]", depth, s)
    assert "[" not in s, s; return s
def light(src, subj, side, quality, lit_side, face=True):
    s = S("LIGHT-SHOT")
    if not face:  # no face in frame: the face/catchlight clause would invite one
        s = s.replace("so the face has a lit side toward [SIDE] and a softer shadow side, with a small catchlight in the eyes", "so it has a lit side toward [SIDE] and a softer shadow side")
    s = s.replace("[SOURCE from the light plan — the window on the room's WALL, or the named practical]", src)
    s = s.replace("[SUBJECT]", subj).replace("[SCREEN SIDE]", side).replace("[TIME-OF-DAY QUALITY and the act's light state]", quality)
    s = s.replace("toward [SIDE]", "toward " + lit_side)
    assert "[" not in s, s; return s

CARRIED = ("magnolia walls over a dark-stained dado rail with cream anaglypta below, tall white-gloss Victorian skirting, "
           "stripped pine four-panel doors with brass knobs, the burgundy-and-cream patterned runner")
PROPREF = S("PROP-REF").replace("[THE CARRIED FINISHES, NAMED IN ONE CLAUSE]", CARRIED)
P_FACE = ("THE SAME WOMAN exactly as in the attached reference sheet — a white British woman of sixty-nine, short and petite with a slight stoop, "
          "a small fine-boned oval face, pale grey-blue eyes, a small straight nose, a thin upper lip with a small mole above its right corner, "
          "chin-length layered hair dyed chestnut brown with silver roots at the parting, tucked behind the ears — unchanged in face, age and build; "
          "only her clothes are different today.")
D_FACE = ("THE SAME MAN exactly as in the attached reference sheet — a white British man of fifty-four, broad square face, light blue-grey eyes set wide apart, "
          "a short snub nose, fair ruddy freckled skin, short sandy-red hair going grey at the sides with a left side parting, clean-shaven, "
          "a small flat brown mole high on his right cheekbone, stocky and broad through the chest — unchanged in face, age and build.")
D_WARD = ("Dressed as a doctor at work, as in the attached photograph of him at his desk: a crisp white knee-length doctor's coat worn on and open over a pale blue "
          "button-down shirt with the top button undone and no tie, a black stethoscope round his neck over the coat collar, a plain steel watch.")
NEG_BASE = lambda: [pick("NEG-M1", "no AI face", "no plastic skin", "no extra fingers", "no fused fingers", "no melted hands",
                         "no CGI look", "no fake commercial gloss", "no moody dark grade"),
                    pick("NEG-LIGHT", "no glowing skin", "no shadows falling in two directions", "no lens flare")]
NOTEXT = "no readable text, logos, brand names or labels anywhere"

B = {}
# HK1-01a — P-D2, the hall, coming DOWN one stair facing forwards; low · front · FULL · clean; deep; key R 5600K; worn CONCEALED
B["HK1-01a"] = dict(model="nano_banana_2", refs=["P-PATIENT", "P0-PROP-P v2"], body=[S("CAM-LOCK"),
  angle("low", "the front", "the woman on the stairs"),
  focus("everything", "everything from near to far stays sharp"),
  PROPREF + " The hall and the wide straight staircase of the attached property photograph: the stairs rise away along the left-hand wall, the dark turned banister and handrail on the open right side, the patterned runner held by brass rods on every tread.",
  "A snapshot from a phone held at hip height by someone standing on the hall floor a couple of metres back from the foot of the stairs, not looking at the screen, tilted a touch. "
  + P_FACE + " Today she wears a white cotton shirt with the sleeves turned back, an open coral lightweight cardigan, wide-leg navy linen trousers down to the ankle, and tan leather flat loafers; small gold hoop earrings. "
  "She is coming down her own stairs FACING FORWARDS, four steps from the bottom, caught in the middle of one ordinary step: her weight on her right foot on the upper tread, her left foot already in the air and lowering towards the next tread down, "
  "her right hand resting lightly on the banister rail, not gripping, her left arm loose at her side. Her eyes are on the tread below, her face calm and easy, mouth shut. "
  "The trousers hang straight and loose from the hip and crease softly at the knees as linen does, both legs reading as ordinary covered legs. "
  "Her whole body from hair to shoes is in frame with clear stairs above her and the hall floor in front of her.",
  light("The front-door glass on the room's east wall, behind the phone", "her", "right", "bright morning sun, the warmer after-light of the house, a warm patch of sun lying across the lower stairs", "the right"),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([S("NEG-CONCEAL"), *NEG_BASE(), "no walking backwards, no both hands on the rail, no clutching the banister, no pain on her face, no stick, "
                         "no skirt, no cardigan buttoned, no bare knees, no trousers rolled up, no feet cut off, no second person", NOTEXT])])

# HK1-02a — P-D1 hand, kitchen dresser drawer overfull of braces; high · front · CU · clean; hands; key R 6500K; product absent
B["HK1-02a"] = dict(model="nano_banana_2", refs=["P2-P-KITCHEN v2", "P-PATIENT"], body=[S("CAM-LOCK"),
  angle("high", "the front", "the open dresser drawer and her hand"),
  focus("the hands and what they hold", "the room behind falls to a soft, recognisable shape"),
  PROPREF + " The kitchen of the attached kitchen photograph: the old pine Welsh dresser beside the pine table, its top drawer pulled half open.",
  "A snapshot from a phone held above the drawer by someone standing beside the dresser, looking down into it, not looking at the screen. "
  "In the drawer, crammed so full the pile rises above the drawer's sides: old knee supports tangled together — a black stretchy sleeve, a beige wrap with loose velcro tabs, a grey neoprene sleeve, a white tubular bandage, "
  "all worn, blank and plain, no brand, no writing. Her right hand — the hand of a woman of sixty-nine, thin skin, soft lines across the knuckles, a plain gold wedding band, short unpainted nails, "
  "the cuff of an oatmeal cable-knit cardigan over a cream roll-neck at the wrist — is caught in the middle of pushing one more grey hinged knee brace with metal side bars down onto the top of the pile: "
  "the brace half in the drawer, its end still above the drawer's front edge, her palm flat on it pressing down, all five fingers whole and visible. "
  "The drawer, the pile and the whole hand sit in the middle of the frame with a clear margin of dresser wood all round.",
  light("The window over the sink on the room's west wall", "the drawer and her hand", "right", "flat overcast daylight, the grey, cooler light of the problem days", "the right", face=False),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([*NEG_BASE(), "no face, no strap product, no small padded strap, no knee strap with a silicone pad, no new or packaged supports, no hand cut off at the frame edge, "
                         "no more than one hand, no drawer closed, no tidy folded pile", NOTEXT])])

# HK2-02a — D-D1 hand, the prescription pad slid away across the desk; high · three-quarter · CU · clean; hands; key L 6500K
B["HK2-02a"] = dict(model="nano_banana_2", refs=["P3-D-CONSULT", "D-VOICE-IMG v2"], body=[S("CAM-LOCK"),
  angle("high", "a three-quarter angle", "his hand and the pad on the desk"),
  focus("the hands and what they hold", "the room behind falls to a soft, recognisable shape"),
  "IN THE SAME ROOM as the attached consulting-room photograph: the light-wood desk, the closed laptop to one side, the white plastic knee model, the pale grey wall soft behind.",
  "A snapshot from a phone held at his shoulder by someone standing beside his chair on his side of the desk, looking down at the desktop, not looking at the screen. "
  "On the desk a small plain white prescription pad, blank, nothing written or printed on it, a cheap blue biro lying beside it. "
  "The doctor's right hand — a stocky man's hand of fifty-four, fair freckled skin with reddish hairs on the back, short clean nails, the plain steel watch on the wrist, "
  "the white cuff of his doctor's coat over the pale blue shirt cuff — is caught in the middle of sliding the pad away from himself across the desk, fingers flat on top of it, "
  "the pad already a hand's width from where it lay, clear desk ahead of it for it to travel. The whole hand and the pad sit well inside the frame.",
  light("The consulting-room window on the room's north wall", "the desk and his hand", "left", "steady overcast daylight", "the left", face=False),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([*NEG_BASE(), "no face, no writing on the pad, no printed form, no pharmacy logo, no pills, no pen in the hand, no hand cut off at the frame edge, "
                         "no second hand on the pad, no bare forearm, no coat missing", NOTEXT])])

# HK3-01a — D-D1 standing at the window, knee X-ray held up to the light; eye · profile · MCU · through; key back 6500K
B["HK3-01a"] = dict(model="nano_banana_2", refs=["D-DOC v2", "D-VOICE-IMG v2", "P3-D-CONSULT"], body=[S("CAM-LOCK"),
  angle("eye", "the side, in profile,", "the doctor", ", looking past the edge of the open vertical blinds, soft in the near foreground"),
  focus("the X-ray film he holds", "the room behind falls to a soft, recognisable shape"),
  "IN THE SAME ROOM as the attached consulting-room photograph, at its tall window on the left with the white vertical blinds open.",
  "A snapshot from a phone held at eye height by someone standing just inside the window bay, not looking at the screen. " + D_FACE + " " + D_WARD + " "
  "He stands side-on to the phone, facing the window, holding a grey-and-black knee X-ray film up against the daylight at arm's length in both hands by its top corners, "
  "reading it: the pale bones of one knee show through the film, the thin dark gap in the joint, grey soft shadow around it. "
  "His head is tipped a few degrees to one side as he reads, his eyes on the film, brow at rest, mouth shut. "
  "The film is caught mid-tilt, one corner a little lower than the other. Head, shoulders, both hands and the whole film are in frame, with space above the film.",
  light("The consulting-room window, in front of him", "the film and the side of his face", "left", "steady overcast daylight coming through the film", "the window"),
  S("SKIN-T").replace("[AGE-FEATURES]", "faded freckles and fine sun damage"),
  S("CAP-SHARP"),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([S("NEG-FILE"), *NEG_BASE(), "no lightbox, no glowing screen, no X-ray of a hand or chest, no writing or labels on the film, no coat missing, "
                         "no stethoscope missing, no looking at the camera, no smiling", NOTEXT])])

REF = {"P-PATIENT": "02333782-0c9a-4696-b3f1-fcc7480fe8db", "P0-PROP-P v2": "176c5c39-ac17-46c4-9e9b-2c06735dc0c8",
       "P2-P-KITCHEN v2": "abc2c220-b0f0-43d2-b583-d22b5696225b", "P3-D-CONSULT": "757817ea-6840-487c-879c-1b0310e137b2",
       "D-DOC v2": "71b20c5a-f8ef-48d8-8645-f5685a4a92b6", "D-VOICE-IMG v2": "b17f293d-306f-406c-b145-029402a1c074"}
out = {}
here = pathlib.Path(__file__).parent
for k, b in B.items():
    txt = "\n\n".join(b["body"]); assert "[" not in txt, k
    out[k] = dict(model=b["model"], refs=b["refs"], ref_jobs=[REF[r] for r in b["refs"]], chars=len(txt), prompt=txt)
    (here / f"{k}.image.prompt.txt").write_text(txt); print(f"{k:8s} {len(txt):5d}  refs: {', '.join(b['refs'])}")
json.dump(out, open(here / "hooks.json", "w"), indent=1)
