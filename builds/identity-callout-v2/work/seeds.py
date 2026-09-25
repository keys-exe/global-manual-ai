from lib import A, PS, ncount, BUILD
from plates import shell, propref
import json
SUBJ = {
 "S1": "Carol — a stocky White British woman of sixty-four, grown-out home-dyed auburn shoulder-length hair with two inches of grey roots, broad heavy-jawed face, the left upper eyelid drooping lower than the right",
 "S2": "Mr Hargreaves — a tall, stooped White British man of fifty-eight, long narrow face with a hooked nose, salt-and-pepper hair thinning on top, a short salt-and-pepper beard, a thickened cauliflower left ear",
 "S3": "Hannah — a wiry, small White British woman of thirty-four, very short cropped bleached-blonde hair with dark roots, a sharp face densely freckled, the right brow sitting higher",
}
AGE = {
 "S1": "deep crow's feet at both eyes, two heavy horizontal creases across the low forehead, deep nasolabial folds, marionette lines at the mouth corners, slack crepe under the eyes, broken capillaries across both cheeks and the nose, faded sun freckling on the cheekbones",
 "S2": "deep vertical frown lines between the brows, crow's feet, sagging upper eyelids, deep creases from nose to beard, weathered ruddy cheeks, a few broken capillaries on the nose",
 "S3": "dense ginger freckles across the nose and cheeks, faint lines at the eye corners from squinting outdoors, one or two fine forehead lines, slightly weathered sun-dry skin on the cheekbones",
}
WARD = {
 "D1": "Wearing a white cotton vest under an oversized lilac knitted cardigan, navy cotton shorts ending just above the knee so both knees are bare, grey felt slippers, in lilac, navy and grey.",
 "D2": "Wearing a faded teal cotton crew-neck T-shirt, stone-coloured cotton shorts ending mid-thigh so both knees are bare, scuffed white canvas plimsolls, in teal, stone and white.",
 "D3": "Wearing a cream cable-knit jumper, black straight-leg trousers falling to the ankle, black leather slip-on trainers, in cream and black.",
 "SURG": "Wearing a pale blue cotton shirt with the sleeves rolled to the forearms, no tie, navy chino trousers, dark brown leather brogues, in pale blue and navy.",
 "LAB": "Wearing a plain charcoal zip-neck sports top, black running tights, grey trail running shoes, in charcoal and black.",
}
SCALE = {"PROPPED": "about three quarters", "WIDE": "no more than two thirds", "SELFIE": "head and shoulders, about half", "WALK": "about half"}
def subjref(s): return A("SUBJ-REF").replace("[two or three named markers: hair, build, one distinctive feature]", SUBJ[s].split(" — ",1)[1])
def light(source, side, bounce):
    return A("LIGHT-EVENT").replace("[SOURCE — the vertical blinds / the window / the open door]", source).replace("[SIDE]", side).replace("[BOUNCE — the pale wall / the worktop / the floor]", bounce)
def sceneref(loc, anchors, where):
    return A("SCENE-REF").replace("[LOCATION]", loc).replace("[the location's named anchors, stated in one clause]", anchors).replace("[where the camera now sits, what it looks across, and how that differs from the reference view]", where)
def person_seed(*, subj, framing, prose, day, interior=False, scene=None, face=False, skin=False, light_=None, worn=None, mood=None, extra=None, extra_neg=None, cam="CAM-LOCK", staged=True, prod=False, seat=False):
    parts = [A(cam)]
    if framing in SCALE:
        parts += [A("FRAME-SCALE").replace("[SCALE]", SCALE[framing]), A("FRAME-" + framing)]
    elif framing == "OTS":
        parts += [A("FRAME-OTS")]
    if interior: parts += [propref(), shell()]
    if scene: parts += [sceneref(*scene)]
    parts += [prose, subjref(subj)]
    if face: parts += [A("FACE-SEED").replace("[the character's named markers]", SUBJ[subj].split(" — ",1)[1])]
    if worn or prod or seat: parts += [PS("REF-PROD")] + [PS(w) for w in (worn or [])]
    parts += [WARD[day], A("BODY-WHOLE")]
    if extra: parts += extra
    if mood: parts += [A("MOOD-POS" if mood == "pos" else "MOOD-NEG")]
    if light_: parts += [light(*light_)]
    if skin: parts += [A("SKIN-T").replace("[AGE-FEATURES]", AGE[subj])]
    parts += [A("CAP-SHARP"), A("CAP-FILE")]
    neg = [A("NEG-FILE"), A("NEG-FRAME"), A("NEG-BODY")] + ([A("NEG-STAGED")] if staged else []) + [A("NEG-SUBJ")]
    if scene: neg.append(A("NEG-SCENE"))
    if interior: neg.append(A("NEG-PROP"))
    if worn: neg += [PS("NEG-PLACE"), PS("NEG-ORIENT")]
    if seat: neg += [PS("NEG-SEAT")]
    if prod and not worn and not seat: neg += [PS("NEG-WARP-P")]
    if mood == "pos": neg.append(A("NEG-MOOD"))
    neg += [A("NEG-SKIN"), A("NEG-M1"), "no phone in frame, no second phone, no phone screen, no camera app interface, no recording icon"]
    if extra_neg: neg.append(extra_neg)
    s = " ".join(parts) + "\n\nNegative: " + ", ".join(neg)
    assert "[" not in s, s[s.index("["):][:120]
    return s
