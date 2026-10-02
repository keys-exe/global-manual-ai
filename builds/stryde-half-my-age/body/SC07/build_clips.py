"""Scenes 7 + 8 (day B5, the same morning as SC05/SC06) — SEEDANCE 2.5 takes on Kie AI, ingredients only, no frames.
The user: "confirmed next scene" (SC0506-T1 confirmed), then "confirmed" (INFO-KNEE-N v1, 2026-10-02).
Takes (§24K part 5): SC07-T1 = SH01–SH03 (landing: the strap seated, the first steps down, no banister), SC07-T2 = SH04–SH06
(Barbara in the hall below, the last steps onto the carpet, she looks back up) — both silent, VO L042–L045 laid in the edit;
SC08-T1 = SH01 (L046), SC08-T2 = SH02–SH03 (L047), SC08-T3 = SH04–SH05 (L048 + L049) — split for length (Barbara ≈ 25 s).
The house's geography is SC02's (HT22): from the front door the stairs rise along the LEFT wall, the banister on the open RIGHT side;
from the landing looking down, the banister runs down the left and the photographs down the right. The kitchen seats are SC0506-T1's
(Her at the near end side-on to the window, Barbara across with her back to it — the user: "so the positon of the two is consistent").
FP19: no box anywhere — Barbara taps the table beside her mug. The strap is the spare Barbara gave her, now on Her's RIGHT knee (FP18)."""
import json
import sys
import importlib.util
from pathlib import Path

H = Path(__file__).parent
B = H.parents[1]
_spec = importlib.util.spec_from_file_location("sc05_clips", B / "body" / "SC05" / "build_clips.py")
S5 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(S5)
_spec2 = importlib.util.spec_from_file_location("sc02_clips", B / "body" / "SC02" / "build_clips.py")
S2 = importlib.util.module_from_spec(_spec2)
sys.argv, _argv = [sys.argv[0], "__none__"], sys.argv
_spec2.loader.exec_module(S2)
sys.argv = _argv
SERIES, LOOK, INHERIT, F2, F1, PHYS, AUD, SILENT = S5.SERIES, S5.LOOK, S5.INHERIT, S5.F2, S5.F1, S5.PHYS, S5.AUD, S5.SILENT
NEG_EQUIP, NEG_MORPH, NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND = S5.NEG_EQUIP, S5.NEG_MORPH, S5.NEG_FILM, S5.NEG_SCENECUT, S5.NEG_DRAMA, S5.NEG_SOUND
NEG_STAIRS = S2.NEG_STAIRS
manifest, PLACE, VOICE, state, negs, dialogue, SHEET = S5.manifest, S5.PLACE, S5.VOICE, S5.state, S5.negs, S5.dialogue, S5.SHEET
HER_ID, BARB_ID, HER_B5, BARB_B5, FACE_N, CARD_N, CARD_ROUTINE, CARD_KNEE, STRAP, KITCHEN, VOICE_C1 = (
    S5.HER_ID, S5.BARB_ID, S5.HER_B5, S5.BARB_B5, S5.FACE_N, S5.CARD_N, S5.CARD_ROUTINE, S5.CARD_KNEE, S5.STRAP, S5.KITCHEN, S5.VOICE_C1)
HOUSE, STAIRS, HALL = S2.HOUSE, S2.STAIRS, S2.HALL

KNEE_N = ("is an info card: Her own right knee with the strap on it — copy the strap's place exactly: the bottom of the kneecap sits in the shell's centre notch, "
          "the shell on the tendon just under it, the whole kneecap visible above, the shirt-dress hem a hand's width above the knee; its caption strip never appears in the clip.")
STRAP_ON = ("THE STRAP is on Her's RIGHT knee only, her left leg bare — exactly Image2's place: the bottom of the kneecap in the shell's notch, the shell small, about 12 by 5 centimetres, "
            "rigid and matte black with the grey stryde wordmark toward us; it never bends, slides or changes size.")
