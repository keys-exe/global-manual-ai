"""Scene 5 — THE TURN (day D4, the afternoon Beth lets herself in; L-VANITY, the main bedroom). Seven Seedance 2.5 takes via Higgsfield
(omni_reference, 720p, 9:16), ingredients only, no frames (§4, §24K part 5). User go: "CONFIRMED ALL IMAGE. PROCEED" (2026-10-02) — OUTFIT-N-D4,
OUTFIT-C3-D4, PROD-HAND-CARD, COLOUR-FRONT-CARD, C3-FACE, N-AFTER-FACE and the three client product photos confirmed.
D4 clothes are not the sheets' party outfits, so faces go in as face-and-hair crops and the outfit cards carry the clothes (HT26, HT27).
Susan's face is N-FACE to SH06 and N-AFTER-FACE from SH07 (wardrobe D4), her hair the low unwashed ponytail throughout.
F10: the stick is the real violet stick; Beth's palm covers the wordmark as she takes it out, and the inserts keep the wordmark turned away —
unlabelled to the viewer until the hero (SC09).
Voice refs hold only the take's own words (L33): Beth's L010 cut from her master, the rest voiced by her clone FaceloveBeth; Susan's by her clone."""
import importlib.util, json
from pathlib import Path
H = Path(__file__).parent; B = H.parents[1]
_s = importlib.util.spec_from_file_location("sc01", B / "body/SC01/build_clips.py"); S1 = importlib.util.module_from_spec(_s); _s.loader.exec_module(S1)
_p = importlib.util.spec_from_file_location("ps", B / "product/facelove_product_sheet.py"); PS = importlib.util.module_from_spec(_p); _p.loader.exec_module(PS)
R = S1.R
LINES = {}
for l in (B / "BUILD_SHEET.md").read_text().splitlines():
    p = [x.strip() for x in l.split("|")]
    if len(p) > 5 and p[1].startswith("L0") and "SC05" in p[2]: LINES[p[1]] = p[4]
L = LINES

SERIES = S1.SERIES.replace("the low sun, the string-light bulbs, a candle", "the window through the sheer curtains").replace("the yard layered in depth behind", "the room layered in depth behind")
VOICE_C3 = ("An American woman of forty-nine, a bright, easy, honest voice with a smile in it, clear General American vowels, unhurried and certain without "
            "selling anything. Statements fall at the end; never salesy, never theatrical.")
SUSAN_ID = S1.SUSAN_ID.replace(", worn loose", ", pulled back in a low ponytail, unwashed")
BETH_ID = "a tall, slim woman of forty-nine with straight shoulder-length honey-brown hair, centre-parted, and freckles across her cheekbones"
SUSAN_D4 = "the faded sage-green sweatshirt and grey lounge trousers, grey socks"
BETH_D4 = "the light chambray shirt with the sleeves rolled, white jeans and tan flats"
FACE_N = ("is Susan's face and hair only: her face, age, every line of it and her hair colour exactly as shown; today her hair is pulled back in a low ponytail; "
          "her clothes come from her outfit card, never from anywhere else.")
FACE_NA = ("is Susan's face only, once the foundation is on: the same face, the same lines in the same places, the tone of her skin evened; "
           "her hair stays pulled back in the low ponytail and her clothes stay the sweatshirt — never this picture's hair.")
FACE_C3 = ("is Beth's face and hair only: her face, age, freckles and straight honey-brown hair exactly as shown; her clothes come from her outfit card, never from anywhere else.")
OUT_N = ("is Susan's outfit today, laid flat: the faded sage-green crew sweatshirt, the grey jersey lounge trousers, the grey socks and the black elastic in her "
         "low ponytail — she wears exactly these.")
OUT_C3 = ("is Beth's outfit today, laid flat: the light chambray shirt with the sleeves rolled to the elbow, the white straight jeans, the tan ballet flats, "
          "and the black garment bag she carries — she wears and carries exactly these.")
ROOM = ("is the place: the main bedroom — the white dressing table with its large rectangular mirror under the window, the small upholstered stool, the sheer white "
        "curtains, the end of the bed with the dusty-blue quilt on the left; its layout and light side exactly as shown.")
PROD = lambda end: ("is the product, the FACELOVE Changing Foundation Stick, " + {"closed": "closed, both ends capped", "balm": "with the balm end uncapped",
                    "brush": "with the brush end uncapped"}[end] + ": copied exactly — same shape, same parts, same markings, nothing redesigned.")
HOLDV = ("is how Beth holds the closed stick: low on the barrel in her right hand, fingers wrapped round it; it sets the grip and the size of the stick in her hand, "
         "never the framing.")
COLOURV = ("is how the colour change looks: the balm goes on as an opaque white band; where the brush has worked it, it turns to the skin's own tone, and ahead of the "
           "brush it stays white; every line and pore stays exactly as deep. It sets the look of the product on skin, never the framing.")
SIZE = "The stick is 12.7 cm long and 2.5 cm across, about the size of a lipstick, held in one hand."
GEO = ("THE SCENE SO FAR, an afternoon, the day Beth lets herself in: soft warm daylight, about 5000K, through the sheer curtains over the dressing table on the right, "
       "every face with a lit side and a soft shadow side. The bed with the dusty-blue quilt on the left of the room, the white dressing table and its big mirror under "
       "the window on the right, the stool tucked under it; the doorway behind the camera. The only people here are Susan and Beth.")