LIV_ANCH = "the worn beige fabric sofa with patterned cushions and the crocheted granny-square blanket over its arm, the wooden side table with a mug, the bay window with net curtains and beige drapes, the brass standard lamp, the cream stone fireplace with a carriage clock"
SEEDS = {}
SEEDS["VO-01"] = dict(model="nano_banana_pro", refs=["S1-CAROL", "PLATE-LIVING", "PLATE-PROPERTY"], prompt=person_seed(
    subj="S1", framing="PROPPED", day="D2", interior=True, face=True, skin=True,
    scene=("FRONT LIVING ROOM", LIV_ANCH, "the phone propped low and close on a footstool in the middle of the room, looking straight at the sofa on the left wall from under a metre away, so only the sofa, the blanket, the side table and a strip of the bay window at the right edge are in frame"),
    prose=A("SEED-CANDID").replace("[WHERE THE PHONE IS AND WHO IS HOLDING IT — one clause]", "a phone propped against a book on a footstool right in front of her, recording her talking").replace("[HOW IT IS HELD — low, at eye level, tilted, not looking at the screen]", "at chest height and about eighty centimetres away, so she fills most of the frame from the top of her head to her knees").replace("[THE SUBJECT — gender, age, build, two or three markers, the beat's wardrobe as plain clothes, what they are doing, where their eyes are, mouth shut]", "Carol, sixty-four, stocky, sitting forward on the edge of the sofa with her forearms on her bare knees, about to speak to the phone, eyes on the lens, mouth shut, the two inches of flat grey roots at her parting clearly visible above the auburn, white canvas plimsolls on her feet").replace("[THE ROOM — one sentence of what is actually there, untidied, nothing arranged]", "The sofa cushions squashed where she sits, the blanket half slipped off the arm, the mug on the side table beside her").replace("[WHAT OF THE PHONE-HOLDER IS IN FRAME, if anything, and that it is too close to the lens and soft]", "Nothing of the phone's holder is in frame").rstrip(".") + ".",
    light_=("the bay window net curtains", "camera-right", "the magnolia wall"),
    extra=[A("TEETH-A")], staged=False))
# ------------------------------------------------------------------ B-roll seeds
from lib import P, SIDE
def F(s): return P.fill(s.replace("[TARGET JOINT]", "[TARGET_JOINT]"), side=SIDE)
def candid(where, how, subject, room, holder="Nothing of the phone's holder is in frame."):
    s = A("SEED-CANDID")
    for k, v in [("[WHERE THE PHONE IS AND WHO IS HOLDING IT — one clause]", where), ("[HOW IT IS HELD — low, at eye level, tilted, not looking at the screen]", how),
                 ("[THE SUBJECT — gender, age, build, two or three markers, the beat's wardrobe as plain clothes, what they are doing, where their eyes are, mouth shut]", subject),
                 ("[THE ROOM — one sentence of what is actually there, untidied, nothing arranged]", room),
                 ("[WHAT OF THE PHONE-HOLDER IS IN FRAME, if anything, and that it is too close to the lens and soft]", holder)]:
        s = s.replace(k, v.rstrip("."))
    return s
