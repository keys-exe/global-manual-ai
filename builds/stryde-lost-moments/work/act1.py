#!/usr/bin/env python3
"""stryde-lost-moments — Act 1 (shared B-roll) T2I prompts, assembled from Appendix A and the Product Sheet by ID.

Same order as beats.py (§30E / §30I–§30K): CAM-LOCK → ANGLE-LINE → FOCUS-LINE → SCENE-REF (plated locations) → subject
→ the beat's frame caught mid-action (§27G rule 4) → wardrobe → product strings → LIGHT-SHOT → BROLL-REAL → PHYS-FRAME-C
→ CAP-A → CAP-FILE → AVOID. The two mechanism beats run the §12A anatomical register (ANAT-*), not the capture stack.
One-off B-roll people (G-01…G-10) are cast here with the beat (§13, VN01: about half the people on screen Black).
Usage: act1.py [BEAT …] → work/prompts/<beat>.t2i.txt + <beat>.refs.json
"""
import json, sys, pathlib
from beats import S, PS, ROWS, SIDE, angle_line, focus_line, light_line, HERE

PLATE = json.load(open(HERE.parent / "plates/jobs.json"))
C6 = dict(job="4d32b455-fed9-47eb-a620-40a7cb1cbb1f",
          markers="a chin-length auburn bob gone grey at the roots, an oval face with a strong Roman nose, hazel eyes")
PROD = [("front.webp", "20bc8be5-8526-48b6-a6e0-acbcb17b7c56"), ("worn_front.jpg", "2290ef3b-75a4-4c39-8ea2-b9c4b60e6637")]
PLACEMENT = ("placement reference (user)", "245be41b-3d1a-4f2d-b86a-2bd65f941f62")
BACK = ("back.webp", "c1a2247e-ab40-4eef-ab91-74b9bb0d2c3e")
PACK_OPEN = ("package open (locked V7.49.27)", "a9409405-2d78-4802-bdf0-01c7266b18a1")
CONSULT = "the pale grey consulting room with the desk under the blind window, the anatomical knee model and the X-ray light box on the wall"
KITCHEN = "the family kitchen with the honey oak table, the painted dresser with its drawers, and the sink under the window"
PARK = "the tarmac park path with its fork and wooden waymarker, mown grass either side and the line of plane trees"

G = {  # one-off B-roll people (§13) — cast with the beat
 "G-01": "a Black British woman of about sixty-five — only her hand and forearm in frame: dark brown skin, a plain gold wedding band, short unpolished nails, the cuff of a mustard cardigan",
 "G-02": "a white British man of about seventy — only his right leg from mid-thigh to foot in frame: pale freckled skin with grey leg hair, khaki cotton shorts above the knee, grey walking socks and brown leather trainers",
 "G-03": "a Black British woman of about sixty-six — only her lap, right knee and hand in frame: deep brown skin, a navy cotton dress ending above the knee, a silver ring on her middle finger",
 "G-04": "a British South Asian woman of about sixty-two — only her legs from the knees down in frame: light brown skin, a plum-coloured cotton skirt ending just above the knee, white canvas trainers",
 "G-05": "a Black British man of about seventy-two, round-faced with a close grey beard and wire-rimmed glasses, in a pale blue check shirt with the sleeves rolled",
 "G-06": "a white British man of about sixty-eight — only his hands, right knee and shin in frame: ruddy skin with grey leg hair, grey jersey shorts above the knee",
 "G-07": "a Black British woman of about seventy, slim, with short grey natural hair, reading glasses pushed up, in a yellow short-sleeve blouse and a denim skirt ending above the knee",
 "G-09": "a Black British man of about sixty-seven — only his right leg from the hip down in frame: stone-coloured chinos, brown suede shoes",
 "G-10": "four friends in their sixties and seventies walking side by side — nearest the lens a Black British woman in a green fleece and navy shorts above the knee, then a white British man in a grey sweatshirt and shorts, a Black British man in a navy quarter-zip and walking trousers, a white British woman in a red jacket and cropped trousers",
}
LIVE = "Real unretouched skin with visible pores, creases at the knuckles and knees, faint dry patches on the shins."

