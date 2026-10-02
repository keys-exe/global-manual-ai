"""Scenes 5 + 6 (day B5, Barbara's stay, the kitchen) — SEEDANCE 2.5 takes on Kie AI, ingredients only, no frames.
The user: "lets do 2 scenes at a time now"; ingredient cards confirmed ("confirmed images in the scene 5", 2026-10-02):
OUT-N-B5 v2 (chambray shirt dress), INFO-ROUTINE; real product photos PROD-FRONT, INFO-PLACEMENT, PROD-BOX.
Three takes (§24K part 5): SC05-T1 = SH01–SH03, SC05-T2 = SH04–SH07, SC06-T1 = SH01–SH03 (a new scene starts a take).
Her face goes in as a face-and-hair crop (HT26); Barbara wears her own cast-sheet outfit on B5, so her full sheet goes in.
The plate L-KITCHEN is seen from the hall doorway: the pine table runs along the left of the room under the side window,
so the takes are written from the plate's own side (L17). Product: the real strap, ~12 × 5 cm (FP01, FP02, FP03, FP11, FP12);
no pinned end frames on this team's builds (FP15). VO L035 / L037 / L039 are laid in the edit."""
import json
import sys
import importlib.util
from pathlib import Path

H = Path(__file__).parent
B = H.parents[1]
_spec = importlib.util.spec_from_file_location("sc03_clips", B / "body" / "SC03" / "build_clips.py")
S3 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(S3)
SERIES, LOOK, INHERIT, F2, F1, PHYS, AUD, SILENT = S3.SERIES, S3.LOOK, S3.INHERIT, S3.F2, S3.F1, S3.PHYS, S3.AUD, S3.SILENT
NEG_EQUIP, NEG_MORPH, NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND = S3.NEG_EQUIP, S3.NEG_MORPH, S3.NEG_FILM, S3.NEG_SCENECUT, S3.NEG_DRAMA, S3.NEG_SOUND
VOICE_N, HER_ID = S3.VOICE_N, S3.HER_ID
manifest, PLACE, VOICE, state, negs, dialogue, SHEET = S3.manifest, S3.PLACE, S3.VOICE, S3.state, S3.negs, S3.dialogue, S3._hka.SHEET

VOICE_C1 = ("An English woman of seventy-four from the Midlands, a bright, certain, slightly husky voice with Midlands warmth in the vowels. "
            "Quick and practical, amused underneath — she has seen it work and isn't arguing. Clear consonants; the ends of sentences land firmly.")
BARB_ID = "a tall, big-boned, upright woman of seventy-four with short white hair cropped close at the sides and a little spiky on top"
HER_B5 = ("a chambray-blue cotton shirt dress with a collar, a full button front, the sleeves rolled to the elbow and a fabric tie belt, "
          "the hem a hand's width above the knee, bare legs, white canvas plimsolls and a thin gold watch — exactly her outfit card, no cardigan")
BARB_B5 = "a cobalt-blue quilted gilet over a white long-sleeved top, navy shorts ending just above the knee and white trainers — her own outfit, as on her sheet"
FACE_N = "is Her: her face and hair only, a close crop — her clothes come from the outfit card, never from this picture."
CARD_N = ("is an info card: Her outfit on this day — the chambray-blue shirt dress with its tie belt, ending above the knee, white plimsolls; follow it exactly, "
          "and its caption strip and any text on it never appear in the clip.")
CARD_ROUTINE = ("is the layout of her end of the pine table, seen from above: exactly five objects, spaced as shown — a soft beige pull-on knee sleeve folded once, "
                "a silver painkiller strip, a plain white gel tube with its cap on, a white mug of tea half drunk, a small glass of water; every shot of this table shows these five and nothing else, "
                "in these places, with no brand or writing, and its caption strip never appears in the clip.")
CARD_KNEE = ("is Barbara's own right knee with the strap on it, seated: copy the strap's place exactly — the bottom of the kneecap sits in the shell's centre notch, the shell on the tendon just under it, "
             "the whole kneecap visible above; its caption strip never appears in the clip.")
BACK = ("is the back of the same strap, the side that touches the skin: a grey ribbed silicone pad shaped like a bow tie with one long smooth raised bump down its middle, inside the black shell, "
        "a chrome slide at each end and the knit band; copy it exactly whenever the back shows")
STRAP = ("the real product photo of the strap, copied exactly — the rigid matte-black moulded shell with two rounded peaks around a centre notch, the grey stryde wordmark on its face, "
         "a slim chrome slide at each end and the soft black knit band looping through them; nothing redesigned. It is small: the shell about 12 by 5 centimetres")
