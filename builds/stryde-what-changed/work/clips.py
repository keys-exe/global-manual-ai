#!/usr/bin/env python3
"""stryde-what-changed — Kling clip calls (§35 minified JSON, §27G natural motion, §22X preflight) for confirmed start images.

Kling account short (3 credits) → Kie `kling-3.0/video` (pro 1080x1920, 9:16, single shot, sound off) per §5 / V7.65.0.
E6 lengths: screen time (cut to next cut, from the trimmed variant's word timestamps, cut 3 frames before the anchor word)
+ 0.4 s skip + 0.5 s, rounded up, 3–15 s; §27G human motion 3–6 s.
Usage: clips.py HK1-a HK1-b  → work/clips/<beat>.kling.json + <beat>.call.json
"""
import json, re, sys, pathlib, math

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
T = (ROOT / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
sys.path.insert(0, str(ROOT / "products/stryde"))
import stryde_product_sheet as P  # noqa: E402


def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S)
    if not m: raise KeyError(i)
    return m.group(1).strip()


ROWS = {r["beat"]: r for r in json.loads((HERE / "actmap_rows.json").read_text())}
ANAT_SLOTS = {"[REGION]": "knee", "[STACK]": "quadriceps, hamstrings and calf", "[BONES]": "femur, patella and tibia",
              "[TARGET]": "the patellar tendon", "[TARGET JOINT]": "the knee joint", "[SITE]": "the patellar tendon immediately below the kneecap"}
STILL_CAM = "Locked off on a small tripod: the camera does not move at all, no pan, no tilt, no push, no drift."
NEG_CAM = "no camera travelling with the subject, no camera movement, no zoom"


def length(screen_s, lo=3, hi=6):
    return max(lo, min(hi, math.ceil(screen_s + 0.9)))


def clip(beat, subject, motion, neg, screen_s, hi=6, anat=False, risks=()):
    r = ROWS[beat]
    mot = motion + " " + S("HOLD-C") + " " + (S("ANAT-LOAD") if anat else S("PHYS-MOTION-C"))
    for k, v in ANAT_SLOTS.items():
        mot = mot.replace(k, v)
    d = {"shot": beat.lower().replace("-", "_"), "subject": subject + " Exactly as in the start frame.",
         "camera": {"movement": STILL_CAM, "framing": "As in the start frame."},
         "motion": mot, "lighting": S("INHERIT-CAP"), "style": "As in the start frame.",
         "negatives": ", ".join([S("NEG-WARP-C"), NEG_CAM, neg, "no music, no speech, no slow motion"])}
    return d, length(screen_s, hi=hi), list(risks)


B = {}
B["HK1-a"] = clip("HK1-a",
    "A white British woman of sixty-nine, seen from the side waist-down through the white stair spindles, coming DOWN her stairs forwards: "
    "a navy A-line skirt ending just above the knee, bare knees and shins, white canvas plimsolls, her left hand on the honey oak handrail.",
    "Already mid-step on the first frame: her right foot is planted and taking her weight, the right knee bends a little further under the load "
    "as her left foot comes down onto the next stair below — one careful step in about a second and a half — then her weight settles onto it.",
    "no second person, no face in frame, no knee strap, no knee brace, no walking stick, no going up the stairs, no turning sideways, no extra legs",
    4.28, risks=[{"risk": "legs or feet warp on the stair", "prevented_by": "one step at a countable pace, start frame caught mid-step, HOLD-C + NEG-WARP-C"},
                 {"risk": "camera travels with the moving subject", "prevented_by": "locked-off tripod clause, 'no camera travelling with the subject'"},
                 {"risk": "a strap or brace appears on the bare knee (the before state)", "prevented_by": "'no knee strap, no knee brace' + bare knees in subject"}])
B["HK1-b"] = clip("HK1-b",
    "A premium 3D anatomical model of a single knee seen from the side, near-black field, the patellar tendon just below the kneecap glowing as one tight bright spot.",
    "Already under load on the first frame: one step lands — [STACK] shortens and the glow at [SITE] pulses once brighter and eases back, "
    "about one pulse a second, the glow staying one tight spot on the tendon.",
    "no arrows, no text, no labels, no numbers, no glow on the shin bone, no glow spreading down the leg, no second limb, no product, no camera orbit",
    3.36, hi=5, anat=True,
    risks=[{"risk": "the glow spreads down the shin or across the joint", "prevented_by": "'one tight spot' in subject + motion, negatives on shin and spread"},
           {"risk": "the model swims or melts", "prevented_by": "HOLD-C + NEG-WARP-C, one pulse only"},
           {"risk": "text or arrows appear", "prevented_by": "'no arrows, no text, no labels, no numbers'"}])

