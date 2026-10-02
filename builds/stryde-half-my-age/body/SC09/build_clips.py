"""Scenes 9 + 10 — SEEDANCE 2.5 takes on Kie AI, ingredients only, no frames.
The user: "confirmed next scene" (SC07-T, SC08-T3), then "confirm" (OUT-N-A2, X3–X6, INFO-HIGHST, P-HOUSE-EXT, 2026-10-02).
SC09 (proof, VO L050–L051 in the edit): three one-off places → three takes. SC10 (six weeks later, day A2): one take per place (L51) —
T1 bedroom (strap on, trouser leg down over it), T2 kitchen table (just a mug), T3 high street (she outwalks three younger women),
T4 the checkout (SH04–SH06: L054 VO in the edit, then L055 the cashier / L056 Her), T5 her street home with two bags.
The strap is always the real front photo, ~12 × 5 cm, on the RIGHT knee, bottom of the kneecap in the notch (FP01–FP03, FP18);
on day A2 it is worn under her navy trousers ("Under my clothes. Nobody knows it's there.") and shows only in T1."""
import json
import sys
import importlib.util
from pathlib import Path

H = Path(__file__).parent
B = H.parents[1]
_spec = importlib.util.spec_from_file_location("sc07_clips", B / "body" / "SC07" / "build_clips.py")
S7 = importlib.util.module_from_spec(_spec)
_argv = sys.argv
sys.argv = [sys.argv[0], "__none__"]
_spec.loader.exec_module(S7)
sys.argv = _argv
SERIES, LOOK, INHERIT, F2, PHYS, AUD, SILENT = S7.SERIES, S7.LOOK, S7.INHERIT, S7.F2, S7.PHYS, S7.AUD, S7.SILENT
NEG_EQUIP, NEG_MORPH, NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND = S7.NEG_EQUIP, S7.NEG_MORPH, S7.NEG_FILM, S7.NEG_SCENECUT, S7.NEG_DRAMA, S7.NEG_SOUND
manifest, PLACE, VOICE, state, negs, dialogue, SHEET = S7.manifest, S7.PLACE, S7.VOICE, S7.state, S7.negs, S7.dialogue, S7.SHEET
HER_ID, FACE_N, STRAP, KITCHEN, KNEE_N, CARD_KNEE = S7.HER_ID, S7.FACE_N, S7.STRAP, S7.KITCHEN, S7.KNEE_N, S7.CARD_KNEE
VOICE_N = S7.S5.S3.VOICE_N
NOMOUTH = S7.NOMOUTH

ONEOFF = lambda who: f"is the one-off cast card for {who}: copy the face, age, build and clothes exactly; its grey backdrop and caption strip never appear in the clip."
STRAP_PLACE = ("is an info card that shows only where the strap sits on a knee: the bottom of the kneecap in the shell's centre notch, the shell on the tendon just under it, "
               "the whole kneecap visible above; copy only the strap's place and size, never the leg, the clothes or the room; its caption strip never appears in the clip.")
HER_A2 = "a camel-coloured cotton trench coat worn open over a soft cream crew-neck jumper, straight navy trousers to the ankle and white leather trainers — exactly her outfit card"
CARD_A2 = ("is an info card: Her outfit on this day — the camel trench worn open, the cream jumper, navy trousers, white trainers; follow it exactly, "
           "and its caption strip and any text on it never appear in the clip.")
ON_RIGHT = ("THE STRAP sits on the RIGHT knee only, the left knee bare — the bottom of the kneecap in the shell's notch, the shell small, about 12 by 5 centimetres, about a quarter of the frame wide, "
            "rigid and matte black with the grey stryde wordmark toward us; it never bends, slides or changes size.")
BRISK = ("She walks the way a fit woman walks on a good day: an easy, brisk, even stride, about two steps a second, arms swinging naturally, heel then toe, "
         "never running, never hurrying, never limping, every step landing flat and clean.")

GO = "chat: \"confirm\" (2026-10-02) — every SC09/SC10 ingredient confirmed; SC09 + SC10 as eight takes"
FIX = "first generation — every earlier note on this build kept: one strap only, small (12 × 5 cm), front side up, on the RIGHT knee; no box (FP19); hands off the banister; one take per place (L51)"
L055 = "You alright carrying those, love?"
L056 = "I am, actually."