VOICE = lambda name: S1.VOICE(name)
NEG_PARTY = "no dusty-blue blouse, no emerald satin top, no pearl earrings, no Susan's hair loose or styled"
NEG_LABEL = "no brand name, label or lettering readable on the stick"
F = S1.F2
NOSPK = S1.NOSPK
CROWD = PS.fill(PS.ORIENT_C, "balm")

MEDIA = {"PROD-CLOSED": "7278afd1-9898-41bb-a85f-e23b1e645a73", "PROD-BALM": "e85268b0-5816-4e38-bf31-5f7f829ae31e", "PROD-BRUSH": "10c8c91d-dff7-4675-b394-d414a19f9ec8",
         "C3-FACE": "16a0127c-0945-4187-ae78-eabf7c732819", "N-AFTER-FACE": "860d3197-f292-42d0-9357-6d8b2427389a", "N-FACE": "67d1090e-3546-45d1-ae77-8a07bb5709fa",
         "OUT-N": "586a9154-89db-42db-87e0-bcf867a8969f", "OUT-C3": "99c03052-cd0c-473e-a711-9d21511f49cf", "HOLD": "b2a02fd1-8437-4028-9cdf-243320fc6b7a",
         "COLOUR": "db72e34c-7892-4e1e-ad8d-b3a88a523f10", "L-VANITY": "aeb31e74-e06d-4fdc-9c39-0893e78f59bd"}
FILE = {"PROD-CLOSED": "product/CLOSED.jpg", "PROD-BALM": "product/BALM_END_DEPLOYED.jpg", "PROD-BRUSH": "product/BRUSH_END_DEPLOYED.jpg",
        "C3-FACE": "body/SC05/ingredients/C3-FACE.png", "N-AFTER-FACE": "body/SC05/ingredients/N-AFTER-FACE.png", "N-FACE": "body/SC04/ingredients/N-FACE.png",
        "OUT-N": "body/SC05/ingredients/OUTFIT-N-D4_v1.png", "OUT-C3": "body/SC05/ingredients/OUTFIT-C3-D4_v1.png",
        "HOLD": "body/SC05/ingredients/PROD-HAND-CARD_v1.png", "COLOUR": "body/SC05/ingredients/COLOUR-FRONT-CARD_v1.png", "L-VANITY": "plates/L-VANITY_v1.png"}
AUDIO = {"L010": ("voice/sc05/C3_ref_L010.mp3", "b0ea156a-e9ab-4240-90e4-8e2adc06dc4e"), "L011": ("voice/sc05/N_ref_L011.mp3", "fcc73f66-eb24-48c6-a352-b160e28c1c70"),
         "L012_L013": ("voice/sc05/C3_ref_L012_L013.mp3", "15393217-2c6e-4780-b74e-cb540725c643"), "L014": ("voice/sc05/C3_ref_L014.mp3", "da487e58-ebe3-47c6-8411-6b10dc9ceea8"),
         "L015": ("voice/sc05/C3_ref_L015.mp3", "b610785f-5fbc-4514-9433-adf7d27f388f"), "L016": ("voice/sc05/C3_ref_L016.mp3", "172a987f-ffd0-4018-a92c-1a14e9ad2981"),
         "L012": ("voice/sc05/C3_ref_L012.mp3", "b75e2ffb-e396-4514-b6a8-72444ad937f2"), "L013": ("voice/sc05/C3_ref_L013.mp3", "e7a49bfd-71a9-4ca0-a589-7c1138f12de9"),
         "L014a": ("voice/sc05/C3_ref_L014a.mp3", "1963f18d-b31d-41b8-8170-de6074a0de89"), "L014b": ("voice/sc05/C3_ref_L014b.mp3", "935441ac-ae00-4cfa-9891-ee4620c04227"),
         "L017": ("voice/sc05/N_ref_L017.mp3", "24a0d5d0-2249-4aca-9a62-b01690551450"), "L018": ("voice/sc05/C3_ref_L018.mp3", "bc505bf0-6594-4f81-ab7b-8b2c975ee50d")}
MULTI = lambda n, st: (f"One scene covered in {n} shots within a single take, all on the same side of the action line, with the same light, look and wardrobe throughout. "
                       f"Frame 1: {st}. Everyone stays where the last shot left them. Each shot picks up the movement exactly where the last one left it, "
                       "and the action carries straight across every cut. ")
BASE_NEG = lambda *x: S1.negs(S1.NEG_EQUIP, S1.NEG_MORPH, *x, NEG_PARTY, S1.NEG_FILM, S1.NEG_SCENECUT, S1.NEG_DRAMA, S1.NEG_SOUND)
VIDFILE = {"SC05-T1": "body/SC05/SC05-T1_v1.mp4"}
VIDJOB = {"SC05-T1": "c6e783ab-6035-4f95-92cc-b05753e73ea0"}
T = {}