# Hook 2 — E6 from the trimmed HK2 variant: HK2-a 0–3.36 s ("and" at 3.36), HK2-b 3.36–6.80 s ("it" at 6.80)
B["HK2-a"] = clip("HK2-a",   # v3 image (user Fixes: different B-roll, then anatomy) — the tendon as a band, high three-quarter ECU
    "A premium 3D anatomical model of a knee seen close from a high three-quarter angle, near-black field: the lower edge of the kneecap at "
    "the top and the patellar tendon running down from it as one thick satin band to the top of the shin, a tight bright spot glowing at its top.",
    "Already under load on the first frame: the band draws taut once as [TARGET JOINT] takes a step's load — it straightens and firms "
    "along its length over about a second — and the spot at [SITE] brightens once and eases back as the load passes; the band stays in place.",
    "no arrows, no text, no labels, no numbers, no thumb, no hand, no ruler, no glow on the shin bone, no glow spreading down the band, "
    "no second limb, no product, no camera orbit, no zoom",
    3.36, hi=5, anat=True,
    risks=[{"risk": "the glow spreads down the band onto the shin", "prevented_by": "tight spot in subject + motion, negatives on spread and shin"},
           {"risk": "the model swims or the band warps", "prevented_by": "HOLD-C + NEG-WARP-C, one tightening only, 'the band stays in place'"},
           {"risk": "a thumb or scale object appears (F2)", "prevented_by": "'no thumb, no hand, no ruler'"}])
B["HK2-b"] = clip("HK2-b",   # v4 image (user Fixes) — side-on, cropped at the waist, lifting a box from a deep squat
    "A Black British man of sixty-six seen side-on from low, cropped at the waist: dark grey jogging shorts, a bare bent right knee in side "
    "profile nearest the lens, both hands under the bottom corners of a plain taped cardboard box just off the hall floor, plain white trainers.",
    "Already at the bottom of the squat on the first frame: his knees straighten and he rises steadily, lifting the box up in front of his "
    "shins to thigh height — one smooth lift in about two seconds, feet staying flat — then he holds, standing with the box.",
    "no face in frame, no head entering the frame, no second person, no knee strap, no knee brace, no writing on the box, no logos, "
    "no dropping the box, no box floating, no extra legs, no extra hands",
    3.44, risks=[{"risk": "hands or box warp during the lift", "prevented_by": "one lift at a countable pace, start frame caught mid-lift, HOLD-C + NEG-WARP-C"},
                 {"risk": "his head rises into the frame as he stands", "prevented_by": "rise only to thigh height with the box, 'no head entering the frame', locked-off tripod"},
                 {"risk": "camera travels with the moving subject", "prevented_by": "locked-off tripod clause, 'no camera travelling with the subject'"}])

# Hook 3 — E6 from the trimmed HK3 variant: HK3-a 0–4.14 s ("That" at 4.14), HK3-b 4.14–10.28 s (talking head from "Here")
B["HK3-a"] = clip("HK3-a",   # v3 — user Fixes: "FIX BROLL, WALKING/ STEPPING FAST" was a request FOR a fast walk (misread in v2);
    # v2 read as slow motion → "FASTER WALKING, NOT SLOW MO". Brisk real-time walk, more steps.
    "An older white woman's legs seen from a camera at ground level on a grey paving-slab pavement, cropped at the waist: a navy A-line skirt "
    "ending above the knee, bare knees and shins, plain white canvas plimsolls, walking briskly straight towards the lens along the pavement.",
    "Already mid-stride on the first frame: she walks briskly towards the lens in real time, a quick purposeful everyday walk — about two "
    "steps every second, five or six quick steps in the clip, her skirt hem swinging with each step, each foot landing and pushing off "
    "without pause — and she comes closer to the lens, still cropped at the waist, passing just to one side of it at the end.",
    "no slow motion, no slow walking, no careful steps, no pausing, no face in frame, no head entering the frame, no second person, no dog, "
    "no knee strap, no knee brace, no walking stick, no running, no jogging, no stepping on the camera, no logos, no readable signs, no extra legs",
    4.14, risks=[{"risk": "the walk reads as slow motion again", "prevented_by": "'in real time', about two steps a second named, 'no slow motion, no slow walking'"},
                 {"risk": "brisk walk tips into a jog", "prevented_by": "'a quick purposeful everyday walk', 'no running, no jogging'"},
                 {"risk": "legs warp at the faster pace", "prevented_by": "start frame caught mid-stride, HOLD-C + NEG-WARP-C, locked-off camera"}])
B["HK3-b"] = clip("HK3-b",   # v3 image (user Fixes → anatomy, low front three-quarter, knee bent under a landing)
    "A premium 3D anatomical model of a knee seen close from a low front three-quarter angle on a near-black field, the knee bent under a "
    "landing step, one tight spot glowing on the patellar tendon just below the kneecap.",
    "Already under load on the first frame: the leg takes a landing once a second — the knee bends a little deeper as each step's load "
    "arrives and eases back — and with each landing the spot at [SITE] flares a little brighter and warmer than the last, the landings "
    "stacking up, the glow staying one tight spot the whole time.",
    "no arrows, no text, no labels, no numbers, no counter, no glow on the shin bone, no glow spreading along the leg, no second limb, "
    "no product, no camera orbit, no zoom",
    6.14, hi=8, anat=True,
    risks=[{"risk": "the glow spreads across the joint as it builds", "prevented_by": "'one tight spot the whole time', negatives on spread and shin"},
           {"risk": "the model swims over 8 s", "prevented_by": "HOLD-C + NEG-WARP-C, locked-off, one small repeating bend"},
           {"risk": "numbers or a counter appear (the 70 million is a post overlay)", "prevented_by": "'no text, no numbers, no counter'"}])