STAIR_GEO = A("GEO-LINE").replace("[side]", "front-door side").replace("[fixed feature]", "the staircase rising along the left wall with the dark wooden handrail on its right and the framed seaside print above the third step").replace("[screen side]", "screen-left").replace("[direction]", "up and away from camera when climbing, down toward camera when descending")
STAIR_GEO_DOWN = "Geography: camera on the top landing looking down the straight flight, the dark wooden handrail on her right as she climbs toward the lens (screen-left), the wall with the framed seaside print on her left (screen-right), the front door and hall at the foot of the stairs behind her, direction of travel up toward camera."
HALL_LIGHT = "Soft daylight through the frosted front-door glass and the living-room doorway, falling off up the stairwell, the landing window at the top of the stairs blowing out white, shadows open, colours flat the way a phone renders an overcast British morning."
LIV_LIGHT = "Broad overcast daylight from the bay window, shadows open and soft, the net curtains blowing out, warm bounce off the oatmeal carpet."
EXT_OC = A("LOC-EXT-OVERCAST")
CLIN_ANCH = "the grey padded examination couch with its roll of white paper, the pale wooden desk with the plastic knee-joint model, the blue privacy curtain, the window on the far wall, the blue plastic visitor chair"
NOFACE = "Her face is out of frame — the frame holds only the body from the waist down."
KNEE_BARE = "Her bare right knee is plain skin, nothing worn on it."
def body_neg(): return ", ".join([A("NEG-NOFACE")])
def mech_seed(density, state, prod=False):
    parts = [F(A("ANAT-BASE")), F(A("ANAT-LIGHT")), F(A("ANAT-FIELD")), F(A(density))]
    if prod: parts += [PS("REF-PROD"), PS("PLACE-LOCK-C"), F(A("ANAT-PROD"))]
    parts += [F(state)]
    neg = [F(A("ANAT-NEG")), A("NEG-EXTERNAL"), A("NEG-FLOW")] + ([PS("NEG-PLACE")] if prod else [])
    s = " ".join(parts) + "\n\nNegative: " + ", ".join(neg); assert "[" not in s, s[s.index("["):][:80]; return s
R = {"S1":"S1-CAROL","S2":"S2-HARGREAVES","S3":"S3-HANNAH"}
PROD = ["front", "side"]
def add(bid, model, refs, prompt): SEEDS[bid] = dict(model=model, refs=refs, prompt=prompt)

add("HK1-01", "nano_banana_pro", ["S1-CAROL", "PLATE-PROPERTY"], person_seed(subj="S1", framing="WIDE", day="D1", interior=True, face=True, mood="neg",
  prose=candid("a phone propped on the hall radiator shelf just inside the front door, left recording", "low at waist height, pointing up the hall toward the foot of the stairs",
    "Carol, sixty-four, stocky, standing at the foot of the stairs in her cardigan and slippers, her right hand gripping the dark wooden handrail and her left hand pressed flat on the front of her right knee, looking up the flight, jaw set, bracing herself to start, mouth shut",
    "The hall as it is: a pair of shoes kicked off by the bottom step, a folded newspaper on the third tread") + " " + KNEE_BARE + " " + STAIR_GEO + " " + HALL_LIGHT))
add("HK2-01", "nano_banana_pro", ["S1-CAROL", "PLATE-LIVING", "PLATE-PROPERTY"], person_seed(subj="S1", framing="PROPPED", day="D1", interior=True, face=True, skin=True, mood="neg",
  scene=("FRONT LIVING ROOM", LIV_ANCH, "the phone propped on the side table at her elbow, low and close, looking across her lap toward the bay window, so the bay window is at the far right and the fireplace out of shot"),
  prose=candid("a phone propped against the mug on the side table beside the sofa, left recording", "at knee height, a little under a metre away, tilted up",
    "Carol, sixty-four, stocky, sitting on the front edge of the sofa in her lilac cardigan and navy shorts, both hands wrapped around her bare right knee, thumbs pressing into the soft spot just below the kneecap, a slow wince tightening her face, eyes down on the knee, mouth shut",
    "The blanket rucked on the sofa arm behind her, the TV remote beside her on the cushion") + " " + KNEE_BARE + " " + LIV_LIGHT,
  light_=("the bay window net curtains", "camera-right", "the magnolia wall")))
