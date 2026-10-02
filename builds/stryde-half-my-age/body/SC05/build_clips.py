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
CARD_ROUTINE = ("is a prop card: her morning routine — the black hinged knee brace, a plain white gel tube, a pale-blue gel ice pack, two small white tablets, a plain white mug; "
                "copy each object exactly, with no brand or writing, and its caption strip and grey backdrop never appear in the clip.")
STRAP = ("the real product photo of the strap, copied exactly — the rigid matte-black moulded shell with two rounded peaks around a centre notch, the grey stryde wordmark on its face, "
         "a slim chrome slide at each end and the soft black knit band looping through them; nothing redesigned. It is small: the shell about 12 by 5 centimetres")
KITCHEN = PLACE("her kitchen at the back of the house, seen from the hall doorway — the scrubbed pine table with rush-seat ladder-back chairs along the left under the side window, "
                "the sage-green cupboards and the white butler sink under the back window, the cream range cooker on the right, warm morning sun coming in")
B5_MORNING = ("THE SCENE SO FAR, a bright morning the week after the wedding, one continuous moment in her kitchen: soft morning daylight about 5600K from the side window on the left of the table. "
              "Her, in the outfit of her card, sits at the near end of the long side of the pine table that faces into the room, side-on to the window; "
              "Barbara, in her own gilet and shorts, sits across the table from her with her back to the side window, a mug of tea in front of her. "
              "On the table in front of Her: the black hinged brace, the white gel tube, two white tablets and her mug — exactly the prop card. "
              "The pale-blue ice pack rests on top of Her's bare right knee under the table edge.")
NOSPK = "Nobody speaks until the line written below; mouths stay closed and jaws still until then."

L036 = "Can I show you something?"
L038 = "They come in twos. I never used the spare."
L040 = "Barbara. This can’t possibly work on knees like mine."
L041 = "Just put it on and walk down the stairs."
GO = "chat: \"confirmed images in the scene 5\" (2026-10-02) — SC05 + SC06 as three takes"

P = {}
P["T1_START"] = ("the wide view from the hall doorway: Her at the pine table with her routine laid out in front of her, the ice pack on her right knee, reaching for the two tablets; "
                 "Barbara across the table, both hands round her mug, watching her")
P["T1_END"] = ("Barbara has set her mug down on the table and looks across at Her, her hands flat on the table either side of it; Her looks up at her, the tablets taken, the ice pack still on her knee")
P["T2_START"] = ("Barbara, seated across the table, has turned on her chair so her bare right knee comes out past the table end toward the camera, the strap already on it below the kneecap; Her watches from her chair")
P["T2_END"] = ("Barbara sits back in her chair across the table, hands on her thighs; the small open box with the one spare strap lies on the table beside Her's two tablets; Her looks at the box")
P["T3_START"] = ("Her sits at her place at the pine table holding the spare strap flat across her open right palm, the empty box beside her hand; Barbara across the table watching her")
P["T3_END"] = ("Barbara leans in across the table toward Her, forearms on the table, her face close and certain; Her holds the strap up between them")