# Body — one B-roll at a time (user). E6 from the trimmed variant's word timings (body words sit after the hook):
# B01b "It sits … of the joint," 3.78 s → 5 s; B01c "and every step you take lands on it." ≈ 2.4 s (est.) → 4 s (§30H hold ≥ 3 s).
B["B01b"] = clip("B01b",
    "A Black British man's bare right knee seen very close from the front in his hall: dark brown older skin, the kneecap in the upper "
    "part of the frame and the band of the tendon standing out as a firm ridge just below it, dark grey shorts hem at the top edge.",
    "Already standing on the first frame: he straightens the knee a touch as he settles his weight onto it, the ridge below the kneecap "
    "firming and catching the light, then holds still — one small movement in about a second.",
    "no face in frame, no hands, no knee strap, no knee brace, no marks on the skin, no ruler, no second person, no extra legs, no walking",
    3.78, hi=5,
    risks=[{"risk": "the knee warps or the skin swims", "prevented_by": "one small straighten, HOLD-C + NEG-WARP-C, locked-off camera"},
           {"risk": "a hand or a strap appears on the knee", "prevented_by": "'no hands, no knee strap, no knee brace'"},
           {"risk": "the camera drifts along the leg", "prevented_by": "locked-off tripod clause, 'no camera travelling with the subject'"}])
B["B01c"] = clip("B01c",   # v2 — user Fix "WALKING SINCE THE SCRIPT LINE IS 'EVERY STEP'" (v1 was one step down off the kerb)
    "An older white woman's feet and shins seen side-on from a camera at ground level at the kerb: plain white canvas plimsolls, bare "
    "pale shins, a navy skirt hem, the grey kerb stone and the road.",
    "Already at the landing on the first frame: her right plimsoll settles on the tarmac and she keeps walking straight on across the "
    "frame at an ordinary everyday pace in real time — three or four steps, about two a second, each foot landing flat and the knee "
    "bending a little as it takes her weight — and she walks on out of the side of the frame.",
    "no stopping, no standing still, no slow motion, no slow walking, no running, no face in frame, no torso, no second person, "
    "no cars moving, no knee strap, no walking stick, no logos, no number plates, no extra legs",
    2.4, hi=4,
    risks=[{"risk": "feet or shins warp mid-walk", "prevented_by": "an ordinary pace named, start frame caught at a landing, HOLD-C + NEG-WARP-C"},
           {"risk": "camera travels with her feet", "prevented_by": "locked-off tripod clause, she walks out of frame, 'no camera travelling with the subject'"},
           {"risk": "the walk reads as slow motion or stops", "prevented_by": "'in real time', about two steps a second, 'no stopping, no slow motion'"}])

# B02 "That is the one." ≈ 1 s on screen → 3 s floor (§30H hold ≥ 3 s).
B["B02"] = clip("B02",
    "The front of an older white woman's bare bent knee seen straight on as she sits on her bottom stair: the kneecap centred, her index "
    "fingertip resting on the tendon just below it, a plain gold ring on her hand, a navy skirt hem at the top edge.",
    "Already touching on the first frame: her fingertip presses gently into the tendon just below the kneecap once, the skin dimpling "
    "slightly under it, and holds there — one small press in about a second.",
    "no face in frame, no finger moving onto the kneecap, no finger sliding to the side of the knee, no second hand, no knee strap, "
    "no extra fingers, no walking, no standing up",
    1.0, hi=4,
    risks=[{"risk": "the finger drifts onto the kneecap or to the side", "prevented_by": "one press that holds, negatives on the finger moving"},
           {"risk": "fingers warp or multiply", "prevented_by": "HOLD-C + NEG-WARP-C, one small movement, 'no extra fingers'"},
           {"risk": "camera drifts", "prevented_by": "locked-off tripod clause"}])

# B03 line, split in three (user). Screen times estimated from the line lengths at the locked VO pace (~2.8 words/s):
# B03a ≈ 3.5 s → 5 s; B03b ≈ 3.2 s → 5 s; B03c ≈ 1.5 s → 3 s floor.
B["B03a"] = clip("B03a",
    "A premium 3D anatomical model of a standing leg seen from a low front angle on a near-black field: the big quadriceps muscle filling "
    "the upper frame and narrowing down over the kneecap into one small band below it, a tight spot glowing on that band.",
    "Already under load on the first frame: the thigh muscle tightens once as the leg takes a step's weight, and the load runs down into "
    "the small band — the spot at [SITE] brightens once and eases back, staying one tight spot; the big muscle stays calm after.",
    "no arrows, no text, no labels, no numbers, no thumb, no hand, no ruler, no glow on the thigh, no glow spreading down the shin, "
    "no second limb, no product, no camera orbit, no zoom",
    3.5, hi=5, anat=True,
    risks=[{"risk": "the glow spreads onto the thigh or shin", "prevented_by": "'staying one tight spot', negatives on thigh and shin glow"},
           {"risk": "the model swims", "prevented_by": "HOLD-C + NEG-WARP-C, one tightening only"},
           {"risk": "a thumb or scale object appears (F2)", "prevented_by": "'no thumb, no hand, no ruler'"}])