# T1 — SH01 + SH02: Beth walks in; Susan on the bed
st, en = R["SC05-SH01"]["start_pos"], R["SC05-SH02"]["end_pos"]
T["SC05-T1"] = dict(kind="multi", covers=["SC05-SH01", "SC05-SH02"], duration=14, motion="travels", refs=["C3-FACE", "OUT-C3", "N-FACE", "OUT-N", "L-VANITY"],
  audios=["L010", "L011"], line=L["L010"] + " " + L["L011"], start=st, end=en, product=False,
  title="Scene 5 · T1 — Beth arrives: 'There's a thing Saturday' / Susan on the bed (SH01–SH02)",
  prompt=" ".join([
    S1.manifest([("@image1", FACE_C3), ("@image2", OUT_C3), ("@image3", FACE_N), ("@image4", OUT_N), ("@image5", ROOM),
                 ("@audio1", VOICE("Beth")), ("@audio2", VOICE("Susan"))]),
    SERIES, S1.LOOK, S1.INHERIT, GEO, NOSPK,
    f"THE EXCHANGE, word for word and in this order: {L['L010']} {L['L011']} — Beth says the first three sentences; Susan says the rest. Nobody else speaks.",
    MULTI(2, st) +
    f"SHOT 1, [0s-5s]: WIDE in profile at eye level from the doorway, Camera on a tripod, locked: Susan, {SUSAN_ID}, in {SUSAN_D4}, sits on the end of the bed at frame left, facing into the room. "
    f"Beth, {BETH_ID}, in {BETH_D4}, the black garment bag over her shoulder, walks in past the camera from behind it — three unhurried steps — and stops in profile between the bed and the dressing table, "
    f"facing Susan, and says it plainly: {L['L010']} "
    f"SHOT 2, [5s-14s]: MEDIUM CLOSE-UP from a little above, three-quarter on Susan on the end of the bed: she does not get up; she looks down at her hands in her lap and says it to them: {L['L011']} "
    "On 'Beth' her eyes come up to Beth for a moment, then go back down. Beth stays standing inside the door, the bag on her shoulder, at the edge of frame. "
    "Each cut lands on a completed line. Nobody looks into the lens. Last frame: " + en + ".",
    F, S1.PHYS,
    "While Susan speaks she keeps doing one thing with her hands: her fingers loosely laced in her lap, at one steady hold through the line. It is ordinary and still, and the hands never stop to gesture.",
    "LISTENING: Susan takes Beth's line without moving; Beth's easy face drops a little at 'ten years younger'; nothing on either face arrives before the word that causes it.",
    S1.state("SUSAN", "sitting on the end of the bed in the sweatshirt, hair scraped back, her face bare and tired", "her eyes coming up to Beth once"),
    "FOCUS: SHOT 1 deep, both women sharp; SHOT 2 Susan's nearest eye sharp, Beth soft at the edge. The blur is optical: soft and round, never smeared.",
    S1.dialogue("Beth", L["L010"], VOICE_C3, "she has let herself in to her best friend's house and found her on the bed in the afternoon. Standing, speaking to Susan.",
                "won't take no. Opens light, as news; turns on 'Whole group', as if obvious; exits on 'You're coming', a plain fact. Stress on 'coming'.",
                "easy, bright, conversational, matching the face in this shot.", "she is worried about her friend, which leaks only through how lightly she says it."),
    S1.dialogue("Susan", L["L011"], S1.VOICE_N, "her friend wants her at a party with the people who watched it happen. Sitting, speaking to her hands.",
                "refuses without heat. Opens flat, half a question; turns on 'ten years younger', quieter; exits on 'Everyone saw it', almost nothing. Stress on 'saw'.",
                "low, flat, tired, matching the face in this shot.", "the shame of the party, which leaks only through how still she keeps."),
    S1.AUD,
    BASE_NEG("no Susan standing up, no garment bag opening, no third person, no one looking into the lens")]),
  risks=[{"risk": "the voices swap", "prevented_by": "Audio1 Beth's own words, Audio2 Susan's own words, THE EXCHANGE names who says what in order"},
         {"risk": "party clothes or Susan's hair loose (sheets show both)", "prevented_by": "face crops + D4 outfit cards, ponytail named, NEG_PARTY"},
         {"risk": "the camera follows Beth's walk", "prevented_by": "F2 locked, she walks through the frame"}])

# §28H: L012+L013 (39 words), L014 (34) and L016+L017 (37) do not fit one 15 s take at the refs' own pace, so those rows split on the line's
# sentence ("length", §24K part 5): SH03 | SH04, L014 across SH05 | SH06 (the act map already gives SH06 the line's end), SH08–09 | SH10–11.
L014A, L014B = L["L014"].split(" Goes on white")[0], "Goes on white" + L["L014"].split(" Goes on white")[1]
L016A, L016B = L["L016"].split(" It just")[0], "It just" + L["L016"].split(" It just")[1]

# T2 — SH03: Paula's Botox, the garment bag laid down
# Fix 1 (user's board Fix, 2026-10-03, owner note: "susan should be seating on the bed use this scene as reference but in the defferent camera angle
# Scene 5 · T1"): v1 sat Susan low BESIDE the bed, the mattress at her shoulder — the prompt put her "on the end of the bed at the edge of frame" of a
# MEDIUM three-quarter on Beth, so only her head and shoulders were placed and the model dropped her below the bed. Fixed at the source: confirmed T1 as
# @video1 for Susan's seat and the room, a SEAT clause (on the quilt at the bed's end, as in @video1), both women framed in full by a new angle (low
# three-quarter from the doorway corner at her seated eye height — neither of T1's two set-ups), the bag laid across the quilt BEHIND her, seat negatives.
SEATV2 = ("is where Susan sits and how the room lies: Susan on the end of the bed, on the quilt, as in this clip; it sets her seat, the bed, the door and the "
          "dressing table, never the framing, the words or the action.")
SEAT2 = ("Susan's seat is exactly the one in @video1: she sits ON the end of the bed, on the dusty-blue quilt, her hips on the mattress, her knees bent over "
         "its edge and her feet in grey socks flat on the carpet, facing into the room toward the dressing table; she stays sitting there the whole clip.")
