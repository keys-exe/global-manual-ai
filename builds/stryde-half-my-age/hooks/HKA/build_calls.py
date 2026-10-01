"""Hook A (station stairs) — Seedance 2.5 ingredients calls, one per act-map row (§24K/§24N, V7.68.0: no frames)."""
import json
from pathlib import Path

H = Path(__file__).parent
B = H.parents[1]

SERIES = ("The look of a high-end live-action drama series: shot on a large-format digital cinema camera with spherical prime lenses, 24 frames per second with natural motion blur. "
          "Motivated low-key light from real sources in the scene — a window, a practical lamp, an overhead fixture — with a shadow side on every face, deep shadows that still hold detail and highlights that roll off softly; never flat and never evenly lit. "
          "Shallow depth of field on close shots, the room layered in depth behind. Natural, rich, restrained colour straight from the camera, real skin texture, worn costumes and a lived-in set. Restrained, specific performances.")
LOOK = (B / "cast/LOOK.txt").read_text().strip().replace("shot like a prestige streaming series", "shot like a prestige drama series")
INHERIT = ("The look exactly as set out here, from the first frame to the last: same lens, same depth of field, same colours, same light direction and same optical texture. "
           "Nothing about the look changes across the clip. 24 frames per second with a 180-degree shutter, so moving hands and objects carry natural motion blur.")
F2 = ("Camera on a tripod, framed and locked, with no drift, no sway and no reframe. The only camera life is one small operator pan or tilt of a few degrees to keep the subject in frame as they shift. "
      "It arrives a beat late and corrects only part of the way. The subject and the room carry all the other movement.")
F1 = lambda cm: (f"Camera on a dolly, already moving on the first frame: a slow, steady push toward the subject covering about {cm} centimetres across the whole clip, perfectly level, with no bounce and no sway. "
                 "As the line lands the move eases and slows but never stops. Still creeping in on the final frame. The subject stays in place — seated, standing or speaking — and never walks while the camera moves.")
PHYS = ("Everything in frame keeps the exact form, proportion and count it has from the first frame to the last — nothing melts, merges, splits, grows or becomes something else. "
        "Same person every frame: same face, bone structure, age, hair and wardrobe. Five separate fingers on each hand throughout, never fusing and never passing through anything. "
        "Limbs stay attached, keep their length, and bend only the way real joints bend. Mass and momentum in all movement: nothing at uniform speed, nothing stops instantly; "
        "weight transfers first and the hands arrive last; hair, coat hems and bag straps lag and settle after the body stops.")
AUD = ("Audio is clean production sound from a boom microphone just out of frame above the speaker: close, clear and even, with a little of the room's natural tone behind the voice. "
       "The microphone and all sound equipment stay completely outside the picture: nothing hangs into the top of the frame. Breath and mouth detail are present but never exaggerated. "
       "No phone-microphone proximity, no compression pumping, no music and no sound effects anywhere in the clip — dialogue only.")
SILENT = "The clip carries no dialogue and no voice at all: nobody speaks."
NEG_EQUIP = "no microphone in frame, no boom pole, no film equipment, no crew in frame"
NEG_MORPH = "no morphing, no warping, no melting, no merging, no splitting, no duplicate people, no background bending, no texture swimming, no flickering geometry"
NEG_FILM = ("no phone camera look, no smartphone processing, no HDR tone-mapping, no flat lifted shadows, no over-sharpening halos, no selfie framing, no front-camera distortion, "
            "no handheld phone jitter, no digital video look, no CGI look, no plastic skin, no beauty retouch, no diffusion filter glow on skin, no soft-focus beauty lighting, "
            "no flat frontal key, no unmotivated light, no applied vignette oval, no letterbox bars, no generated film grain, no slow motion, no speed ramp, no stock footage look, "
            "no commercial gloss, no perfect symmetrical face, no actor looking into the lens")
NEG_SCENECUT = ("no light direction changing within the scene, no colour changing between shots, no graded look, no wardrobe changing within the scene, no prop moving between shots unless shown moving, "
                "no character changing position between shots, no camera crossing the action line, no eyeline pointing the wrong way, no time of day changing within the scene, no different room, "
                "no extra people, no missing people, no tears, redness or sweat appearing or vanishing between shots, no hair or clothing state resetting between shots, no prop jumping to the other hand")
