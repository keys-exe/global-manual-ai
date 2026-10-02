"""Scene 1 / Hook 1 — THE TOAST (day D1, the hosts' yard at golden hour). Seedance 2.5 takes via Higgsfield (omni_reference, 720p, 9:16),
ingredients only, no frames (§4 V7.68.0, §24K part 5 V7.88.0). User go: "PROCEED" (2026-10-02) with VOICE-N, VOICE-C1 and CAKE-CARD confirmed.
D1 outfits = the cast sheets' own outfits (wardrobe.json), so full sheets go in (HT26 applies only when the day's outfit differs).
Voice refs hold only the take's own words (L33): Greg's cut from his master, Susan's 'Greg. Sit down.' voiced by her clone 'Mother'.
Director's notes: the camera lives on Susan once Greg is cruel — Greg is heard, never seen, in T2/T3; room tone, no music (VN07).
Shared strings follow the sister build's hook builder; AUD is the current AUD-FILM (L13: no microphone named)."""
import json, re, sys
from pathlib import Path
H = Path(__file__).parent; B = H.parents[1]; ROOT = B.parents[1]
T = (ROOT / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
S = lambda i: re.search(r"\*\*`%s`\*\*[^\n]*\n```\n(.*?)\n```" % re.escape(i), T, re.S).group(1).strip()

SERIES = ("The look of a high-end live-action drama series: shot on a large-format digital cinema camera with spherical prime lenses, 24 frames per second with natural motion blur. "
          "Motivated low-key light from real sources in the scene — the low sun, the string-light bulbs, a candle — with a shadow side on every face, deep shadows that still hold detail and highlights that roll off softly; never flat and never evenly lit. "
          "Shallow depth of field on close shots, the yard layered in depth behind. Natural, rich, restrained colour straight from the camera, real skin texture, real clothes and a lived-in set. Restrained, specific performances.")
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
        "weight transfers first and the hands arrive last; hair and fabric lag and settle after the body stops.")
AUD = S("AUD-FILM")
NEG_SOUND = S("NEG-SOUND")
NEG_EQUIP = "no film equipment, no crew in frame"
NEG_MORPH = "no morphing, no warping, no melting, no merging, no splitting, no duplicate people, no background bending, no texture swimming, no flickering geometry"
NEG_FILM = ("no phone camera look, no smartphone processing, no HDR tone-mapping, no flat lifted shadows, no over-sharpening halos, no selfie framing, no front-camera distortion, "
            "no handheld phone jitter, no digital video look, no CGI look, no plastic skin, no beauty retouch, no diffusion filter glow on skin, no soft-focus beauty lighting, "
            "no flat frontal key, no unmotivated light, no applied vignette oval, no letterbox bars, no generated film grain, no slow motion, no speed ramp, no stock footage look, "
            "no commercial gloss, no perfect symmetrical face, no actor looking into the lens")
NEG_SCENECUT = ("no light direction changing within the scene, no colour changing between shots, no graded look, no wardrobe changing within the scene, no prop moving between shots unless shown moving, "
                "no character changing position between shots, no camera crossing the action line, no eyeline pointing the wrong way, no time of day changing within the scene, no different place, "
                "no extra people, no missing people, no tears, redness or sweat appearing or vanishing between shots, no hair or clothing state resetting between shots, no prop jumping to the other hand")
NEG_DRAMA = ("no theatrical acting, no mugging, no soap-opera reactions, no exaggerated crying, no streaming tears, no glycerin tears, no frozen listener, no blank face while being spoken to, "
             "no reaction arriving before the line that causes it, no emotion resetting between shots, no two characters speaking at once unless the script overlaps them, no speech directed at the camera, "
             "no performing to the lens, no expression held for effect, no nodding along while speaking, no constant half-smile, no eyebrows rising on every stressed word, no hand gesture on every phrase, "
             "no head tilt on every line, no voice steadier or brighter than the face, no voice resetting between lines")
NEG_CAKE = "no writing or lettering on the cake, no cut cake, no slice taken, no knife at the cake, no second cake"

VOICE_N = ("An American woman of forty-nine from the suburban Midwest, a low, warm, slightly smoky voice, plain General American vowels, unhurried. She says the worst things quietly and flatly, "
           "almost to herself, and lets a line sit. Statements fall at the end; never breathy, never theatrical.")