STEPS_DOWN = ("Each step is spelled out: one foot moves forward and down onto the very next tread and lands flat, then the other foot moves past it down onto the tread below that — "
              "one tread per step, never two at once, never skipping a tread, never shuffling; she walks down normally, at an easy steady pace, about one step a second.")
B5_STAIRS = ("THE SCENE SO FAR, the same bright morning as the kitchen, one continuous moment: soft morning daylight, about 5600K, through the frosted landing window; the lamps are off. "
             "Her, in the outfit of her card, has come upstairs and has the spare strap Barbara gave her. Barbara has come out of the kitchen into the hall to watch.")
B5_TABLE = ("THE SCENE SO FAR, the same bright morning, one continuous moment, back in her kitchen after the stairs: soft morning daylight about 5600K from the side window on the left of the table. "
            "Her, in the outfit of her card, sits in the same chair as before at the near end of the long side of the pine table, side-on to the window, the strap on her RIGHT knee; "
            "Barbara, in her own gilet and shorts, sits in the same chair across the table from her with her back to the side window, her mug of tea in front of her, her own strap on her bare right knee. "
            "On the table: exactly the five objects of the table card in their places. No box, no packaging anywhere.")
SEATS = ("THE POSITIONS NEVER CHANGE: Her always on the left of frame at the near end of the table, Barbara always on the right across the table with the window behind her; "
         "nobody stands, moves chairs or swaps sides, and every shot is taken from the same side of the table.")
NOSPK = S5.NOSPK
NOMOUTH = "Nobody speaks in this clip: every mouth stays closed and every jaw still from the first frame to the last."

L046 = "Everything you’ve tried was designed to make you comfortable while your knee got worse. This one fixes why it hurts."
L047 = "There’s one spot below the kneecap where every step lands. Every brace, every injection, every pill you’ve ever taken treated the whole knee. Not that spot."
L048 = "That’s why nothing worked. The pain is pressure. Nothing more."
L049 = "This sits on that spot and lifts the weight off."
GO = "chat: \"confirmed\" (2026-10-02) — INFO-KNEE-N v1 confirmed; SC07 + SC08 as five takes"
FIX = "first generation — every earlier note on this build kept: one strap only, small (12 × 5 cm), front side up, on the right knee; no box (FP19); the same seats as SC0506-T1"

P = {}
P["S7A_START"] = "on the landing at the top of the stairs, Her stands with the strap at the middle of her bare right shin, her right hand on it, about to slide it up"
P["S7A_END"] = "Her stands on the third step down, facing down the stairs, hands at her sides, the strap seated under her right kneecap, the banister untouched"
P["S7B_START"] = "Barbara stands in the hall at the foot of the stairs on the banister side, arms folded, looking up; Her is a few steps from the bottom, coming down facing forwards"
P["S7B_END"] = "Her stands on the hall carpet at the foot of the stairs, turned back to look up the flight, the strap on her right knee; Barbara in the hall beside the newel post"
P["S8A_START"] = "Barbara already seated across the pine table with her mug; Her coming back to her chair at the near end and starting to sit down"
P["S8A_END"] = "both seated in their chairs across the table, Barbara looking at Her, her hands resting on the table either side of her mug"
P["S8B_START"] = "both seated across the pine table; Barbara turned a little on her chair, her bare right knee with its strap just out from under the table edge"
P["S8B_END"] = "Barbara leaning in across the table toward Her, forearms on the wood, holding Her's eyes"
P["S8C_START"] = "Her seated at the near end of the table looking down at the strap on her own right knee; Barbara across the table"
P["S8C_END"] = "Barbara's right hand resting flat on the table beside her mug after one tap, her eyes on Her"