SHOTS = []
SHOTS.append(dict(beat="SC05-T1", take="SC05-T1", kind="multi", covers=["SC05-SH01", "SC05-SH02", "SC05-SH03"], duration=12, line=L036, vo="L035", subject_motion="in_place",
    files=["N-FACE", "C1", "L-KITCHEN", "OUT-N-B5", "INFO-ROUTINE"], audios=["C1"],
    title="Scene 5 · T1 — the morning routine; Can I show you something? (SH01–SH03)", start_pos=P["T1_START"], end_pos=P["T1_END"],
    prompt=" ".join([
        manifest([("@image1", FACE_N), ("@image2", SHEET("Barbara", BARB_B5)), ("@image3", KITCHEN), ("@image4", CARD_N), ("@image5", CARD_ROUTINE), ("@audio1", VOICE("Barbara"))]),
        SERIES, LOOK, INHERIT, B5_MORNING, NOSPK,
        "One scene covered in 3 shots within a single take, all on the same side of the action line, with the same light, look and wardrobe throughout. Frame 1: " + P["T1_START"] + ". "
        "Everyone stays seated in their place. The action carries straight across every cut: each shot picks up the movement exactly where the last one left it — the same hand, the same object, the same direction — and everyone is where the last shot left them. "
        f"SHOT 1, [0s-5s]: WIDE, exactly the view of Image3 from the hall doorway, Camera on a tripod, locked: Her, {HER_ID}, in {HER_B5}, works through her morning: she presses the ice pack down on her right knee "
        f"and picks up the two tablets; across the table Barbara, {BARB_ID}, in {BARB_B5}, sits with her mug and watches her, saying nothing. "
        "SHOT 2, [5s-8s]: ECU straight down from above the table: the routine laid out on the scrubbed pine — the black hinged brace, the white gel tube, Her's mug — and Her's hand lifting the two white tablets from the wood. "
        "SHOT 3, [8s-12s]: MCU over Her's right shoulder onto Barbara across the table: Barbara sets her mug down on the wood, looks at Her, and says, light and certain: " + L036 + " "
        "Each cut lands on a completed action. The eyelines match across the table. Nobody looks into the lens. Last frame: " + P["T1_END"] + ".",
        F2, PHYS,
        "While the line is spoken, Barbara keeps doing one thing with their hands: both hands resting flat on the table either side of her mug, at one steady hold through the line. It is ordinary and unhurried, and the hands never stop to gesture.",
        state("HER", "in the outfit of her card at the pine table, the ice pack on her right knee, her routine in front of her", "she has taken the two tablets"),
        "FOCUS: SHOT 1 deep, both women sharp; SHOT 2 the objects on the table sharp; SHOT 3 Barbara's eyes sharp, Her's shoulder soft in the foreground. The blur is optical: soft and round, never smeared.",
        dialogue("Barbara", L036, VOICE_C1, "she has watched her cousin's whole routine in silence and has decided. Speaking across the table to Her.",
                 "offers, lightly, as if it is nothing. Opens easy; turns on 'show', where she smiles a little; exits holding Her's eyes. Stress on 'show'.",
                 "light and certain, conversational, matching the face in this shot.", "she has been exactly where Her is, which leaks only through how sure she sounds."),
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, "no cardigan, no jumper, no knee brace worn, no brand or writing on the gel tube or ice pack, no strap visible yet, no Her speaking", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "the plate's layout lost (L17)", "prevented_by": "SHOT 1 is exactly the plate's doorway view; the table and the window side named"},
           {"risk": "Her back in a cardigan (L21)", "prevented_by": "face-and-hair crop, the shirt-dress card, cardigan negative"},
           {"risk": "someone speaks during the VO shots", "prevented_by": "NOSPK; the only line is Barbara's in SHOT 3"}]))