P = {
 "9A_S": "in a bright sports-medicine clinic the doctor kneels beside a seated patient's bare right knee, the small strap in his hands just below it",
 "9A_E": "the strap sits under the patient's kneecap; the doctor's hands come away and he looks up at the patient with a small nod",
 "9B_S": "on a sunny fairway Barbara's husband stands addressed to the ball, club behind it, knees softly bent, the strap on his right knee",
 "9B_E": "he holds a full, balanced follow-through, club over his shoulder, watching the ball go, the strap still on his right knee",
 "9C_S": "on a hard tennis court in sunshine Barbara's niece stands at the baseline, racket ready, knees bent, the strap on her right knee",
 "9C_E": "she has hit a forehand on the run and settles back into her stance, the strap still on her right knee",
 "10A_S": "Her sits on the edge of her bed, her right trouser leg rolled up above the knee, the strap low on her bare right shin",
 "10A_E": "the strap seated under her kneecap and the navy trouser leg pulled down over it, smooth, nothing showing; her hand rests on her thigh",
 "10B_S": "the pine table in the morning light, seen from straight above, with one white mug of tea on it and nothing else",
 "10B_E": "the same: the pine table with one white mug of tea, steam rising a little",
 "10C_S": "on the high-street pavement Her walks in from the left of frame in her camel trench, three younger women walking ahead of her the same way",
 "10C_E": "Her has passed all three women and walks on out to the right of frame, the three a little behind her",
 "10D_S": "Her stands square in the checkout queue, a full shopping basket in her right hand, weight even on both feet",
 "10D_E": "Her holds a full shopping bag in each hand at the end of the checkout, a small smile, the cashier smiling back from her seat",
 "10E_S": "Her walks up her street on the pavement toward her green front door, a full bag in each hand, her back to the camera",
 "10E_E": "Her turns in at her own gate by the privet hedge, a full bag in each hand",
}

SHOTS = []
def take(beat, scene, covers, dur, title, files, imgs, body, motion, focus, st, risks, neg, line="", audios=(), vo=None, kind=None, dlg=None):
    kind = kind or ("multi" if len(covers) > 1 else "take")
    head = ("One continuous shot, never cut and never restarted, one camera. " if kind == "take" else
            f"One scene covered in {body.count('SHOT ')} shots within a single take, all on the same side of the action line, with the same light, look and wardrobe throughout. ")
    parts = [manifest(imgs), SERIES, LOOK, INHERIT]
    parts += [head + "Frame 1: " + st[0] + ". " +
              ("The action carries straight across every cut: each shot picks up the movement exactly where the last one left it, in the same direction. " if kind == "multi" else "") +
              body + " Last frame: " + st[1] + "."]
    if motion:
        parts.append(motion)
    parts += [F2, PHYS, state(*st[2]), focus]
    if dlg:
        parts += dlg + [AUD]
    else:
        parts += [NOMOUTH, SILENT]
    parts.append(negs(NEG_EQUIP, NEG_MORPH, neg, NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND))
    SHOTS.append(dict(beat=beat, take=beat, kind=kind, covers=covers, duration=dur, title=title, files=files, prompt=" ".join(parts),
                      start_pos=st[0], end_pos=st[1], risks=risks, line=line, audios=list(audios), vo=vo, scene=scene,
                      subject_motion="travels" if "travels" in (motion or "") else "in_place"))

