"""Step 7 — start-frame T2I and §35 Kling JSON for every act-map row (stryde-cascade)."""
import json, pathlib, sys
from lib import s
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "products/stryde"))
import stryde_product_sheet as P
from plates import PROPREF, shell, P1
HERE = pathlib.Path(__file__).parent; B = HERE.parent; PR = B / "prompts"
ROWS = {r["beat"]: r for r in json.loads((B / "actmap.json").read_text())}
MID = json.loads((HERE / "media_ids.json").read_text())
SIDE = "right"
def fill(t, **kw):
    for k, v in kw.items(): t = t.replace(f"[{k}]", v)
    return t
SL = P.SLOTS
PLACE = fill(P.PLACE_LOCK, SIDE=SIDE)
ORIENTC = fill(s("ORIENT-C"), **{"BAND-MATERIAL": SL["BAND_MATERIAL"], "REAR-PATH": SL["REAR_PATH"], "BAND-INNER": "two small black keeper loops on the band's outer face", "HARDWARE": SL["HARDWARE"]})
NEGPLACE = fill(s("NEG-PLACE"), LANDMARK=SL["LANDMARK"])
WARD = {
 "N": "Wearing a grey crew-neck T-shirt, a faded navy half-zip work fleece with no logo, dark charcoal work trousers, scuffed tan leather work boots, in navy and charcoal.",
 ("C1",1): "Wearing a cream blouse, a lilac lambswool cardigan buttoned up, a navy pleated skirt ending just above the knee with both knees bare, flat navy fleece-lined slippers, in lilac and navy.",
 ("C1",2): "Wearing a small-floral cream blouse, a navy cardigan, a plain grey skirt ending just above the knee with both knees bare, flat navy fleece-lined slippers, in navy and grey.",
 ("C1",3): "Wearing a white cotton nightdress, a quilted dusty-pink dressing gown tied at the waist, flat navy fleece-lined slippers, in dusty pink and white.",
 "C2": "Wearing a washed-out olive short-sleeved polo shirt, khaki cotton shorts ending just above the knee with both knees bare, white sports socks, plain grey unbranded trainers, in olive and khaki.",
}
MARK = {
 "N": "close-cropped grey hair receding at the temples, grey stubble, a nose bent at the bridge, a pale scar through the outer end of his left eyebrow, stocky",
 "C1": "short fine white curls, a small round face with soft jowls, a flat brown mole on her left cheekbone, small and round-shouldered",
 "C2": "thin white hair combed back, a white trimmed moustache, a wide ruddy face, heavyset with a round belly",
}
SHEET = {"N": "N_sheet", "C1": "C1_sheet", "C2": "C2_sheet", "N-hands": "N_sheet"}
LOCREF = {"P1-HALL": ["P1_PROP"], "P1-FRONT": ["P1_PROP", "P1_FRONT"], "C2-HALL": ["C2_HALL"], "WORK": ["WORK"], "VAN": ["VAN"], "ANAT": []}
LOCTXT = {
 "P1-HALL": PROPREF + " " + shell(P1) + " The hall and the straight flight of thirteen carpeted stairs with brass stair rods rising along the left wall, the white spindle banister with a dark varnished handrail on the open side.",
 "P1-FRONT": s("SCENE-REF").replace("[LOCATION]", "FRONT ROOM of this house").replace("[the location's named anchors, stated in one clause]", "the floral chintz armchair by the bay with its crocheted blanket, the tiled fireplace with the carriage clock, the dark wood china cabinet, the brass standard lamp, the single divan with the pale blue candlewick bedspread against the right-hand wall").replace("[where the camera now sits, what it looks across, and how that differs from the reference view]", "[CAMPOS]") + " " + PROPREF,
 "C2-HALL": s("SCENE-REF").replace("[LOCATION]", "HALL AND STAIRCASE").replace("[the location's named anchors, stated in one clause]", "the light oak treads with white risers, the white square-spindle banister with the pale pine handrail, the harbour-at-sunset print on the stair wall, the walking boots on the mat by the bottom step, the tall green plant in the white pot").replace("[where the camera now sits, what it looks across, and how that differs from the reference view]", "[CAMPOS]"),
 "WORK": s("SCENE-REF").replace("[LOCATION]", "WORKSHOP").replace("[the location's named anchors, stated in one clause]", "the pegboard of hand tools, the scarred oak workbench, the offcut handrail lengths standing in the corner, the tray of brass handrail brackets").replace("[where the camera now sits, what it looks across, and how that differs from the reference view]", "[CAMPOS]"),
 "VAN": s("SCENE-REF").replace("[LOCATION]", "VAN LOAD AREA").replace("[the location's named anchors, stated in one clause]", "the steel shelving with clear organiser boxes, the handrail lengths ratchet-strapped to the wall, the black tool bag on the floor").replace("[where the camera now sits, what it looks across, and how that differs from the reference view]", "[CAMPOS]"),
}
HEIGHT = {"ground": "from almost at floor level, the phone near the ground looking along it", "low": "from low down, the phone at knee height looking slightly up",
          "eye": "at eye level", "high": "from above, the phone held high looking down", "overhead": "from straight overhead, looking down"}