add("HK3-01", "nano_banana_pro", ["S1-CAROL", "PLATE-PROPERTY"], person_seed(subj="S1", framing="WIDE", day="D1", interior=True, face=True, mood="neg",
  prose=candid("a phone propped on the hall floor by the front door mat, left recording", "low at shin height, tilted up the stairs",
    "Carol, sixty-four, stocky, coming down the stairs one step at a time, halfway down, her right hand white-knuckled on the dark handrail, her left hand on the wall, her bare right knee bent over the edge of a tread with her weight held back, lowering the other foot onto the same step, looking down at her feet, mouth shut",
    "A laundry basket left on the top landing, a coat hung over the newel post") + " " + KNEE_BARE + " " + STAIR_GEO + " " + HALL_LIGHT))
add("B01", "nano_banana_pro", ["S1-CAROL", "PLATE-PROPERTY"], person_seed(subj="S1", framing="OTS", day="D1", interior=True, mood="neg",
  prose=candid("a phone held low by someone two steps below her on the stairs", "at knee height, close, pointing up at her legs",
    "Carol from the waist down, climbing: her slippered right foot just landing on the next oatmeal-carpeted tread, the bare right knee starting to bend and take her weight, her right hand gripping the dark wooden handrail at the top of frame",
    "The carpet worn pale at the front edge of each tread") + " " + NOFACE + " " + KNEE_BARE + " " + STAIR_GEO + " " + HALL_LIGHT))
add("B02", "nano_banana_pro", [], mech_seed("ANAT-B", A("ANAT-REST") + " The knee is bent as if on a stair tread, the thigh angled down into it from above, the lower leg below, the load about to arrive."))
add("B03", "nano_banana_pro", [], mech_seed("ANAT-C", A("ANAT-HOT")))
add("B04", "nano_banana_pro", ["S2-HARGREAVES", "PLATE-CLINIC", "front", "side"], person_seed(subj="S2", framing="PROPPED", day="SURG", face=True, mood="pos",
  scene=("ORTHOPAEDIC CONSULTING ROOM", CLIN_ANCH, "the phone propped on the couch at the right of the room looking across at the desk, so the window is behind him at frame left and the curtain out of shot on the right"),
  prose=candid("a phone propped on the examination couch, left recording", "at desk height, a metre and a half away",
    "Mr Hargreaves, fifty-eight, tall and stooped, sitting at the desk in his rolled blue shirt sleeves, holding the black strap in both hands and pressing its notched shell against the kneecap of the plastic knee-joint model on the desk, studying the fit closely, eyes down on it, mouth shut",
    "Papers and a box of gloves on the desk, the monitor turned away") + " The strap is held, not worn, in his hands, its wordmark facing the phone. " + PS("HOLD-PROD"),
  prod=True, extra=["Cool overcast daylight from the window behind him mixing with flat overhead fluorescent light."]))
SEAT_PROSE = lambda angle: candid("a phone held low by a friend kneeling on the carpet in front of the sofa", angle,
    "Carol from the knees down only, the frame cutting across her lower thighs so nothing above the knee is in shot, sitting on the sofa with her right foot flat on the carpet in a scuffed white canvas plimsoll and the knee bent, both hands holding the black strap already closed around her leg a hand's width below the knee, about to slide it up into place, white canvas plimsolls on both feet",
    "The oatmeal carpet, the sofa's beige front edge behind her calves, her plimsolls") + " " + NOFACE
add("B05", "nano_banana_pro", ["S1-CAROL", "PLATE-LIVING", "front", "worn_bent"], person_seed(subj="S1", framing="CLOSE", day="D2", interior=True, mood="pos",
  prose=SEAT_PROSE("at knee height, forty centimetres away, square to the front of the knee") + " " + PS("SEAT-LOCK").split(" Both hands")[0] + " " + LIV_LIGHT, seat=True))
add("B06", "nano_banana_pro", ["S1-CAROL", "PLATE-LIVING", "front", "side"], person_seed(subj="S1", framing="CLOSE", day="D2", interior=True,
  prose=candid("a phone held by Carol's friend over her shoulder", "at chest height, close, looking down at her hands in her lap",
    "Carol's two hands only, in her lap over her stone shorts: in her left hand the STRYDE strap, in her right hand a plain unbranded thin black neoprene tube strap barely wider than two fingers, held side by side so the difference in size is obvious — the cheap one visibly narrower than a kneecap, the STRYDE shell spanning a whole palm, its outer face flat toward the phone, upright, the concave notch at the top with the two matching pointed peaks either side clearly visible and the stryde wordmark readable left to right beneath the notch",
    "The sofa cushion under her hands") + " " + NOFACE + " The STRYDE strap is held, not worn. " + PS("HOLD-PROD") + " " + LIV_LIGHT,
  extra_neg="no brand name on the generic strap, no logo on the generic strap, no text anywhere but the stryde wordmark", prod=True))