def place(extra=""):
    return (PS.REF_PROD + " a single unit. The strap sits EXACTLY as in the placement reference: snug on the patellar tendon directly under the "
            "kneecap, the concave notch hugging the lower edge of the kneecap with no gap, the two peaks rising either side of the base of the "
            "kneecap, the kneecap itself fully uncovered, the brushed-chrome slide with its three chevrons at the outer end, the black knit band "
            "wrapping round the back of the calf, on the RIGHT leg only." + extra)

def tail(r, subject, quality, neg):
    return [light_line(r, subject, quality), S("BROLL-REAL"), S("PHYS-FRAME-C"), S("CAP-A"), S("CAP-FILE"),
            "AVOID: " + ", ".join([S("NEG-LIGHT"), S("NEG-M1"), S("NEG-FILE")] + neg)]

PRODNEG = [PS.NEG_WORDMARK, "no gap between the strap and the kneecap, no strap low on the shin, no strap over the kneecap, no flat pad, "
           "no sleeve, no wrap, no strap on the left knee, no second strap, no hands on the strap"]
AFTER = [S("NEG-SUPPORT"), S("NEG-EFFORT")]
B = {}

def sh01():
    r = ROWS["SH-01"]
    return dict(model="nano_banana_pro", face="FACE", refs=[("C6 sheet", C6["job"]), ("P8-CONSULT plate", PLATE["P8-CONSULT"])] + PROD[:1], body=[
     S("CAM-LOCK"), angle_line(r, "her"), focus_line(r, "the surgeon"),
     S("SCENE-REF").replace("[LOCATION]", "CONSULTING ROOM").replace("[the location's named anchors, stated in one clause]", CONSULT)
       .replace("[where the camera now sits, what it looks across, and how that differs from the reference view]", "the camera sits in the patient's chair across the desk at her eye height, three-quarter on to her, the blind window behind her right shoulder"),
     S("SUBJ-REF").replace("[two or three named markers: hair, build, one distinctive feature]", C6["markers"]),
     S("FACE-SEED").replace("[the character's named markers]", "the Roman nose, the hazel eyes and the greying auburn bob"),
     "Medium close-up at her desk: she holds the knee strap still at chest height in both hands, fingers on the shell's edges, the anatomical knee model on the desk beside her. "
     "Caught as she lifts her eyes from the strap to the patient across the desk — calm, sure, a small professional warmth. " + PS.REF_PROD + " a single unit, held with the shell face and wordmark toward the camera.",
     PS.WORDMARK_LOCK, PS.SIZE_HELD, "Wearing navy surgical scrubs.", S("SKIN-B1")] + tail(r, "her", "even afternoon daylight through the blind — authority, clear and calm",
     [S("NEG-SUBJ"), S("NEG-SCENE"), PS.NEG_WORDMARK, PS.NEG_HELD_P, "no white coat, no stethoscope, no second person in focus, no readable text on the X-rays"]))
B["SH-01"] = sh01

def sh02():
    r = ROWS["SH-02"]
    return dict(model="nano_banana_2", face="NOFACE", refs=[("P9-KITCHEN plate", PLATE["P9-KITCHEN"])], body=[
     S("CAM-LOCK"), angle_line(r, "the open drawer"), focus_line(r, "her"),
     S("SCENE-REF").replace("[LOCATION]", "KITCHEN").replace("[the location's named anchors, stated in one clause]", KITCHEN)
       .replace("[where the camera now sits, what it looks across, and how that differs from the reference view]", "the camera is above and beside the dresser looking down into its open top drawer, the oak table soft behind"),
     "Close-up looking down into an open wooden dresser drawer: a grey knitted knee sleeve and a black hinged knee brace with metal side hinges and velcro straps lie tangled together among tea towels. "
     "A woman's hand is caught mid-push on the drawer front, the drawer already sliding shut on them. Her hand: " + G["G-01"] + ".", LIVE]
     + tail(r, "the drawer and her hand", "cool morning daylight from the sink window — everyday, plain",
     ["no strap, no stryde product anywhere, no black shell with peaks, no readable brand names, no face in frame, no second hand"]))
B["SH-02"] = sh02