VOICE_C1 = ("An American man of fifty-two, a warm, easy baritone with a little gravel, relaxed General American vowels, sociable and sure of himself; when he talks quietly the warmth drops out and it goes flat. "
            "Tonight a few drinks in: the consonants a little soft, the timing loose. Never shouting, never theatrical.")
SUSAN_ID = "a slim woman of forty-nine with shoulder-length layered honey-brown hair, blonde streaks and grey at the roots, worn loose"
GREG_ID = "a tall, broad man of fifty-two with thick salt-and-pepper hair combed back and a tanned, lined face"
PAULA_ID = "a slim woman of forty-nine with a chin-length wavy chestnut bob and a grey streak at the left temple"
SUSAN_D1 = "a dusty-blue loose chiffon blouse with a soft V neck and cream linen trousers, small pearl drop earrings"
GREG_D1 = "a navy textured blazer over a pale blue open-collar shirt and khaki chinos"
PAULA_D1 = "a plum satin sleeveless cowl-neck top and charcoal trousers"
FA_D1, FB_D1 = "a mustard linen wrap dress", "a pale pink silk shirt and white wide-leg trousers"

def manifest(items):
    return ("INGREDIENTS. " + " ".join(f"{t} {c}" for t, c in items) +
            " These references set who, where and what things ARE; the prose below sets the shot and what HAPPENS, and nothing in them is a shot to cut to.")
SHEET = lambda name, out: f"is {name}: face, age, hair and build, wearing exactly the outfit shown on this sheet ({out}) — tonight's outfit."
VOICE = lambda name: f"is {name}'s voice, its timbre, pitch, accent and pace, for the words {name} speaks; it sets who they sound like, never how they feel in this shot."
YARD = ("is the place: the hosts' back yard at golden hour — the one long white-clothed table running down the middle of the lawn toward the house, the swags of warm bulb lights on tall wooden posts, "
        "the house's pale grey clapboard back with its raised deck at the far end, the hedge and trees on both sides; its layout and light side exactly as shown.")
CAKE = ("is the layout of the middle of that table seen from above: the one plain white rectangular sheet cake on its board, smooth white frosting with nothing written on it, uncut, "
        "a jar of white roses at each end of it, glass candle holders, white plates and wine glasses; every shot of this table copies it exactly.")
def state(name, what, change="nothing"):
    return f"{name} still carries exactly what this scene has done to them so far: {what}. None of it resets: it is the same as in the previous shot, except {change}. It holds in every frame."
def negs(*extra): return "NEGATIVES: " + ", ".join(x for x in extra if x) + "."
def dialogue(who, line, voice, moment, playing, now, under):
    return (f"DIALOGUE ({who}, verbatim): {line} {voice} IN THIS MOMENT: {moment} PLAYING: {playing} VOICE NOW: {now} "
            f"UNDER THE LINE: {under} Played small and true, for a camera close enough to see a thought. Never theatrical, never pushed, never performed to the lens.")

GEO = ("THE SCENE SO FAR, the thirtieth wedding anniversary dinner, one continuous moment at golden hour: the low sun sits behind the house at the far end of the yard and to the left, about 3800K, "
       "the warm bulbs glowing above the table, every face with a warm lit side and a soft shadow side. The long table runs away from us down the lawn toward the house, about thirty friends seated "
       "along both sides in muted creams, blues and greys — nobody in red. Halfway down the table, on its LEFT side, Susan sits in her chair facing across the table; Greg's chair is beside her on her left, "
       "nearer the garden end. Directly across the table from Susan, on the RIGHT side, sits Paula. The one white cake sits on the table between Susan and Paula, uncut. "
       "Friend A and Friend B sit further down the right side toward the house. Plates, glasses, candles and roses exactly as the cake card shows.")
NOSPK = "Nobody speaks except the words written below, by the person named; every other mouth stays closed."

L001 = "Thirty years. Thirty. Somebody get this woman a medal for putting up with me, right?"
L002 = "…thirty years. And I look at you lately and I just, I don't know."
L003 = "You look like my mother, Susan. When did that happen?"
L004 = "Greg. Sit down."
L005 = "Paula's the same age as you. Exact same. Look at her, then look at you. Just ask her what she does. That's all I'm saying."
R = {r["beat"]: r for r in json.load(open(B / "step5/act_map.json"))}
GO = "chat: \"PROCEED\" (user, 2026-10-02) — VOICE-N, VOICE-C1 and CAKE-CARD confirmed on the board"
SHOTS = []