take("SC09-T1", 9, ["SC09-SH01"], 8, "Scene 9 · T1 — the sports doctor fits the strap on a patient (SH01)",
     ["X4-DOCTOR", "PROD-FRONT"],
     [("@image1", ONEOFF("the sports doctor")), ("@image2", "is " + STRAP + ".")],
     "MEDIUM, eye level, three-quarter, Camera on a tripod, locked: a bright, modern sports-medicine clinic, a padded treatment couch, white walls, a window of soft daylight about 5600K. "
     "The doctor of Image1 kneels beside a fit man of about sixty who sits on the couch edge in grey shorts, his right knee bare. The strap of Image2 is ALREADY ON as a closed loop round the man's lower shin, a hand's length below the knee, the black knit band snug all the way round the leg, the shell at the front. "
     "The doctor puts one thumb and finger on each chrome slide and, in one smooth, practised move, slides the whole strap straight UP the shin until the shell seats just under the kneecap, the bottom of the kneecap in its centre notch; "
     "he checks it with one light press of two fingers, takes his hands away and looks up with a small reassuring nod. He never opens, unwraps, stretches or wraps the band — it stays a closed loop round the leg the whole time. "
     "THE STRAP IS SMALL: the shell is about 12 by 5 centimetres — clearly NARROWER than the man's knee, about two-thirds of the knee's width, no taller than two fingers, the knee and kneecap much bigger than it; it is about a fifth of the frame wide. Both faces calm and professional.",
     None, "FOCUS: the strap and the doctor's hands sharp, the faces a little soft. The blur is optical: soft and round, never smeared.",
     (P["9A_S"], P["9A_E"], ("THE PATIENT", "seated on the couch, the strap now on his right knee", "the strap is fitted")),
     [{"risk": "the wrong product or size (FP01, FP02)", "prevented_by": "the real front photo, 12 × 5 cm, a quarter of the frame"},
      {"risk": "the strap on the kneecap (FP03)", "prevented_by": "the place card, 'just under the kneecap'"},
      {"risk": "a brand or text appears in the clinic", "prevented_by": "no lettering negatives"}],
     "no opening the band, no wrapping the band round the leg, no long loose band, no strap as wide as the knee, no oversized strap, no strap on the kneecap, no lettering or logos anywhere, no posters with text, no second strap, no brace, no talking, no mouth moving", vo="L050")

take("SC09-T2", 9, ["SC09-SH02"], 5, "Scene 9 · T2 — Barbara's husband, 76, a full golf swing, the strap on his knee (SH02)",
     ["X5-HUSBAND", "PROD-FRONT", "INFO-KNEE-C1"],
     [("@image1", ONEOFF("Barbara's husband, 76")), ("@image2", "is " + STRAP + "."), ("@image3", STRAP_PLACE)],
     "FULL, low and front-on from the edge of the fairway, Camera on a tripod, locked: a green fairway on a sunny morning, trees beyond. Barbara's husband of Image1, seventy-six, tall and lean, in his golf clothes, "
     "stands over the ball and takes one full, smooth, balanced golf swing — backswing, strike, follow-through — and holds the finish, watching the ball, a quiet satisfied look. "
     "The small strap of Image2 sits on his bare right knee just under the kneecap as Image3 shows, the knee facing the camera, the strap rigid through the whole swing.",
     None, "FOCUS: deep — him and the strap sharp, the trees soft. The blur is optical: soft and round, never smeared.",
     (P["9B_S"], P["9B_E"], ("HIM", "on the fairway, the strap on his right knee", "he has swung and holds the finish")),
     [{"risk": "the strap hidden or wrong (FP01, FP11)", "prevented_by": "knee facing the camera, front photo, rigid through the swing"},
      {"risk": "the swing breaks his body", "prevented_by": "one swing, smooth and balanced, holds the finish"},
      {"risk": "a ball or club glitches", "prevented_by": "morph negatives"}],
     "no second swing, no falling, no club bending, no second strap, no strap on the left knee, no lettering or logos, no talking, no mouth moving", vo="L051")

take("SC09-T3", 9, ["SC09-SH03"], 5, "Scene 9 · T3 — Barbara's niece, 22, runs for a forehand, the strap on her knee (SH03)",
     ["X6-NIECE", "PROD-FRONT", "INFO-KNEE-C1"],
     [("@image1", ONEOFF("Barbara's niece, 22")), ("@image2", "is " + STRAP + "."), ("@image3", STRAP_PLACE)],
     "WIDE, eye level, front-on from behind the net, Camera on a tripod, locked: a green hard tennis court in sunshine. Barbara's niece of Image1, twenty-two, athletic, in her tennis clothes, "
     "takes three quick side-steps across the baseline, plants her feet and hits one clean forehand, then settles back into her ready stance, bright and easy. "
     "The small strap of Image2 sits on her bare right knee just under the kneecap as Image3 shows, rigid the whole time.",
     "MOVE: she travels only a few steps sideways along the baseline; the camera never moves.", "FOCUS: deep — her and the strap sharp. The blur is optical: soft and round, never smeared.",
     (P["9C_S"], P["9C_E"], ("HER NIECE", "on court, the strap on her right knee", "she has hit the forehand")),
     [{"risk": "the strap lost at that size (FP11)", "prevented_by": "the knee toward the camera, the strap named on it every moment"},
      {"risk": "feet skate on the court", "prevented_by": "three quick side-steps then planted feet, skating negatives"},
      {"risk": "the racket or ball glitches", "prevented_by": "morph negatives"}],
     "no falling, no racket bending, no feet sliding, no second strap, no strap on the left knee, no lettering or logos, no talking, no mouth moving", vo="L051")