NEG_SEAT2 = "no Susan sitting on the floor, no Susan below the mattress, no Susan beside the bed, no Susan standing"
st, en = R["SC05-SH03"]["start_pos"], "Beth beside the bed, the garment bag laid flat across the quilt behind Susan; Susan on the end of the bed looking up at her"
T["SC05-T2"] = dict(kind="take", covers=["SC05-SH03"], duration=13, motion="in_place", refs=["C3-FACE", "OUT-C3", "N-FACE", "OUT-N", "L-VANITY"],
  videos=["SC05-T1"], audios=["L012"], line=L["L012"], start=st, end=en, product=False, generation=2,
  fault="susan should be seating on the bed use this scene as reference but in the defferent camera angle Scene 5 · T1",
  fix_note=("prompt fault: Susan was placed only as 'on the end of the bed at the edge of frame' of a MEDIUM on Beth, so v1 sat her low beside the bed → "
            "confirmed T1 attached as @video1 for her seat, SEAT clause (on the quilt at the bed's end, feet on the carpet), a new low three-quarter angle from the doorway corner "
            "at her seated eye height that frames both women in full, the bag laid behind her on the quilt, NEG_SEAT2"),
  title="Scene 5 · T2 — Beth on Paula's Botox, laying the garment bag down (SH03)",
  prompt=" ".join([
    S1.manifest([("@image1", FACE_C3), ("@image2", OUT_C3), ("@image3", FACE_N), ("@image4", OUT_N), ("@image5", ROOM), ("@video1", SEATV2), ("@audio1", VOICE("Beth"))]),
    SERIES, S1.LOOK, S1.INHERIT, GEO, SEAT2, NOSPK,
    "One continuous shot, never cut and never restarted, 13s, in one place with the same light, look and wardrobe throughout. Frame 1: " + st + ", sitting on it exactly as in @video1. "
    f"MEDIUM WIDE from low, at Susan's seated eye height, from the corner by the doorway, lower and closer than @video1's wide, three-quarter front on Susan, {SUSAN_ID}, in {SUSAN_D4}, sitting on the end of the bed at frame left, the whole of her in frame from her ponytail to her socks on the carpet; "
    f"Beth, {BETH_ID}, in {BETH_D4}, stands beside the bed just behind her at frame right, the whole bed end and the quilt between them. "
    f"[0s-9s]: Beth lays the black garment bag flat across the dusty-blue quilt behind Susan while she talks, easy and honest, and smooths it once with one hand: {L['L012']} "
    "[9s-13s]: she straightens up and looks down at Susan; Susan, still sitting on the bed, turns her head and looks up at her. Last frame: " + en + ".",
    F, S1.PHYS,
    "While Beth speaks Susan keeps doing one thing with her hands: her fingers loosely laced in her lap, as in @video1, at one steady hold through the line.",
    "LISTENING: Susan looks up at Beth on 'Botox'; nothing on her face arrives before the word that causes it.",
    S1.state("SUSAN", "sitting on the end of the bed in the sweatshirt, hair scraped back, her face bare, guarded", "her eyes coming up to Beth"),
    "FOCUS: deep enough that both women read; Beth's eyes sharpest. The blur is optical: soft and round, never smeared.",
    S1.dialogue("Beth", L["L012"], VOICE_C3, "her friend thinks she just looks old next to Paula. Standing by the bed, laying the bag down.",
                "levels with her. Opens matter-of-fact on 'Botox'; turns on 'needles', a small shrug; exits on 'twelve weeks', plain. Stress on 'needles'.",
                "easy, honest, a little lower than before, matching the face in this shot.", "she is on Susan's side, which leaks only through how ordinary she makes it sound."),
    S1.AUD,
    BASE_NEG("no Susan speaking, no garment bag unzipped, no third person, no stick or product in this take", NEG_SEAT2)]),
  risks=[{"risk": "Susan below or beside the bed again (v1 fault)", "prevented_by": "@video1 = confirmed T1 for her seat, SEAT2 clause, framed head to socks, NEG_SEAT2"},
         {"risk": "Susan speaks Beth's words", "prevented_by": "one voice ref, Beth's own words; NOSPK; 'no Susan speaking'"},
         {"risk": "party clothes or Susan's hair loose", "prevented_by": "face crops + D4 outfit cards, ponytail named, NEG_PARTY"}])

# T3 — SH04: 'Come sit. Watch this.'
st, en = "Beth beside the bed by the laid-down garment bag; Susan on the end of the bed looking up at her", R["SC05-SH04"]["end_pos"]
T["SC05-T3"] = dict(kind="take", covers=["SC05-SH04"], duration=8, motion="travels", refs=["C3-FACE", "OUT-C3", "N-FACE", "OUT-N", "L-VANITY"],
  audios=["L013"], line=L["L013"], start=st, end=en, product=False,
  title="Scene 5 · T3 — 'Come sit. Watch this.': the stool, Susan sits at the mirror (SH04)",
  prompt=" ".join([
    S1.manifest([("@image1", FACE_C3), ("@image2", OUT_C3), ("@image3", FACE_N), ("@image4", OUT_N), ("@image5", ROOM), ("@audio1", VOICE("Beth"))]),
    SERIES, S1.LOOK, S1.INHERIT, GEO, NOSPK,
    "One continuous shot, never cut and never restarted, 8s, in one place with the same light, look and wardrobe throughout. Frame 1: " + st + ". "
    f"MEDIUM WIDE in profile at eye level, Camera on a tripod, locked, the bed on the left and the dressing table on the right both in frame: Beth, {BETH_ID}, in {BETH_D4}, says softly: {L['L013']} "
    "[0s-4s]: as she speaks she crosses two steps to the dressing table, pulls the stool out with one hand and nods Susan to it. "
    f"[4s-8s]: Susan, {SUSAN_ID}, in {SUSAN_D4}, gets up from the bed, takes three slow steps and sits on the stool facing the mirror; Beth stands at her left shoulder. Last frame: " + en + ".",
    F, S1.PHYS,
    "LISTENING: Susan's face loosens a little on 'You don't need to'; she gets up only after 'Come sit'; nothing arrives before the words.",
    S1.state("SUSAN", "the sweatshirt, hair scraped back, her face bare, guarded but going along", "her getting up and sitting at the mirror"),
    "FOCUS: deep, both women sharp. The blur is optical: soft and round, never smeared.",
    S1.dialogue("Beth", L["L013"], VOICE_C3, "she has just told Susan what Paula did. Walking to the dressing table, pulling the stool out.",
                "takes the pressure off, then invites. Opens on 'I'm not saying', gentle; turns on 'You don't need to', warmer; exits on 'Watch this', lighter. Stress on 'need'.",
                "softer, warm, matching the face in this shot.", "she wants Susan to say yes, which leaks only through the small smile."),
    S1.AUD,
    BASE_NEG("no Susan speaking, no third person, no stick or product in this take, no camera following the walk")]),
  risks=[{"risk": "the camera follows the walk", "prevented_by": "F2 locked, a wide holding bed and table, 'no camera following the walk'"},
         {"risk": "Susan sits before the line", "prevented_by": "timed beats, LISTENING clause"},
         {"risk": "Susan speaks Beth's words", "prevented_by": "one voice ref, NOSPK, 'no Susan speaking'"}])

