"""Act map (§18 step 5, E4) + B-roll T2I and Kling I2V prompts. Durations from the voice masters (E6)."""
import json, math, re
from lib import *
M = dict(PT="735ae689-870f-45d4-9fd1-f5f85ad06e48", DR="c7f0b639-ccf2-4bda-adba-db564b45779f",
  STAIRS="866fa4c5-1fd4-4989-8f3a-397cdea1ee07", LIVING="0e111a5c-521c-49ed-9101-e67156d0416e",
  GARDEN="a48713bc-da97-4e6b-b599-7dd5b58dfb52", PROP="ea51fa7e-a1ab-4f2d-8b8a-1b6bc5792caf", CLINIC="52da3180-a52a-45e2-b8d0-00a31ddd458e",
  front="cdbd3614-14b7-44ef-9485-643d0fb8b65a", back="e54b691d-1108-4e08-8918-8068044b5305", tq_left="c463fe3e-fd82-4b53-8e50-bad1e2a465a0",
  macro="adafd66e-3686-4318-af16-755fafc17c85", package_open="1cf90fd6-db30-4b1b-a6d8-4dfb1aa193d6",
  wornF="51bbba5b-4271-4e49-8245-b785b96cd30a", wornR="f2e5943d-b2a3-4dd5-a593-f6ed79625da4", wornB="dedcd2b6-1639-42b1-99ff-45daaebc271e")
L = dict(
 full={"type":"full"},
 cut={"type":"pip","over":"broll","corner":"bl","scale":0.33,"border":0},
 pip={"type":"pip","over":"th","corner":"br","scale":0.45,"border":6},
 split={"type":"split","broll_pos":"bottom","ratio":0.45})
FRAMING = {"cut":"the action in the upper two thirds and the right side of the frame, the lower-left third quiet floor or wall",
           "pip":"one subject, large and centred, readable at a third of the width",
           "split":"the subject near the vertical middle of the frame with nothing important at the very top or bottom, one single continuous image",
           "full":"the subject centred with room around it"}
PT_SUBJ = ("THE SAME WOMAN exactly as in the attached subject reference sheet -- seventy-one, heavyset and short, a broad round face with small hooded brown eyes, "
  "chin-length grown-out auburn hair with two inches of silver-white roots, a small dark mole beside her left nostril -- unchanged in face, age and build, "
  "wearing her heather-grey cardigan over a cream blouse and a navy jersey skirt ending a hand's width above the knee, bare legs, flat brown slip-on shoes")
PROPH = S("PROP-REF").replace("[THE CARRIED FINISHES, NAMED IN ONE CLAUSE]",
   "magnolia walls, white-gloss skirting, white four-panel doors with brass levers, beige carpet, dark pine handrail")
REFP = P.REF_PROD.replace("the attached reference image","the attached product photos")
WORN = REFP + " worn on her LEFT leg only, her right knee bare. " + P.fill(P.PLACE_LOCK_C, side="left") + " " + P.SIZE_WORN
MECH = ("A 3D anatomical visualisation for medical education, the style of a patient-information animation: a translucent pale-grey human left leg seen from the front-side at knee height "
  "against a plain soft dark-grey background, the skin a faint glassy outline, the thigh bone, kneecap and shin bone rendered in clean matte ivory, "
  "the patellar tendon -- the thumb-wide band running from the bottom of the kneecap down to the top of the shin, about two centimetres below the kneecap -- "
  "rendered in a clear warm orange so it is the one coloured thing in frame. No text, no labels, no arrows, no numbers. Clean satin sheen on the surfaces.")
def neg_person(worn=False):
    n = [S("NEG-FILE"), S("NEG-BODY"), "no phone interface, no status bar"]
    if worn: n.append(P.fill(P.NEG_PLACE, side="left"))
    return "Avoid: " + ", ".join(n) + "."