def sh03():
    r = ROWS["SH-03"]
    return dict(model="nano_banana_2", face="NOFACE", refs=[("P8-CONSULT plate", PLATE["P8-CONSULT"]), ("C6 sheet", C6["job"])], body=[
     S("CAM-LOCK"), angle_line(r, "the knee model"), focus_line(r, "the surgeon"),
     S("SCENE-REF").replace("[LOCATION]", "CONSULTING ROOM").replace("[the location's named anchors, stated in one clause]", CONSULT)
       .replace("[where the camera now sits, what it looks across, and how that differs from the reference view]", "the camera is low at desk height beside the knee model, looking along the desk, the room a soft blur behind"),
     "Close-up of the life-size anatomical knee model on the desk — ivory bones, red ligaments, the kneecap and the tendon below it — seen side-on. "
     "The surgeon's fingertip is caught mid-trace along the joint line of the model, moving slowly. Only her hand and the cuff of her navy scrubs are in frame: fair skin, short clean nails, no rings.",
     "Real unretouched skin on the hand, fine lines at the knuckles."] + tail(r, "the model and her hand", "even afternoon daylight — authority, clear",
     ["no strap, no product, no face in frame, no labels on the model, no readable text"]))
B["SH-03"] = sh03

def sh04a():
    r = ROWS["SH-04a"]
    return dict(model="nano_banana_pro", face="NOFACE", refs=[PLACEMENT] + PROD, body=[
     S("CAM-LOCK"), angle_line(r, "his right knee"), focus_line(r, "him"),
     "A back garden: three low York-stone steps up to a lawn, a terracotta pot of lavender at the side, afternoon sun.",
     "Extreme close-up from the side at step height: his right leg caught mid-step as he steps up onto the next stone step, foot planted, weight already coming onto the right leg, knee bending under it. " + G["G-02"] + ".",
     place(), PS.PLACE_PROFILE, PS.WORDMARK_LOCK, PS.SIZE_WORN, S("AFTER-EASE"), LIVE]
     + tail(r, "his knee", "warm afternoon sun — after, bright and open", PRODNEG + AFTER + ["no face in frame, no stumble, no slipping foot"]))
B["SH-04a"] = sh04a

def sh04b():
    r = ROWS["SH-04b"]
    return dict(model="nano_banana_pro", face="NOFACE", refs=[PLACEMENT] + PROD, body=[
     S("CAM-LOCK"), angle_line(r, "her right knee"), focus_line(r, "her"),
     "A sunny living room: she sits on a cream sofa, a patterned cushion beside her, a window bright to the right.",
     "Close-up looking down at her right knee as she sees it: her fingertips caught mid-slide along the skin just BELOW the strap's lower edge, touching skin only, never the strap. "
     "The skin at the strap's edge is smooth and unmarked — no redness, no rubbing, no indent. " + G["G-03"] + ".",
     place(), PS.WORDMARK_LOCK, PS.SIZE_WORN, LIVE]
     + tail(r, "her knee and hand", "warm afternoon light through the window — after, soft and warm",
     [PS.NEG_WORDMARK, "no redness, no sores, no rash, no marks on the skin, no fingers on the strap, no strap low on the shin, no strap over the kneecap, no strap on the left knee, no second strap, no face in frame"]))
B["SH-04b"] = sh04b

def sh04c():
    r = ROWS["SH-04c"]
    return dict(model="nano_banana_pro", face="NOFACE", refs=[("P2-PARK plate", PLATE["P2-PARK"]), PLACEMENT] + PROD, body=[
     S("CAM-LOCK"), angle_line(r, "her legs"), focus_line(r, "her"),
     S("SCENE-REF").replace("[LOCATION]", "PARK").replace("[the location's named anchors, stated in one clause]", PARK)
       .replace("[where the camera now sits, what it looks across, and how that differs from the reference view]", "the camera sits on the path itself a few centimetres off the tarmac, looking up the path at her legs walking toward it, the trees soft behind"),
     "Knee-and-shin only, walking toward the lens along the path, caught mid-stride: her left foot planted, her right foot swinging forward, heel about to land, the strap riding exactly in place on the moving knee. " + G["G-04"] + ".",
     place(), PS.WORDMARK_LOCK, PS.SIZE_WORN, S("AFTER-EASE"), LIVE]
     + tail(r, "her legs", "warm afternoon sun — after, bright and open", PRODNEG + [S("NEG-EFFORT"), "no face in frame, no strap slipping, no strap rolled down"]))
B["SH-04c"] = sh04c