take("SC10-T1", 10, ["SC10-SH01"], 6, "Scene 10 · T1 — six weeks later: the strap on, the trouser leg pulled down over it (SH01)",
     ["N-FACE", "OUT-N-A2", "PROD-FRONT", "INFO-KNEE-N", "L-BEDROOM"],
     [("@image1", FACE_N), ("@image2", CARD_A2), ("@image3", "is " + STRAP + "."), ("@image4", STRAP_PLACE), ("@image5", PLACE("her bedroom upstairs — the bed with the pale green candlewick bedspread, the window with its net curtains"))],
     "ECU, low and front-on at knee height, Camera on a tripod, locked, her head and shoulders out of frame: six weeks later, a warm morning about 5000K, Her sits on the edge of the bed in her navy trousers and cream jumper, "
     "the right trouser leg rolled up above her bare knee. Her right hand slides the small strap of Image3 up her shin in one smooth move until it seats just under the kneecap as Image4 shows; "
     "then both hands unroll the navy trouser leg and pull it down smoothly over the strap to her ankle, so nothing shows. Two moves, unhurried, practised, every day.",
     None, "FOCUS: the strap and her hands sharp, the bedroom soft behind. The blur is optical: soft and round, never smeared.",
     (P["10A_S"], P["10A_E"], ("HER", "on the bed edge in her A2 outfit, the strap on her right knee", "the trouser leg is down over it")),
     [{"risk": "the strap left showing (the script: under her clothes)", "prevented_by": "the trouser leg pulled down over it at the end"},
      {"risk": "she bends her face into frame (FP17)", "prevented_by": "head and shoulders out of frame, both hands within reach"},
      {"risk": "wrong place or size (FP02, FP03)", "prevented_by": "front photo + place card"}],
     "no face in frame, no second strap, no strap on the left knee, no oversized strap, no strap over the kneecap, no trench coat on yet, no talking, no mouth moving", vo="L052")

take("SC10-T2", 10, ["SC10-SH02"], 4, "Scene 10 · T2 — the pine table, just a mug of tea (SH02)",
     ["L-KITCHEN"],
     [("@image1", KITCHEN)],
     "ECU straight down from above the scrubbed pine table of Image1, Camera on a tripod, locked: warm morning sun about 5000K across the wood; on the table one plain white mug of tea and nothing else — "
     "no pills, no gel, no knee sleeve, no glass of water; a thin curl of steam rises from the mug. Nothing else moves.",
     None, "FOCUS: the mug and the wood grain sharp. The blur is optical: soft and round, never smeared.",
     (P["10B_S"], P["10B_E"], ("THE TABLE", "one mug of tea on the pine", "nothing")),
     [{"risk": "the old routine objects come back", "prevented_by": "'one mug and nothing else', negatives naming each"},
      {"risk": "a hand or person appears", "prevented_by": "no people negative"},
      {"risk": "the mug changes", "prevented_by": "one plain white mug, morph negatives"}],
     "no people, no hands, no pills, no tablet strip, no gel tube, no knee sleeve, no glass, no lettering or logos, no talking", vo="L052")

take("SC10-T3", 10, ["SC10-SH03"], 8, "Scene 10 · T3 — the high street: she outwalks three younger women (SH03)",
     ["N-FACE", "OUT-N-A2", "INFO-HIGHST"],
     [("@image1", FACE_N), ("@image2", CARD_A2), ("@image3", PLACE("the high street of the plate — the stone shopfronts, the red post box, the flagged pavement, the street running left to right"))],
     f"FULL, eye level, in profile from across the pavement, Camera on a tripod, locked, the high street of Image3 running left to right behind: late-morning sun about 5600K. Her, {HER_ID}, in {HER_A2}, "
     "walks in from the left edge of frame along the pavement. Ahead of her, walking the same way, three women in their thirties chatting with shopping bags, strolling slowly. "
     "She comes up behind them and passes all three on the outside, one by one, without changing her pace, and walks on out of the right edge of frame, the three a little behind her. " + BRISK,
     "MOVE: she travels left to right across the frame on the pavement; the camera never moves and never follows her.",
     "FOCUS: deep — her and the shopfronts sharp. The blur is optical: soft and round, never smeared.",
     (P["10C_S"], P["10C_E"], ("HER", "on the high street in her A2 outfit", "she has passed the three women")),
     [{"risk": "her walk turns into a jog or a limp", "prevented_by": "BRISK: two steps a second, never running, never limping"},
      {"risk": "the street flips direction (HT22)", "prevented_by": "left to right named, the plate, camera locked"},
      {"risk": "lettering on the shops", "prevented_by": "blank signs in the plate, lettering negative"}],
     "no running, no jogging, no limping, no bumping into the women, no camera following, no lettering or logos, no strap visible, no talking, no mouth moving", vo="L053")