# beat: id, phrase, kind, layout, loc, refs, scene, motion, (worn)
B = [
 ("BR01","A patient of mine. Nine years of knee pain.","life","cut","LIVING",["PT","LIVING"],
  "She sits in the green wing armchair of the attached living room, seen from across the room at seated height, both hands rubbing slowly round her bare left knee, her eyes down on it, the walking stick against the chair arm. The bay window with net curtains behind her on the left.",
  "her hands keep rubbing slow circles round the left knee, she shifts her weight in the chair with a small wince, eyes staying down", False),
 ("BR02","Bone on bone on the left, the right one following it.","object","pip","CLINIC",["CLINIC"],
  "Close on a wall-mounted X-ray lightbox in the attached consulting room: one grey-and-white X-ray film clipped to it showing BOTH knees of one person from the front side by side, the left knee joint space visibly narrowed to nothing so the bones nearly touch, the right joint space narrower than normal; no text, no letters, no numbers, no markers anywhere on the film. The lightbox's white glow fills most of the frame.",
  "a doctor's hand enters from the right and his index finger traces slowly along the narrowed gap of the left knee on the film, then moves across toward the right knee", False),
 ("BR03","Two centimetres below your kneecap there is a band of tendon about as wide as your thumb.","mech","split",None,[],
  MECH + " The leg is straight, the camera level with the knee.",
  "the camera slowly pushes in toward the orange tendon band below the kneecap while the band brightens gently, the leg staying still", False),
 ("BR04","Every step you take lands on it. Seventeen times your bodyweight.","mech","split",None,[],
  MECH + " The leg is mid-step, knee slightly bent, the foot about to land.",
  "the leg takes one step: as the foot lands the orange tendon band flares bright and visibly tensions, then eases as the weight passes, and starts to flare again on the next landing at walking cadence", False),
 ("BR05","Put your finger under your kneecap and press.","life","cut","LIVING",["PT","LIVING"],
  "Close on her bare LEFT knee as she sits in the armchair, her own right index finger pressing into the soft spot just below the kneecap, the skin dimpling under the fingertip; her cardigan sleeve and skirt hem in frame, her face out of frame above.",
  "her fingertip presses in a little deeper under the kneecap, holds, and eases off, the skin springing back, then presses again", False),
 ("BR06","Coming down is worse than going up.","life","cut","STAIRS",["PT","STAIRS"],
  "She stands at the top of the attached staircase on the landing, seen from a few steps below looking up, her right hand gripping the dark pine handrail hard, her left hand on the wall, looking down the flight with a set, wary face, not yet moving.",
  "she shifts her weight, tightens her grip on the rail and edges one foot toward the top step, then hesitates, still looking down", False),
 ("BR07","Going up, your muscles lift you. Coming down, you are catching yourself, and the catch lands on that band.","mech","split",None,[],
  MECH + " The thigh muscles at the front are shown in a soft translucent red, the knee bending as if stepping down.",
  "the knee bends as the body lowers onto it: the red thigh muscles lengthen and as the weight catches, the orange tendon band flares bright and stretches, then the leg straightens and the glow fades, and the knee starts to bend again", False),
 ("BR08","That is why she came down backwards.","life","cut","STAIRS",["PT","STAIRS"],
  "She is halfway down the attached staircase BACKWARDS, facing the stairs as if on a ladder, both hands gripping the handrail, one foot reaching down behind her for the next step, seen from the hall below at an angle, her face in profile tight with concentration.",
  "she lowers herself one more step backwards, both hands sliding down the rail, her reaching foot finding the tread and taking her weight carefully, the next foot starting to move", False),
 ("BR09","That is why the chair took three tries.","life","cut","LIVING",["PT","LIVING"],
  "She sits forward in the green wing armchair, both hands pushing down on the wooden arms, trying to stand, her body rocked forward, her face strained, the walking stick beside her.",
  "she pushes up, rises a few centimetres and sinks back into the seat, rocks forward again and pushes once more, not yet up", False),
 ("BR10","That is why the good knee started going the same way. She had been leading with it for years.","life","cut","STAIRS",["PT","STAIRS"],
  "Low and close on her legs on the attached staircase: she comes down a step FORWARDS but in a careful step-to pattern, always putting her RIGHT foot down first and bringing the left foot to join it on the same tread, her right hand on the rail; framed from her hips to her feet, face out of frame.",
  "her right foot goes down to the next tread, takes the weight with the knee bending, and the left foot follows to the same step, then the right foot starts down again", False),
 ("BR11","The long walk. The garden.","life","pip","GARDEN",["PT","GARDEN"],
  "She stands in the open back door of the house looking out at the attached overgrown back garden, one hand on the door frame, her back three-quarter to the camera, the weedy raised beds and the cracked greenhouse beyond her.",
  "she looks out at the garden for a moment, her hand tightening on the door frame, then her head drops a little and she starts to turn back inside", False),
 ("BR12","Her family coming to her instead.","life","cut","LIVING",["PT","LIVING"],
  "Her daughter, about forty, and a grandson of about eight in a school jumper sit on the brown sofa of the attached living room with mugs, visiting, while she stays in the green armchair across from them, her left leg stretched out on a footstool; a warm but slightly awkward afternoon.",
  "the boy leans over to show her something on a tablet and she reaches to take it without getting up, the daughter sipping her tea", False),
 ("BR13","A sleeve squeezes the whole knee.","object","pip",None,[],
  "Close on an adult's bare knee wearing a plain grey knitted compression knee sleeve covering the whole joint from mid-thigh to mid-shin, no logo, no text, on a living-room carpet background, seated.",
  "two hands pull the sleeve up over the knee and smooth it, the fabric squeezing the whole joint", False),
 ("BR14","A hinged brace stops it going sideways, and her knee was never going sideways.","object","pip",None,[],
  "A kitchen drawer pulled open, crammed with old knee supports: a bulky black hinged knee brace with metal side hinges and velcro straps on top, a crumpled grey sleeve and a tube of cream underneath; no logos, no text.",
  "a hand drops the hinged brace back into the drawer and pushes the drawer slowly shut", False),
 ("BR15","A gel sits on the skin.","object","pip",None,[],
  "Close on a bare knee, a plain unbranded white tube squeezing a clear gel onto the skin just above the kneecap, the gel sitting glossy on the surface.",
  "fingers rub the gel in small circles over the skin, the gel spreading thin and shiny on the surface", False),
 ("BR16","It is called Stryde.","held","full","CLINIC",["DR","front","tq_left","CLINIC"],
  P.PRODUCT_SET_HELD.replace("an adult casually showing the strap to the camera at chest height in a lived-in living room","the doctor's hand from the attached sheet, white coat cuff and pale blue shirt cuff visible, holding the strap up to the camera at chest height in the attached consulting room").replace("the hand of an adult of about sixty","the hand of a man of sixty-one")
    + " " + REFP + " a single unit. " + P.PRODUCT_SET_GEOM + " " + P.SIZE_HELD + " " + P.INNER_PAD,
  "the wrist turns the strap slowly a little to one side so the chrome slides catch the light, then back to square with the lens, the band swinging slightly under its own weight", False),
 ("BR17","It sits two centimetres below the kneecap, on the tendon. It never crosses the joint.","worn","cut","LIVING",["PT","wornF","front","LIVING"],
  "Close on her LEFT knee as she stands on the living-room carpet, the frame running from mid-thigh with her skirt hem to mid-shin, her bare right leg partly at the edge of frame on the left of the picture, the strap already in place on the left knee.",
  "she shifts her weight onto the left leg and back, the knee flexing very slightly, the strap holding its place exactly", True),
 ("BR18","A silicone pad inside holds pressure on that one band instead of spreading it round the whole knee.","object","full",None,["back","front"],
  P.PAD_BACK_SHOT + " " + REFP + " a single unit. Held by the fingertips at each end of the shell's lower edge against a plain soft-grey backdrop. " + P.SIZE_OBJECT,
  "the hand tilts the strap slowly so the light slides across the smooth inner pad, then brings it back square", False),
 ("BR19","The weight gets caught and moved off the worn part before it reaches the joint.","mech","split",None,["front"],
  MECH + " A slim matte-black strap sits on the front of the leg just below the kneecap, directly over the orange tendon band, its shell pressing on it -- the strap exactly the shape of the attached product photo, no wordmark needed.",
  "the leg takes a step: as the foot lands, the orange glow gathers under the strap's shell and stays there instead of travelling up into the knee joint, the joint staying cool ivory, then the step passes and it eases", False),
 ("BR20","The placement is the whole thing. A centimetre too high and it is a sleeve again.","seat","cut","LIVING",["PT","wornF","front","LIVING"],
  "She sits on the edge of the green armchair with her LEFT leg straight out in front of her, foot on the carpet, both hands flat on the two sides of the strap's shell at mid-shin. " + REFP + " " + P.fill(P.SEAT_LOCK, side="left"),
  "both hands slide the strap up the front of the shin in one unhurried movement until the kneecap stops it on the tendon, fingers just beginning to lift away", False),
 ("BR21","Ten seconds to put on.","seat","cut","LIVING",["PT","wornF","front","LIVING"],
  "Close and low, from her left side: her bare LEFT foot and shin, the closed strap already pulled over her foot and sitting at mid-shin, both her hands on its shell. " + REFP + " " + P.fill(P.SEAT_LOCK, side="left"),
  "both hands slide the strap up the shin in one movement and seat it under the kneecap, then the hands come away", False),
 ("BR22","No sores, no rolling down, and nobody can see it.","life","cut","PROP",["PT","PROP"],
  "She walks along the attached hall toward the front door in grey wool trousers instead of her skirt, cardigan on, handbag on her arm, an easy ordinary walk, seen from behind and to the side; the trouser legs hang straight with no shape showing at the knee. " + P.WEAR_CONCEAL.replace("[GARMENT]","grey wool trousers"),
  "she walks two easy steps toward the front door and reaches for the latch, the trousers moving naturally at the knee", False),
 ("BR23","You do not have to take my word for it. One knee only. Leave the other bare.","worn","cut","LIVING",["PT","wornB","front","LIVING"],
  "She sits in the green armchair, both knees bent at about a right angle, feet flat on the carpet, seen from low and slightly to her left: the strap on her LEFT knee, her RIGHT knee bare beside it. " + P.fill(P.PLACE_BENT, side="left"),
  "she rests her hands on her thighs and looks down at the two knees, then straightens a little in the chair", True),
 ("BR24","Go to your own stairs and come down forwards.","worn","cut","STAIRS",["PT","STAIRS","wornF"],
  "She stands at the top of the attached staircase facing DOWN the stairs, the strap on her LEFT knee under her skirt hem, her right hand resting lightly on the handrail, about to take the first step forwards.",
  "she steps down forwards onto the first tread with her left foot, then the right foot passes it to the next tread, a normal alternating step", True),
 ("BR25","Her scan looks exactly the same as it did in March. I have both of them.","object","pip","CLINIC",["CLINIC"],
  "Close on the X-ray lightbox in the attached consulting room with TWO grey-and-white X-ray films of the same pair of knees clipped side by side, identical, the left knee joint space narrowed to nothing on both; no text, no letters, no numbers, no markers.",
  "a doctor's hand clips the second film up beside the first and smooths it flat, then taps the two narrowed left knees one after the other", False),
 ("BR26","Because the load is not landing on that band any more.","worn","cut","STAIRS",["PT","STAIRS","wornF"],
  "She comes DOWN the attached staircase FORWARDS in a normal alternating stride, seen from the hall below, the strap on her LEFT knee visible under her skirt hem, her right hand only brushing the rail, her face calm and a little surprised.",
  "she takes two steady alternating steps down forwards, left then right, not stopping on each tread", True),
 ("BR27","Two for one, so you do both knees, which is what she needed.","object","full",None,["package_open","front"],
  "Product photograph, vertical 9:16, the opened box on a light oak kitchen table in daylight. " + P.PACKAGE_LOCK + " " + REFP.replace("The product","Each strap") + " two identical straps.",
  "a hand lifts the lid fully off the box and sets it aside, the two straps sitting in their wells", False),
 ("BR28","The copies stretch, and a stretched strap stops holding the spot.","object","pip",None,[],
  P.FAKE_BASE + " Held up by two hands against a kitchen, " + P.FAKE_ARCHETYPES[2][1] + ".",
  "the two hands pull the band apart and it stretches out long and stays slack, the shell tipping loose", False),
 ("BR29","Nothing to lose but the pain. Go and do your stairs.","worn","cut","STAIRS",["PT","STAIRS","wornF"],
  "She reaches the bottom of the attached staircase coming down forwards, stepping off the last tread into the hall, the strap on her LEFT knee under her skirt hem, a small relieved breath, her hand leaving the rail.",
  "she steps off the last stair onto the hall carpet and turns toward the living-room door, a small smile starting", True),
 ("HK1-01","In six weeks, this woman stopped coming down her own stairs backwards.","worn","pip","STAIRS",["PT","STAIRS","wornF"],
  "Seen from the hall looking up the attached staircase: she is coming DOWN FORWARDS, three steps from the bottom, in a normal alternating stride, the strap on her LEFT knee under her skirt hem, her hand light on the rail.",
  "she comes down two steady alternating steps forwards, left then right", True),
 ("HK1-02","Without one more brace going in the drawer.","object","pip",None,[],
  "A bedroom chest of drawers with the top drawer open, already full of old knee supports -- sleeves, a hinged brace, neoprene wraps -- no logos, no text.",
  "a hand drops one more black knee support on top of the pile and slides the drawer shut", False),
 ("HK2-01","It takes ten seconds and it is not a prescription.","seat","cut","LIVING",["PT","wornF","front","LIVING"],
  "Close on her LEFT leg from the front as she sits on the armchair edge, leg straight, the closed strap at mid-shin under both hands. " + REFP + " " + P.fill(P.SEAT_LOCK, side="left"),
  "both hands slide the strap up to seat under the kneecap in one movement, fingers lifting away", False),
 ("HK3-01","Every week somebody brings me a scan of a knee and asks what can be done about the cartilage.","object","pip","CLINIC",["CLINIC"],
  "Over the doctor's desk in the attached consulting room: an older patient's hand slides a large brown X-ray envelope across the desk, a grey knee X-ray film half out of it; the doctor's hands in white coat cuffs at the edge of frame; no text on the film or envelope.",
  "the patient's hand pushes the envelope across the desk and the doctor's hand draws the film out of it", False),
]
def words(n): return json.load(open(f"{n}.words.json"))
def span(part, phrase):
    ws = words(part); toks = [re.sub(r"[^a-z0-9']","",w[2].lower()) for w in ws]
    tgt = [re.sub(r"[^a-z0-9']","",t.lower()) for t in phrase.split()]
    for i in range(len(toks)-len(tgt)+1):
        if toks[i:i+len(tgt)] == tgt: return ws[i][0], ws[i+len(tgt)-1][1]
    raise ValueError(phrase)