NEG_DRAMA = ("no theatrical acting, no mugging, no soap-opera reactions, no exaggerated crying, no streaming tears, no glycerin tears, no frozen listener, no blank face while being spoken to, "
             "no reaction arriving before the line that causes it, no emotion resetting between shots, no two characters speaking at once unless the script overlaps them, no speech directed at the camera, "
             "no performing to the lens, no expression held for effect, no nodding along while speaking, no constant half-smile, no eyebrows rising on every stressed word, no hand gesture on every phrase, "
             "no head tilt on every line, no voice steadier or brighter than the face, no voice resetting between lines")
NEG_SOUND = "no music, no score, no sound effects, no foley, no background ambience events, no singing, no humming, no background music, no soundtrack"
NEG_STAIRS = "no stairs bending, no steps changing count or height, no rail bending or breaking, no foot passing through a step, no feet sliding or skating, no stumble, no trip, no running"

VOICE_C2 = ("An English woman of forty-six from the north of England, a quick, warm mid-range voice with the same flat northern vowels as her mother, a little brisker and higher. "
            "Concern tucked under teasing; words tumble slightly faster than her mother's.")
VOICE_N = ("An English woman of seventy-one from the north of England, Lancashire, a light, dry, slightly reedy voice with a little gravel at the bottom of her range. Plain northern vowels, flat \"a\", "
           "unhurried and understated — she says the big things quietly and lets a line land without pushing it. A dry humour just under the surface. Statements fall at the end; never sing-song, never theatrical.")

HER_OUT = "a buttoned knee-length forest-green wool coat, straight grey wool trousers, black flat ankle boots, and a small tan leather shoulder bag"
DAU_OUT = "an olive hooded parka open over a cream cable-knit jumper, dark indigo jeans and tan ankle boots"
HER_ID = "a slight, narrow-shouldered woman of seventy-one with a steel-grey blunt chin-length bob and a heavy straight fringe"
DAU_ID = "a sturdy woman in her mid-forties with dark brown hair in a loose low bun, strands loose at the temples"

STATION = ("THE SET, exactly as in the location reference: a small British railway station on an overcast late morning — worn sandstone steps with a black iron centre rail down to the platform, "
           "green-and-cream painted iron columns holding a glass canopy, and a train standing at the platform with its doors open. Light: flat cool overcast daylight, about 6500K, through the glass canopy, "
           "brighter from the left; soft shadows on the right side of every face.")
CARRIAGE = ("THE SET, exactly as in the location reference: the inside of a British regional train carriage — blue moquette facing seats across a grey table, yellow grab poles, "
            "wide windows on the left with the overcast town sliding past. Light: cool overcast daylight, about 6500K, through the windows on the left; the aisle side of each face falls into soft shadow.")


def manifest(items):
    """items: list of (tag, clause). ING-MANIFEST (§4, V7.68.0)."""
    return ("INGREDIENTS. " + " ".join(f"{t} {c}" for t, c in items) +
            " These references set who, where and what things ARE; the prose below sets the shot and what HAPPENS, and nothing in them is a shot to cut to.")


SHEET = lambda name, out: f"is {name}: face, age, hair and build only, with the wardrobe as written below ({out}) and never from this sheet."
VOICE = lambda name: f"is {name}'s voice, its timbre, pitch, accent and pace, for every line {name} speaks; it sets who they sound like, never how they feel in this shot."
PLACE = lambda desc: f"is the place: {desc}, its walls, windows, furniture and light side exactly as shown."
CARD = ("is an info card: Her outfit on this day — the forest-green wool coat, grey trousers, black ankle boots and the tan shoulder bag; follow it exactly, "
        "and its caption strip and any text on it never appear in the clip.")


def state(name, what, change="nothing"):
    return f"{name} still carries exactly what this scene has done to them so far: {what}. None of it resets: it is the same as in the previous shot, except {change}. It holds in every frame."


def negs(*extra):
    return "NEGATIVES: " + ", ".join(x for x in extra if x) + "."


SHOTS = []