# T4 — SH05: chin to the light, the closed stick out, the balm end uncapped
st, en = R["SC05-SH05"]["start_pos"], R["SC05-SH05"]["end_pos"]
T["SC05-T4"] = dict(kind="take", covers=["SC05-SH05"], duration=15, motion="in_place",
  refs=["PROD-CLOSED", "PROD-BALM", "HOLD", "C3-FACE", "OUT-C3", "N-FACE", "OUT-N", "L-VANITY"], audios=["L014a"], line=L014A, start=st, end=en, product=True,
  title="Scene 5 · T4 — Beth tilts Susan's chin, takes out the closed stick, uncaps the balm end (SH05)",
  prompt=" ".join([
    S1.manifest([("@image1", PROD("closed")), ("@image2", PROD("balm")), ("@image3", HOLDV), ("@image4", FACE_C3), ("@image5", OUT_C3), ("@image6", FACE_N),
                 ("@image7", OUT_N), ("@image8", ROOM), ("@audio1", VOICE("Beth"))]),
    SERIES, S1.LOOK, S1.INHERIT, GEO, NOSPK,
    "One continuous shot, never cut and never restarted, 15s, in one place with the same light, look and wardrobe throughout. Frame 1: " + st + ". "
    f"MEDIUM CLOSE-UP from a little above, three-quarter over the dressing table toward the mirror: Susan, {SUSAN_ID}, in {SUSAN_D4}, seated on the stool facing the mirror; "
    f"Beth, {BETH_ID}, in {BETH_D4}, standing at her left shoulder, says: {L014A} "
    "[0s-5s]: Beth tilts Susan's chin toward the window with two fingers, looking at her skin in the light. "
    "[5s-10s]: she takes exactly one closed violet stick from her jeans pocket with her right hand, her palm wrapped over the barrel so no lettering shows, and holds it low by Susan's cheek. "
    "[10s-15s]: her left hand draws the cap off the balm end straight along the barrel in one unhurried pull, without twisting, and the white balm end comes clear exactly as it already was; "
    "the cap stays in her left hand, low, out of the way. " + SIZE + " Last frame: " + en + ".",
    F, S1.PHYS,
    PS.fill(PS.UNCAP_LOCK, "balm").replace("The cap is still in the second hand and still travelling at the cut, the movement unfinished.", "The cap ends in her left hand, held low."),
    CROWD.replace("One wordmark only, set along the barrel on its front centreline below the working end, upright to the balm end, never across the barrel and never twice in frame. ",
                  "Her palm covers the barrel's front, so no lettering is seen. "),
    "Exactly one stick and exactly one cap the whole time. Clothing, walls and furniture plain — no lettering, logos or labels anywhere.",
    "LISTENING: Susan lets her chin be turned and watches Beth in the mirror; her eyes drop to the stick when it comes out; nothing on her face arrives before the words.",
    S1.state("SUSAN", "seated at the mirror in the sweatshirt, hair scraped back, her face bare, wary but letting it happen", "her chin turned to the window"),
    "FOCUS: Susan's cheek and the stick sharp; the mirror and the room behind soft. The blur is optical: soft and round, never smeared.",
    S1.dialogue("Beth", L014A, VOICE_C3, "she has Susan at the mirror at last. Standing at her shoulder, close, the stick coming out.",
                "explains it like a friend, not a salesperson. Opens on 'Everything you've been wearing', plain; turns on 'ages you'; exits on 'made for us', warmer. Stress on 'us'.",
                "easy, close, a little quieter at the mirror, matching the face in this shot.", "she has been through this herself, which leaks only through how sure she sounds."),
    S1.AUD,
    BASE_NEG(PS.fill(PS.NEG_UNCAP, "balm"), "no second stick, no lettering on the stick, no balm touching the skin yet, no Susan speaking")]),
  risks=[{"risk": "the stick twists up or the cap goes back on", "prevented_by": "UNCAP_LOCK, NEG_UNCAP"},
         {"risk": "the wordmark shows before the hero (F10)", "prevented_by": "palm over the barrel, 'no lettering on the stick'"},
         {"risk": "the stick doubles or changes shape", "prevented_by": "product photos first, 'exactly one stick and exactly one cap', size anchor"}])