def angle_line(r):
    a = r["angle"]; subj = {"N-hands": "his hands", "none": "the scene", "product": "the strap", "anatomy": "the knee"}.get(r["subject"], "her" if r["subject"] == "C1" else "him")
    SIDEP = {"front": f"straight on to the front of {subj}", "three-quarter": f"a three-quarter angle on {subj}", "profile": f"the side, {subj} in profile",
             "three-quarter-back": f"behind {subj} at a three-quarter angle, over the shoulder", "behind": f"directly behind {subj}", "ots": f"over the shoulder of {subj}"}
    t = f"THE CAMERA ANGLE: {HEIGHT[a['height']]}, seen from {SIDEP[a['side']]}"
    if a["fg"] == "through": t += ", looking past the banister spindles, soft in the near foreground"
    return t + ". This exact angle, not a straight-on eye-level view."
PLANE = {"eyes": "the nearest eye", "hands": "the hands and what they hold", "product": "the strap and its wordmark", "foreground": "the foreground", "background": "the subject further back", "deep": "everything"}
def focus_line(r):
    f = r["focus"]; depth = "everything from near to far stays sharp" if f["dof"] == "deep" else "the room behind falls to a soft, recognisable shape"
    return f"FOCUS: {PLANE[f['plane']]} is in sharp focus; {depth}. The blur is optical: soft and round, never smeared."
SCREEN = {"L": "from the left of the frame", "R": "from the right of the frame", "front": "from the front, slightly to one side", "back": "from behind the subject, the window behind them"}
def light_line(r):
    l = r["light"]
    if r["location"] == "ANAT": return s("ANAT-LIGHT").replace("[TARGET]", SL["TARGET"])
    return (f"THE LIGHT: {l['source']} lights the scene {SCREEN[l['key_side']]}, {l['time']} daylight, {l['arc']}, "
            "so the subject has a lit side and a softer shadow side. The shadows fall away from that source, one way only.")
def person(r):
    sub = r["subject"]
    if sub in ("C1", "C2", "N"):
        w = WARD[(sub, r["story_day"])] if sub == "C1" else WARD[sub]
        return s("SUBJ-REF").replace("[two or three named markers: hair, build, one distinctive feature]", MARK[sub]) + " " + w
    if sub == "N-hands":
        return "The hands of THE SAME MAN as in the attached subject reference — square, weathered workman's hands, the cuff of his faded navy work fleece at the wrist — his face out of frame."
    return ""
def product(r):
    ps = r["product_state"]
    if ps == "worn": return " ".join([P.REF_PROD, PLACE, P.WORDMARK_LOCK, P.SIZE_WORN, P.FIT_SNUG])
    if ps == "held": return " ".join([P.REF_PROD, P.WORDMARK_LOCK, P.SIZE_HELD])
    if ps == "object": return " ".join([P.REF_PROD, P.WORDMARK_LOCK, P.SIZE_OBJECT])
    if ps == "fake": return P.FAKE_BASE + " Its soft band has stretched out of shape so the strap sags and slides down the shin."
    return ""
PAIR = {"A5-B1", "A5-P1", "A4-P3"}  # two units in frame: pair-pack carve-out (product sheet NEG_HELD_P note)
def refs(r):
    ids = []
    if r["subject"] in SHEET: ids.append(MID[SHEET[r["subject"]]])
    ids += [MID[k] for k in LOCREF[r["location"]]]
    ps = r["product_state"]
    if ps == "worn": ids += [MID["front"], MID["worn_front"]]
    elif ps in ("held", "object"): ids += [MID["front"], MID["back"]]
    if r["beat"] == "A5-P1": ids += [MID["package_open"]]
    if r["beat"] == "A4-P2": ids += [MID["macro"]]
    return ids