KITCHEN = PLACE("her kitchen at the back of the house, seen from the hall doorway — the scrubbed pine table with rush-seat ladder-back chairs along the left under the side window, "
                "the sage-green cupboards and the white butler sink under the back window, the cream range cooker on the right, warm morning sun coming in")
B5_MORNING = ("THE SCENE SO FAR, a bright morning the week after the wedding, one continuous moment in her kitchen: soft morning daylight about 5600K from the side window on the left of the table. "
              "Her, in the outfit of her card, sits at the near end of the long side of the pine table that faces into the room, side-on to the window; "
              "Barbara, in her own gilet and shorts, sits across the table from her with her back to the side window, a mug of tea in front of her. "
              "On the table in front of Her: exactly the five objects of the table card, in their places — the beige knee sleeve, the painkiller strip, the gel tube, her mug of tea, the glass of water — and nothing else. "
              "No brace, no box, no ice pack anywhere.")
NOSPK = "Nobody speaks until the line written below; mouths stay closed and jaws still until then."

L036 = "Can I show you something?"
L038 = "They come in twos. I never used the spare."
L040 = "Barbara. This can’t possibly work on knees like mine."
L041 = "Just put it on and walk down the stairs."
GO = "chat: \"confirmed images in the scene 5\" (2026-10-02) — SC05 + SC06 as three takes"
GO2 = "board Fix + chat \"fix those\" (2026-10-02) — v2 of the three takes; INFO-ROUTINE v2 confirmed, INFO-KNEE-C1 v2 made for the knee"
NOTE5 = "the user: scene 5 not realistic — the brace looked like a support for a broken knee, the table things not consistent or correct, no box: Barbara just gives her 1 Stryde"
FIX = {"SC05-T1": NOTE5 + " → the table is the five-object layout card (soft knee sleeve, painkiller strip, gel, tea, water), no brace, no ice pack; her voice ref holds only her own line (v1 spoke 'They come in twos' under the wide)",
       "SC05-T2": NOTE5 + " → Barbara's knee from her own info card (v1 copied a man's leg), the strap with the kneecap in its notch; no box — she hands Her one strap from her gilet pocket",
       "SC06-T1": "the user: this is the back of the silicon for the scene 6 → the back photo attached and named when she turns it; v1 bent the shell and dropped 'Barbara.' → rigid shell said, every word of the line said, the name first"}

P = {}
P["T1_START"] = ("the wide view from the hall doorway: Her at the pine table with her five things laid out in front of her, pressing a tablet out of the strip; "
                 "Barbara across the table, both hands round her mug, watching her")
P["T1_END"] = ("Barbara has set her mug down on the table and looks across at Her, her hands flat on the table either side of it; Her looks up at her, the tablet taken, the glass of water back on the table")
P["T2_START"] = ("Barbara, seated across the table, has turned on her chair so her bare right knee comes out past the table end toward the camera, the strap already on it just under the kneecap; Her watches from her chair")
P["T2_END"] = ("Barbara sits back in her chair across the table, hands on her thighs; Her holds the one spare strap Barbara has just put in her hand, looking down at it")
P["T3_START"] = ("Her sits at her place at the pine table holding the spare strap flat across her open right palm, front side up; Barbara across the table watching her")
P["T3_END"] = ("Barbara leans in across the table toward Her, forearms on the table, her face close and certain; Her holds the strap up between them")