SHOTS.append(dict(beat="SC05-T2", take="SC05-T2", kind="multi", covers=["SC05-SH04", "SC05-SH05", "SC05-SH06", "SC05-SH07"], duration=14, line=L038, vo="L037", subject_motion="in_place",
    files=["PROD-FRONT", "INFO-PLACEMENT", "PROD-BOX", "C1", "N-FACE", "L-KITCHEN", "OUT-N-B5", "INFO-ROUTINE"], audios=["C1"],
    title="Scene 5 · T2 — the strap on Barbara's knee; the box; They come in twos (SH04–SH07)", start_pos=P["T2_START"], end_pos=P["T2_END"],
    prompt=" ".join([
        manifest([("@image1", "is " + STRAP + "."), ("@image2", "is a real photo of the strap worn: centred on the patellar tendon, just below the kneecap, the kneecap's lower edge seated in the shell's notch — wear it exactly there."),
                  ("@image3", "is a real photo of the open product box: small and black, the strap's slots inside; copy the box exactly, but in this scene ONE strap lies in it and the other slot is empty."),
                  ("@image4", SHEET("Barbara", BARB_B5)), ("@image5", FACE_N), ("@image6", KITCHEN), ("@image7", CARD_N), ("@image8", CARD_ROUTINE), ("@audio1", VOICE("Barbara"))]),
        SERIES, LOOK, INHERIT, B5_MORNING, NOSPK,
        "One scene covered in 4 shots within a single take, all on the same side of the action line, with the same light, look and wardrobe throughout. Frame 1: " + P["T2_START"] + ". "
        "Everyone stays seated in their place. The action carries straight across every cut: each shot picks up the movement exactly where the last one left it — the same hand, the same object, the same direction — and everyone is where the last shot left them. "
        f"SHOT 1, [0s-4s]: ECU, low and front-on at knee height, Camera on a tripod, locked: Barbara's bare right knee fills the frame, the navy shorts hem just above it; the strap of Image1 sits exactly as in Image2, "
        "centred on the tendon just below her kneecap, its shell about a third of the frame wide, the wordmark facing us. She holds the knee still for us to see. "
        f"SHOT 2, [4s-7s]: CU, three-quarter, Her, {HER_ID}, in {HER_B5}, looks down at Barbara's knee, unimpressed, one eyebrow barely lifting, her lips sealed and jaw still. "
        "SHOT 3, [7s-10s]: ECU from above at a high three-quarter: Barbara's hand lays the small open box of Image3 on the pine table beside Her's two white tablets — one spare strap lying in it, the other slot empty — and lets go. "
        f"SHOT 4, [10s-14s]: MCU in profile, Barbara, {BARB_ID}, in {BARB_B5}, sits back in her chair, matter-of-fact, and says: " + L038 + " "
        "Each cut lands on a completed action. The eyelines match across the table. Nobody looks into the lens. Last frame: " + P["T2_END"] + ".",
        F2, PHYS,
        "THE STRAP, every time it is seen: exactly Image1 — the rigid black shell keeps its shape and size, never bends, never stretches, never turns into a sleeve, a brace or a band; only the knit band is soft.",
        "While the line is spoken, Barbara keeps doing one thing with their hands: her hands resting on her thighs, at one steady hold through the line. It is ordinary and unhurried, and the hands never stop to gesture.",
        state("BARBARA", "in her own gilet and shorts across the table, the strap on her bare right knee", "she has laid the box down and sat back"),
        "FOCUS: SHOT 1 the strap and kneecap sharp; SHOT 2 Her's nearest eye; SHOT 3 the box and strap sharp; SHOT 4 Barbara's eye. The blur is optical: soft and round, never smeared.",
        dialogue("Barbara", L038, VOICE_C1, "she has shown Her the strap and put the spare in front of her. Speaking across the table to Her.",
                 "states it plainly, a fact not a sale. Opens matter-of-fact; turns on 'spare', a small shrug in the voice; exits looking at Her. Stress on 'never'.",
                 "plain and certain, conversational, matching the face in this shot.", "she wants Her to try it without being asked twice, which leaks only through leaving the box there."),
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, "no neoprene sleeve, no padded brace on Barbara, no strap over the kneecap or on the shin, no oversized strap, no second strap in the box, no cardigan, no Her speaking", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "the wrong product (FP01) or the wrong size (FP02)", "prevented_by": "the real front photo first, named with its 12 × 5 cm size and shape, a third of the frame in the ECU (FP11)"},
           {"risk": "the strap on the wrong place (FP03)", "prevented_by": "the real worn photo as Image2, 'centred on the tendon just below the kneecap', shin/kneecap negatives"},
           {"risk": "two straps in the box though Barbara wears one", "prevented_by": "'one spare strap, the other slot empty', negative"}]))