SHOTS = []
SHOTS.append(dict(beat="SC07-T1", take="SC07-T1", kind="multi", covers=["SC07-SH01", "SC07-SH02", "SC07-SH03"], duration=10, line="", vo="L042", subject_motion="travels", scene=7,
    files=["N-FACE", "INFO-KNEE-N", "PROD-FRONT", "L-STAIRS", "OUT-N-B5"], audios=[],
    title="Scene 7 · T1 — on the landing she seats the strap, then the first steps down without the banister (SH01–SH03)", start_pos=P["S7A_START"], end_pos=P["S7A_END"],
    prompt=" ".join([
        manifest([("@image1", FACE_N), ("@image2", KNEE_N), ("@image3", "is " + STRAP + "."), ("@image4", STAIRS), ("@image5", CARD_N)]),
        SERIES, LOOK, INHERIT, HOUSE, B5_STAIRS, NOMOUTH, STRAP_ON,
        "One scene covered in 3 shots within a single take, all on the same side of the action line, with the same light, look and wardrobe throughout. Frame 1: " + P["S7A_START"] + ". "
        "The action carries straight across every cut: each shot picks up the movement exactly where the last one left it, in the same direction, and she is where the last shot left her. "
        "SHOT 1, [0s-3s]: ECU low and front-on at knee height on the landing, Camera on a tripod, locked, her head and shoulders out of frame: her right hand slides the small strap up her bare right shin in one smooth move until it seats just under the kneecap, "
        "the bottom of the kneecap settling into the shell's notch exactly as in Image2; her hand lets go and drops to her side. The strap is about a third of the frame wide. "
        f"SHOT 2, [3s-6.5s]: FULL, high and from behind her at the top of the stairs, looking down the flight exactly as Image4 shows it, Camera on a tripod, locked: Her, {HER_ID}, in {HER_B5}, stands at the top step facing DOWN the stairs; "
        "her right hand hovers over the banister rail, then she lowers it to her side without touching the rail and takes the first step down. " + STEPS_DOWN + " "
        "SHOT 3, [6.5s-10s]: MEDIUM, low and front-on from lower down the flight, Camera on a tripod, locked: she comes down the second and third steps toward the camera, facing forwards, both hands at her sides, eyes on the steps, "
        "her face calm and concentrated, the strap visible on her right knee under the dress hem. Last frame: " + P["S7A_END"] + ".",
        "MOVE: she travels only down the stairs, one tread per step, toward the bottom of the frame; the camera never moves with her.",
        F2, PHYS,
        state("HER", "in the outfit of her card on the stairs, the strap on her right knee", "she is three steps down, the banister untouched"),
        "FOCUS: SHOT 1 the strap and kneecap sharp; SHOT 2 deep, the whole flight sharp; SHOT 3 her eyes sharp. The blur is optical: soft and round, never smeared.",
        SILENT,
        negs(NEG_EQUIP, NEG_MORPH, NEG_STAIRS, "no hand on the banister, no holding the rail, no facing up the stairs, no stepping backwards, no second strap, no strap on the left knee, no oversized strap, no strap over the kneecap or low on the shin, no cardigan, no talking, no mouth moving", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "she grips the banister (the line says she didn't)", "prevented_by": "hand hovers then drops to her side, both hands at her sides, banister negatives"},
           {"risk": "feet skip or shuffle on the treads (FP16)", "prevented_by": "each step spelled foot by foot, one tread per step, stairs negatives"},
           {"risk": "the strap in the wrong place or size (FP02, FP03, FP18)", "prevented_by": "her knee card as Image2, the strap photo, right knee only, size and place negatives"}]))

SHOTS.append(dict(beat="SC07-T2", take="SC07-T2", kind="multi", covers=["SC07-SH04", "SC07-SH05", "SC07-SH06"], duration=11, line="", vo="L044", subject_motion="travels", scene=7,
    files=["N-FACE", "C1", "INFO-KNEE-N", "PROD-FRONT", "P-HOUSE", "OUT-N-B5"], audios=[],
    title="Scene 7 · T2 — Barbara watching from the hall; the last steps onto the carpet; she looks back up (SH04–SH06)", start_pos=P["S7B_START"], end_pos=P["S7B_END"],
    prompt=" ".join([
        manifest([("@image1", FACE_N), ("@image2", SHEET("Barbara", BARB_B5)), ("@image3", KNEE_N), ("@image4", "is " + STRAP + "."), ("@image5", HALL), ("@image6", CARD_N)]),
        SERIES, LOOK, INHERIT, HOUSE, B5_STAIRS, NOMOUTH, STRAP_ON,
        "THE POSITIONS: Barbara stands in the hall at the foot of the stairs on the open banister side, beside the bottom newel post, and never moves from there; Her comes down the flight toward the hall.",
        "One scene covered in 3 shots within a single take, all on the same side of the action line, with the same light, look and wardrobe throughout. Frame 1: " + P["S7B_START"] + ". "
        "The action carries straight across every cut: each shot picks up the movement exactly where the last one left it, in the same direction, and everyone is where the last shot left them. "
        f"SHOT 1, [0s-2.5s]: MCU, eye level, three-quarter on Barbara, {BARB_ID}, in {BARB_B5}, in the hall, Camera on a tripod, locked: she stands with her arms folded, looking up the stairs, and a small smile grows, lips sealed. "
        f"SHOT 2, [2.5s-7s]: FULL, ground level, in profile at the foot of the stairs, Camera on a tripod, locked: Her's legs and feet come down the last steps facing forwards, both hands at her sides, "
        "the strap on her right knee, and she steps off the bottom tread onto the hall carpet. " + STEPS_DOWN + " "
        f"SHOT 3, [7s-11s]: CU, eye level, front-on on Her, {HER_ID}, in {HER_B5}, at the foot of the stairs, Camera on a tripod, locked (the push-in is made in the edit): she has turned and looks back up the whole flight, "
        "her breath caught, eyes wide and wet at the rims, lips parted a little but silent. Last frame: " + P["S7B_END"] + ".",
        "MOVE: she travels only down the last steps and onto the carpet, then turns her head and shoulders back up the flight; the camera never travels with her.",
        F2, PHYS,
        state("HER", "in the outfit of her card, the strap on her right knee, at the foot of the stairs", "she has walked down the whole flight and looks back up it"),
        "FOCUS: SHOT 1 Barbara's eyes; SHOT 2 deep, her feet and the treads sharp; SHOT 3 her nearest eye. The blur is optical: soft and round, never smeared.",
        SILENT,
        negs(NEG_EQUIP, NEG_MORPH, NEG_STAIRS, "no hand on the banister, no stepping backwards, no Barbara on the stairs, no Barbara moving, no second strap, no strap on the left knee, no oversized strap, no cardigan, no talking, no mouth moving", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "the hall's geography flips (HT22)", "prevented_by": "the hall plate, HOUSE block, Barbara fixed beside the bottom newel post on the banister side"},
           {"risk": "feet skip or shuffle on the treads (FP16)", "prevented_by": "each step spelled foot by foot, stairs negatives"},
           {"risk": "someone speaks", "prevented_by": "NOMOUTH, silent clip, talking negatives"}]))

SHOTS.append(dict(beat="SC08-T1", take="SC08-T1", kind="take", covers=["SC08-SH01"], duration=12, line=L046, vo=None, subject_motion="in_place", scene=8,
    files=["C1", "N-FACE", "INFO-KNEE-N", "L-KITCHEN", "OUT-N-B5", "INFO-ROUTINE"], audios=["C1-L049"],
    title="Scene 8 · T1 — back at the table: Everything you’ve tried… This one fixes why it hurts. (SH01)", start_pos=P["S8A_START"], end_pos=P["S8A_END"],
    prompt=" ".join([
        manifest([("@image1", SHEET("Barbara", BARB_B5)), ("@image2", FACE_N), ("@image3", KNEE_N), ("@image4", KITCHEN), ("@image5", CARD_N), ("@image6", CARD_ROUTINE), ("@audio1", VOICE("Barbara"))]),
        SERIES, LOOK, INHERIT, S5.B5_MORNING.replace("a bright morning the week after the wedding", "a bright morning the week after the wedding, back from the stairs"), B5_TABLE, SEATS, NOSPK,
        "THE LINE, word for word: " + L046 + " — Barbara says it; Her says nothing.",
        "One continuous shot, never cut and never restarted, one camera. Frame 1: " + P["S8A_START"] + ". "
        f"MEDIUM, eye level, three-quarter on Barbara, {BARB_ID}, in {BARB_B5}, across the table, Her on the left edge of frame, Camera on a tripod, locked: "
        f"Her, {HER_ID}, in {HER_B5}, sits down in her chair, the strap on her right knee; as she settles, Barbara looks at her and says, plainly: " + L046 + " "
        "Last frame: " + P["S8A_END"] + ".",
        F2, PHYS,
        "While the line is spoken, Barbara keeps doing one thing with her hands: both hands resting flat on the table either side of her mug, at one steady hold through the line. It is ordinary and unhurried, and the hands never stop to gesture.",
        state("BOTH", "back at the table in the same chairs, the strap on Her's right knee", "both seated, Barbara has said it"),
        "FOCUS: Barbara's eyes sharp, Her a little soft in the foreground. The blur is optical: soft and round, never smeared.",
        dialogue("Barbara", L046, VOICE_C1, "her cousin has just walked down the stairs without the banister. Speaking across the table to Her.",
                 "explains, plain and sure, no selling. Opens level; turns on 'worse', a little harder; exits on 'why it hurts', holding Her's eyes. Stress on 'fixes'.",
                 "plain and certain, conversational, matching the face in this shot.", "she was angry once about the years she lost, which leaks only through the weight on 'worse'."),
        AUD,
        "Audio1 is only Barbara's voice: its words are never spoken in this clip; she says only the line above.",
        negs(NEG_EQUIP, NEG_MORPH, "no box, no packaging, no one changing seats, no swapped sides, no second strap on Her, no oversized strap, no cardigan, no Her speaking, no word of the voice reference spoken", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "the seats swap from SC0506-T1", "prevented_by": "SEATS block, same chairs, one side of the table"},
           {"risk": "the voice ref's words leak (L33)", "prevented_by": "the ref is L049, named as voice only, its words negated"},
           {"risk": "a box appears (FP19)", "prevented_by": "no box in the scene so far and the negatives"}]))

SHOTS.append(dict(beat="SC08-T2", take="SC08-T2", kind="multi", covers=["SC08-SH02", "SC08-SH03"], duration=15, line=L047, vo=None, subject_motion="in_place", scene=8,
    files=["PROD-FRONT", "INFO-KNEE-C1", "C1", "N-FACE", "L-KITCHEN", "OUT-N-B5", "INFO-ROUTINE"], audios=["C1-L049"],
    title="Scene 8 · T2 — the spot below the kneecap (SH02–SH03)", start_pos=P["S8B_START"], end_pos=P["S8B_END"],
    prompt=" ".join([
        manifest([("@image1", "is " + STRAP + "."), ("@image2", CARD_KNEE), ("@image3", SHEET("Barbara", BARB_B5)), ("@image4", FACE_N), ("@image5", KITCHEN), ("@image6", CARD_N), ("@image7", CARD_ROUTINE), ("@audio1", VOICE("Barbara"))]),
        SERIES, LOOK, INHERIT, B5_TABLE, SEATS, NOSPK,
        "THE LINE, word for word: " + L047 + " — Barbara says all of it, across both shots; Her says nothing.",
        "One scene covered in 2 shots within a single take, all on the same side of the action line, with the same light, look and wardrobe throughout. Frame 1: " + P["S8B_START"] + ". "
        "The action carries straight across the cut: the second shot picks up the movement exactly where the last one left it, and everyone is where it left them. "
        "SHOT 1, [0s-4s]: ECU, low three-quarter at knee height beside the table, Camera on a tripod, locked: Barbara's bare right knee with her strap on it exactly as in Image2; she presses two fingers once on the shell just under her kneecap and holds them there, "
        "as her voice begins: There’s one spot below the kneecap where every step lands. The strap about a third of the frame wide, rigid, the wordmark toward us. "
        f"SHOT 2, [4s-15s]: MCU over Her's right shoulder onto Barbara, {BARB_ID}, in {BARB_B5}, across the table, Camera on a tripod, locked: Barbara leans in, forearms on the table, and counts it off plainly: "
        "Every brace, every injection, every pill you’ve ever taken treated the whole knee. — a beat — Not that spot. "
        "Each cut lands on a completed action. The eyelines match across the table. Nobody looks into the lens. Last frame: " + P["S8B_END"] + ".",
        F2, PHYS,
        "THE STRAP, every time it is seen: exactly Image1 — the rigid black shell keeps its shape and size, never bends; only the knit band is soft.",
        "While the line is spoken, Barbara keeps doing one thing with her hands: in SHOT 2 her forearms resting on the table, hands loosely together, at one steady hold. It is ordinary and unhurried, and the hands never stop to gesture.",
        state("BARBARA", "seated across the table, her strap on her bare right knee", "she has leaned in across the table"),
        "FOCUS: SHOT 1 her fingers and the strap sharp; SHOT 2 Barbara's eyes, Her's shoulder soft in the foreground. The blur is optical: soft and round, never smeared.",
        dialogue("Barbara", L047, VOICE_C1, "she is showing her cousin the one spot that matters. Speaking across the table to Her.",
                 "teaches, simple and sure. Opens on 'one spot', a touch slower; counts off brace, injection, pill evenly; lands hard and quiet on 'Not that spot.' Stress on 'one' and 'Not'.",
                 "plain, certain, a little lower on the last three words, matching the face in this shot.", "she is a little angry at all the wasted years, which leaks only through the beat before 'Not that spot.'"),
        AUD,
        "Audio1 is only Barbara's voice: its words are never spoken in this clip; she says only the line above.",
        negs(NEG_EQUIP, NEG_MORPH, "no box, no packaging, no one changing seats, no swapped sides, no oversized strap, no strap over the kneecap, no cardigan, no Her speaking, no word of the voice reference spoken, no word left out", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "the press lands on the kneecap, not the spot below (FP03)", "prevented_by": "Barbara's knee card, 'on the shell just under her kneecap', kneecap negative"},
           {"risk": "the line is cut or rushed in 13 s", "prevented_by": "the whole line written in its two shots, 'no word left out'"},
           {"risk": "the voice ref's words leak (L33)", "prevented_by": "voice only, its words negated"}]))

SHOTS.append(dict(beat="SC08-T3", take="SC08-T3", kind="multi", covers=["SC08-SH04", "SC08-SH05"], duration=12, line=L048 + " " + L049, vo=None, subject_motion="in_place", scene=8,
    files=["N-FACE", "INFO-KNEE-N", "PROD-FRONT", "C1", "L-KITCHEN", "OUT-N-B5", "INFO-ROUTINE"], audios=["C1-L049"],
    title="Scene 8 · T3 — That’s why nothing worked… This sits on that spot and lifts the weight off. (SH04–SH05; no box — she taps the table by her mug)", start_pos=P["S8C_START"], end_pos=P["S8C_END"],
    prompt=" ".join([
        manifest([("@image1", FACE_N), ("@image2", KNEE_N), ("@image3", "is " + STRAP + "."), ("@image4", SHEET("Barbara", BARB_B5)), ("@image5", KITCHEN), ("@image6", CARD_N), ("@image7", CARD_ROUTINE), ("@audio1", VOICE("Barbara"))]),
        SERIES, LOOK, INHERIT, B5_TABLE, SEATS, NOSPK,
        "THE LINES, word for word and in this order: " + L048 + " " + L049 + " — Barbara says both; Her says nothing.",
        "One scene covered in 2 shots within a single take, all on the same side of the action line, with the same light, look and wardrobe throughout. Frame 1: " + P["S8C_START"] + ". "
        "The action carries straight across the cut: the second shot picks up the movement exactly where the last one left it, and everyone is where it left them. "
        f"SHOT 1, [0s-6s]: CU in profile on Her, {HER_ID}, in {HER_B5}, Camera on a tripod, locked: she listens, looking down at the strap on her own right knee, lips sealed and jaw still, while Barbara's voice says, off-screen: " + L048 + " "
        f"SHOT 2, [6s-12s]: CU, low three-quarter on Barbara, {BARB_ID}, in {BARB_B5}, across the table, Camera on a tripod, locked (the push-in is made in the edit): she taps the table once with two fingers beside her mug, sure, and says: " + L049 + " "
        "The eyelines match across the table. Nobody looks into the lens. Last frame: " + P["S8C_END"] + ".",
        F2, PHYS,
        "While the lines are spoken, Barbara keeps doing one thing with her hands: one tap beside her mug, then her hand resting flat on the table. It is ordinary and unhurried, and the hands never stop to gesture.",
        state("HER", "seated at the near end of the table, the strap on her right knee", "she is still looking down at it, taking it in"),
        "FOCUS: SHOT 1 Her's nearest eye; SHOT 2 Barbara's eyes. The blur is optical: soft and round, never smeared.",
        dialogue("Barbara", L048 + " " + L049, VOICE_C1, "her cousin is looking down at the strap on her own knee. Speaking across the table to Her.",
                 "settles it, quiet and certain. Opens soft on 'That’s why nothing worked'; turns on 'pressure'; exits sure on 'lifts the weight off'. Stress on 'pressure' and 'lifts'.",
                 "quiet, certain and warm, matching the face in this shot.", "she is glad, which leaks only through how gently she says it."),
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, "no box, no packaging, no one changing seats, no swapped sides, no second strap on Her, no strap on Her's left knee, no oversized strap, no cardigan, no Her speaking, no word left out", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "a box appears for the tap (FP19)", "prevented_by": "'beside her mug', box negatives"},
           {"risk": "Her mouths Barbara's off-screen line", "prevented_by": "her lips sealed in SHOT 1, 'Barbara's voice says, off-screen', Her-speaking negative"},
           {"risk": "the strap on the wrong knee (FP18)", "prevented_by": "her knee card, 'her own right knee', left-knee negative"}]))

FILES = dict(S5.FILES)
FILES.update({"INFO-KNEE-N": "body/SC07/ingredients/INFO-KNEE-N_v1.png", "P-HOUSE": "plates/P-HOUSE_v1.png", "L-STAIRS": "plates/L-STAIRS_v4.png"})
AUDIO = {"C1-L049": "voice/C1_line_L049.mp3"}

if __name__ == "__main__":
    only = sys.argv[1:]
    for s in SHOTS:
        if only and s["beat"] not in only:
            continue
        call = {"beat": s["beat"], "build": "stryde-half-my-age", "connector": "seedance", "model": "bytedance/seedance-2-5", "mode": 4, "kind": s["kind"], "prompt": s["prompt"],
                "take": s["take"], "covers": s["covers"], "start_pos": s["start_pos"], "end_pos": s["end_pos"],
                "duration": s["duration"], "resolution": "720p", "aspect_ratio": "9:16", "start_image": None,
                "ingredients_approved": True, "files": [FILES[f] for f in s["files"]], "audios": [AUDIO[a] for a in s["audios"]],
                "generate_audio": bool(s["line"]), "dialogue": s["line"] or None, "script_line": s["line"] or None, "pace": "unhurried",
                "subject_motion": s["subject_motion"], "prefer_multi_shots": "false", "generation": 1, "user_go": GO, "fix_note": FIX,
                "risks": s["risks"], "vo": s.get("vo"), "scene": s["scene"], "title": s["title"],
                "taste": ["HT02", "HT17", "HT18", "HT22", "HT23", "HT26", "FP01", "FP02", "FP03", "FP10", "FP11", "FP12", "FP15", "FP16", "FP18", "FP19"]}
        out = H / f"{s['beat']}.call.json"
        out.write_text(json.dumps(call, indent=1, ensure_ascii=False))
        (H / f"{s['beat']}.prompt.txt").write_text(s["prompt"])
        print(s["beat"], s["duration"], "s", len(s["prompt"]), "chars")