# T5 — SH06 insert: the white stripe — 'Goes on white, don't panic.' heard from Beth, out of frame
st, en = R["SC05-SH06"]["start_pos"], R["SC05-SH06"]["end_pos"]
T["SC05-T5"] = dict(kind="take", covers=["SC05-SH06"], duration=4, motion="in_place", refs=["PROD-BALM", "COLOUR", "N-FACE"], audios=["L014b"], line=L014B, start=st, end=en, product=True,
  title="Scene 5 · T5 — Insert: the balm draws a white stripe up her cheekbone — 'Goes on white, don't panic.' (SH06)",
  prompt=" ".join([
    S1.manifest([("@image1", PROD("balm")), ("@image2", COLOURV), ("@image3", FACE_N), ("@audio1", VOICE("Beth"))]),
    SERIES, S1.LOOK, S1.INHERIT,
    "THE SCENE SO FAR: Susan seated at her dressing table in the warm afternoon window light from the right; Beth, out of frame beside her, holds the uncapped stick at her cheek.",
    f"Beth's words, heard from just out of frame: {L014B} Only Beth speaks; Susan's mouth stays closed.",
    "One continuous shot, never cut and never restarted, 4s, in one place with the same light, look and wardrobe throughout. Frame 1: " + st + ". "
    "EXTREME CLOSE-UP in profile at eye level on Susan's cheekbone, the real lines at the corner of her eye in frame, a strand of her scraped-back hair at the edge. "
    "[0s-3s]: Beth's fingers hold exactly one violet stick, the white balm end against the skin; the balm's flat crest draws one slow stripe up the cheekbone, about four centimetres long, "
    "leaving an opaque warm white band on the skin. [3s-4s]: the stick lifts away out of frame. " + SIZE + " Last frame: " + en + ".",
    F, S1.PHYS,
    PS.fill(PS.CONTACT_LOCK_C, "balm"), PS.TERRAIN_LOCK,
    "The barrel's lettered side faces her cheek, away from the lens: no lettering is seen. Exactly one stick in frame.",
    S1.state("SUSAN", "seated at the mirror, hair scraped back, her face bare, holding still for it", "the white stripe on her cheek"),
    "FOCUS: the balm crest and the stripe sharp; her eye a little soft. The blur is optical: soft and round, never smeared.",
    S1.dialogue("Beth (heard, just out of frame)", L014B, VOICE_C3, "the stripe goes on white and she knows how it looks. At Susan's shoulder, the stick at her cheek.",
                "heads off the alarm. Opens on 'Goes on white', light; exits on 'don't panic', a grin in it. Stress on 'white'.",
                "close, easy, amused, matching the work in this shot.", "she remembers panicking herself, which leaks only through the grin."),
    S1.AUD,
    S1.negs(S1.NEG_EQUIP, S1.NEG_MORPH, PS.NEG_CONTACT, PS.NEG_SURFACE_FAILURES, "no lettering on the stick, no second stick, no brush in this clip, no Susan speaking",
            S1.NEG_FILM, S1.NEG_SCENECUT, S1.NEG_DRAMA, S1.NEG_SOUND)]),
  risks=[{"risk": "the balm floats above the skin or fills the lines", "prevented_by": "CONTACT_LOCK_C, TERRAIN_LOCK, NEG_CONTACT"},
         {"risk": "the stripe looks grey or foamy", "prevented_by": "COLOUR card, NEG_SURFACE_FAILURES"},
         {"risk": "the wordmark shows (F10)", "prevented_by": "lettered side to her cheek, 'no lettering on the stick'"}])

# T6 — SH07 insert: the brush; white to her shade behind it
st, en = R["SC05-SH07"]["start_pos"], R["SC05-SH07"]["end_pos"]
T["SC05-T6"] = dict(kind="take", covers=["SC05-SH07"], duration=13, motion="in_place", refs=["PROD-BRUSH", "COLOUR", "N-FACE", "N-AFTER-FACE"], audios=["L015"], line=L["L015"],
  start=st, end=en, product=True,
  title="Scene 5 · T6 — Insert: the brush works the stripe; white turns to her skin behind it (SH07)",
  prompt=" ".join([
    S1.manifest([("@image1", PROD("brush")), ("@image2", COLOURV), ("@image3", FACE_N), ("@image4", FACE_NA), ("@audio1", VOICE("Beth"))]),
    SERIES, S1.LOOK, S1.INHERIT,
    "THE SCENE SO FAR: Susan seated at her dressing table in the warm afternoon window light from the right, a white stripe of balm up her cheekbone; Beth beside her, out of frame except her hand.",
    f"Beth's words, heard from just out of frame: {L['L015']} Only Beth speaks; Susan's mouth stays closed.",
    "One continuous shot, never cut and never restarted, 13s, in one place with the same light, look and wardrobe throughout. Frame 1: " + st + ". "
    "CLOSE-UP straight on at eye level on Susan's cheek and eye, her face as @image3 at the start. "
    "[0s-10s]: Beth's hand holds exactly one violet stick by its lower barrel, brush end working; the side of the white brush crown works the stripe in slow, small circles from its lower end upward. "
    "Behind the brush the white thins and turns to Susan's own skin tone; ahead of the brush the stripe stays opaque white; the change happens only where the brush has been. "
    "[10s-13s]: the brush lifts away; the cheek is evened, as @image4 shows, every line and pore still there. Susan blinks once. " + SIZE + " Last frame: " + en + ".",
    F, S1.PHYS,
    PS.fill(PS.CONTACT_LOCK_C, "brush"), PS.TERRAIN_LOCK,
    "The barrel's lettered side faces her cheek, away from the lens: no lettering is seen. Exactly one stick in frame.",
    "LISTENING: Susan's eyes shift toward Beth's voice on 'your exact shade'; nothing arrives before the words.",
    S1.state("SUSAN", "seated at the mirror, hair scraped back, the stripe on her cheek, still", "the stripe turning to her own tone"),
    "FOCUS: the brush crown and the colour edge sharp; her eye a little soft. The blur is optical: soft and round, never smeared.",
    S1.dialogue("Beth (heard, just out of frame)", L["L015"], VOICE_C3, "she is putting it on her friend's face. Standing at her shoulder, working the brush.",
                "talks her through it, practical. Opens on 'It reads your skin', plain; turns on 'takes the red down'; exits on 'cracking on top', satisfied. Stress on 'exact'.",
                "close, quiet, unhurried, matching the work in this shot.", "she wants Susan to see it work, which leaks only through how slowly she goes."),
    S1.AUD,
    S1.negs(S1.NEG_EQUIP, S1.NEG_MORPH, PS.NEG_CONTACT, PS.NEG_LOOK, "no lettering on the stick, no second stick, no Susan speaking", S1.NEG_FILM, S1.NEG_SCENECUT, S1.NEG_DRAMA, S1.NEG_SOUND)]),
  risks=[{"risk": "colour appears ahead of the brush / the whole cheek at once", "prevented_by": "COLOUR card, 'only where the brush has been', NEG_CONTACT"},
         {"risk": "lines erased (cover, not erase)", "prevented_by": "TERRAIN_LOCK, NEG_CONTACT, NEG_LOOK"},
         {"risk": "Susan mouths Beth's line", "prevented_by": "Beth out of frame, 'Susan's mouth stays closed'"}])