SHOTS.append(dict(beat="SC01-T1", kind="multi", covers=["SC01-SH01", "SC01-SH02", "SC01-SH03"], duration=12, line=L001, subject_motion="in_place",
    files=["C1", "N", "C2", "C5", "C6", "L-YARD", "CAKE"], audios=["C1-L001"],
    title="Hook 1 · T1 — the toast begins: Thirty years (SH01–SH03)", start_pos=R["SC01-SH01"]["start_pos"], end_pos=R["SC01-SH03"]["end_pos"],
    prompt=" ".join([
        manifest([("@image1", SHEET("Greg", GREG_D1)), ("@image2", SHEET("Susan", SUSAN_D1)), ("@image3", SHEET("Paula", PAULA_D1)),
                  ("@image4", SHEET("Friend A", FA_D1)), ("@image5", SHEET("Friend B", FB_D1)), ("@image6", YARD), ("@image7", CAKE), ("@audio1", VOICE("Greg"))]),
        SERIES, LOOK, INHERIT, GEO, NOSPK,
        "One scene covered in 3 shots within a single take, all on the same side of the action line, with the same light, look and wardrobe throughout. Frame 1: " + R["SC01-SH01"]["start_pos"] + ". "
        "Everyone stays in their place. The action carries straight across every cut: each shot picks up the movement exactly where the last one left it, and everyone is where the last shot left them. "
        f"SHOT 1, [0s-4s]: WIDE from the garden end of the table at eye height, three-quarter, Camera on a tripod, locked: the whole long table under the bulbs, the friends mid-laugh; halfway down on the left, "
        f"Greg, {GREG_ID}, in {GREG_D1}, pushes up from his chair, sways a little and taps his wine glass twice with a fork; heads turn to him, smiling. "
        f"SHOT 2, [4s-9s]: MEDIUM from low across the table, three-quarter on Greg standing over the table, glass raised, a warm wide grin, the bulbs behind him; he says to the table, warm and loud: {L001} "
        f"SHOT 3, [9s-12s]: MCU at eye level from across the table, straight on Susan, {SUSAN_ID}, in {SUSAN_D1}, seated beside him: glasses rise all around her; she almost smiles and lifts her glass an inch off the table, her lips sealed. "
        "Each cut lands on a completed action. The eyelines match across the table. Nobody looks into the lens. Last frame: " + R["SC01-SH03"]["end_pos"] + ".",
        F2, PHYS,
        "While the line is spoken, Greg keeps doing one thing with his hands: his right hand holding his wine glass raised at chest height, at one steady hold through the line. It is ordinary and loose, and the hand never stops to gesture.",
        state("SUSAN", "seated at the table in the dusty-blue blouse, composed, a small polite smile", "her glass lifting an inch"),
        "FOCUS: SHOT 1 deep, the whole table sharp; SHOT 2 Greg's eyes sharp, the table soft; SHOT 3 Susan's nearest eye sharp, the raised glasses soft. The blur is optical: soft and round, never smeared.",
        dialogue("Greg", L001, VOICE_C1, "his thirtieth anniversary, a few drinks in, the whole table on his side. Standing, speaking to the table.",
                 "charms the table. Opens big and warm; turns on 'medal', a grin at his own joke; exits on 'right?' looking round for the laugh. Stress on 'Thirty'.",
                 "warm, loud, loose with drink, matching the face in this shot.", "the joke is half true and he knows it, which leaks only through not looking at Susan."),
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, NEG_CAKE, "no one in red, no Susan speaking", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "the cake gets writing or is cut", "prevented_by": "the cake card as Image7, 'nothing written on it, uncut', cake negatives"},
           {"risk": "the wrong person gives the toast or Susan speaks", "prevented_by": "the voice ref is Greg's own words only; NOSPK; 'no Susan speaking'"},
           {"risk": "the table layout drifts", "prevented_by": "GEO block: who sits where, left/right named from the plate's own view (HT22)"}]))