take("SC10-T4", 10, ["SC10-SH04", "SC10-SH05", "SC10-SH06"], 10, "Scene 10 · T4 — the checkout: You alright carrying those, love? / I am, actually. (SH04–SH06)",
     ["N-FACE", "X3-CASHIER", "OUT-N-A2", "L-SHOP"],
     [("@image1", FACE_N), ("@image2", ONEOFF("the cashier")), ("@image3", CARD_A2), ("@image4", PLACE("the supermarket checkout lane of the plate — the conveyor, the till, the bagging area, the chrome queue rail")), ("@audio1", VOICE("Her"))],
     f"SHOT 1, [0s-4s]: MEDIUM, low three-quarter, Camera on a tripod, locked: Her, {HER_ID}, in {HER_A2}, stands square in the checkout queue, a full shopping basket in her right hand, weight even on both feet, completely still and easy, waiting her turn; nobody speaks in this shot. "
     "SHOT 2, [4s-7s]: MCU over Her's shoulder onto the young cashier of Image2 in her seat at the till, Camera on a tripod, locked: the cashier nods at the two full shopping bags packed at the end of the counter, half-reaches toward them to help and, only now, says kindly: " + L055 + " "
     "SHOT 3, [7s-10s]: CU, eye level, three-quarter on Her, Camera on a tripod, locked: her basket is already set down empty on the floor; she takes the two full shopping bags from the end of the counter, one in her right hand and one in her left, lifts both easily to her sides, and says with a small smile: " + L056 + " "
     "Each cut lands on a completed action. The eyelines match across the counter. Nobody looks into the lens.",
     None, "FOCUS: SHOT 1 her eyes; SHOT 2 the cashier's eyes; SHOT 3 Her's nearest eye. The blur is optical: soft and round, never smeared.",
     (P["10D_S"], P["10D_E"], ("HER", "at the checkout in her A2 outfit", "she has lifted both bags herself")),
     [{"risk": "the voices swap", "prevented_by": "Audio1 is Her; the cashier's line named with her; speakers in order"},
      {"risk": "lettering or logos on packaging", "prevented_by": "the plate's blank labels, lettering negative"},
      {"risk": "she shifts her weight in the queue (the line says she didn't)", "prevented_by": "'completely still, weight even on both feet'"}],
     "no line spoken before 4 seconds, no basket in her hands in SHOT 3, no lettering or logos on any packaging or sign, no Her shifting her weight or leaning, no cashier carrying the bags, no strap visible, no word left out, no voices swapped",
     line=L055 + " " + L056, audios=["N-STOOD"], vo="L054", kind="multi",
     dlg=["THE EXCHANGE, word for word and in this order: " + L055 + " " + L056 + " — the cashier says the first line, Her answers with the second; nobody else speaks.",
          "Audio1 is only Her's voice: its words are never spoken in this clip.",
          dialogue("the cashier", L055, "A young English woman of about twenty from the north, a light, friendly, warm voice.", "she sees an older woman about to lift two heavy bags.",
                   "offers help, kind and casual. Rises on 'love'.", "light and kind, matching the face in this shot.", "she means it, which leaks only through the half-reach."),
          dialogue("Her", L056, VOICE_N, "six weeks ago she couldn't have carried one bag.", "declines, lightly, pleased. Stress on 'actually'.",
                   "light, warm, a little proud, matching the face in this shot.", "she is quietly delighted, which leaks only through the small smile.")])