add("B07", "nano_banana_pro", ["S1-CAROL", "PLATE-LIVING", "front", "side"], person_seed(subj="S1", framing="CLOSE", day="D2", interior=True,
  prose=candid("a phone held by Carol's friend beside her", "at chest height, close, looking at her hands against the bay window light",
    "Carol's two hands only, holding the strap up toward the window light, the shell upright with the concave notch and its two matching pointed peaks at the top, her right thumb pressing firmly into the outer face of the shell just below the notch, the stryde wordmark reading left to right the right way up, the band hanging loose from both chrome slides, only her hands and forearms in frame",
    "The bay window's net curtains glowing out of focus behind") + " " + NOFACE + " The strap is held, not worn, outer face and wordmark toward the phone. " + PS("HOLD-PROD") + " " + LIV_LIGHT, prod=True))
add("B08", "nano_banana_pro", ["front", "worn_front"], mech_seed("ANAT-B", "Calm resting state: the load is about to arrive; [SITE] cool and pale beneath the shell.", prod=True))
add("B09", "nano_banana_pro", ["S3-HANNAH", "S1-CAROL", "front", "worn_front"], person_seed(subj="S3", framing="OTS", day="LAB", mood="pos",
  prose=candid("a phone held over Hannah's shoulder in a university gait lab", "at shoulder height, behind her, looking past her",
    "Hannah, thirty-four, wiry, cropped bleached hair, her near shoulder and the back of her head large and soft at frame left, holding a clipboard, watching Carol — sixty-four, stocky, auburn hair with grey roots, in her teal T-shirt and stone shorts — walk on a treadmill a few metres away, the strap on Carol's right knee, a laptop on a trolley turned away from the phone",
    "Cool overhead LED panels, grey rubber flooring, a second treadmill, cables taped to the floor") + " Carol is THE SAME PERSON as the second attached subject reference image, unchanged in face, age and build.",
  worn=["PLACE-LOCK-C", "ORIENT-C"], extra=["Cool flat overhead LED light, the window at the back of the lab blowing out."],
  extra_neg="no readable screen, no graphs, no numbers on any display"))
WALK_KNEE = lambda where, doing: candid("a phone held low by someone walking backwards just ahead of her", "at knee height, a metre away, three-quarter from her front right, so the front of her right knee faces the lens",
    f"Carol from the waist down in her stone shorts and white plimsolls, {doing}", where) + " " + NOFACE
add("B10", "nano_banana_pro", ["S1-CAROL", "front", "worn_front"], person_seed(subj="S1", framing="CLOSE", day="D2", mood="pos",
  prose=WALK_KNEE("A quiet residential British pavement, pebble-dashed semis and low garden walls behind, a lamppost", "mid-stride on the pavement, the right leg swinging through with the knee just bending, the strap on the right knee") + " " + EXT_OC,
  worn=["PLACE-LOCK-C", "ORIENT-C"]))
add("B11", "nano_banana_pro", ["S1-CAROL", "PLATE-LIVING", "PLATE-PROPERTY"], person_seed(subj="S1", framing="PROPPED", day="D1", interior=True, face=True, mood="neg",
  scene=("FRONT LIVING ROOM", LIV_ANCH, "the phone propped low on the hearth beside the fireplace at knee height, a metre from the sofa, looking across at her, so the bay window is at the right edge of frame and the doorway out of shot"),
  prose=candid("a phone propped on the hearth beside the fireplace", "at knee height, a metre away, tilted up",
    "Carol, sixty-four, stocky, in her lilac cardigan and navy shorts, her bottom still on the front edge of the sofa cushion, just starting to push herself up off the sofa, both hands braced on the tops of her bare knees, elbows locked, face tight with the effort, eyes on the floor, mouth shut",
    "The sofa cushion still dented where she sat, the blanket slid onto the floor") + " " + KNEE_BARE + " " + LIV_LIGHT))