# SH01 — the daughter at the top, HER already three steps down. L001.
L1 = "Mum… the next one’s in ten minutes, we can…"
SHOTS.append(dict(
    beat="HKA-SH01", kind="dialogue", duration=6, speaker="C2", line=L1, subject_motion="in_place",
    files=["C2", "N", "L-STATION", "OUT-N-HA"], audios=["C2"],
    prompt=" ".join([
        manifest([("@image1", SHEET("the daughter", DAU_OUT)), ("@image2", SHEET("Her", "the outfit on the info card")),
                  ("@image3", PLACE("the station steps down to the platform under the glass canopy")), ("@image4", CARD),
                  ("@audio1", VOICE("the daughter"))]),
        SERIES, LOOK, INHERIT, STATION,
        "THE SHOT: a high wide shot from just behind and above the daughter's right shoulder at the top of the station steps, looking down the whole flight: "
        "the daughter, " + DAU_ID + ", in " + DAU_OUT + ", fills the near right third of the frame from behind; below her, Her — " + HER_ID + ", in " + HER_OUT + " — is already three steps down, small in the frame, going down.",
        "The clip opens with Her three steps down. The daughter reaches her left hand for the black iron rail and calls down after her: \"" + L1 + "\" "
        "Her keeps going, stepping down one step per second, one foot per step, her right hand holding the bag strap, never looking back in this shot. "
        "The daughter stays at the top; only her arm and head move.",
        F2, PHYS,
        "While the line is spoken, the daughter keeps doing one thing with their hands: her left hand closing on the rail and resting there, at one grip through the line. It is ordinary and unhurried, and the hands never stop to gesture.",
        state("THE DAUGHTER", "slightly out of breath from hurrying, hair in its loose low bun, parka open, standing on the top step", "nothing"),
        state("HER", "calm, brisk, the tan bag's strap in her right hand, three steps down and going", "she is one step further down each second"),
        "FOCUS: everything from the daughter's shoulder to Her on the steps is in sharp focus; everything from near to far stays sharp. The blur is optical: soft and round, never smeared.",
        "DIALOGUE (the daughter, verbatim): \"" + L1 + "\" " + VOICE_C2 + " IN THIS MOMENT: she is trying to slow her mother down and cannot quite believe she has to. Speaking to her mother, fond and a little exasperated. "
        "PLAYING: coaxes her mother. Opens hurried, a breath behind; turns on the exact word 'ten', where her voice lifts as if the number should settle it; exits trailing off as her mother simply keeps going. Stress on 'ten'. "
        "VOICE NOW: a little breathless, raised to carry down the stairs, quick, continuing from how the daughter sounded on the previous line, and matching the face in this shot. "
        "UNDER THE LINE: she is the one struggling to keep up, and she knows it, which leaks only through the second 'we can…' fading out. Played small and true, for a camera close enough to see a thought. Never theatrical, never pushed, never performed to the lens.",
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, NEG_STAIRS, NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "HER turns back or stops on the stairs", "prevented_by": "'never looking back in this shot', one step per second, STATE-CARRY"},
           {"risk": "stairs warp or feet skate", "prevented_by": "PHYS + stairs negatives, locked tripod, HER small in frame"},
           {"risk": "wardrobe taken from the sheets", "prevented_by": "sheet clauses name the story-day outfit; outfit info card for Her"}]))

# SH02 — HER, low three-quarter, turns her head back up. L002.
L2 = "Not waiting ten minutes, love."
SHOTS.append(dict(
    beat="HKA-SH02", kind="dialogue", duration=4, speaker="N", line=L2, subject_motion="travels",
    files=["N", "L-STATION", "OUT-N-HA"], audios=["N"],
    prompt=" ".join([
        manifest([("@image1", SHEET("Her", "the outfit on the info card")), ("@image2", PLACE("the station steps down to the platform under the glass canopy")),
                  ("@image3", CARD), ("@audio1", VOICE("Her"))]),
        SERIES, LOOK, INHERIT, STATION,
        "THE SHOT: a medium shot from low on the steps below her, three-quarter on, the camera looking up: Her, " + HER_ID + ", in " + HER_OUT + ", coming down the sandstone steps toward the camera side, the glass canopy and the top of the stairs behind her.",
        "She keeps stepping down one step per second, one foot per step, left hand free of the rail and swinging easily, the tan bag's strap in her right hand. "
        "Without stopping she turns her head back up over her left shoulder toward her daughter above, out of frame at the top, and says: \"" + L2 + "\" Then her eyes come forward again and she carries on down.",
        F2, PHYS,
        "While the line is spoken, Her keeps doing one thing with their hands: her right hand carrying the bag by its strap, at one easy swing per step. It is ordinary and unhurried, and the hands never stop to gesture.",
        state("HER", "calm, dry-eyed, bob and fringe in place, coat buttoned, bag strap in her right hand, three steps down and going", "she has come a few steps further down"),
        "FOCUS: the nearest eye of Her is in sharp focus; the stairs and canopy behind fall to a soft, recognisable shape. The blur is optical: soft and round, never smeared.",
        "DIALOGUE (Her, verbatim): \"" + L2 + "\" " + VOICE_N + " IN THIS MOMENT: she is enjoying herself and does not need rescuing. Speaking to her daughter, fond, teasing. "
        "PLAYING: teases her daughter. Opens light and dry over her shoulder; turns on the exact word 'love', where it softens into warmth; exits already looking where she is going. Stress on 'Not'. "
        "VOICE NOW: easy, dry, not out of breath at all, a little raised to carry up the stairs, continuing from how Her sounded on the previous line, and matching the face in this shot. "
        "UNDER THE LINE: six weeks ago she could not have done this, which leaks only through a tiny private pleasure at the corner of her mouth. Played small and true, for a camera close enough to see a thought. Never theatrical, never pushed, never performed to the lens.",
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, NEG_STAIRS, NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "she stops walking to speak", "prevented_by": "'Without stopping', one step per second, STATE-CARRY"},
           {"risk": "legs or steps distort on the descent", "prevented_by": "PHYS + stairs negatives, medium framing, tripod"},
           {"risk": "voice not hers", "prevented_by": "VOICE-N master as @audio1 + VOICE-N profile"}]))