B["B03b"] = clip("B03b",
    "A white British woman of sixty-nine in a kitchen, three-quarter on, in a dusty-pink cardigan and navy skirt, bending at the knees in "
    "front of a low sage-green cupboard with a heavy orange cast-iron pot in both hands.",
    "Already at the bottom of the bend on the first frame: she rises steadily with the heavy pot, her knees straightening under the "
    "weight, and stands upright holding it at her waist — one careful lift in about two seconds, real time.",
    "no dropping the pot, no looking at the camera, no wincing, no second person, no knee strap, no extra hands, no slow motion, "
    "no walking out of frame",
    3.2, hi=5,
    risks=[{"risk": "hands or pot warp during the lift", "prevented_by": "one lift at a countable pace, start frame caught mid-bend, HOLD-C + NEG-WARP-C"},
           {"risk": "her face drifts off the sheet", "prevented_by": "three-quarter, face turned to the pot, short 5 s clip"},
           {"risk": "camera travels with her", "prevented_by": "locked-off tripod clause"}])
B["B03c"] = clip("B03c",
    "Seen from straight above: an old family photo album open on a pale-oak kitchen table, a faded 1970s snapshot of a teenage girl on a "
    "seaside promenade, an older woman's hand resting at the edge of the page.",
    "Already touching the page on the first frame: her hand lifts the edge of the page slightly and holds it, about to turn it — one small "
    "movement in about a second; the photograph stays still and flat.",
    "no page turning fully, no text appearing, no second hand, no extra fingers, no photograph moving, no camera movement",
    1.5, hi=3,
    risks=[{"risk": "the photograph warps or animates", "prevented_by": "'the photograph stays still and flat', HOLD-C + NEG-WARP-C"},
           {"risk": "the hand multiplies or warps", "prevented_by": "one small lift, 'no second hand, no extra fingers'"},
           {"risk": "text appears on the page", "prevented_by": "'no text appearing'"}])

# B04c "so coming down puts more through that band than going up does." ≈ 3.5 s (est.) → 5 s.
B["B04c"] = clip("B04c",   # image v2 (user Fix "WALKING DOWN THE STAIR"): the silhouette figure walking down visible steps — a new shot, gen 1
    "A premium 3D anatomical figure from the waist down as dark translucent silhouettes on a near-black field, seen from a high "
    "three-quarter angle, walking down a short flight of faintly edge-lit steps, the leading foot landing on the step below, a tight "
    "spot glowing on the patellar tendon below the leading knee.",
    "Already mid-stride on the first frame: the figure walks DOWN the stairs at an ordinary pace, in real time — the leading foot lands on "
    "the step below and that knee bends to catch the body's weight, the one spot on its patellar tendon flaring brighter as it lands and "
    "easing back, the figure travelling down within the frame. ONLY THE LEADING KNEE GLOWS: the other leg and its knee stay dark "
    "silhouette the whole time, never lit.",
    "no glow on the other knee, no second glowing spot, no both knees lit, no stepping up, no standing still, no arrows, no text, "
    "no labels, no numbers, no glow spreading down the shin, no extra legs, no product, no camera orbit, no camera following the figure, "
    "no zoom, no slow motion",
    3.5, hi=5, anat=True,
    risks=[{"risk": "both knees light up again", "prevented_by": "'ONLY THE LEADING KNEE GLOWS', the other knee named dark, 'no glow on the other knee, no both knees lit'"},
           {"risk": "legs warp or multiply mid-stride", "prevented_by": "start frame caught mid-stride, HOLD-C + NEG-WARP-C, 'no extra legs'"},
           {"risk": "the camera follows the figure down", "prevented_by": "locked-off tripod clause, 'no camera following the figure'"}])
# B04a v2 image (user confirmed): Desmond struggling up. "Going up the stairs, your muscles lift you." ≈ 2.2 s → 4 s.
B["B04a"] = clip("B04a",
    "A Black British man of sixty-six part-way up his stairs, three-quarter on, one hand gripping the dark handrail, the other pressed on "
    "his thigh, leaning forward over his bent knee, face set with effort.",
    "Already mid-effort on the first frame: he pushes down on his thigh and pulls on the rail and levers himself up onto the next tread, "
    "slowly and with effort, then pauses there to breathe — one heavy step up in about two seconds, real time.",
    "no falling, no crying, no looking at the camera, no second person, no knee strap, no walking stick, no going down, no slow motion, "
    "no extra hands",
    2.2, hi=4,
    risks=[{"risk": "hands or legs warp on the step", "prevented_by": "one step at a countable pace, start frame caught mid-effort, HOLD-C + NEG-WARP-C"},
           {"risk": "his face drifts off the sheet", "prevented_by": "short 4 s clip, three-quarter, face stays set"},
           {"risk": "camera travels with him up the stairs", "prevented_by": "locked-off tripod clause"}])

# B04b v4 image (user confirmed). "Going down, nothing lifts you. You are catching yourself on every step," ≈ 4.6 s → 6 s (human cap).
B["B04b"] = clip("B04b",
    "A white British woman of sixty-nine near the top of her stairs coming down towards a low lens, one hand gripping the honey oak "
    "handrail, the other braced on the wall, dusty-pink cardigan and navy skirt, a small tired wince.",
    "Already mid-step on the first frame: she lowers her foot carefully onto the next tread and her knee bends to catch her weight, she "
    "steadies herself on the rail and the wall, then takes one more careful step down the same way — two slow, careful steps in about "
    "five seconds, real time, coming a little closer to the lens.",
    "no falling, no stumbling, no looking at the camera, no second person, no knee strap, no walking stick, no stairlift, no going up, "
    "no slow motion, no extra hands",
    4.6, hi=6,
    risks=[{"risk": "legs or hands warp on the steps", "prevented_by": "two careful steps at a countable pace, start frame mid-step, HOLD-C + NEG-WARP-C"},
           {"risk": "her face drifts off the sheet", "prevented_by": "face small in a full-figure shot, the wince held, 6 s cap"},
           {"risk": "camera travels with her", "prevented_by": "locked-off tripod clause"}])