def t2i(b):
    bid, ph, kind, lay, loc, refs, scene, motion, worn = b
    parts = [S("CAM-LOCK").replace("handheld", "handheld" if kind in ("life","worn","seat") else "handheld")]
    if kind == "mech":
        parts = [scene, "Framing: " + FRAMING[lay] + "."]
        return " ".join(parts)
    if loc in ("LIVING","STAIRS","PROP") and kind != "object": parts.append(PROPH)
    parts.append("Vertical 9:16 phone photo. Framing: " + FRAMING[lay] + ".")
    if "PT" in refs: parts.append(PT_SUBJ + ".")
    parts.append(scene)
    if worn: parts.append(WORN)
    if kind in ("life","worn","seat","held"): parts.append(S("BODY-WHOLE"))
    parts += [S("CAP-A"), S("CAP-FILE")]
    parts.append(neg_person(worn) if kind != "object" else "Avoid: no text, no logos, no brand names, no labels, no phone interface, no status bar, no advertising image, no studio lighting.")
    return " ".join(parts)
def i2v(b):
    bid, ph, kind, lay, loc, refs, scene, motion, worn = b
    subj = "Exactly as in the start frame, unchanged in every respect."
    if worn: subj += " " + P.fill(P.PLACE_LOCK_C, side="left")
    negs = [S("NEG-WARP-C"), "no cut, no scene change, no text, no captions, no music"]
    if (kind in ("seat","held","object") and "front" in refs) and not worn: negs.append(P.NEG_WARP_P)
    if worn: negs.append(", ".join(P.fill(P.NEG_PLACE, side="left").split(", ")[:14]))
    if "PT" in refs: negs.append(S("NEG-SUBJ"))
    j = {"shot": bid.lower().replace("-","_"), "subject": subj,
         "camera": {"movement": "handheld phone, a slight natural drift and breathing sway, no zoom" if kind!="mech" else "slow steady push-in",
                    "framing": ("PROPPED as in the start frame; " if kind!="mech" else "as in the start frame; ") + FRAMING[lay]},
         "motion": motion + ". The movement is already underway at the first frame and still going at the last. " + (P.HOLD_PROD + " " if (worn or kind in ("seat","held")) else "") + S("HOLD-C"),
         "lighting": S("INHERIT-CAP"), "style": "real phone footage, documentary" if kind!="mech" else "clean medical-education 3D animation",
         "negatives": ", ".join(negs)}
    s = json.dumps(j, ensure_ascii=False, separators=(",",":"))
    if len(s) > 2500:  # §37 trim ladder: drop NEG-SUBJ, then the long product holds
        j["negatives"] = ", ".join(n for n in negs if n != S("NEG-SUBJ")); s = json.dumps(j, ensure_ascii=False, separators=(",",":"))
    if len(s) > 2500:
        j["motion"] = motion + ". The movement is already underway at the first frame and still going at the last. " + P.HOLD_PC + " " + S("HOLD-C"); s = json.dumps(j, ensure_ascii=False, separators=(",",":"))
    if len(s) > 2500 and worn:
        j["subject"] = "Exactly as in the start frame, unchanged in every respect; the strap stays on the left knee exactly where it is."; s = json.dumps(j, ensure_ascii=False, separators=(",",":"))
    return s