SHOTS.append(dict(beat="SC01-T2", kind="take", covers=["SC01-SH04"], duration=13, line=L002 + " " + L003, subject_motion="still",
    files=["N", "L-YARD", "CAKE"], audios=["C1-L001"],
    title="Hook 1 · T2 — 'You look like my mother': the push-in on Susan (SH04)", start_pos=R["SC01-SH04"]["start_pos"], end_pos=R["SC01-SH04"]["end_pos"],
    prompt=" ".join([
        manifest([("@image1", SHEET("Susan", SUSAN_D1)), ("@image2", YARD), ("@image3", CAKE), ("@audio1", VOICE("Greg"))]),
        SERIES, LOOK, INHERIT, GEO, NOSPK,
        "Greg's words, heard and never seen, in this order: " + L002 + " " + L003 + " ",
        "One continuous shot, never cut and never restarted, 13s, in one place with the same light, look and wardrobe throughout. Frame 1: " + R["SC01-SH04"]["start_pos"] + ". "
        f"CLOSE-UP at eye level from across the table, three-quarter on Susan, {SUSAN_ID}, in {SUSAN_D1}, seated; the white cake soft and out of focus in the near foreground between the lens and her. "
        "Greg stands just out of frame on her left and is never seen; only his voice is heard, close and quiet above her. "
        "[0s-7s]: his voice drops, almost to himself, puzzled, with the first line, then a small drunk laugh. [7s-13s]: quiet, a verdict not a rant, the second line. "
        "Susan does not look up at him. Her almost-smile goes; her eyes stay level, on nothing across the table; her lips stay sealed and her jaw still, the face holding the expression of the frame. "
        "On the last words her right hand moves slowly to the edge of the table and rests there. Last frame: " + R["SC01-SH04"]["end_pos"] + ". "
        "The movement is continuous from the first frame to the last: nobody jumps position or appears somewhere new, and the yard behind her stays the same yard. The frame holds on her face while the camera creeps in.",
        F1(40), PHYS,
        "LISTENING: Susan takes each word as it lands — a slow blink after 'mother', a breath held — and does not answer; nothing on her face arrives before the word that causes it.",
        state("SUSAN", "seated in the dusty-blue blouse, the smile gone, very still", "her hand coming to rest on the table edge"),
        "FOCUS: Susan's nearest eye sharp throughout; the cake in the foreground soft and round. The blur is optical: soft and round, never smeared.",
        dialogue("Greg (heard, off screen)", L002 + " " + L003, VOICE_C1, "the toast curdles; he is looking down at his wife in front of thirty friends. Standing just behind her left shoulder, out of frame.",
                 "names what he sees, as if it only just occurred to him. Opens trailing off; turns on 'mother', quieter, puzzled; exits on the question, genuinely asking. Stress on 'mother'.",
                 "quiet, slowed by drink, flat where it was warm a moment ago, matching his last line's level.", "he means it, which leaks only through how calm he sounds."),
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, NEG_CAKE, "no Greg in frame, no Susan speaking, no Susan crying, no tears", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "Greg appears in frame (the camera must live on Susan)", "prevented_by": "'never seen; only his voice is heard', 'no Greg in frame'"},
           {"risk": "Susan mouths his words", "prevented_by": "lips sealed and jaw still clause, 'no Susan speaking'"},
           {"risk": "the push-in becomes a zoom or drift", "prevented_by": "F1 at 40 cm, level, never stops; locked subject"}]))