# T7 — SH08 + SH09: cover, not erase; Susan in the mirror
st, en = R["SC05-SH08"]["start_pos"], "Susan seated at the mirror, leaning an inch toward it, looking at her cheek; Beth one step behind her left shoulder"
T["SC05-T7"] = dict(kind="multi", covers=["SC05-SH08", "SC05-SH09"], duration=15, motion="still", refs=["C3-FACE", "OUT-C3", "N-AFTER-FACE", "OUT-N", "L-VANITY"],
  audios=["L016"], line=L["L016"], start=st, end=en, product=False,
  title="Scene 5 · T7 — Beth steps back: 'It won't erase a wrinkle'; Susan in the mirror (SH08–SH09)",
  prompt=" ".join([
    S1.manifest([("@image1", FACE_C3), ("@image2", OUT_C3), ("@image3", FACE_NA), ("@image4", OUT_N), ("@image5", ROOM), ("@audio1", VOICE("Beth"))]),
    SERIES, S1.LOOK, S1.INHERIT, GEO, NOSPK,
    f"Beth's words, in this order: {L['L016']} Only Beth speaks.",
    MULTI(2, st) +
    f"SHOT 1, [0s-7s]: MEDIUM at eye level, three-quarter from the dressing table's corner: Beth, {BETH_ID}, in {BETH_D4}, the closed stick in her right hand, steps one step back behind "
    f"Susan's left shoulder and talks to Susan's reflection; Susan, {SUSAN_ID}, in {SUSAN_D4}, seated on the stool facing the mirror: {L016A} "
    f"SHOT 2, [7s-15s]: CLOSE-UP straight on, in the mirror: Susan's reflection leans an inch toward the glass and looks at her own cheek, the tone evened, every line still there, "
    f"while Beth's voice, behind her, finishes: {L016B} "
    "Each cut lands on a completed line. Nobody looks into the lens. Last frame: " + en + ".",
    F, S1.PHYS,
    "The mirror shows exactly what is in front of it: one Susan, one reflection, the same moves at the same moment, the room behind her reversed.",
    "While Beth speaks she keeps doing one thing with her hands: the closed stick held low in her right hand at her side, at one steady hold through the line. It is ordinary and still, and the hands never stop to gesture.",
    "LISTENING: Susan's eyes go to her own cheek on 'first thing anyone sees' and stay there; nothing arrives before the words.",
    S1.state("SUSAN", "seated at the mirror in the sweatshirt, hair scraped back, the foundation on, every line still there", "her lean to the glass"),
    "FOCUS: SHOT 1 Beth's eyes sharp; SHOT 2 her reflection's cheek and eyes sharp. The blur is optical: soft and round, never smeared.",
    S1.dialogue("Beth", L["L016"], VOICE_C3, "Susan is looking at herself. Standing behind her shoulder, talking to her reflection.",
                "tells the truth about it. Opens on 'It won't erase a wrinkle', plain; turns on 'the first thing anyone sees'; exits on 'Thirty seconds', light. Stress on 'first'.",
                "easy, warm, unhurried, matching the face in this shot.", "she is proud of her friend's face, which leaks only through the smile in her voice."),
    S1.AUD,
    BASE_NEG("no lines erased, no smooth flawless skin, no reflection moving on its own, no second Susan, no tears, no lettering on the stick, no Susan speaking")]),
  risks=[{"risk": "the reflection breaks", "prevented_by": "mirror clause, 'no reflection moving on its own, no second Susan'"},
         {"risk": "the after face reads as erased or the hair goes styled (N-AFTER sheet has waves)", "prevented_by": "FACE_NA keeps the ponytail and the lines, NEG_PARTY"},
         {"risk": "Susan speaks Beth's words", "prevented_by": "one voice ref, NOSPK, 'no Susan speaking'"}])