if __name__ == "__main__":
    rows = []
    for b in B:
        part = "body" if b[0].startswith("BR") else b[0][:3]
        a, e = span(part, b[1])
        d = min(15, max(3, math.ceil(e - a + 0.5)))
        p1, p2 = t2i(b), i2v(b)
        open(f"../beats/{b[0]}.t2i.txt","w").write(p1); open(f"../beats/{b[0]}.i2v.json","w").write(p2)
        model = "nano_banana_pro"  # V: every class passes pro; the §5 route logs it one tier down (nano_banana_2). Passing nano_banana_2 logs nano_banana_flash = failed
        rows.append(dict(beat_id=b[0], part=part, phrase=b[1], type="MECH" if b[2]=="mech" else ("PRODUCT" if b[2] in ("held","object") and "front" in b[5] else "BR"),
            kind=b[2], layout=L[b[3]], location_id=b[4], refs=[M[r] for r in b[5]], ref_names=b[5], span=[a,e], duration=d, model=model,
            story_day="D1", capture_event_id=f"{b[4] or 'NONE'}-D1", side="left" if b[8] or b[2]=="seat" else None,
            t2i_chars=len(p1), i2v_chars=len(p2)))
    json.dump(rows, open("../act_map.json","w"), indent=1)
    tot = sum(r["duration"] for r in rows)
    for r in rows: print(r["beat_id"], r["kind"], r["duration"], r["model"], r["t2i_chars"], r["i2v_chars"])
    print("total clip seconds", tot, "clips", len(rows))