SHOTS.append(dict(beat="SC01-T3", kind="multi", covers=["SC01-SH05", "SC01-SH06", "SC01-SH07"], duration=15, line=L004 + " " + L005, subject_motion="still",
    files=["N", "C2", "C1", "L-YARD", "CAKE"], audios=["N-L004", "C1-L005"],
    title="Hook 1 · T3 — 'Greg. Sit down.' / 'Paula's the same age as you' (SH05–SH07)", start_pos=R["SC01-SH05"]["start_pos"], end_pos=R["SC01-SH07"]["end_pos"],
    prompt=" ".join([
        manifest([("@image1", SHEET("Susan", SUSAN_D1)), ("@image2", SHEET("Paula", PAULA_D1)), ("@image3", "is Greg: only his navy blazer sleeve and his right hand are ever seen in this take."),
                  ("@image4", YARD), ("@image5", CAKE), ("@audio1", VOICE("Susan")), ("@audio2", VOICE("Greg"))]),
        SERIES, LOOK, INHERIT, GEO, NOSPK,
        "THE EXCHANGE, word for word and in this order: " + L004 + " " + L005 + " — Susan says the first line; Greg, heard and never seen, says the rest. Nobody else speaks.",
        "One scene covered in 3 shots within a single take, all on the same side of the action line, with the same light, look and wardrobe throughout. Frame 1: " + R["SC01-SH05"]["start_pos"] + ". "
        "Everyone stays in their place. Each shot picks up exactly where the last one left it. "
        f"SHOT 1, [0s-3s]: CLOSE-UP in profile from Susan's left at eye level, Camera on a tripod, locked: Susan, {SUSAN_ID}, in {SUSAN_D1}, lifts her eyes up to the left of frame toward Greg standing just out of frame "
        f"and says it low, just to him: {L004} "
        f"SHOT 2, [3s-9s]: MCU from a little above, straight on Paula, {PAULA_ID}, in {PAULA_D1}, seated across the table: she keeps her eyes down on her plate, mortified, her lips sealed; "
        "Greg's navy sleeve and loose right hand drift into the edge of the frame from the left, pointing across the table at her, then drop away; his voice, unseen, says the first part of his line. "
        f"SHOT 3, [9s-15s]: CLOSE-UP at eye level from across the table, straight on Susan again: absolutely still, eyes level, one slow breath, her right hand flat on the table edge, lips sealed, while Greg's unseen voice finishes the line. "
        "Each cut lands on a completed line. Nobody looks into the lens. Last frame: " + R["SC01-SH07"]["end_pos"] + ".",
        F2, PHYS,
        "While the lines are spoken, Susan keeps doing one thing with her hands: her right hand resting flat on the table edge, at one steady hold through the lines. It is ordinary and still, and the hands never stop to gesture.",
        "LISTENING: Paula takes the words without looking up — her jaw tightens on 'Look at her' — and Susan holds still through the rest; nothing on either face arrives before the word that causes it.",
        state("SUSAN", "seated in the dusty-blue blouse, still, the smile long gone, her hand on the table edge", "nothing"),
        "FOCUS: each shot's nearest eye sharp; the yard soft behind. The blur is optical: soft and round, never smeared.",
        dialogue("Susan", L004, VOICE_N, "her husband has just said it in front of everyone. Speaking up to him, low, so only he hears.",
                 "stops him, quietly. Opens on his name, flat; turns on 'down', firm; exits with her eyes going back to the table. Stress on 'down'.",
                 "low and level, very quiet, a little tight, matching the face in this shot.", "she is holding everything in front of these people, which leaks only through how quiet it is."),
        dialogue("Greg (heard, off screen)", L005, VOICE_C1, "she has told him to sit down and he hasn't. Standing beside her, gesturing loosely across the table at Paula.",
                 "makes his point as if it is reasonable. Opens loose; turns on 'what she does', leaning on it; exits on 'That's all I'm saying', already reaching for his chair. Stress on 'same'.",
                 "quiet, loose with drink, matter-of-fact, continuing from his last line's level.", "he thinks he is being helpful, which leaks only through how casual he sounds."),
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, NEG_CAKE, "no Greg's face in frame, no Paula speaking, no Paula looking at the lens, no Susan crying, no tears", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "the voices swap (Susan speaks Greg's line)", "prevented_by": "Audio1 Susan's own three words, Audio2 Greg's own words; THE EXCHANGE names who says what in order"},
           {"risk": "Greg's face appears", "prevented_by": "Image3 limited to his sleeve and hand; 'no Greg's face in frame'"},
           {"risk": "Paula reacts before the line", "prevented_by": "LISTENING clause, NEG_DRAMA"}]))