# T8 — SH10 + SH11: '…and this is all you did?' / 'This is all I did.'
st, en = en, R["SC05-SH11"]["end_pos"]
T["SC05-T8"] = dict(kind="multi", covers=["SC05-SH10", "SC05-SH11"], duration=6, motion="still", refs=["C3-FACE", "OUT-C3", "N-AFTER-FACE", "OUT-N", "L-VANITY"],
  audios=["L017", "L018"], line=L["L017"] + " " + L["L018"], start=st, end=en, product=False,
  title="Scene 5 · T8 — '…and this is all you did?' / 'This is all I did.' (SH10–SH11)",
  prompt=" ".join([
    S1.manifest([("@image1", FACE_C3), ("@image2", OUT_C3), ("@image3", FACE_NA), ("@image4", OUT_N), ("@image5", ROOM), ("@audio1", VOICE("Susan")), ("@audio2", VOICE("Beth"))]),
    SERIES, S1.LOOK, S1.INHERIT, GEO, NOSPK,
    f"THE EXCHANGE, word for word and in this order: {L['L017']} {L['L018']} — Susan asks the first; Beth answers. Nobody else speaks.",
    MULTI(2, st) +
    f"SHOT 1, [0s-3s]: CLOSE-UP from a little below, three-quarter on Susan, {SUSAN_ID}, in {SUSAN_D4}: she turns her head a little toward Beth behind her and says, quietly: {L['L017']} "
    f"SHOT 2, [3s-6s]: MEDIUM CLOSE-UP at eye level, three-quarter on Beth, {BETH_ID}, in {BETH_D4}, behind Susan's left shoulder, the soft edge of Susan's ponytail in the near foreground: "
    f"she meets Susan's eyes, nods once and says it plainly: {L['L018']} A small easy smile after. "
    "Each cut lands on a completed line. The eyelines match. Nobody looks into the lens. Last frame: " + en + ".",
    F, S1.PHYS,
    "While Beth speaks she keeps doing one thing with her hands: the closed stick held low in her right hand at her side, at one steady hold through the line. It is ordinary and still, and the hands never stop to gesture.",
    "LISTENING: Beth lets Susan's question land before she nods; nothing arrives before the words.",
    S1.state("SUSAN", "seated at the mirror, hair scraped back, the foundation on, every line still there, something coming back", "her turn to Beth"),
    "FOCUS: SHOT 1 Susan's nearest eye sharp; SHOT 2 Beth's nearest eye sharp, Susan's shoulder soft. The blur is optical: soft and round, never smeared.",
    S1.dialogue("Susan", L["L017"], S1.VOICE_N, "she can see her own face again. Seated, turning to Beth.",
                "can't quite believe it. Opens trailing; exits on 'all you did?', a real question. Stress on 'all'.",
                "quiet, low, almost a whisper, matching the face in this shot.", "something is coming back, which leaks only through how quiet she is."),
    S1.dialogue("Beth", L["L018"], VOICE_C3, "Susan has asked if that is all. Standing behind her, meeting her eyes.",
                "answers it straight. One beat, plain; exits on 'did', with the nod. Stress on 'all'.",
                "easy, low, certain, matching the face in this shot.", "she is glad, which leaks only through the small smile after."),
    S1.AUD,
    BASE_NEG("no lines erased, no lettering on the stick, no third person, no tears")]),
  risks=[{"risk": "the voices swap", "prevented_by": "Audio1 Susan's own words, Audio2 Beth's own words; THE EXCHANGE in order"},
         {"risk": "the after face reads as erased or the hair goes styled", "prevented_by": "FACE_NA keeps the ponytail and the lines, NEG_PARTY"},
         {"risk": "the eyeline breaks across the cut", "prevented_by": "same side of the line (MULTI), 'The eyelines match'"}])

if __name__ == "__main__":
    for b, s in T.items():
        call = {"beat": b, "build": "facelove-my-mother", "connector": "seedance", "model": "seedance_2_5", "mode": 4, "kind": s["kind"], "prompt": s["prompt"],
                "take": b, "covers": s["covers"], "start_pos": s["start"], "end_pos": s["end"], "duration": s["duration"], "resolution": "720p", "aspect_ratio": "9:16",
                "start_image": None, "ingredients_approved": True, "files": [FILE[r] for r in s["refs"]] + [VIDFILE[v] for v in s.get("videos", [])] + [AUDIO[a][0] for a in s["audios"]],
                "audios": [AUDIO[a][0] for a in s["audios"]], "generate_audio": bool(s["line"]), "dialogue": s["line"] or None, "script_line": s["line"] or None,
                "pace": "brisk", "subject_motion": s["motion"], "prefer_multi_shots": "false", "generation": s.get("generation", 1), "product": s["product"],
                "user_go": "chat: \"CONFIRMED ALL IMAGE. PROCEED\" (user, 2026-10-02) — Scene 5's ingredient cards confirmed",
                "risks": s["risks"], "scene": 5, "title": s["title"], "taste": ["HT17", "HT18", "HT22", "HT23", "HT25", "HT26", "HT27"],
                "media": [MEDIA[r] for r in s["refs"]], "audio_media": [AUDIO[a][1] for a in s["audios"]],
                "video_jobs": [VIDJOB[v] for v in s.get("videos", [])]}
        if s.get("fix_note"): call.update(fault=s["fault"], fix_note=s["fix_note"], user_go="board Fix (owner, 2026-10-03): " + s["fault"])
        (H / f"{b}.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
        (H / f"{b}.prompt.txt").write_text(s["prompt"])
        print(b, s["duration"], "s", len(s["prompt"]), "chars")