def t2i(r, campos, scene, extra=""):
    anat = r["location"] == "ANAT"
    if anat:
        base = fill(s("ANAT-BASE"), REGION=SL["REGION"], **{"TARGET JOINT": SL["TARGET_JOINT"]})
        parts = [base, fill(s("ANAT-A"), STACK=SL["STACK"], BONES=SL["BONES"]), scene,
                 (product(r) + " " + s("ANAT-PROD")) if r["product_state"] == "worn" else "", light_line(r), s("ANAT-FIELD")]
        neg = s("ANAT-NEG").rstrip(", ")
        if r["product_state"] == "worn": neg = neg.replace("no rigid brace, ", "")
        return "\n\n".join(p for p in parts if p) + "\n\nAVOID: " + neg
    loc = LOCTXT[r["location"]].replace("[CAMPOS]", campos)
    parts = [s("CAM-LOCK"), scene, person(r), loc, product(r), extra, angle_line(r), focus_line(r), light_line(r)]
    if r["subject"] not in ("none", "product"): parts.append(s("BODY-WHOLE"))
    if r["subject"] in ("C1", "C2", "N"): parts.append(s("MOOD-NEG") if r["act"] in ("Hook 1","Hook 2","Hook 3","Act 1","Act 3") else "")
    parts += [s("CAP-A"), s("CAP-FILE")]
    neg = [s("NEG-FILE"), s("NEG-STAGED")]
    if r["subject"] not in ("none", "product"): neg += [s("NEG-BODY")]
    if r["subject"] in ("C1", "C2", "N", "N-hands"): neg.append(s("NEG-SUBJ"))
    if r["location"] in ("P1-HALL", "P1-FRONT"): neg.append(s("NEG-PROP"))
    if r["location"] in ("P1-FRONT", "C2-HALL", "WORK", "VAN"): neg.append(s("NEG-SCENE"))
    if r["product_state"] == "worn": neg += [NEGPLACE, P.NEG_WORDMARK, P.NEG_OBSERVED]
    if r["product_state"] in ("held", "object"): neg += [P.NEG_WORDMARK, P.NEG_OBSERVED, (P.NEG_HELD_P.replace(", no second strap", "") if r["beat"] in PAIR else P.NEG_HELD_P) if r["product_state"]=="held" else ""]
    if r["product_state"] == "fake": neg.append(P.NEG_FAKE_HERO)
    if r["product_state"] == "absent": neg.append("no knee strap, no knee brace, no product")
    neg += [s("NEG-LIGHT"), s("NEG-M1"), "no logos, no brand names, no text" + ("" if "phone" in r["action"] else ", no phone in frame")]
    return "\n\n".join(p for p in parts if p) + "\n\nAVOID: " + ", ".join(n for n in neg if n)
RIGS = {"sway": s("RIG-R1")}
def kling(r, motion, subject_line):
    cam = r["camera"]
    mv = s("RIG-RVD") if r["location"] == "ANAT" else (RIGS["sway"] if cam == "sway" else s("RIG-R1").split(". One deliberate")[0] + ". " + cam.split(": ")[-1].capitalize() + ", slow and continuous, the only move in the clip. Still drifting on the final frame.")
    lay = r["layout"]["type"]
    framing = "As in the start frame" + {"split": "; the action sits in the middle band of the frame, nothing that matters in the top or bottom quarter.", "pip": "; one subject, large and centred, readable at a third of the width.", "full": "."}[lay]
    prod = ""
    if r["product_state"] in ("worn", "held", "object"):
        prod = " The strap keeps its exact shape, size and wordmark in every frame and moves only with what holds it; its rigid shell never bends, flexes or changes proportion."
    body = s("HOLD-C") + ("" if r["location"] == "ANAT" else " " + s("PHYS-MOTION-C"))
    j = {"shot": r["beat"].lower().replace("-", "_"), "subject": subject_line,
         "camera": {"movement": mv, "framing": framing},
         "motion": motion + prod + " " + body,
         "lighting": s("INHERIT-CAP") if r["location"] != "ANAT" else "Exactly as in the start frame.",
         "style": "As in the start frame.",
         "negatives": ", ".join(x for x in [s("NEG-WARP-C"), "no bending, no curling, no folding, no melting, no flipping of the product" if r["product_state"] in ("worn","held","object") else "",
                    "no strap sliding up or down the leg" if r["product_state"]=="worn" else "",
                    "no second person, no camera travelling with the subject" if r["location"]!="ANAT" else "no glow inside the joint, no glow on the kneecap, no pause, no freeze", "no music, no speech"] if x)}
    return json.dumps(j, ensure_ascii=False, separators=(",", ":"))