add("B12", "nano_banana_pro", ["S1-CAROL"], person_seed(subj="S1", framing="WIDE", day="D1", face=True, mood="neg",
  prose=candid("a phone propped on the back doorstep of the pebble-dashed semi", "low, at step height, looking down the small back garden",
    "Carol, sixty-four, stocky, in her lilac cardigan and navy shorts, lowering herself toward a kneeling pad on the lawn edge beside a flower border, her left hand on a garden fork stuck in the soil, her right hand clamped over her bare right knee, face screwed up, eyes on the ground, mouth shut",
    "Outdoors in the small back garden: a lawn, a wooden panel fence, a rotary washing line, pots of geraniums, a trowel lying on the grass, the pebble-dashed back wall of the house behind the phone") + " " + KNEE_BARE + " " + EXT_OC, extra_neg="no indoor room, no hall, no stairs, no carpet, no teal T-shirt"))
add("B13", "nano_banana_pro", ["S1-CAROL", "front", "worn_front"], person_seed(subj="S1", framing="WIDE", day="D2", face=True, mood="pos",
  prose=candid("a phone propped on a park bench", "at waist height, three metres from the path",
    "Carol, sixty-four, stocky, walking briskly along a tarmac park path toward the phone in her teal T-shirt, stone shorts and plimsolls, arms swinging freely, the black strap visible on her right knee, looking ahead up the path, a small private smile",
    "A British municipal park: mown grass, a green-painted bench, oak trees, a dog walker far behind") + " " + EXT_OC,
  worn=["PLACE-LOCK-C", "ORIENT-C"]))
add("B14", "nano_banana_pro", ["S1-CAROL", "PLATE-PROPERTY", "front", "worn_bent"], person_seed(subj="S1", framing="WIDE", day="D2", interior=True, mood="pos",
  prose=candid("a phone propped on the top landing, left recording", "at floor level, tilted down the flight",
    "Carol, sixty-four, stocky, in her teal T-shirt and stone shorts, climbing the stairs toward the phone one foot per step, the dark wooden handrail and spindles at the LEFT edge of the frame and the plain wall with the framed seaside print on the RIGHT, her right foot planted on a tread with the knee bent and taking her weight, her left foot lifting to the next tread, both hands free at her sides, not touching the handrail, the black strap on the front of her right knee facing the phone",
    "A coat over the newel post at the bottom, the front door beyond") + " " + STAIR_GEO_DOWN + " " + HALL_LIGHT,
  worn=["PLACE-BENT", "ORIENT-C"]))
add("B15", "nano_banana_pro", ["S1-CAROL", "PLATE-PROPERTY", "front", "worn_bent"], person_seed(subj="S1", framing="CLOSE", day="D2", interior=True, mood="pos",
  prose=candid("a phone held by someone crouched two steps above her on the stairs", "at knee height, close, square to the front of her right knee",
    "Carol's right leg only, her plimsoll planted on an oatmeal-carpeted tread, the knee bent at the start of a step up with her weight going onto it, one slim black strap seated just below the kneecap with the kneecap fully bare above it, nothing else on the leg",
    "The dark handrail blurred at the top of frame, the worn edge of the tread") + " " + NOFACE + " " + HALL_LIGHT,
  worn=["PLACE-BENT", "ORIENT-C"], extra_neg="no knee sleeve, no hinged brace, no wrap-around support, no hole around the kneecap, no straps above the knee"))
add("B16", "nano_banana_pro", ["front", "worn_bent"], mech_seed("ANAT-C", "The knee bent as on a stair tread, the load arriving; [SITE] cool and pale beneath the shell.", prod=True))
add("B17", "nano_banana_pro", ["S1-CAROL", "PLATE-LIVING", "front", "side"], person_seed(subj="S1", framing="CLOSE", day="D2", interior=True,
  prose=candid("a phone held by Carol's friend beside her", "at chest height, close, looking down at her hands",
    "Carol's two hands only, holding the strap by the shell in her left hand while her right hand pinches the tail of the knit band just beyond one chrome slide, starting to draw it through the slide",
    "The sofa arm and the crocheted blanket out of focus beneath") + " " + NOFACE + " The strap is held, not worn. " + PS("HOLD-PROD") + " " + LIV_LIGHT, prod=True))