def sh05():
    r = ROWS["SH-05"]
    return dict(model="nano_banana_pro", face="NOFACE", refs=[PACK_OPEN, ("P9-KITCHEN plate", PLATE["P9-KITCHEN"])] + PROD[:1], body=[
     S("CAM-LOCK"), angle_line(r, "the table"), focus_line(r, "the box"),
     S("SCENE-REF").replace("[LOCATION]", "KITCHEN").replace("[the location's named anchors, stated in one clause]", KITCHEN)
       .replace("[where the camera now sits, what it looks across, and how that differs from the reference view]", "the camera is directly above the oak table looking straight down at it"),
     "Overhead on the honey oak table: his two hands are caught lifting the lid off the box, the lid already raised clear at one edge and tilting away. Inside, exactly as in the attached open-package reference: "
     + PS.PACKAGE_LOCK + " His hands: " + G["G-05"].split(",")[0] + " — dark brown skin, a steel watch on the left wrist.",
     "A mug of tea and a folded newspaper at the edge of the table."]
     + tail(r, "the table", "bright morning daylight from the sink window — the offer, clean and bright",
     [PS.NEG_PACKAGE, "no third strap, no single strap, no offer text, no price, no face in frame"]))
B["SH-05"] = sh05

def sh06():
    r = ROWS["SH-06"]
    return dict(model="nano_banana_pro", face="FACE", refs=[PACK_OPEN, ("P9-KITCHEN plate", PLATE["P9-KITCHEN"])], body=[
     S("CAM-LOCK"), angle_line(r, "him"), focus_line(r, "him"),
     S("SCENE-REF").replace("[LOCATION]", "KITCHEN").replace("[the location's named anchors, stated in one clause]", KITCHEN)
       .replace("[where the camera now sits, what it looks across, and how that differs from the reference view]", "the camera is at his eye height across the corner of the oak table, three-quarter on to him, the dresser behind"),
     "Medium close-up at the kitchen table: " + G["G-05"] + ". The open box sits on the table in front of him, two straps in their wells exactly as in the attached open-package reference. "
     "He is caught lowering his mug of tea to the table, looking at the straps with a quiet, satisfied half-smile.", S("SKIN-B1"), S("NEG-DEFAULT-FACE")]
     + tail(r, "him", "bright morning daylight from the sink window — the offer, clean and bright",
     [PS.NEG_PACKAGE, "no third strap, no offer text, no price, no second person"]))
B["SH-06"] = sh06

def anat_slots(s):
    for k, v in PS.SLOTS.items():
        if isinstance(v, str): s = s.replace("[" + k.replace("_", " ") + "]", v).replace("[" + k + "]", v)
    return s

def mech01():
    r = ROWS["MECH-01"]
    return dict(model="nano_banana_2", face="NOFACE", refs=[], body=[
     anat_slots(S("ANAT-LAT")), anat_slots(S("ANAT-A")),
     anat_slots(S("ANAT-HOT")), PS.ANAT_A_POINT_TIGHT,
     "Load arriving down the leg from the hip: the femur driving down onto the kneecap and the tendon beneath it; the warm ember sits in one small spot on the patellar tendon just below the kneecap.",
     "AVOID: " + ", ".join([anat_slots(S("ANAT-NEG")), anat_slots(S("NEG-EXTERNAL")), "no product, no strap, no calm resting structure, no cold unlit target, no glow covering the whole limb, no emission on the bone shafts"])])
B["MECH-01"] = mech01

def mech02():
    r = ROWS["MECH-02"]
    return dict(model="nano_banana_2", face="NOFACE", refs=PROD, body=[
     anat_slots(S("ANAT-BASE")), anat_slots(S("ANAT-LIGHT")), S("ANAT-FIELD"), anat_slots(S("ANAT-A")),
     "STATE — ALREADY SEATED AND ALREADY WORKING. " + PS.REF_PROD + " a single unit, " + PS.fill(PS.PLACE_LOCK, side=SIDE),
     S("ANAT-PROD"),
     "A load already descending through the femur; the rigid shell meets it first, its edges catching a cool bright tone, the band stretched along the line of force. Beneath it the patellar tendon is quiet — only a faint, dim warmth left at the spot below the kneecap.",
     PS.WORDMARK_LOCK,
     "AVOID: " + ", ".join([anat_slots(S("ANAT-NEG")), anat_slots(S("NEG-EXTERNAL")), S("NEG-PROT"), PS.NEG_WORDMARK, "no strap on the left knee"])])