# B06-BR image v1 (user "GO CONFIRM"): bus stop, three people of different ages with knee trouble. "It happens to everybody." ≈ 1.4 s → 3 s.
B["B06-BR"] = clip("B06-BR",
    "A bus stop on a grey British residential street: a white-haired man in his seventies in a grey anorak sits on the shelter bench with "
    "his hand on his knee; a Black British woman in her forties in a camel coat with a work bag leans one hand on the shelter post; a young "
    "South Asian British man in a pale running jacket, black tights and shorts walks along the pavement in the foreground, a hand on his thigh.",
    "Already moving on the first frame, all three at once and small: the young runner takes two short, uneven steps forward along the "
    "pavement, favouring his right knee with a slight limp, his hand pressing his thigh; the older man rubs his knee slowly with his hand, "
    "once; the woman shifts her weight off her left knee onto the post and lets that foot rest. Real time, about three seconds.",
    "no fourth person, no bus arriving, no one looking at the camera, no falling, no crying, no walking stick, no knee strap, no knee brace, "
    "no readable signs, no extra legs, no extra hands, no one walking out of frame",
    1.4, hi=6,
    risks=[{"risk": "three people moving at once warp or merge", "prevented_by": "one small action each at a countable pace, 3 s, HOLD-C + NEG-WARP-C"},
           {"risk": "the runner's legs warp mid-limp", "prevented_by": "two short steps only, start frame mid-stride"},
           {"risk": "camera travels with the runner", "prevented_by": "locked-off tripod clause"}])

# B06 image v4 (user CONFIRM): force arrows down the thigh onto the one tendon spot + pointer arrow; pip (host bottom-left).
# "Seventeen times your bodyweight is still arriving, every step, in exactly the same place." ≈ 4.6 s → 6 s.
# Video v2 — user Fix 'MOVING ALL ARROW, DETAILED FOCUS ON THE TENDON' (v1: arrows held still, locked camera, only light ran along
# them; the pointer drifted). Now every arrow travels in onto the spot, and the camera pushes in slowly onto the tendon (the model
# stays in place, so the camera never travels with a moving subject, §27G).
B["B06"] = clip("B06",
    "A premium 3D anatomical model of a single knee on a near-black field, low three-quarter, under load: "
    "four glowing force arrows on the thigh and one white pointer arrow, all aimed at one glowing spot on the patellar tendon below the kneecap.",
    "Already under load on the first frame, the leg itself stays where it is. ALL FIVE ARROWS MOVE: the four force arrows slide DOWN "
    "along the thigh and the pointer arrow slides IN from the dark field, all five travelling onto the one spot below the kneecap and "
    "arriving together; as they arrive the spot flares brighter and the thigh tenses slightly, then the arrows ease back a little and "
    "travel in again — about once a second, same spot. The arrows keep their shape and count. As "
    "they arrive, the view closes in slowly on the patellar tendon until it fills much of the frame: its long fibres, its banded grain "
    "and the glowing spot on it in crisp detail.",
    "no arrows changing shape, no new arrows, no arrows disappearing, no glow down the shin, no second spot, no leg moving, "
    "no second limb, no text, no camera orbit, no rotation, no slow motion",
    4.6, hi=8, anat=True,
    risks=[{"risk": "the arrows morph, multiply or vanish as they move", "prevented_by": "count and shape named fixed ('ALL FIVE', 'keep their shape and count'), one simple slide in, 'no new arrows, no arrows disappearing'"},
           {"risk": "the push-in turns into an orbit or the leg moves", "prevented_by": "slow push-in only, 'no camera orbit, no rotation', 'the leg itself stays where it is', 'no leg moving'"},
           {"risk": "a second limb edge appears (seen in v1)", "prevented_by": "'no second limb' + the push-in crops the frame edges away"}])
B["B06"][0]["camera"] = {"movement": "A slow, steady push-in straight towards the patellar tendon over the whole clip, no pan, no tilt, no orbit.",
                         "framing": "Starts as in the start frame, ends close on the patellar tendon and the glowing spot."}
B["B06"][0]["negatives"] = B["B06"][0]["negatives"].replace(", no camera movement, no zoom", "")

# B01a image v1 (user Confirm on the board): ANAT-B, the tendon band front-on, the spot glowing. "That band is the patellar tendon." ≈ 1.8 s → 3 s.
B["B01a"] = clip("B01a",
    "A premium 3D anatomical model of a single knee seen straight from the front on a near-black field, a faint glass-like body shell, "
    "ivory bones, the kneecap at the centre and the patellar tendon running down from it to the shin as one pale band, a soft spot "
    "glowing on the tendon just below the kneecap.",
    "Already glowing on the first frame: a soft light traces slowly DOWN the patellar tendon band from the kneecap to the top of the shin, "
    "once, and the spot below the kneecap swells a little brighter and settles — the model itself does not move.",
    "no model moving, no bones moving, no glow spreading onto the shin bone, no second glowing spot, no arrows, no text, no labels, "
    "no numbers, no product, no camera orbit, no zoom, no slow motion",
    1.8, hi=5, anat=True,
    risks=[{"risk": "the glow spreads down the shin", "prevented_by": "the light traces the band only, 'no glow spreading onto the shin bone'"},
           {"risk": "the model rotates or warps", "prevented_by": "'the model itself does not move', locked-off camera, HOLD-C + NEG-WARP-C"},
           {"risk": "a second spot appears", "prevented_by": "'no second glowing spot'"}])