SHOTS.append(dict(beat="SC01-T4", kind="multi", covers=["SC01-SH08", "SC01-SH09"], duration=7, line="", subject_motion="in_place",
    files=["N", "C1", "C2", "L-YARD", "CAKE"], audios=[],
    title="Hook 1 · T4 — dead silence: he sits, thirty forks not moving; the untouched cake (SH08–SH09)", start_pos=R["SC01-SH08"]["start_pos"], end_pos=R["SC01-SH09"]["end_pos"],
    prompt=" ".join([
        manifest([("@image1", SHEET("Susan", SUSAN_D1)), ("@image2", SHEET("Greg", GREG_D1)), ("@image3", SHEET("Paula", PAULA_D1)), ("@image4", YARD), ("@image5", CAKE)]),
        SERIES, LOOK, INHERIT, GEO,
        "The clip carries no dialogue and no voice at all: nobody speaks; every mouth stays closed.",
        "One scene covered in 2 shots within a single take, with the same light, look and wardrobe throughout. Frame 1: " + R["SC01-SH08"]["start_pos"] + ". "
        "The second shot picks up the movement exactly where the last one left it: Greg's hand settling with his drink, and then nothing moving at all. "
        f"SHOT 1, [0s-4s]: WIDE from high behind Susan's right shoulder, looking down the length of the table: Greg, {GREG_ID}, drops back into his chair beside her and reaches past the cake for his drink; "
        "the whole table is frozen — forks held still above plates, glasses down, faces turned away or down, nobody moving. Susan's back and shoulder, still, in the near foreground. "
        "SHOT 2, [4s-7s]: CLOSE from a little above, the middle of the table exactly as the cake card shows it: the untouched white cake, a fork resting beside a plate, the candle flames barely moving; nothing else moves. "
        "Last frame: " + R["SC01-SH09"]["end_pos"] + ".",
        F2, PHYS,
        state("SUSAN", "seated in the dusty-blue blouse, still, her hand on the table edge", "nothing"),
        "FOCUS: SHOT 1 deep; SHOT 2 the cake sharp, the plates soft. The blur is optical: soft and round, never smeared.",
        negs(NEG_EQUIP, NEG_MORPH, NEG_CAKE, "no one speaking, no one laughing, no one eating", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "people move or talk in the frozen table", "prevented_by": "silent clip (generate_audio false), 'nobody moving', speaking negatives"},
           {"risk": "the cake changes (cut, writing)", "prevented_by": "the cake card, cake negatives"},
           {"risk": "Greg's face read as the focus", "prevented_by": "high behind Susan, Greg small in the wide"}]))

FILES = {"N": "cast/N-SUSAN_v1.png", "C1": "cast/C1-GREG_v1.png", "C2": "cast/C2-PAULA_v1.png", "C5": "cast/C5-FRIEND-A_v1.png", "C6": "cast/C6-FRIEND-B_v1.png",
         "L-YARD": "plates/L-YARD_v1.png", "CAKE": "body/SC01/ingredients/CAKE-CARD_v1.png"}
JOBS = {"N": "47cd159a-30fa-41d7-b1f5-68d4871c20b3", "C1": "5c5dd2ea-d555-4d43-ac32-6befddd3e2ce", "C2": "ca74192d-f209-4bab-97dd-7b7814c9e7ea",
        "C5": "9e17f3d8-44f6-4e9e-a9ca-914616a6feee", "C6": "36640bd2-6fc6-451a-a045-9e61290741ff", "L-YARD": "afd99bdc-94bc-40d9-982d-39327d629a5e", "CAKE": "cd9c042a-f261-4786-af27-1256d897461a"}
AUDIO = {"C1-L001": "voice/C1_ref_L001.mp3", "C1-L005": "voice/C1_ref_L005.mp3", "N-L004": "voice/N_ref_L004.mp3"}

if __name__ == "__main__":
    for s in SHOTS:
        call = {"beat": s["beat"], "build": "facelove-my-mother", "connector": "seedance", "model": "seedance_2_5", "mode": 4, "kind": s["kind"], "prompt": s["prompt"],
                "take": s["beat"], "covers": s["covers"], "start_pos": s["start_pos"], "end_pos": s["end_pos"], "duration": s["duration"], "resolution": "720p", "aspect_ratio": "9:16",
                "start_image": None, "ingredients_approved": True, "files": [FILES[f] for f in s["files"]], "audios": [AUDIO[a] for a in s["audios"]],
                "generate_audio": bool(s["line"]), "dialogue": s["line"] or None, "script_line": s["line"] or None, "pace": "unhurried", "subject_motion": s["subject_motion"],
                "prefer_multi_shots": "false", "generation": 1, "user_go": GO, "risks": s["risks"], "scene": 1, "title": s["title"],
                "taste": ["HT17", "HT18", "HT22", "HT23", "HT25"], "jobs": [JOBS[f] for f in s["files"]]}
        (H / f"{s['beat']}.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
        (H / f"{s['beat']}.prompt.txt").write_text(s["prompt"])
        print(s["beat"], s["duration"], "s", len(s["prompt"]), "chars")