take("SC10-T5", 10, ["SC10-SH07"], 5, "Scene 10 · T5 — up her street to the front door, a full bag in each hand (SH07)",
     ["N-FACE", "OUT-N-A2", "P-HOUSE-EXT"],
     [("@image1", FACE_N), ("@image2", CARD_A2), ("@image3", PLACE("her street of the plate — the red-brick semis, the privet hedge, the green front door"))],
     f"WIDE, eye level, from behind her on the pavement, Camera on a tripod, locked: afternoon sun about 5000K on her street of Image3. Her, in {HER_A2}, walks away from the camera up the pavement toward her green front door, "
     "EXACTLY TWO full brown paper shopping bags in total — one bag in her right hand and one bag in her left hand, never two in either hand — arms easy, back straight, and turns in at her own gate by the privet hedge. " + BRISK,
     "MOVE: she travels away from the camera up the pavement; the camera never moves.",
     "FOCUS: deep — her and the house sharp. The blur is optical: soft and round, never smeared.",
     (P["10E_S"], P["10E_E"], ("HER", "on her street in her A2 outfit, two full bags", "she turns in at her gate")),
     [{"risk": "she drops or swaps the bags", "prevented_by": "a full bag in each hand throughout"},
      {"risk": "the house changes", "prevented_by": "the street plate, the green door named"},
      {"risk": "a limp or slow walk", "prevented_by": "BRISK"}],
     "no third or fourth bag, no two bags in one hand, no dropping the bags, no limping, no running, no house numbers or lettering, no strap visible, no talking, no mouth moving", vo="L057")

GEN2 = {"SC09-T1": 2, "SC10-T4": 2, "SC10-T5": 2}
FIX2 = {"SC09-T1": "the user (board Fix): wrong way of putting it and also its so big → the strap already a closed loop round the lower shin, the doctor slides it straight up by the two slides in one move (FP10), never opening or wrapping the band; the shell narrower than the knee, about two-thirds of its width, a fifth of the frame; the enlarged knee card dropped (FP02, FP05)",
        "SC10-T4": "agent's check of v1 (not put up, L16): the cashier spoke in SHOT 1 and Her answered still holding her basket, never lifting the bags → the cashier speaks only in SHOT 2; in SHOT 3 the basket is down and she lifts the two bags herself",
        "SC10-T5": "agent's check of v1 (not put up, L16): she carried four bags, two in each hand — the line is two bags → exactly two bags, one in each hand"}
FILES = {"X4-DOCTOR": "body/SC09/ingredients/X4-DOCTOR_v1.png", "X5-HUSBAND": "body/SC09/ingredients/X5-HUSBAND_v1.png", "X6-NIECE": "body/SC09/ingredients/X6-NIECE_v1.png",
         "X3-CASHIER": "body/SC09/ingredients/X3-CASHIER_v1.png", "OUT-N-A2": "body/SC09/ingredients/OUT-N-A2_v1.png", "INFO-HIGHST": "body/SC09/ingredients/INFO-HIGHST_v1.png",
         "P-HOUSE-EXT": "body/SC09/ingredients/P-HOUSE-EXT_v1.png", "PROD-FRONT": "../../products/stryde/stryde_refs/front.webp", "INFO-KNEE-C1": "body/SC05/ingredients/INFO-KNEE-C1_v3.png",
         "INFO-KNEE-N": "body/SC07/ingredients/INFO-KNEE-N_v1.png", "N-FACE": "cast/N-HER_face.png", "L-BEDROOM": "plates/L-BEDROOM_v1.png", "L-KITCHEN": "plates/L-KITCHEN_v1.png",
         "L-SHOP": "plates/L-SHOP_v1.png"}
AUDIO = {"N-STOOD": "voice/N_line_stood.mp3"}

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
                "subject_motion": s["subject_motion"], "prefer_multi_shots": "false", "generation": GEN2.get(s["beat"], 1), "user_go": GO, "fix_note": FIX2.get(s["beat"], FIX),
                "risks": s["risks"], "vo": s.get("vo"), "scene": s["scene"], "title": s["title"],
                "taste": ["HT02", "HT17", "HT18", "HT22", "HT23", "HT26", "FP01", "FP02", "FP03", "FP10", "FP11", "FP12", "FP15", "FP17", "FP18", "FP19"]}
        (H / f"{s['beat']}.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
        (H / f"{s['beat']}.prompt.txt").write_text(s["prompt"])
        print(s["beat"], s["duration"], "s", len(s["prompt"]), "chars")