B["MECH-02"] = mech02

def ns03a():
    r = ROWS["NS-03a"]
    seat = (PS.fill(PS.SEAT_LOCK, side=SIDE)
            .replace("sitting clearly off-position at mid-shin, well below the knee, on a straight leg.", "caught a few centimetres below its final place and still travelling up, the leg bent.")
            .replace("Fingers are just beginning to lift away at the cut, still in contact, the movement unfinished.", "Both hands are on the shell's edges mid-slide, the movement unfinished."))
    return dict(model="nano_banana_pro", face="NOFACE", refs=[PLACEMENT] + PROD, body=[
     S("CAM-LOCK"), angle_line(r, "his right knee"), focus_line(r, "him"),
     "A bright bedroom in the morning: he sits on the edge of a made bed with a white duvet, a bedside table with a lamp, bare floorboards and a rag rug.",
     "Close-up looking down at his right knee as he sees it: both hands slide the closed strap up his shin toward its place under the kneecap. " + PS.REF_PROD + " a single unit. " + seat + " " + G["G-06"] + ".",
     PS.WORDMARK_LOCK, PS.SIZE_WORN, LIVE]
     + tail(r, "his knee and hands", "fresh morning daylight from the window — after, clean",
     [PS.fill(PS.NEG_SEAT, side=SIDE), PS.NEG_WORDMARK, PS.NEG_ADJUST, "no strap on the left knee, no second strap, no face in frame"]))
B["NS-03a"] = ns03a

def ns03b():
    r = ROWS["NS-03b"]
    return dict(model="nano_banana_pro", face="NOFACE", refs=[BACK] + PROD[:1], body=[
     S("CAM-LOCK"), angle_line(r, "the strap"), focus_line(r, "his hands"),
     "The same bright bedroom, the white duvet soft behind.",
     "Close-up: his two hands hold the strap up in front of the lens and are caught mid-tilt as they turn it toward the camera. " + PS.PAD_BACK_SHOT + " " + PS.INNER_PAD
     + " His hands hold it by the shell's edges, never on the band or the slides. His hands: ruddy white skin, grey hairs on the wrists, a plain steel watch.",
     "Real unretouched skin on the hands, creased knuckles."]
     + tail(r, "the strap and hands", "fresh morning daylight from the window — after, clean",
     [PS.NEG_HELD_P, "no wordmark on the pad side, no texture on the pad, no second colour on the pad, no second strap, no face in frame"]))
B["NS-03b"] = ns03b

def ns04b():
    r = ROWS["NS-04b"]
    return dict(model="nano_banana_pro", face="FACE", refs=[PLACEMENT] + PROD, body=[
     S("CAM-LOCK"), angle_line(r, "her"), focus_line(r, "her"),
     "A small back garden in summer: a slatted wooden table and chair on a patio, pots of geraniums, a honeysuckle fence behind.",
     "Medium shot: " + G["G-07"] + ", sitting at the garden table doing the newspaper crossword, her right leg crossed forward so the knee sits clear of the table edge in the lower part of the frame. "
     "She is caught mid-word, pen moving, entirely absorbed — she has forgotten the strap is there.",
     place(), PS.PLACE_BENT, PS.WORDMARK_LOCK, PS.SIZE_WORN, S("SKIN-B1"), S("NEG-DEFAULT-FACE")]
     + tail(r, "her", "warm afternoon sun — after, bright and relaxed", PRODNEG + ["no looking at the knee, no hand on the knee, no readable crossword text"]))
B["NS-04b"] = ns04b