# B07-BRa image v1 (user CONFIRM GO): ANAT-B front-on, the cartilage cushion worn thin. "The cushion gets thinner." ≈ 1.4 s → 3 s.
# Video v2 — user Fix 'THINNER' (v1: the cushion flattened only a little, a red dot appeared): the cushion now wears to a sliver,
# bones almost touching; 4 s so the change reads.
B["B07-BRa"] = clip("B07-BRa",
    "A premium 3D anatomical model of a single knee seen straight from the front on a near-black field, a faint glass-like body shell, "
    "ivory bones: the end of the thigh bone above, the top of the shin bone below, the kneecap in front, and between the bones a thin, "
    "pearly, worn cartilage cushion.",
    "The model stays still. Over the clip the pale cushion between the bones wears away CLEARLY and steadily: it shrinks to less than "
    "half its height, its edges fray and flake away, until only a thin, patchy sliver is left and the two bone ends sit almost touching "
    "— an obvious, unmistakable thinning from the first frame to the last. One steady change, no glow.",
    "no bones moving apart, no cushion growing back, no model rotating, no glow, no emission, no red spot, no blood, no cracking, "
    "no breaking, no second limb, no arrows, no text, no labels, no product, no camera orbit, no zoom, no slow motion",
    2.2, hi=5, anat=True,
    risks=[{"risk": "the model rotates or the bones warp", "prevented_by": "'the model stays still', locked-off camera, HOLD-C + NEG-WARP-C, 'no model rotating'"},
           {"risk": "a glow appears on a condition beat", "prevented_by": "'no glow, no emission' in motion and negatives"},
           {"risk": "the cushion shatters instead of thinning", "prevented_by": "one slow steady change, 'no cracking, no breaking'"}])
_load = S("ANAT-LOAD")
for _k, _v in ANAT_SLOTS.items():
    _load = _load.replace(_k, _v)
B["B07-BRa"][0]["motion"] = B["B07-BRa"][0]["motion"].replace(" " + _load, "")  # a condition beat: no muscle layer, no load pulse

# B07-BRb image v1 (user CONFIRM GO): Maureen, waist-down from the front, low at the foot of her stairs, laundry basket on her hip.
# "The weight stays exactly the same." ≈ 1.8 s → 3 s.
B["B07-BRb"] = clip("B07-BRb",
    "A white British woman of sixty-nine seen from the front, low, cropped below her chin, coming DOWN her carpeted stairs towards the "
    "lens: a dusty-pink cardigan over a navy-and-white striped top, a navy skirt ending above the knee, bare pale legs, white canvas "
    "plimsolls; a full white laundry basket of towels on her hip at the left of the frame, her other hand on the oak handrail at the right.",
    "Already mid-step on the first frame: her front foot comes down and lands flat on the tread nearest the lens, her knee bends under "
    "her whole weight and the basket as it lands, and she settles onto it — one careful step down in about a second and a half, real time.",
    "no face in frame, no falling, no stumbling, no dropping the basket, no towels falling, no second person, no knee strap, no walking "
    "stick, no going up, no extra legs, no extra hands",
    1.8, hi=6,
    risks=[{"risk": "legs or feet warp on the tread", "prevented_by": "one step at a countable pace, start frame mid-step, HOLD-C + NEG-WARP-C"},
           {"risk": "her face comes into frame", "prevented_by": "cropped below the chin, 'no face in frame', locked-off camera"},
           {"risk": "the basket or towels fall", "prevented_by": "'no dropping the basket, no towels falling'"}])

# B07 image v2 (user CONFIRM): kitchen, morning, Maureen stopped at the table, hand on her knee, puzzled. "That is why it feels like it
# arrived overnight." ≈ 2.2 s → 4 s.
B["B07"] = clip("B07",
    "A white British woman of sixty-nine with short white hair in her kitchen in the morning, a dusty-pink cardigan over a navy-and-white "
    "striped top, standing at the pale-oak table with tea and toast, one hand on the table edge, the other on her right knee, looking down "
    "at it with a small puzzled frown.",
    "Already still on the first frame: she rubs her right knee slowly once with her hand and presses it, looking down at it, then lifts "
    "her eyes a little, puzzled, as if it was fine yesterday — small and quiet, about three seconds, real time.",
    "no wincing, no crying, no grimace, no sitting down, no walking away, no looking at the camera, no second person, no knee strap, "
    "no extra hands, no extra fingers",
    2.2, hi=6,
    risks=[{"risk": "her face drifts off the sheet as she moves", "prevented_by": "small movement only, eyes lift a little, 4 s cap, HOLD-C"},
           {"risk": "hands warp on the knee", "prevented_by": "one slow rub and press, 'no extra hands, no extra fingers', NEG-WARP-C"},
           {"risk": "the frown becomes pain", "prevented_by": "'puzzled… as if it was fine yesterday', 'no wincing, no grimace'"}])