SHOTS = []
SHOTS.append(dict(beat="SC05-T1", take="SC05-T1", kind="multi", covers=["SC05-SH01", "SC05-SH02", "SC05-SH03"], duration=12, line=L036, vo="L035", subject_motion="in_place",
    files=["N-FACE", "C1", "L-KITCHEN", "OUT-N-B5", "INFO-ROUTINE"], audios=["C1-L036"],
    title="Scene 5 · T1 — the morning routine; Can I show you something? (SH01–SH03)", start_pos=P["T1_START"], end_pos=P["T1_END"],
    prompt=" ".join([
        manifest([("@image1", FACE_N), ("@image2", SHEET("Barbara", BARB_B5)), ("@image3", KITCHEN), ("@image4", CARD_N), ("@image5", CARD_ROUTINE), ("@audio1", VOICE("Barbara"))]),
        SERIES, LOOK, INHERIT, B5_MORNING, NOSPK,
        "One scene covered in 3 shots within a single take, all on the same side of the action line, with the same light, look and wardrobe throughout. Frame 1: " + P["T1_START"] + ". "
        "Everyone stays seated in their place. The action carries straight across every cut: each shot picks up the movement exactly where the last one left it — the same hand, the same object, the same direction — and everyone is where the last shot left them. "
        f"SHOT 1, [0s-5s]: WIDE, exactly the view of Image3 from the hall doorway, Camera on a tripod, locked: Her, {HER_ID}, in {HER_B5}, works through her morning: she presses one tablet out of the painkiller strip "
        f"and swallows it with a sip from the glass of water; across the table Barbara, {BARB_ID}, in {BARB_B5}, sits with her mug and watches her, saying nothing. "
        "SHOT 2, [5s-8s]: ECU straight down from above the table: the five things of the table card in their places on the scrubbed pine — the beige knee sleeve, the painkiller strip, the gel tube, the mug, the glass — and Her's hand putting the strip back down. "
        "SHOT 3, [8s-12s]: MCU over Her's right shoulder onto Barbara across the table: Barbara sets her mug down on the wood, looks at Her, and says, light and certain: " + L036 + " "
        "Each cut lands on a completed action. The eyelines match across the table. Nobody looks into the lens. Last frame: " + P["T1_END"] + ".",
        F2, PHYS,
        "While the line is spoken, Barbara keeps doing one thing with their hands: both hands resting flat on the table either side of her mug, at one steady hold through the line. It is ordinary and unhurried, and the hands never stop to gesture.",
        state("HER", "in the outfit of her card at the pine table, her five things in front of her", "she has taken one tablet"),
        "FOCUS: SHOT 1 deep, both women sharp; SHOT 2 the objects on the table sharp; SHOT 3 Barbara's eyes sharp, Her's shoulder soft in the foreground. The blur is optical: soft and round, never smeared.",
        dialogue("Barbara", L036, VOICE_C1, "she has watched her cousin's whole routine in silence and has decided. Speaking across the table to Her.",
                 "offers, lightly, as if it is nothing. Opens easy; turns on 'show', where she smiles a little; exits holding Her's eyes. Stress on 'show'.",
                 "light and certain, conversational, matching the face in this shot.", "she has been exactly where Her is, which leaks only through how sure she sounds."),
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, "no cardigan, no jumper, no hinged brace, no ice pack, no box, no brand or writing on any object, no strap visible yet, no Her speaking", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "the plate's layout lost (L17)", "prevented_by": "SHOT 1 is exactly the plate's doorway view; the table and the window side named"},
           {"risk": "Her back in a cardigan (L21)", "prevented_by": "face-and-hair crop, the shirt-dress card, cardigan negative"},
           {"risk": "someone speaks during the VO shots", "prevented_by": "NOSPK; the only line is Barbara's in SHOT 3"}]))