add("B18", "nano_banana_pro", ["S1-CAROL", "front", "worn_bent"], person_seed(subj="S1", framing="CLOSE", day="D2", mood="pos",
  prose=WALK_KNEE("A quiet residential British street kerb, a parked silver hatchback, a privet hedge", "stepping up from the road onto the kerb with the right foot, the right knee bent high and taking her weight, the strap on the right knee") + " " + EXT_OC,
  worn=["PLACE-BENT", "ORIENT-C"]))
add("B19", "nano_banana_pro", ["S1-CAROL", "PLATE-PROPERTY"], person_seed(subj="S1", framing="WIDE", day="D3", interior=True, face=True, mood="pos",
  prose=candid("a phone held by a friend standing on the bottom stair", "at chest height, looking along the hall toward the front door",
    "Carol, sixty-four, stocky, in a cream cable-knit jumper and black straight-leg trousers, just come in through the front door behind her and walking briskly up the hall toward the stairs, facing the lens, her handbag on her shoulder, her face open and relaxed, glancing past the lens up the stairs",
    "Coats on hooks by the door, post on the mat") + " " + P.WEAR_CONCEAL.replace("[GARMENT]", "her black straight-leg trousers") + " " + HALL_LIGHT,
  extra_neg=P.NEG_CONCEAL))
add("B20", "nano_banana_pro", ["S2-HARGREAVES", "S1-CAROL", "PLATE-CLINIC", "front", "worn_front"], person_seed(subj="S2", framing="OTS", day="SURG", mood="pos",
  scene=("ORTHOPAEDIC CONSULTING ROOM", CLIN_ANCH, "the phone held behind Carol's shoulder at the head of the couch looking down the couch at her leg and at him, so the window is on the left and the curtain behind him on the right"),
  prose=candid("a phone held behind Carol's shoulder as she sits on the examination couch", "at shoulder height, looking past her shoulder",
    "Carol — sixty-four, stocky, auburn hair with grey roots, teal T-shirt and stone shorts — sitting on the couch paper with her right leg out straight, the strap on her right knee; Mr Hargreaves, fifty-eight, tall, stooped, bearded, in his rolled blue shirt sleeves, crouched beside the couch, pointing with one finger at the notch sitting under her kneecap and nodding, eyes on the knee, mouth shut",
    "The paper roll crumpled under her, the knee model on the desk behind him") + " Carol is THE SAME PERSON as the second attached subject reference image.",
  worn=["PLACE-LOCK-C", "ORIENT-C"], extra=["Cool overcast daylight from the window mixing with flat overhead fluorescent light."]))
S4 = ("a White British man of about seventy, small and wiry, bald on top with a white fringe, a sunburnt scalp, a white moustache, in a navy polo shirt, grey cargo shorts to just above the knee and grey trainers")
add("B21", "nano_banana_pro", ["front", "worn_front"], " ".join([A("CAM-LOCK"), A("FRAME-SCALE").replace("[SCALE]", SCALE["WIDE"]), A("FRAME-WIDE"),
  candid("a phone propped on a bin by the kerb of a British high street", "at waist height, looking up the pavement",
    "one-off passer-by: " + S4 + ", walking briskly toward the phone among Saturday shoppers, ONE black strap on his right knee only -- a single band directly below the kneecap, nothing above the kneecap, the left knee bare -- looking ahead, mouth shut",
    "A busy British market-town high street: a bakery, a charity shop, a bus stop, shoppers with bags, bunting, nothing branded readable"),
  PS("REF-PROD"), PS("PLACE-LOCK-C"), PS("ORIENT-C"), A("BODY-WHOLE"), A("MOOD-POS"), EXT_OC, A("CAP-SHARP"), A("CAP-FILE")])
  + "\n\nNegative: " + ", ".join([A("NEG-FILE"), A("NEG-FRAME"), A("NEG-BODY"), A("NEG-STAGED"), PS("NEG-PLACE"), PS("NEG-ORIENT"), A("NEG-MOOD"), A("NEG-SKIN"), A("NEG-M1"), "no readable shop signs, no brand names, no logos, no hinged brace, no second band above the knee, no thigh strap, no two straps on one leg, no strap on the left knee"]))
add("B22", "nano_banana_pro", ["S1-CAROL", "PLATE-LIVING", "front", "side"], person_seed(subj="S1", framing="CLOSE", day="D2", interior=True, mood="pos",
  prose=candid("a phone held by Carol's friend in front of her", "at chest height, close",
    "Carol's two hands only, one strap held up in each hand side by side toward the phone, both identical, wordmarks facing the lens, the chrome slides catching the window light, the band tails hanging",
    "The bay window out of focus behind") + " " + NOFACE + " TWO straps, both held, neither worn. " + PS("HOLD-PROD") + " " + LIV_LIGHT, prod=True))