# B08-BR image v1 (user Confirm on the board): Maureen from behind, walking down her hall to the front door.
# "Nothing about the way you walk changed, so you assume nothing changed." ≈ 3.6 s → 5 s.
B["B08-BR"] = clip("B08-BR",
    "A white British woman of sixty-nine with short white hair, seen from behind, walking away down her pale duck-egg blue hall towards "
    "the white front door: a dusty-pink cardigan, a navy skirt ending above the knee, bare legs, white canvas plimsolls; the half-moon "
    "hall table with a vase of dried lavender on the left, the white spindles and oak handrail of the stairs on the right.",
    "Already mid-stride on the first frame: she walks on down the hall away from the lens at an ordinary, unhurried pace — about four "
    "easy, even steps, one step a second, real time — getting a little smaller in the frame, arms swinging naturally. She does not turn "
    "round.",
    "no turning round, no looking back, no face, no limp, no stopping, no reaching the door, no opening the door, no second person, "
    "no walking stick, no knee strap, no extra legs",
    3.6, hi=6,
    risks=[{"risk": "legs warp or swap mid-stride", "prevented_by": "even steps at one a second, start frame mid-stride, HOLD-C + NEG-WARP-C"},
           {"risk": "she turns and her face appears", "prevented_by": "'She does not turn round', 'no turning round, no looking back, no face'"},
           {"risk": "camera follows her down the hall", "prevented_by": "locked-off tripod clause, 'no camera travelling with the subject'"}])

# B06-BR2 image v2 (user confirm): close-up of Desmond's right knee, side-on at knee height on the pavement.
# "The load does not thin with it." ≈ 1.8 s → 3 s.
B["B06-BR2"] = clip("B06-BR2",
    "A close-up, side-on at knee height on a grey pavement: a Black British man's bare right knee filling the frame, dark brown older "
    "skin, the kneecap and the band of tendon below it under the skin, dark grey jogging shorts above, the other leg a soft shape "
    "behind, a soft blurred street of hedges and houses beyond.",
    "Already mid-step on the first frame: his right foot lands out of frame below and the knee takes his whole weight — it bends a "
    "little under the load, the tendon below the kneecap tightens and the thigh firms — then straightens as he moves over it, the knee "
    "drifting only a little to the right. One heavy step, about a second and a half, real time.",
    "no knee leaving the frame, no second knee coming into focus, no feet in frame, no face, no limp, no stumbling, no knee strap, "
    "no extra legs, no skin warping",
    1.8, hi=6,
    risks=[{"risk": "the knee walks out of the close frame", "prevented_by": "one step only, 'drifting only a little', 'no knee leaving the frame'"},
           {"risk": "skin or knee shape warps under the bend", "prevented_by": "one small bend and straighten, HOLD-C + NEG-WARP-C, 'no skin warping'"},
           {"risk": "camera follows the leg", "prevented_by": "locked-off tripod clause, 'no camera travelling with the subject'"}])

# B08-BRb image v1 (user CONFIRM): Desmond on his stairs, hand gripping his knee, caught out; seen from the landing above.
# "And here is the part that catches people out." ≈ 2.0 s → 3 s.
B["B08-BRb"] = clip("B08-BRb",
    "A Black British man of sixty-six with close-cropped grey-white hair and a short grey-white beard, seen from above on his carpeted "
    "stairs, a navy zip-neck top, dark grey shorts, bare knees, one hand on the dark handrail, the other gripping the front of his knee, "
    "black-framed football team photos on the grey wall beside him.",
    "Already stopped on the first frame: his hand squeezes the front of his knee once and holds it, his head dips a little as he looks "
    "down at it, and his brow draws into a surprised, caught-out frown — he stays where he is on the stair. Small and quiet, real time.",
    "no stepping, no falling, no wincing in agony, no looking at the camera, no second person, no knee strap, no extra hands, "
    "no extra fingers, no photos changing",
    2.0, hi=6,
    risks=[{"risk": "his face drifts off the sheet", "prevented_by": "small movement only, head dips a little, 3 s, HOLD-C"},
           {"risk": "hand warps on the knee", "prevented_by": "one squeeze and hold, 'no extra hands, no extra fingers', NEG-WARP-C"},
           {"risk": "he climbs or steps and the legs warp", "prevented_by": "'he stays where he is on the stair', 'no stepping'"}])

# B08-BRc image v1 (user CONFIRM): Maureen at her kitchen worktop with the kettle, side-on, an ordinary morning.
# "You do not have to have done anything to your knees for this to happen." ≈ 3.4 s → 5 s.
B["B08-BRc"] = clip("B08-BRc",
    "A white British woman of sixty-nine with short white hair, side-on at her kitchen worktop by the sink and the window, a dusty-pink "
    "cardigan over a navy-and-white striped top, a navy skirt, holding a cream kettle on its base, shelves of mugs and jars behind.",
    "Already moving on the first frame: she closes the kettle lid with a small press, settles it on its base and flicks the switch on, then "
    "rests her hand on the worktop and waits, looking out of the window — calm, unhurried, an ordinary morning, real time.",
    "no pouring, no steam burst, no looking at the camera, no pain, no hand on her knee, no second person, no extra hands, no extra "
    "fingers, no readable text on the kettle",
    3.4, hi=6,
    risks=[{"risk": "hands warp on the kettle", "prevented_by": "two small actions at an easy pace, NEG-WARP-C, 'no extra hands'"},
           {"risk": "her face drifts off the sheet", "prevented_by": "side-on, calm, small head turn only, HOLD-C"},
           {"risk": "text appears on the kettle", "prevented_by": "'no readable text on the kettle'"}])