SHOTS.append(dict(beat="SC05-T2", take="SC05-T2", kind="multi", covers=["SC05-SH04", "SC05-SH05", "SC05-SH06", "SC05-SH07"], duration=14, line=L038, vo="L037", subject_motion="in_place",
    files=["PROD-FRONT", "INFO-KNEE-C1", "C1", "N-FACE", "L-KITCHEN", "OUT-N-B5", "INFO-ROUTINE"], audios=["C1-L038"],
    title="Scene 5 · T2 — the strap on Barbara's knee; she hands Her one; They come in twos (SH04–SH07)", start_pos=P["T2_START"], end_pos=P["T2_END"],
    prompt=" ".join([
        manifest([("@image1", "is " + STRAP + "."), ("@image2", CARD_KNEE),
                  ("@image3", SHEET("Barbara", BARB_B5)), ("@image4", FACE_N), ("@image5", KITCHEN), ("@image6", CARD_N), ("@image7", CARD_ROUTINE), ("@audio1", VOICE("Barbara"))]),
        SERIES, LOOK, INHERIT, B5_MORNING, NOSPK,
        "One scene covered in 4 shots within a single take, all on the same side of the action line, with the same light, look and wardrobe throughout. Frame 1: " + P["T2_START"] + ". "
        "Everyone stays seated in their place. The action carries straight across every cut: each shot picks up the movement exactly where the last one left it — the same hand, the same object, the same direction — and everyone is where the last shot left them. "
        f"SHOT 1, [0s-4s]: ECU, low and front-on at knee height, Camera on a tripod, locked: Barbara's bare right knee fills the frame, the navy shorts hem just above it; the strap of Image1 sits exactly as in Image2, "
        "the bottom of her kneecap in the shell's notch, its shell about a third of the frame wide, the wordmark facing us. She holds the knee still for us to see. "
        f"SHOT 2, [4s-7s]: CU, three-quarter, Her, {HER_ID}, in {HER_B5}, looks down at Barbara's knee, unimpressed, one eyebrow barely lifting, her lips sealed and jaw still. "
        "SHOT 3, [7s-10s]: MEDIUM CLOSE across the table at hand height: Barbara takes one spare strap, the same as Image1, out of her gilet pocket and puts it straight into Her's open right hand across the table; Her's fingers close round it. Just the one strap, hand to hand. "
        f"SHOT 4, [10s-14s]: MCU in profile, Barbara, {BARB_ID}, in {BARB_B5}, sits back in her chair, matter-of-fact, and says: " + L038 + " "
        "Each cut lands on a completed action. The eyelines match across the table. Nobody looks into the lens. Last frame: " + P["T2_END"] + ".",
        F2, PHYS,
        "THE STRAP, every time it is seen: exactly Image1 — the rigid black shell keeps its shape and size, never bends, never stretches, never turns into a sleeve, a brace or a band; only the knit band is soft.",
        "While the line is spoken, Barbara keeps doing one thing with their hands: her hands resting on her thighs, at one steady hold through the line. It is ordinary and unhurried, and the hands never stop to gesture.",
        state("BARBARA", "in her own gilet and shorts across the table, the strap on her bare right knee", "she has given Her the spare strap and sat back"),
        "FOCUS: SHOT 1 the strap and kneecap sharp; SHOT 2 Her's nearest eye; SHOT 3 the strap passing hand to hand sharp; SHOT 4 Barbara's eye. The blur is optical: soft and round, never smeared.",
        dialogue("Barbara", L038, VOICE_C1, "she has shown Her the strap and put the spare in her hand. Speaking across the table to Her.",
                 "states it plainly, a fact not a sale. Opens matter-of-fact; turns on 'spare', a small shrug in the voice; exits looking at Her. Stress on 'never'.",
                 "plain and certain, conversational, matching the face in this shot.", "she wants Her to try it without being asked twice, which leaks only through not taking it back."),
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, "no box, no packaging, no neoprene sleeve on Barbara, no strap over the kneecap or low on the shin, no gap between kneecap and strap, no oversized strap, no cardigan, no Her speaking", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "the wrong product (FP01) or the wrong size (FP02)", "prevented_by": "the real front photo first, named with its 12 × 5 cm size and shape, a third of the frame in the ECU (FP11)"},
           {"risk": "the strap on the wrong place (FP03)", "prevented_by": "the real worn photo as Image2, 'centred on the tendon just below the kneecap', shin/kneecap negatives"},
           {"risk": "a box or packaging appears (the user: no box)", "prevented_by": "one strap from her gilet pocket, hand to hand; box/packaging negatives"}]))