SHOTS.append(dict(beat="SC06-T1", take="SC06-T1", kind="multi", covers=["SC06-SH01", "SC06-SH02", "SC06-SH03"], duration=13, line=L040 + " " + L041, vo="L039", subject_motion="in_place",
    files=["PROD-FRONT", "N-FACE", "C1", "L-KITCHEN", "OUT-N-B5"], audios=["N", "C1"],
    title="Scene 6 · T1 — the sceptic: the strap in her palm; Just put it on and walk down the stairs (SH01–SH03)", start_pos=P["T3_START"], end_pos=P["T3_END"],
    prompt=" ".join([
        manifest([("@image1", "is " + STRAP + " — it fits across one palm, slide to slide no longer than the hand."), ("@image2", FACE_N), ("@image3", SHEET("Barbara", BARB_B5)), ("@image4", KITCHEN), ("@image5", CARD_N),
                  ("@audio1", VOICE("Her")), ("@audio2", VOICE("Barbara"))]),
        SERIES, LOOK, INHERIT, B5_MORNING.replace("two white tablets and her mug", "her mug and the small open box Barbara has just put down"), NOSPK,
        "THE EXCHANGE, word for word and in this order: " + L040 + " " + L041 + " — Her says the first line, Barbara answers with the second; nobody else speaks.",
        "One scene covered in 3 shots within a single take, all on the same side of the action line, with the same light, look and wardrobe throughout. Frame 1: " + P["T3_START"] + ". "
        "Everyone stays seated in their place. The action carries straight across every cut: each shot picks up the movement exactly where the last one left it — the same hand, the same object, the same direction — and everyone is where the last shot left them. "
        "SHOT 1, [0s-4s]: ECU straight down from above, Camera on a tripod, locked: the strap of Image1 rests across Her's open right palm, the shell filling about half the frame, the wordmark up; "
        "she turns it over once, slowly, to look at the back, and back again. Her lips sealed and jaw still. "
        f"SHOT 2, [4s-9s]: MCU, three-quarter, Camera on a tripod, locked: Her, {HER_ID}, in {HER_B5}, holds the strap up between finger and thumb at chin height, sceptical, and says, dry and flat: " + L040 + " "
        f"SHOT 3, [9s-13s]: CU, low three-quarter on Barbara, {BARB_ID}, in {BARB_B5}: she leans in across the table toward Her, forearms on the wood, and says, certain and simple: " + L041 + " "
        "Each cut lands on a completed line. The eyelines match across the table. Nobody looks into the lens. Last frame: " + P["T3_END"] + ".",
        F2, PHYS,
        "THE STRAP, every time it is seen: exactly Image1 — the rigid black shell keeps its shape and size in her hand, never bends, never stretches, never turns into a sleeve or a brace; only the knit band hangs soft.",
        "While the lines are spoken, Her keeps doing one thing with their hands: her right hand holding the strap up at chin height, at one steady hold through the line. It is ordinary and unhurried, and the hands never stop to gesture.",
        state("HER", "in the outfit of her card at the pine table, the ice pack on her right knee, the spare strap in her hand", "she holds the strap up"),
        "FOCUS: SHOT 1 the strap sharp in her palm; SHOT 2 her nearest eye, the strap a little soft; SHOT 3 Barbara's eyes. The blur is optical: soft and round, never smeared.",
        dialogue("Her", L040, VOICE_N, "she has been handed a small strap after years of braces and pills. Speaking across the table to Barbara.",
                 "dismisses it, dry. Opens on the name as a sigh; turns on 'possibly'; exits looking at the strap. Stress on 'possibly'.",
                 "dry and flat, a little tired, matching the face in this shot.", "part of her wants it to work, which leaks only through her not putting it down."),
        dialogue("Barbara", L041, VOICE_C1, "her cousin has dismissed it, as she once did. Leaning in across the table.",
                 "a simple instruction, no argument. Opens level; turns on 'stairs', where she nods once; exits holding Her's eyes. Stress on 'walk'.",
                 "certain and simple, a little lower, matching the face in this shot.", "she knows the stairs will do the arguing for her, which leaks only through how calm she is."),
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, "no neoprene sleeve, no padded brace, no oversized strap, no strap bending like rubber, no cardigan, no standing up, no Barbara saying Her's line", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "the strap changes shape in her hand (FP01, FP05)", "prevented_by": "the real front photo first, rigid shell named, bending/sleeve negatives"},
           {"risk": "the voices swap", "prevented_by": "Audio1 Her, Audio2 Barbara, every line named with its speaker, negative"},
           {"risk": "the strap too big for her palm (FP02)", "prevented_by": "12 × 5 cm, 'no longer than the hand', oversized negative"}]))

FILES = {"N-FACE": "cast/N-HER_face.png", "C1": "cast/C1-BARBARA_v1.png", "L-KITCHEN": "plates/L-KITCHEN_v1.png",
         "OUT-N-B5": "body/SC05/ingredients/OUT-N-B5_v2.png", "INFO-ROUTINE": "body/SC05/ingredients/INFO-ROUTINE_v1.png",
         "PROD-FRONT": "../../products/stryde/stryde_refs/front.webp", "INFO-PLACEMENT": "../../products/stryde/stryde_refs/worn_front.jpg",
         "PROD-BOX": "../../products/stryde/stryde_refs/package_open.jpg"}
AUDIO = {"N": "voice/N_voice_master.mp3", "C1": "voice/C1_voice_master.mp3"}

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
                "subject_motion": s["subject_motion"], "prefer_multi_shots": "false", "generation": s.get("gen", 1), "user_go": GO,
                "risks": s["risks"], "vo": s.get("vo"), "scene": int(s["beat"][2:4]), "title": s["title"],
                "taste": ["HT02", "HT17", "HT18", "HT22", "HT23", "HT26", "FP01", "FP02", "FP03", "FP11", "FP12", "FP15"]}
        out = H / f"{s['beat']}.call.json"
        out.write_text(json.dumps(call, indent=1, ensure_ascii=False))
        (H / f"{s['beat']}.prompt.txt").write_text(s["prompt"])
        print(s["beat"], s["duration"], "s", len(s["prompt"]), "chars")