def ns05():
    r = ROWS["NS-05"]
    return dict(model="nano_banana_pro", face="FACE", refs=[("C6 sheet", C6["job"]), ("P8-CONSULT plate", PLATE["P8-CONSULT"])] + PROD[:1], body=[
     S("CAM-LOCK"), angle_line(r, "her").replace("the near shoulder", "the patient's near shoulder"), focus_line(r, "the surgeon"),
     S("SCENE-REF").replace("[LOCATION]", "CONSULTING ROOM").replace("[the location's named anchors, stated in one clause]", CONSULT)
       .replace("[where the camera now sits, what it looks across, and how that differs from the reference view]", "the camera is behind the patient's chair, over the patient's shoulder, looking across the desk at her"),
     S("SUBJ-REF").replace("[two or three named markers: hair, build, one distinctive feature]", C6["markers"]),
     S("FACE-SEED").replace("[the character's named markers]", "the Roman nose, the hazel eyes and the greying auburn bob"),
     "Medium close-up over the patient's shoulder (the patient soft and out of focus in the near foreground, only a shoulder and the back of a grey head): the surgeon is caught mid-pass, handing the strap across the desk, her hand holding it by the shell's edge, the patient's hand just reaching to take it. She meets the patient's eye with a reassuring nod. "
     + PS.REF_PROD + " a single unit, the wordmark toward the camera.", PS.WORDMARK_LOCK, PS.SIZE_HELD, "Wearing navy surgical scrubs.", S("SKIN-B1")]
     + tail(r, "her", "even afternoon daylight through the blind — authority, clear and calm",
     [S("NEG-SUBJ"), S("NEG-SCENE"), PS.NEG_WORDMARK, PS.NEG_HELD_P, "no white coat, no stethoscope, no readable text on the X-rays"]))
B["NS-05"] = ns05

def ns06():
    r = ROWS["NS-06"]
    return dict(model="nano_banana_pro", face="NOFACE", refs=[PLACEMENT] + PROD, body=[
     S("CAM-LOCK"), angle_line(r, "his right leg"), focus_line(r, "him"),
     "A narrow hallway in the morning: a coat rack, a small console table with keys, a patterned hall runner, light through the front door glass.",
     "Close-up from the side of his right leg as he stands, knee very slightly bent: his hand has just let go of the rolled-up chino leg, which is caught mid-fall, sliding down over the knee — the lower edge of the strap still just visible as the fabric drops, the rest already covered, the fabric lying flat over it with no bulge. " + G["G-09"] + ".",
     PS.REF_PROD + " a single unit, on the right knee directly under the kneecap, as in the placement reference.", PS.fill(PS.WEAR_CONCEAL.replace("[GARMENT]", "his stone-coloured chinos"), side=SIDE)]
     + tail(r, "his leg", "fresh morning daylight through the door glass — after, clean",
     ["no bulge under the fabric, no strap outline, no hand on the strap, no strap on the left knee, no second strap, no face in frame"]))
B["NS-06"] = ns06

def ns07():
    r = ROWS["NS-07"]
    return dict(model="nano_banana_pro", face="FACE", refs=[("P2-PARK plate", PLATE["P2-PARK"]), PLACEMENT] + PROD, body=[
     S("CAM-LOCK"), angle_line(r, "them"), focus_line(r, "them"),
     S("SCENE-REF").replace("[LOCATION]", "PARK").replace("[the location's named anchors, stated in one clause]", PARK)
       .replace("[where the camera now sits, what it looks across, and how that differs from the reference view]", "the camera is low at hip height on the path, three-quarter on to them as they walk toward it, the fork and the trees behind"),
     "Medium shot: " + G["G-10"] + ", walking toward the lens along the park path, caught mid-stride, chatting and laughing, an easy pace. "
     "The woman nearest the lens wears the strap on her right knee, clearly visible below the hem of her shorts.",
     place(), PS.WORDMARK_LOCK, PS.SIZE_WORN, S("AFTER-EASE"), S("NEG-DEFAULT-FACE")]
     + tail(r, "them", "warm afternoon sun — after, bright and open", PRODNEG + [S("NEG-EFFORT"), "no fifth person, no dogs, no bikes, no readable signs"]))
B["NS-07"] = ns07

if __name__ == "__main__":
    out = HERE / "prompts"; out.mkdir(exist_ok=True)
    for b in sys.argv[1:] or B:
        d = B[b](); p = "\n\n".join(d["body"])
        assert "[" not in p, (b, p[p.index("["):p.index("[") + 80])
        (out / f"{b}.t2i.txt").write_text(p)
        (out / f"{b}.refs.json").write_text(json.dumps(dict(model=d["model"], face=d["face"], refs=d["refs"]), indent=1))
        print(b, d["model"], len(p), "chars", [x[0] for x in d["refs"]])