SHOTS.append(dict(beat="SC06-T1", take="SC06-T1", kind="multi", covers=["SC06-SH01", "SC06-SH02", "SC06-SH03"], duration=13, line=L040 + " " + L041, vo="L039", subject_motion="in_place",
    files=["PROD-FRONT", "PROD-BACK", "N-FACE", "C1", "L-KITCHEN", "OUT-N-B5"], audios=["N-STOOD", "C1-L036"],
    title="Scene 6 · T1 — the sceptic: the strap in her palm; Just put it on and walk down the stairs (SH01–SH03)", start_pos=P["T3_START"], end_pos=P["T3_END"],
    prompt=" ".join([
        manifest([("@image1", "is " + STRAP + " — it fits across one palm, slide to slide no longer than the hand."), ("@image2", BACK), ("@image3", FACE_N), ("@image4", SHEET("Barbara", BARB_B5)), ("@image5", KITCHEN), ("@image6", CARD_N),
                  ("@audio1", VOICE("Her")), ("@audio2", VOICE("Barbara"))]),
        SERIES, LOOK, INHERIT, B5_MORNING, NOSPK,
        "THE EXCHANGE, word for word and in this order: " + L040 + " " + L041 + " — Her says the first line, Barbara answers with the second; nobody else speaks.",
        "One scene covered in 3 shots within a single take, all on the same side of the action line, with the same light, look and wardrobe throughout. Frame 1: " + P["T3_START"] + ". "
        "Everyone stays seated in their place. The action carries straight across every cut: each shot picks up the movement exactly where the last one left it — the same hand, the same object, the same direction — and everyone is where the last shot left them. "
        "SHOT 1, [0s-4s]: ECU straight down from above, Camera on a tripod, locked: the strap of Image1 rests across Her's open right palm, the shell filling about half the frame, the wordmark up; "
        "she turns it over once, slowly, so we see its back exactly as Image2 — the grey ribbed silicone pad with the long raised bump — then turns it front up again; the shell stays rigid the whole time, only the knit band moves. Her lips sealed and jaw still. "
        f"SHOT 2, [4s-9s]: MCU, three-quarter, Camera on a tripod, locked: Her, {HER_ID}, in {HER_B5}, holds the strap up between finger and thumb at chin height, sceptical, and says the whole line, beginning with the name — Barbara. — a short pause, then: This can’t possibly work on knees like mine. Every word of " + L040 + " is said. "
        f"SHOT 3, [9s-13s]: CU, low three-quarter on Barbara, {BARB_ID}, in {BARB_B5}: she leans in across the table toward Her, forearms on the wood, and says, certain and simple: " + L041 + " "
        "Each cut lands on a completed line. The eyelines match across the table. Nobody looks into the lens. Last frame: " + P["T3_END"] + ".",
        F2, PHYS,
        "THE STRAP, every time it is seen: exactly Image1 — the rigid black shell keeps its shape and size in her hand, never bends, never stretches, never turns into a sleeve or a brace; only the knit band hangs soft.",
        "While the lines are spoken, Her keeps doing one thing with their hands: her right hand holding the strap up at chin height, at one steady hold through the line. It is ordinary and unhurried, and the hands never stop to gesture.",
        state("HER", "in the outfit of her card at the pine table, the spare strap in her hand", "she holds the strap up"),
        "FOCUS: SHOT 1 the strap sharp in her palm; SHOT 2 her nearest eye, the strap a little soft; SHOT 3 Barbara's eyes. The blur is optical: soft and round, never smeared.",
        dialogue("Her", L040, VOICE_N, "she has been handed a small strap after years of braces and pills. Speaking across the table to Barbara.",
                 "dismisses it, dry. Opens on the name as a sigh; turns on 'possibly'; exits looking at the strap. Stress on 'possibly'.",
                 "dry and flat, a little tired, matching the face in this shot.", "part of her wants it to work, which leaks only through her not putting it down."),
        dialogue("Barbara", L041, VOICE_C1, "her cousin has dismissed it, as she once did. Leaning in across the table.",
                 "a simple instruction, no argument. Opens level; turns on 'stairs', where she nods once; exits holding Her's eyes. Stress on 'walk'.",
                 "certain and simple, a little lower, matching the face in this shot.", "she knows the stairs will do the arguing for her, which leaks only through how calm she is."),
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, "no box, no neoprene sleeve, no padded brace, no oversized strap, no shell bending or folding, no invented back, no cardigan, no standing up, no Barbara saying Her's line, no word left out", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "the strap changes shape in her hand (FP01, FP05)", "prevented_by": "the real front photo first, rigid shell named, bending/sleeve negatives"},
           {"risk": "the voices swap", "prevented_by": "Audio1 Her, Audio2 Barbara, every line named with its speaker, negative"},
           {"risk": "the strap too big for her palm (FP02)", "prevented_by": "12 × 5 cm, 'no longer than the hand', oversized negative"}]))

FILES = {"N-FACE": "cast/N-HER_face.png", "C1": "cast/C1-BARBARA_v1.png", "L-KITCHEN": "plates/L-KITCHEN_v1.png",
         "OUT-N-B5": "body/SC05/ingredients/OUT-N-B5_v2.png", "INFO-ROUTINE": "body/SC05/ingredients/INFO-ROUTINE_v2.png", "INFO-KNEE-C1": "body/SC05/ingredients/INFO-KNEE-C1_v3.png", "PROD-BACK": "../../products/stryde/stryde_refs/back_silicone.webp",
         "PROD-FRONT": "../../products/stryde/stryde_refs/front.webp", "INFO-PLACEMENT": "../../products/stryde/stryde_refs/worn_front.jpg",
         "PROD-BOX": "../../products/stryde/stryde_refs/package_open.jpg"}
AUDIO = {"N-STOOD": "voice/N_line_stood.mp3", "C1-L036": "voice/C1_L036_ref.mp3", "C1-L038": "voice/C1_line_L038.mp3"}

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
                "subject_motion": s["subject_motion"], "prefer_multi_shots": "false", "generation": 2, "user_go": GO2, "fix_note": FIX[s["beat"]], "fix_notes_all": [FIX[s["beat"]]],
                "risks": s["risks"], "vo": s.get("vo"), "scene": int(s["beat"][2:4]), "title": s["title"],
                "taste": ["HT02", "HT17", "HT18", "HT22", "HT23", "HT26", "FP01", "FP02", "FP03", "FP11", "FP12", "FP15"]}
        out = H / f"{s['beat']}.call.json"
        out.write_text(json.dumps(call, indent=1, ensure_ascii=False))
        (H / f"{s['beat']}.prompt.txt").write_text(s["prompt"])
        print(s["beat"], s["duration"], "s", len(s["prompt"]), "chars")