# B08a image v4 (user CONFIRM): Maureen seated at the bus stop on her street, handbag on her lap.
# "Some of the people it happens to have never run a mile in their life." ≈ 3.2 s → 5 s.
B["B08a"] = clip("B08a",
    "A white British woman of sixty-nine with short white hair, seated side-on on the wooden bench of a glass bus shelter on a grey British "
    "residential street, a dusty-pink cardigan over a navy-and-white striped top, a navy skirt, white plimsolls, a brown handbag on her lap "
    "under both hands, parked cars and 1930s semis beyond.",
    "Already still on the first frame: she settles the handbag a little on her lap, smooths it with one hand, then turns her head slowly "
    "to glance up the road for the bus and back — calm and unhurried, an ordinary wait, real time.",
    "no standing up, no bus arriving, no second person, no looking at the camera, no cars moving, no walking stick, no knee strap, "
    "no extra hands, no extra fingers, no readable text",
    3.2, hi=6,
    risks=[{"risk": "her face drifts off the sheet as she turns", "prevented_by": "one slow head turn and back, 5 s cap, HOLD-C"},
           {"risk": "hands warp on the handbag", "prevented_by": "one small settle and smooth, NEG-WARP-C, 'no extra hands'"},
           {"risk": "a bus or people wander in", "prevented_by": "'no bus arriving, no second person, no cars moving'"}])

START = {"B08a": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_111706_9b645285-1aef-43ba-99f4-f95ac2ed5c6b.png",
         "B08-BRb": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_103917_57a208e9-a3f0-44c8-9602-b7a6f6ee6d42.png",
         "B08-BRc": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_103918_c1db651c-8d38-40ec-8f3b-0468a2ed021b.png",
         "B06-BR2": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_230724_8d894c4c-441e-428d-aeed-497f8383a717.png",
         "B08-BR": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_225901_8a563cef-0c03-48f0-94fa-92dd33e9b572.png",
         "B07": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_225901_b28d6f1c-bceb-447c-9792-c9ed9f38a4a6.png",
         "B07-BRa": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_220935_8b097287-2a0e-4aa7-8dde-2b2d9ea7f463.png",
         "B07-BRb": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_220935_39e2cddd-d187-4527-85ab-16bd1b581a42.png",
         "B01a": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_185450_3c452d7b-23e8-414a-bcad-4435a876272c.png",
         "HK1-a": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_140551_661eba13-ffd8-4a6f-8b1c-2bfca7beddcc.png",
         "HK1-b": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_140550_bca03c1b-07b2-4580-8709-6f3a74007ee7.png",
         "HK2-a": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_173257_512cb5a0-c05b-4ab8-af5f-723322275d70.png",
         "HK2-b": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_174627_a9e02dbb-2d91-4a3d-a960-2a053cdfef10.png",
         "HK3-a": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_175116_4eefcbcd-8107-4478-bc49-7de4c9de2bb4.png",
         "HK3-b": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_183345_15bd1d26-4f28-4cc9-9e05-a4a65495715d.png",
         "B01b": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_194456_c2453c7e-9832-4f3f-9b00-9c7dbad21a16.png",
         "B01c": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_194456_656ef52d-b5ca-473e-a831-c1dbaed4c5b6.png",
         "B02": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_200235_5d3a123f-a2c4-4faa-8af7-b1513056106b.png",
         "B03a": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_202127_fabbd7d4-506d-47ae-ac06-d559f3c40e63.png",
         "B03b": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_202128_46596a96-c9cc-487c-a63d-ba91a8d96c67.png",
         "B03c": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_200831_62aeddb0-e97c-4589-9d43-6d675499545c.png",
         "B04c": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_211843_6ae8e4ac-2507-4735-9b38-7f1edc3a2b07.png",
         "B04b": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_211843_dc076019-ac3b-475f-a315-f311f4d298f0.png",
         "B04a": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_205729_cf751279-1d57-43d5-9b56-f8b0adbb16f5.png",
         "B06": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_215836_f898adbd-fc7c-47b3-9528-088a1df6aa36.png",
         "B06-BR": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_215145_b3e86d93-f337-4226-9feb-1ae2a35a886e.png"}

if __name__ == "__main__":
    out = HERE / "clips"; out.mkdir(exist_ok=True)
    for b in sys.argv[1:] or B:
        d, dur, risks = B[b]
        s = json.dumps(d, ensure_ascii=False, separators=(",", ":"))
        (out / f"{b}.kling.json").write_text(s)
        call = {"beat": b, "connector": "kling", "mode": 1, "kind": "broll", "prompt": s, "duration": dur, "resolution": "1080p", "aspect_ratio": "9:16",
                "start_image": START[b], "start_approved": True, "pinned": False, "end_image": None, "end_approved": False,
                "subject_motion": "in_place" if "ANAT" in d["subject"] or "anatomical" in d["subject"] else "travels",
                "prefer_multi_shots": "false", "generation": 1, "risks": risks, "approved_by": "user: board Confirm + 'confirm' / 'CONFIRM' (2026-09-29)"}
        (out / f"{b}.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
        print(b, dur, "s", len(s), "chars")