add("B23", "nano_banana_pro", ["S1-CAROL", "PLATE-LIVING", "PLATE-PROPERTY", "front", "worn_bent"], person_seed(subj="S1", framing="PROPPED", day="D2", interior=True, face=True, mood="pos",
  scene=("FRONT LIVING ROOM", LIV_ANCH, "the phone propped on the mantelpiece on the right wall looking across at the sofa, so the bay window is at the right edge of frame"),
  prose=candid("a phone propped against the carriage clock on the mantelpiece", "at chest height, two metres away",
    "Carol, sixty-four, stocky, in her teal T-shirt and stone shorts, sitting back on the sofa, lifting her right leg straight out in front of her and bending the knee again easily, the strap on her right knee, watching the knee move, a small pleased smile",
    "A cup of tea steaming on the side table, the blanket folded on the arm") + " " + LIV_LIGHT,
  worn=["PLACE-BENT", "ORIENT-C"], light_=("the bay window net curtains", "camera-right", "the magnolia wall")))
add("B24", "nano_banana_pro", ["S1-CAROL", "PLATE-PROPERTY", "front", "worn_bent"], person_seed(subj="S1", framing="WIDE", day="D2", interior=True, face=True, mood="pos",
  prose=candid("a phone propped on the hall floor by the front door mat", "low at shin height, tilted up the stairs",
    "Carol, sixty-four, stocky, in her teal T-shirt and stone shorts, coming down the stairs toward the phone one foot per step, hands free at her sides, not holding the handrail, her right foot landing on the next tread with the knee bending to take her weight, the strap on her right knee facing the phone, looking down the flight, relaxed",
    "A coat over the newel post, a folded newspaper on the bottom step") + " " + STAIR_GEO + " " + HALL_LIGHT,
  worn=["PLACE-BENT", "ORIENT-C"]))
add("B25", "nano_banana_pro", ["S1-CAROL", "PLATE-LIVING", "front", "worn_bent"], person_seed(subj="S1", framing="CLOSE", day="D2", interior=True, mood="pos",
  prose=SEAT_PROSE("at knee height, forty centimetres away, three-quarter from her right") + " " + PS("SEAT-LOCK").split(" Both hands")[0] + " The kneecap is completely bare, with a full hand's width of bare shin skin showing between the bottom of the kneecap and the top edge of the strap. " + LIV_LIGHT, seat=True,
  extra_neg="no strap at the kneecap, no strap already in place under the kneecap, no strap touching the kneecap"))
add("B26", "nano_banana_pro", ["S1-CAROL", "PLATE-PROPERTY", "front", "worn_bent", "B14-FRAME"], person_seed(subj="S1", framing="WIDE", day="D2", interior=True, mood="pos",
  prose=candid("a phone propped on the top landing, left recording", "at floor level, tilted down the flight",
    "Carol, sixty-four, stocky, in her teal T-shirt and stone shorts, at the foot of the stairs facing up toward the phone, her right foot already up on the first tread, knee bent and loading, hands free, starting to climb briskly, the strap on the front of her right knee facing the phone, looking up the flight with a small determined smile",
    "Shoes by the bottom step, the coat on the newel post, the front door behind her") + " " + STAIR_GEO_DOWN + " THE SAME STAIRCASE FROM THE SAME CAMERA POSITION as the attached stair reference image: the dark wooden handrail and white spindles down the left of frame, the framed seaside print on the wall at the right of frame. Both her hands hang free at her sides and neither touches the handrail. " + HALL_LIGHT,
  worn=["PLACE-BENT", "ORIENT-C"], extra_neg="no hand on the handrail, no gripping the rail, no handrail on the right of frame, no print on the left wall"))

if __name__ == "__main__":
    for k, v in SEEDS.items():
        (BUILD/"beats"/f"{k}.t2i.txt").write_text(v["prompt"]); print(k, v["model"], ncount(v["prompt"]))
    json.dump({k: {"model": v["model"], "refs": v["refs"]} for k, v in SEEDS.items()}, open(BUILD/"work/seed_index.json", "w"), indent=1)