# SH03 — silent profile: the last steps and through the open train doors.
SHOTS.append(dict(
    beat="HKA-SH03", kind="broll", duration=4, speaker=None, line="", subject_motion="travels",
    files=["N", "L-STATION", "OUT-N-HA"], audios=[],
    prompt=" ".join([
        manifest([("@image1", SHEET("Her", "the outfit on the info card")), ("@image2", PLACE("the platform with the train standing, doors open, under the glass canopy")), ("@image3", CARD)]),
        SERIES, LOOK, INHERIT, STATION,
        "THE SHOT: a full-length profile shot at eye height from the platform side: Her, " + HER_ID + ", in " + HER_OUT + ", seen side-on, whole body in frame, the train's open doors ahead of her at frame right.",
        "She comes down the last two steps onto the platform, one step per second, one foot per step, walks three even strides to the open train doors and steps up through them into the carriage, brisk and even, "
        "the tan bag's strap in her right hand. The clip ends as she is inside the doors.",
        F2, PHYS,
        state("HER", "calm, bob and fringe in place, coat buttoned, bag strap in her right hand, reaching the bottom of the stairs", "she reaches the platform and boards"),
        "FOCUS: everything from the stairs to the train doors is in sharp focus; everything from near to far stays sharp. The blur is optical: soft and round, never smeared.",
        SILENT,
        negs(NEG_EQUIP, NEG_MORPH, NEG_STAIRS, "no doors closing on her, no other passengers boarding", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "the camera follows her (travels with a moving subject)", "prevented_by": "F2 locked tripod, one late partial pan only"},
           {"risk": "doors or train deform as she boards", "prevented_by": "PHYS + morph negatives, plate reference"},
           {"risk": "sound or music generated", "prevented_by": "generate_audio false, SILENT line, NEG-SOUND"}]))

# SH04 — the daughter drops into the seat opposite. L003.
L3 = "When did that happen?"
SHOTS.append(dict(
    beat="HKA-SH04", kind="dialogue", duration=4, speaker="C2", line=L3, subject_motion="still",
    files=["C2", "L-CARRIAGE"], audios=["C2"],
    prompt=" ".join([
        manifest([("@image1", SHEET("the daughter", DAU_OUT)), ("@image2", PLACE("the inside of the train carriage, facing seats across a table")), ("@audio1", VOICE("the daughter"))]),
        SERIES, LOOK, INHERIT, CARRIAGE,
        "THE SHOT: a medium close-up, three-quarter on, at seated eye height: the daughter, " + DAU_ID + ", in " + DAU_OUT + ", seated by the window side of the table, looking across the table at her mother just off the lens to frame left.",
        "The clip opens with her just sat down, chest still rising from the stairs. She catches her breath, staring across at her mother, and says: \"" + L3 + "\"",
        F1(25), PHYS,
        "While the line is spoken, the daughter keeps doing one thing with their hands: her right hand resting flat on the grey table, still, at one rest through the line. It is ordinary and unhurried, and the hands never stop to gesture.",
        state("THE DAUGHTER", "out of breath from the stairs, a few strands loose from her low bun, parka open, seated opposite her mother", "her breathing settles a little"),
        "FOCUS: the nearest eye of the daughter is in sharp focus; the carriage behind falls to a soft, recognisable shape. The blur is optical: soft and round, never smeared.",
        "DIALOGUE (the daughter, verbatim): \"" + L3 + "\" " + VOICE_C2 + " IN THIS MOMENT: she is amazed and a little put out that she missed it. Speaking to her mother, genuinely asking. "
        "PLAYING: questions her mother. Opens winded, a breath first; turns on the exact word 'that', where her eyebrows draw together, curious; exits waiting for an answer. Stress on 'that'. "
        "VOICE NOW: breathy from the stairs, lower than on the platform, slower, continuing from how the daughter sounded on the previous line, changed only by the climb down and the run for the train, and matching the face in this shot. "
        "UNDER THE LINE: she is a little worried she has not been paying attention to her mother, which leaks only through a glance down at her own hand before she looks back up. Played small and true, for a camera close enough to see a thought. Never theatrical, never pushed, never performed to the lens.",
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "she stands or moves while the camera pushes", "prevented_by": "seated, still; F1 on a still subject"},
           {"risk": "a different carriage", "prevented_by": "L-CARRIAGE plate + SET line"},
           {"risk": "voice drifts from the master", "prevented_by": "VOICE-C2 master as @audio1"}]))

# SH05 — over the daughter's shoulder onto HER, calm by the window. VO L004 laid in the edit (6.3s).
SHOTS.append(dict(
    beat="HKA-SH05", kind="broll", duration=7, speaker=None, line="", vo="L004", subject_motion="still",
    files=["N", "C2", "L-CARRIAGE", "OUT-N-HA"], audios=[],
    prompt=" ".join([
        manifest([("@image1", SHEET("Her", "the outfit on the info card")), ("@image2", SHEET("the daughter", DAU_OUT)),
                  ("@image3", PLACE("the inside of the train carriage, facing seats across a table")), ("@image4", CARD)]),
        SERIES, LOOK, INHERIT, CARRIAGE,
        "THE SHOT: a close-up over the daughter's shoulder: the soft back of the daughter's head and parka shoulder frame the near right edge, out of focus; across the table, Her, " + HER_ID + ", in " + HER_OUT + ", sits by the window, the tan bag on her lap, both hands resting on it.",
        "She sits settled, looking out of the window at the town sliding past, and a small private smile arrives at the corner of her mouth and stays. She blinks naturally; nothing else moves but the light from the passing window.",
        F1(20), PHYS,
        state("HER", "calm, not out of breath at all, bob and fringe in place, coat buttoned, the tan bag on her lap under both hands, seated by the window", "the small smile arrives"),
        state("THE DAUGHTER", "still a little out of breath, parka open, seated opposite with her back to the camera", "nothing"),
        "FOCUS: the nearest eye of Her is in sharp focus; the daughter's shoulder in front and the carriage behind fall to a soft, recognisable shape. The blur is optical: soft and round, never smeared.",
        SILENT,
        negs(NEG_EQUIP, NEG_MORPH, "no talking, no mouth moving", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "her mouth moves as if speaking", "prevented_by": "SILENT line, 'no talking, no mouth moving', generate_audio false"},
           {"risk": "the smile overplayed", "prevented_by": "'small private smile', NEG-DRAMA (no constant half-smile, no expression held for effect)"},
           {"risk": "window light flicker or the town warping", "prevented_by": "morph negatives, overcast flat light"}]))

FILES = {"C2": "cast/C2-DAUGHTER_v1.png", "N": "cast/N-HER_v1.png", "L-STATION": "plates/L-STATION_v1.png",
         "L-CARRIAGE": "plates/L-CARRIAGE_v1.png", "OUT-N-HA": "hooks/HKA/OUT-N-HA_v1.png"}
AUDIO = {"C2": "voice/C2_voice_master.mp3", "N": "voice/N_voice_master.mp3"}

if __name__ == "__main__":
    for s in SHOTS:
        call = {"beat": s["beat"], "connector": "seedance", "mode": 4, "kind": s["kind"], "prompt": s["prompt"],
                "duration": s["duration"], "resolution": "720p", "aspect_ratio": "9:16", "start_image": None,
                "ingredients_approved": True, "files": [FILES[f] for f in s["files"]],
                "audios": [AUDIO[a] for a in s["audios"]], "generate_audio": bool(s["line"]),
                "dialogue": s["line"] or None, "script_line": s["line"] or None, "pace": "unhurried",
                "subject_motion": s["subject_motion"], "prefer_multi_shots": "false", "generation": 1,
                "risks": s["risks"], "vo": s.get("vo")}
        (H / f"{s['beat']}.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
        (H / f"{s['beat']}.prompt.txt").write_text(s["prompt"])
        print(s["beat"], s["duration"], "s", len(s["prompt"]), "chars")
