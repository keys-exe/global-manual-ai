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

# B08b image v7 (user CONFIRM): POV on his stairs, his hands holding the old 1980s team photo, his knees below.
# "Others played sport for thirty years." ≈ 2.0 s → 3 s.
B["B08b"] = clip("B08b",
    "A point-of-view shot looking down from a man seated on his carpeted stairs: his two dark-skinned hands hold an old faded colour "
    "photograph of a 1980s amateur football team in navy-and-white kit, his bare knees, grey shorts and white trainers below, the stairs "
    "falling away beneath.",
    "Already holding it on the first frame: his hands tilt the photo very slightly towards him and his right thumb moves slowly across "
    "its edge, as if touching the memory — small, calm, real time. The knees stay still.",
    "no photo changing, no faces in the photo changing, no hands moving out of frame, no extra hands, no extra fingers, no readable text, "
    "no camera shake beyond a slight natural hold",
    2.0, hi=6,
    risks=[{"risk": "the faces or kit in the photo morph", "prevented_by": "only the thumb and a slight tilt move, 'no faces in the photo changing', HOLD-C + NEG-WARP-C"},
           {"risk": "fingers multiply on the print", "prevented_by": "one slow thumb movement, 'no extra fingers, no extra hands'"},
           {"risk": "camera drifts", "prevented_by": "locked-off tripod clause"}])

# B08c image v3 (user CONFIRM): Desmond getting up off a low front-garden wall on his street.
# "It is coming from standing up and walking." ≈ 2.4 s → 4 s.
B["B08c"] = clip("B08c",
    "A Black British man of sixty-six with close-cropped grey-white hair and a short grey-white beard on a grey British residential "
    "pavement, a navy zip-neck top, dark grey shorts, bare knees, white trainers, rising from a low brick front-garden wall with a hedge "
    "behind, parked cars along the kerb.",
    "Already rising on the first frame: he pushes off the wall with one hand, his knees straighten as he comes up to standing, and he "
    "takes two ordinary steps away along the pavement to the right — an everyday, unhurried movement, real time.",
    "no wincing, no stumbling, no looking at the camera, no second person, no cars moving, no knee strap, no walking stick, no extra legs, "
    "no extra hands, no walking out of frame",
    2.4, hi=4,
    risks=[{"risk": "legs warp as he rises and steps", "prevented_by": "one rise then two steps at an easy pace, start frame mid-rise, HOLD-C + NEG-WARP-C"},
           {"risk": "his face drifts off the sheet", "prevented_by": "three-quarter, short clip, calm expression, HOLD-C"},
           {"risk": "camera follows him", "prevented_by": "locked-off tripod clause, 'no walking out of frame'"}])

# B06b image v2 (user CONFIRM 2026-09-30): ANAT ECU front-on on the patellar tendon, blazing target core, five rings, fibre
# streaks, heat halo, particle swirl — all inside the tendon. "in exactly the same place." ≈ 1.7 s → 3 s.
B["B06b"] = clip("B06b",
    "A premium 3D anatomical model seen very close and straight on: the lower edge of the kneecap at the top and the patellar tendon as a "
    "broad satin-white band of fibres filling the frame, one blazing near-white core dead centre on it with concentric rings of light, "
    "a red-orange heat halo and a swirl of glowing particles around it, all inside the tissue.",
    "Already under load on the first frame, the tendon stays where it is. Impacts land on the one core, about once a second: at each one "
    "the tendon draws taut, the core flares brighter, a new ring of light ripples outward through the fibres from exactly the same point "
    "while the older rings keep spreading and fade at the edges, bright streaks race along the fibres into the core, and the particle swirl "
    "turns slowly around it. The core never moves off its spot.",
    "no second spot, no core moving, no rings leaving the tendon, no light outside the body, no energy flying in from outside, "
    "no glow down the shin, no text, no numbers, no second limb, no camera orbit, no explosion of the tendon",
    1.7, hi=4, anat=True,
    risks=[{"risk": "the core wanders or a second spot appears", "prevented_by": "'exactly the same point', 'the core never moves off its spot', 'no second spot, no core moving'"},
           {"risk": "the rings or light spill outside the tendon", "prevented_by": "'all inside the tissue', 'no rings leaving the tendon, no light outside the body'"},
           {"risk": "the tendon swims or tears", "prevented_by": "HOLD-C + NEG-WARP-C, one taut draw per impact, 'the tendon stays where it is'"}])
B["B06b"][0]["motion"] = B["B06b"][0]["motion"].replace(
    "quadriceps, hamstrings and calf shortens and thickens as the load arrives, the patellar tendon visibly tightens",
    "The patellar tendon visibly tightens").replace(", and the whole structure compresses a few degrees", "")

# B08-BR2 image v1 (user CONFIRM 2026-09-30): Desmond's hand holding his old muddy football boots by the laces/heel in his hall by the
# front door, the oak console and shoe space at left. "It makes almost no difference," ≈ 1.5 s → 3 s.
B["B08-BR2"] = clip("B08-BR2",
    "A Black man's hand in a navy sweatshirt cuff holding a pair of old black leather football boots by the heels, dried mud on the "
    "studs and uppers, in a British hall by the white front door, the stairs behind, a wood floor and a doormat below.",
    "Already moving on the first frame: his hand lowers the boots slowly and sets them down on the wood floor below, the studs touch "
    "the floor, and his fingers let go of them — one unhurried set-down, about a second and a half. The boots stay a pair, side by side.",
    "no dropping the boots, no boots falling over, no second hand, no face, no person entering the frame, no walking, no door moving, "
    "no logos on the boots, no stripes, no swoosh, no extra fingers",
    1.5, hi=4,
    risks=[{"risk": "fingers or boots warp as he lets go", "prevented_by": "one slow set-down, HOLD-C + NEG-WARP-C, 'no extra fingers'"},
           {"risk": "a logo or stripes appear on the boots", "prevented_by": "'no logos on the boots, no stripes, no swoosh'"},
           {"risk": "a face or body enters the frame", "prevented_by": "'no face, no person entering the frame', hand and boots only"}])

# B06 video gen 3 (user CONFIRM on B06 after the §22X ask, 2026-09-30) from image v6: whole leg mid-step, white-gold wave-fronts
# inside the thigh, impact flare with rings and a particle swirl at the knee; pip (host bottom-left). First half of the line,
# "Seventeen times your bodyweight is still arriving, every step," ≈ 2.9 s → 4 s. v2's arrows are gone with the new image.
B["B06"] = clip("B06",
    "A premium 3D anatomical model of a whole leg mid-step on a near-black field, low three-quarter, the knee upper right: curved "
    "white-gold wave-fronts of light inside the thigh, a hot glow in the knee joint and an impact flare with rings of light and a swirl "
    "of glowing particles at the patellar tendon below the kneecap, all inside the translucent body shell.",
    "Already under load on the first frame, the leg itself stays where it is. The curved wave-fronts of light TRAVEL DOWN through the "
    "inside of the thigh one after another towards the knee, like pulses of force, about one arriving every second; as each one reaches "
    "the knee the flare at the tendon below the kneecap bursts brighter, a new ring of light ripples out from it and fades, and the "
    "particle swirl turns faster for a moment, then settles. The thigh tenses slightly with each arrival. The flare stays on its one spot.",
    "no wave-fronts leaving the leg, no light outside the body shell, no energy flying in from outside, no second spot, no glow down the shin, "
    "no leg moving, no second limb, no text, no numbers, no camera orbit, no zoom, no slow motion",
    1.7, hi=6, anat=True,   # line now "Seventeen times your bodyweight" (B06a2 takes the rest) ≈ 1.7 s → 3 s
    risks=[{"risk": "the wave-fronts morph, multiply or leave the leg", "prevented_by": "'travel down through the inside of the thigh', HOLD-C + NEG-WARP-C, 'no wave-fronts leaving the leg, no light outside the body shell'"},
           {"risk": "the leg moves or the camera orbits", "prevented_by": "'the leg itself stays where it is', locked-off camera, 'no leg moving, no camera orbit'"},
           {"risk": "the flare wanders or a second spot appears", "prevented_by": "'the flare stays on its one spot', 'no second spot, no glow down the shin'"}])

# B09-BR image v1 (user CONFIRM 2026-09-30): Maureen's kitchen table, grey sleeve, black hinged brace, white gel tube, blister pack
# under her hand. "Which is why most of what gets sold for this cannot work." ≈ 3.2 s → 4 s.
B["B09-BR"] = clip("B09-BR",
    "An older white woman's hand in a dusty-pink cardigan cuff, a gold wedding ring, resting on a blister pack of white tablets on a "
    "wooden kitchen table, beside a plain white gel tube, a grey knit knee sleeve and a black hinged knee brace on a linen runner.",
    "Already moving on the first frame: her hand slides the blister pack a little way into line beside the gel tube, lets go, and "
    "comes to rest flat on the table beside it — one unhurried movement, about two seconds. The four things stay exactly where they are.",
    "no second hand, no face, no person entering the frame, no picking anything up, no tablets popping out, no readable text, no labels, "
    "no logos, no extra fingers, no objects moving on their own",
    3.2, hi=5,
    risks=[{"risk": "fingers warp or multiply on the pack", "prevented_by": "one slide and let go, HOLD-C + NEG-WARP-C, 'no extra fingers'"},
           {"risk": "text or labels appear on the tube or pack", "prevented_by": "'no readable text, no labels, no logos'"},
           {"risk": "the other objects drift or morph", "prevented_by": "'the four things stay exactly where they are', 'no objects moving on their own'"}])

# B10b image v1 (user CONFIRM 2026-09-30): high three-quarter CU on the kitchen table, her hands on the black hinged brace's metal
# hinge. "A hinged brace stops the knee going sideways, and it was never going sideways." ≈ 4.3 s → 6 s.
B["B10b"] = clip("B10b",
    "An older white woman's two hands in dusty-pink cardigan cuffs, a gold wedding ring, holding a bulky black hinged knee brace on a "
    "wooden kitchen table by its brushed-metal side bar and hinge, a linen runner and a jug of flowers behind.",
    "Already moving on the first frame: her hands push once to bend the brace sideways at the metal hinge, pressing harder for a moment "
    "— the metal bar does not give at all and stays dead straight — then her grip eases off and her hands rest on it. One push and "
    "release, at an unhurried pace over about two seconds. The brace stays where it is on the table.",
    "no metal bending, no hinge breaking, no brace folding, no brace changing shape, no second pair of hands, no face, no person entering "
    "the frame, no readable text, no labels, no logos, no extra fingers",
    4.3, hi=6,
    risks=[{"risk": "the metal bar bends or the brace morphs under her hands", "prevented_by": "'does not give at all and stays dead straight', HOLD-C + NEG-WARP-C, 'no metal bending, no brace changing shape'"},
           {"risk": "fingers warp or multiply on the hinge", "prevented_by": "one push and release, 'no extra fingers', 'no second pair of hands'"},
           {"risk": "text or logos appear on the brace", "prevented_by": "'no readable text, no labels, no logos'"}])

# B10a image v2 (user Confirm on the board 2026-09-30): low front-on, Maureen standing in her kitchen, the grey sleeve snug round
# her whole right knee, her hands on it. "A sleeve squeezes the whole knee and leaves that band carrying everything." ≈ 4.3 s → 6 s.
B["B10a"] = clip("B10a",
    "An older white woman's legs seen low and front-on as she stands on a tiled kitchen floor: a plain grey knit sleeve pulled on round "
    "her whole right knee, both her hands resting on it, pink cardigan cuffs, a navy skirt hem above, white canvas plimsolls below.",
    "Already moving on the first frame: her hands smooth the sleeve once round the knee, pressing it snug from the sides and then down "
    "over the kneecap, and come to rest on it — one unhurried smoothing, about two seconds. She stays standing where she is, her feet "
    "planted, and the sleeve stays one even grey tube round the whole knee.",
    "no walking, no stepping, no pulling the sleeve off, no sleeve slipping down, no sleeve changing colour or shape, no face, no second "
    "person, no knee strap, no brace, no readable text, no logos, no extra fingers, no extra hands",
    4.3, hi=6,
    risks=[{"risk": "the sleeve warps, slips or morphs under her hands", "prevented_by": "one slow smoothing, 'stays one even grey tube', HOLD-C + NEG-WARP-C, 'no sleeve slipping down'"},
           {"risk": "hands or fingers warp", "prevented_by": "one movement then rest, 'no extra fingers, no extra hands'"},
           {"risk": "she walks or the legs move out of frame", "prevented_by": "'She stays standing where she is, her feet planted', 'no walking, no stepping'"}])

# B10a2 image v1 (user CONFIRM 2026-09-30): ANAT-B three-quarter, a faint grey knit sleeve round the whole knee, the tendon under it
# lit and taut. "and leaves that band carrying everything." ≈ 2.3 s → 4 s.
B["B10a2"] = clip("B10a2",
    "A premium 3D anatomical model of a knee on a near-black field, three-quarter front, wrapped in a faint translucent grey knit sleeve "
    "from the lower thigh to the upper shin; under it the patellar tendon is the one lit structure, a tight spot glowing below the kneecap.",
    "Already under load on the first frame, the knee stays where it is. One step's load arrives: [TARGET] draws taut and the spot below "
    "the kneecap pulses brighter over about a second and eases back, while the sleeve round the whole joint stays exactly as it is — "
    "it does not tighten, glow or move.",
    "no sleeve moving, no sleeve glowing, no second spot, no glow down the shin, no leg moving, no second limb, no text, no camera orbit",
    2.3, hi=5, anat=True,
    risks=[{"risk": "the sleeve warps, glows or slides", "prevented_by": "'the sleeve ... stays exactly as it is', 'no sleeve moving, no sleeve glowing', HOLD-C + NEG-WARP-C"},
           {"risk": "the glow spreads or a second spot appears", "prevented_by": "one tight spot named, 'no second spot, no glow down the shin'"},
           {"risk": "the leg moves or the camera orbits", "prevented_by": "'the knee stays where it is', locked camera, 'no leg moving, no camera orbit'"}])
B["B10a2"][0]["motion"] = B["B10a2"][0]["motion"].replace(
    "quadriceps, hamstrings and calf shortens and thickens as the load arrives, the patellar tendon visibly tightens",
    "The patellar tendon visibly tightens").replace(", and the whole structure compresses a few degrees", "")

# B10c image v1 (user CONFIRM GO 2026-09-30): Maureen seated side-on, clear gel glossy on her bare knee, her hand resting on her thigh.
# "Gel sits on the skin." ≈ 1.5 s → 3 s.
B["B10c"] = clip("B10c",
    "An older white woman seated on a wooden kitchen chair, seen side-on at knee height: a glossy film of clear gel on the front of her "
    "bare right knee, her hand with a gold wedding ring resting on her thigh just above it, a pink cardigan cuff, a navy skirt hem.",
    "Already moving on the first frame: her fingertips slide down from her thigh and smooth the gel once over the front of the knee, "
    "the glossy film spreading thin and still sitting on the surface of the skin, then her hand comes to rest on the knee — one "
    "unhurried stroke, about a second and a half.",
    "no gel soaking in, no gel dripping, no rubbing hard, no second hand, no face, no second person, no label on the tube, no readable text, "
    "no extra fingers",
    1.5, hi=4,
    risks=[{"risk": "fingers warp as they smooth the gel", "prevented_by": "one slow stroke then rest, HOLD-C + NEG-WARP-C, 'no extra fingers'"},
           {"risk": "the gel vanishes or drips", "prevented_by": "'still sitting on the surface of the skin', 'no gel soaking in, no gel dripping'"},
           {"risk": "a face or second hand appears", "prevented_by": "'no second hand, no face, no second person'"}])

# B10d image v1 (user CONFIRM GO): her hands holding a plain blister pack over the kitchen table, a glass of water beside.
# "A painkiller turns the alarm off" ≈ 1.7 s → 3 s.
B["B10d"] = clip("B10d",
    "An older white woman's two hands in pink cardigan cuffs, a gold wedding ring, holding a plain silver blister pack of small white "
    "tablets over a wooden kitchen table, a plain glass of water beside them.",
    "Already moving on the first frame: her thumb presses down on one tablet and it pops out through the foil into her other palm — "
    "one press, about a second — then her hands hold still. The glass of water stays where it is.",
    "no tablets multiplying, no pack changing shape, no printing on the pack, no readable text, no face, no second person, "
    "no extra hands, no extra fingers",
    1.7, hi=4,
    risks=[{"risk": "fingers or the pack warp during the press", "prevented_by": "one press then still, HOLD-C + NEG-WARP-C, 'no pack changing shape'"},
           {"risk": "extra tablets or hands appear", "prevented_by": "'no tablets multiplying', 'no extra hands, no extra fingers'"},
           {"risk": "text appears on the blister pack", "prevented_by": "'no printing on the pack, no readable text'"}])

# B10d2 image v2 (user Fix 'give me different broll here', then 'confirm'): Desmond at the foot of his stairs, low side-on, legs only,
# hands on his thighs, knees bent, pushing himself up.
B["B10d2"] = clip("B10d2",
    "A Black British man of sixty-six seen side-on from low in his hall, cropped at the waist: dark grey jogging shorts, a navy zip-neck top, "
    "bare dark-skinned knees and shins, plain white trainers, both hands pressed on his thighs just above the knees, the grey-carpeted "
    "bottom stairs behind him.",
    "Already moving on the first frame: he pushes down on his thighs and straightens up — both knees taking his whole weight as they "
    "slowly straighten — one ordinary push up, about two seconds, then he stands still with his hands leaving his thighs. His feet stay "
    "planted; he stays in frame.",
    "no stepping, no walking out of frame, no stumbling, no face, no head, no second person, no knee strap, no brace, no logos on the "
    "trainers, no extra legs, no extra hands",
    2.3, hi=5,
    risks=[{"risk": "legs warp as he straightens", "prevented_by": "one slow push up, feet planted, HOLD-C + NEG-WARP-C, 'no extra legs'"},
           {"risk": "the head/face comes into frame as he stands", "prevented_by": "locked-off tripod, 'no face, no head', cropped at the waist in subject"},
           {"risk": "the swoosh on the trainers stays visible", "prevented_by": "'no logos on the trainers' (the start frame shows it; the edit can blur it if it stays)"}])

# B06 video gen 4 (user 'B06 GO', 2026-09-30) from image v7: close-up on the knee joint, low three-quarter, wave-fronts into the joint,
# impact flare with rings and particles below the kneecap. v3 faults fixed at the source: the waves ran on past the knee onto the shin
# (now: they end AT the knee), the leg bent and lifted (now: the knee holds its pose), a second limb edge showed (now: named out).
B["B06"] = clip("B06",
    "A premium 3D anatomical model, close up on a knee joint on a near-black field, low three-quarter: bright wave-fronts of light "
    "inside the lower thigh, a heat glow in the joint and a blazing impact flare with rings of light and a swirl of glowing particles "
    "at the patellar tendon just below the kneecap, all inside the translucent body shell.",
    "Already under load on the first frame, and the knee holds exactly this pose. The wave-fronts of light travel down through the lower "
    "thigh one after another and END AT THE KNEE, about one arriving every second; as each one arrives the flare below the kneecap bursts "
    "brighter, a new ring of light ripples out through the tendon and fades, and the particle swirl turns faster for a moment. Nothing "
    "travels past the knee onto the shin. The flare stays on its one spot.",
    "no leg moving, no knee bending, no light travelling down the shin, no rings on the shin, no second limb, no light outside the body "
    "shell, no text, no camera orbit, no zoom",
    1.7, hi=6, anat=True,
    risks=[{"risk": "the waves run on past the knee onto the shin (seen in v3)", "prevented_by": "'END AT THE KNEE', 'Nothing travels past the knee onto the shin', 'no light travelling down the shin, no rings on the shin'"},
           {"risk": "the leg bends or lifts (seen in v3)", "prevented_by": "'the knee holds exactly this pose', 'no leg moving, no knee bending', locked camera"},
           {"risk": "a second limb edge appears (seen in v3)", "prevented_by": "'no second limb', close framing on the one knee"}])
B["B06"][0]["motion"] = B["B06"][0]["motion"].replace(", and the whole structure compresses a few degrees", "")

# B12 image v1 (user Confirm 2026-09-30): ANAT-A profile, the knee under load, the tendon spot below the kneecap glowing hot; pip.
# "What that band actually needs" ≈ 1.6 s → 3 s.
B["B12"] = clip("B12",
    "A premium 3D anatomical model of a knee seen from the side on a near-black field: the thigh muscles, the kneecap and the patellar "
    "tendon below it drawn taut, one tight spot on the tendon just below the kneecap glowing hot red-orange.",
    "Already under load on the first frame, the knee holds its pose. One step's load arrives: [TARGET] draws a little tauter and the "
    "spot below the kneecap pulses hotter and brighter over about a second, then eases back a little. The spot stays one tight spot.",
    "no leg moving, no knee bending, no glow spreading down the shin, no second spot, no second limb, no text, no camera orbit, no zoom",
    1.6, hi=4, anat=True,
    risks=[{"risk": "the glow spreads down the shin", "prevented_by": "'The spot stays one tight spot', 'no glow spreading down the shin, no second spot'"},
           {"risk": "the leg moves or bends", "prevented_by": "'the knee holds its pose', 'no leg moving, no knee bending', locked camera"},
           {"risk": "a second limb appears", "prevented_by": "'no second limb', HOLD-C + NEG-WARP-C"}])
B["B12"][0]["motion"] = B["B12"][0]["motion"].replace(", and the whole structure compresses a few degrees", "")

# B12b image v1 (user Confirm 2026-09-30): ANAT-B close on the patellar tendon, a soft warm spot below the kneecap.
# "is for less of your weight to land on it." ≈ 2.2 s → 4 s.
B["B12b"] = clip("B12b",
    "A premium 3D anatomical model seen close and front-on on a near-black field: the lower edge of the kneecap and the patellar "
    "tendon below it as a broad pearly band, one soft warm glow on it just below the kneecap.",
    "Already on the first frame, the tendon is at rest. Over about two seconds the warm red-orange at the centre of the spot cools and "
    "fades to a gentle, even pearly light, and the band eases a little, relaxed — less load landing on it. It settles and stays calm.",
    "no glow brightening, no glow spreading, no second spot, no bones moving, no second limb, no text, no camera orbit, no zoom",
    2.2, hi=5, anat=True,
    risks=[{"risk": "the glow brightens instead of calming", "prevented_by": "'cools and fades to a gentle, even pearly light', 'no glow brightening'"},
           {"risk": "the model swims or the band warps", "prevented_by": "HOLD-C + NEG-WARP-C, one slow fade, 'no bones moving'"},
           {"risk": "the glow spreads or a second spot appears", "prevented_by": "'no glow spreading, no second spot'"}])
B["B12b"][0]["motion"] = (B["B12b"][0]["motion"]
    .replace("quadriceps, hamstrings and calf shortens and thickens as the load arrives, the patellar tendon visibly tightens and straightens along its length, and the whole structure compresses a few degrees", "The patellar tendon loosens a little and rests as the load eases")
    .replace("The anatomy takes the weight — it is not a still model with light played over it.", "The anatomy eases — it is not a still model with light played over it."))

# B11-BR image v2 (user confirm 2026-09-30): ANAT-A front-on, a ghosted sleeve round the joint and ghosted brace bars down both
# sides; the one spot on the tendon below the kneecap glowing untouched. "None of them are aimed at the spot." ≈ 1.8 s → 3 s.
B["B11-BR"] = clip("B11-BR",
    "A premium 3D anatomical model of a knee seen straight from the front on a near-black field, a faint ghosted grey sleeve round the "
    "whole joint and the ghosted black side bars and hinges of a brace down both sides, one tight spot glowing on the patellar tendon "
    "just below the kneecap in the middle.",
    "Already under load on the first frame, the knee holds its pose. The spot below the kneecap pulses brighter once over about a "
    "second and eases back, while the sleeve and the brace bars around the knee stay exactly as they are — they do not move, tighten "
    "or glow. The spot stays one tight spot.",
    "no sleeve moving, no brace moving, no brace glowing, no second spot, no glow down the shin, no leg moving, no second limb, no text, "
    "no camera orbit",
    1.8, hi=4, anat=True,
    risks=[{"risk": "the ghosted sleeve or brace bars warp, slide or glow", "prevented_by": "'stay exactly as they are — they do not move, tighten or glow', 'no sleeve moving, no brace moving', HOLD-C + NEG-WARP-C"},
           {"risk": "the glow spreads or a second spot appears", "prevented_by": "'The spot stays one tight spot', 'no second spot, no glow down the shin'"},
           {"risk": "the leg moves or a second limb appears", "prevented_by": "'the knee holds its pose', 'no leg moving, no second limb', locked camera"}])
B["B11-BR"][0]["motion"] = B["B11-BR"][0]["motion"].replace(", and the whole structure compresses a few degrees", "")

# B14a image v4 (user Fix 'MAKE SURE THE STRAP STAY IN THAT PLACE', then 'CONFIRM'): side-on, Maureen seated on her bottom stair, the
# strap already on her right knee, both hands resting on the knee above it. Generation 2 (v1 slid the strap and turned it — §22X: the
# strap no longer moves at all). One action: her hands lift off her knee and settle on her thigh; the strap stays exactly where it is.
B["B14a"] = clip("B14a",
    "A slight white British woman of sixty-nine seen side-on sitting on her bottom stair: sage-green cardigan, denim skirt, pale older "
    "legs, white canvas plimsolls; a black STRYDE knee strap with a chrome slide already worn on her right leg just below the kneecap, "
    "both her hands resting on top of the knee above it.",
    "Already moving on the first frame: both her hands lift slowly off her knee and settle on her thigh — one slow movement, about a "
    "second and a half — then she sits still. The strap does not move at all: it stays exactly where it is on her leg, rigid, keeping "
    "its shape, its slide and its wordmark.",
    "no strap moving, no strap sliding, no strap turning, no strap changing shape, no strap changing size, no hands touching the strap, "
    "no standing up, no face, no second strap, no extra hands, no extra fingers",
    4.0, hi=5,
    risks=[{"risk": "the strap moves or turns with the hands (v1)", "prevented_by": "hands lift off the knee, never touch the strap; 'no strap moving/sliding/turning, no hands touching the strap'"},
           {"risk": "the shell warps", "prevented_by": "rigid line in motion, 'no strap changing shape/size'"},
           {"risk": "hands duplicate", "prevented_by": "HOLD-C + NEG-WARP-C, 'no extra hands, no extra fingers'"}])
B["B14a"][0]["motion"] = B["B14a"][0]["motion"].replace("hair, fabric and straps lag and keep moving after the body stops", "the cardigan cuffs settle; the strap never moves")

# B13 image v6 (user Fixes, then 'CONFIRM GO'): the strap front face up on her one open palm in the kitchen, wordmark to the lens.
# One small lift into the light; the strap is rigid and still on the palm, only the band sways (§27G rigid product).
B["B13"] = clip("B13",
    "An older woman's open right palm held out in a kitchen, a small black STRYDE knee strap lying across it front face to the lens: two "
    "rounded peaks, chrome slides, the grey stryde wordmark; the soft black band looping behind her hand.",
    "Already moving on the first frame: her open hand lifts a few centimetres towards the window light — one small slow lift, about a "
    "second and a half — then holds still. The strap rests still on her palm the whole time, rigid, keeping its shape, size and wordmark; "
    "only the soft band behind her hand sways a little.",
    "no strap sliding, no strap turning, no strap changing shape, no strap changing size, no wordmark changing, no fingers closing over "
    "the strap, no second hand, no second strap, no extra fingers",
    3.0, hi=5,
    risks=[{"risk": "the shell warps or the wordmark smears", "prevented_by": "rigid line in motion, 'no strap changing shape/size, no wordmark changing'"},
           {"risk": "the strap slides off the palm", "prevented_by": "one small slow lift, 'rests still on her palm', 'no strap sliding, no strap turning'"},
           {"risk": "fingers close over the wordmark", "prevented_by": "'no fingers closing over the strap'"}])
B["B13"][0]["motion"] = B["B13"][0]["motion"].replace("hair, fabric and straps lag and keep moving after the body stops", "the soft band lags and settles; the shell never moves on the palm")

# B14b image v5 (user Fixes, then 'CONFIRM GO'): the whole strap upright in her one hand, the grey pad to the lens. Generation 2 — v1
# tilted the wrist and the strap bent like rubber (§22X motion fault): now the hand holds still and only the band loop sways.
B["B14b"] = clip("B14b",
    "An older woman's hand holding a small black knee strap upright, its inside turned to the lens: a grey grooved pad with one smooth "
    "comma-shaped ridge inside a thin black rim, a chrome slide at each end, the black band hanging below in a soft loop, a kitchen soft behind.",
    "Already on the first frame: her hand holds the strap still. The soft band loop below it sways gently once and settles, over about "
    "two seconds. The shell and its pad do not move, bend or turn at all — rigid, facing the lens, keeping their shape and size.",
    "no strap bending, no shell flexing, no strap turning, no strap tilting, no pad changing shape, no ridge moving, no strap changing size, "
    "no front of the shell showing, no wordmark, no second hand, no extra fingers",
    3.0, hi=5,
    risks=[{"risk": "the shell bends like rubber (v1)", "prevented_by": "the hand holds still; only the band sways; 'no strap bending, no shell flexing'"},
           {"risk": "the pad pattern swims", "prevented_by": "'no pad changing shape, no ridge moving', HOLD-C"},
           {"risk": "the strap turns to its front", "prevented_by": "'no strap turning, no front of the shell showing, no wordmark'"}])
B["B14b"][0]["motion"] = B["B14b"][0]["motion"].replace("hair, fabric and straps lag and keep moving after the body stops", "only the band loop lags and settles; the shell never moves")

# One slow fade: the warm glow on the tendon under the strap calms to a soft pearly light; the strap never moves (rigid product).
B["B14c"] = clip("B14c",
    "A premium 3D anatomical model of a knee seen straight from the front on a near-black field, a black STRYDE knee strap with two "
    "rounded peaks, chrome slides and a grey stryde wordmark seated across the front of the leg just below the kneecap.",
    "Already under load on the first frame: a soft warm glow shows on the tendon at the edges of the strap; over about two seconds it "
    "fades and cools to a calm, even pearly light as the strap takes the load, then stays calm. The strap stays exactly where it is — "
    "rigid, its shape, peaks and wordmark unchanged; the kneecap stays uncovered above it.",
    "no strap moving, no strap sliding, no strap changing shape, no strap changing size, no wordmark changing, no second strap, no "
    "arrows, no text, no labels, no glow spreading down the shin, no second limb, no camera orbit, no zoom",
    3.0, hi=5,
    risks=[{"risk": "the strap warps or the wordmark smears", "prevented_by": "rigid-product line in motion, 'no strap changing shape/size, no wordmark changing'"},
           {"risk": "the strap slides up onto the kneecap", "prevented_by": "'stays exactly where it is', 'no strap moving, no strap sliding'"},
           {"risk": "the glow spreads or text appears", "prevented_by": "'no glow spreading down the shin', 'no arrows, no text, no labels'"}])

B["B14c"][0]["motion"] = B["B14c"][0]["motion"].replace("hair, fabric and straps lag and keep moving after the body stops", "the strap never moves")

# ── 2026-09-30 B15, B16a, B16c (images confirmed) — worn strap in motion: rigid, never slides (§27G) ──
B["B15"] = clip("B15",
    "A slight older white woman's pale right knee seen front-on at knee height in her hall: the hem of a denim skirt above, a black "
    "STRYDE strap seated just below the kneecap, the kneecap's lower edge sitting in the strap's notch, the grey stryde wordmark readable.",
    "Already on the first frame: she shifts her weight onto this leg, the knee straightening a touch and settling — one small, slow "
    "movement, about a second and a half — then she stands still. the strap stays exactly where it is on the leg — rigid, keeping its shape, size and wordmark, moving only as one piece with the knee; the kneecap stays in the notch.",
    "no strap sliding, no strap moving up, no strap moving down, no strap changing shape, no strap changing size, no wordmark changing, "
    "no hands, no walking out of frame, no camera movement, no extra legs",
    3.0, hi=5,
    risks=[{"risk": "the strap slides or warps", "prevented_by": "one small weight shift, rigid line, 'no strap sliding/moving/changing shape'"},
           {"risk": "the leg warps", "prevented_by": "HOLD-C + NEG-WARP-C, 'no extra legs'"},
           {"risk": "the camera travels", "prevented_by": "locked-off tripod clause"}])
B["B16a"] = clip("B16a",
    "A Black British man's strong dark-brown right knee seen front-on at knee height on his stairs: the hem of khaki shorts above, a "
    "black STRYDE strap seated just below the kneecap, the grey stryde wordmark readable, the grey stair carpet behind.",
    "Already moving on the first frame: he bends this knee and steps down one stair towards the lens, easily — one ordinary step, about "
    "a second — then stands on the lower stair. the strap stays exactly where it is on the leg — rigid, keeping its shape, size and wordmark, moving only as one piece with the knee.",
    "no second step, no stumbling, no strap sliding, no strap moving up, no strap moving down, no strap changing shape, no strap changing "
    "size, no wordmark changing, no face, no camera movement, no extra legs",
    3.0, hi=5,
    risks=[{"risk": "the strap slides or bends with the knee", "prevented_by": "rigid line in motion, 'no strap sliding/changing shape'"},
           {"risk": "legs warp on the step", "prevented_by": "one ordinary step, HOLD-C + NEG-WARP-C, 'no extra legs'"},
           {"risk": "the camera follows him", "prevented_by": "locked-off tripod clause, 'no camera movement'"}])
def _walker_clip(beat, who):
    return clip(beat,
        who + " seen front-on from low, walking towards the lens, a black STRYDE strap seated just below the kneecap, the grey stryde "
        "wordmark readable, the place soft behind.",
        "Already mid-stride on the first frame: they walk towards the lens at an easy walking pace, two steps, about two seconds, and "
        "the legs pass just out of the bottom of the frame. The strap stays exactly where it is on the leg — rigid, keeping its shape, "
        "size and wordmark, moving only as one piece with the knee.",
        "no running, no strap sliding, no strap moving up, no strap moving down, no strap changing shape, no strap changing size, no "
        "wordmark changing, no logos on the shoes, no face, no camera movement, no extra legs",
        3.0, hi=5,
        risks=[{"risk": "the strap slides as they walk", "prevented_by": "rigid line, 'no strap sliding/moving'"},
               {"risk": "legs warp mid-stride", "prevented_by": "easy walking pace, two steps, HOLD-C + NEG-WARP-C, 'no extra legs'"},
               {"risk": "the camera tracks them", "prevented_by": "locked-off tripod clause, 'no camera movement'"}])
# B16c ×3 (user 'GIVE ME 3 BROLLS FOR THIS LINE, WALKING WEARING STRYDE', images confirmed)
B["B16c"] = _walker_clip("B16c", "A British Indian woman in her sixties, a knee-length navy floral skirt, on a park path,")
B["B16c2"] = _walker_clip("B16c2", "A white British man about seventy, stone walking shorts, on a seaside promenade, seen a little three-quarter,")
B["B16c3"] = _walker_clip("B16c3", "A Black British woman in her late fifties, a knee-length khaki skirt and a paper shopping bag, on a high street,")
for _b in ("B15", "B16a", "B16c", "B16c2", "B16c3"):
    B[_b][0]["motion"] = B[_b][0]["motion"].replace("hair, fabric and straps lag and keep moving after the body stops", "the fabric of the hem lags; the strap never slides")

# ── 2026-09-30 "CONFIRM AND GO": B15-BR, B16b, B17a, B17b (images confirmed). Learned on B13/B14b: a strap in a moving hand bends —
# the hand holding it stays still; only the other hand / the person moves (§27G rigid product). ──
B["B15-BR"] = clip("B15-BR",
    "An older white woman standing on her stairs in a sage cardigan and denim skirt, one hand resting on her thigh above her bare knee, "
    "the other hand held out open with a small black STRYDE knee strap lying on the palm, front face up.",
    "Already moving on the first frame: the hand on her thigh slides slowly down and two fingertips come to rest flat just below her "
    "kneecap, marking the spot — one slow movement, about a second and a half. The open hand holding the strap stays completely still. "
    "The strap does not move at all — rigid, keeping its shape, size and wordmark on her palm.",
    "no strap moving, no strap bending, no strap changing shape, no strap changing size, no wordmark changing, no hand closing over the "
    "strap, no face, no second person, no extra hands, no extra fingers",
    3.0, hi=5,
    risks=[{"risk": "the strap bends in the hand (B13/B14b)", "prevented_by": "the holding hand stays still; rigid line; 'no strap bending/moving'"},
           {"risk": "fingers merge with the knee", "prevented_by": "one slow slide, HOLD-C + NEG-WARP-C, 'no extra fingers'"},
           {"risk": "the camera moves", "prevented_by": "locked-off tripod clause"}])
B["B16b"] = clip("B16b",
    "A British surgeon of Pakistani heritage, late fifties, short black hair grey at the temples, navy scrubs and a grey fleece gilet, "
    "seated at his desk in a consulting room, holding a small black STRYDE knee strap up in one hand, a knee model beside him.",
    "Already on the first frame: he lifts his eyes from the strap to someone across the desk and gives a small, calm nod — one look up, "
    "about a second and a half. His hand holding the strap stays completely still. The strap does not move at all — rigid, keeping its shape, size and wordmark.",
    "no strap moving, no strap bending, no strap changing shape, no wordmark changing, no looking at the camera, no talking, no smiling "
    "for the camera, no second person, no extra hands, no extra fingers",
    3.0, hi=5,
    risks=[{"risk": "the strap bends in his hand", "prevented_by": "the hand stays still; rigid line; 'no strap bending/moving'"},
           {"risk": "he looks into the lens", "prevented_by": "'to someone across the desk', 'no looking at the camera'"},
           {"risk": "face drifts from the character", "prevented_by": "one small look and nod only, HOLD-C"}])
B["B17a"] = clip("B17a",
    "A Black British man's strapped right knee seen front-on on his stairs, his navy tracksuit leg bunched above the bare knee, both his "
    "hands at the two chrome-slide ends of a black STRYDE strap seated just below the kneecap.",
    "Already moving on the first frame: both hands give the strap one light press into place, then let go and move away out of frame "
    "to either side — one movement, about a second and a half. The strap does not move at all — rigid, keeping its shape, size and wordmark on the knee.",
    "no strap moving, no strap sliding, no strap bending, no strap changing shape, no wordmark changing, no fabric falling over the "
    "strap, no face, no extra hands, no extra fingers",
    3.0, hi=5,
    risks=[{"risk": "the strap moves with the hands", "prevented_by": "one light press then release; 'no strap moving/sliding'"},
           {"risk": "the bunched trouser drops over it", "prevented_by": "'no fabric falling over the strap'"},
           {"risk": "hands duplicate", "prevented_by": "HOLD-C + NEG-WARP-C, 'no extra hands'"}])
B["B17b"] = clip("B17b",
    "An older white woman's pale right leg seen front-on at knee height on her stairs, the hem of a denim skirt above, a black STRYDE "
    "strap seated just below the kneecap, her white plimsoll on the bottom stair.",
    "Already moving on the first frame: she steps down off the bottom stair onto the hall floor towards the lens — one ordinary step, "
    "about a second — then stands. The strap does not move at all — rigid, keeping its shape, size and wordmark on her leg, never rolling down.",
    "no strap moving, no strap rolling down, no strap sliding, no strap bending, no wordmark changing, no stumbling, no face, no camera "
    "movement, no extra legs",
    3.0, hi=5,
    risks=[{"risk": "the strap slips (the line says it doesn't)", "prevented_by": "rigid line; 'no strap rolling down/sliding'"},
           {"risk": "legs warp on the step", "prevented_by": "one ordinary step, HOLD-C + NEG-WARP-C, 'no extra legs'"},
           {"risk": "the camera follows", "prevented_by": "locked-off tripod clause"}])
for _b in ("B15-BR", "B16b", "B17a", "B17b"):
    B[_b][0]["motion"] = B[_b][0]["motion"].replace("hair, fabric and straps lag and keep moving after the body stops", "fabric lags a little; the strap never moves")

# ── 2026-09-30 B17b v3 / B17c v4 images confirmed → walking clips (like B16c) ──
B["B17b"] = clip("B17b",
    "An older white woman's pale right leg seen front-on from low on a pavement, the hem of a denim skirt above, a black STRYDE strap "
    "seated just below the kneecap, a white plimsoll on the paving, a street of semis soft behind.",
    "Already mid-stride on the first frame: she walks towards the lens at an easy walking pace, two steps, about two seconds, and her "
    "legs pass just out of the bottom of the frame. The strap stays exactly where it is on her leg, never rolling down or sliding — "
    "rigid, keeping its shape, size and wordmark, moving only as one piece with the knee.",
    "no running, no strap sliding, no strap rolling down, no strap moving up, no strap changing shape, no wordmark changing, no face, "
    "no camera movement, no extra legs",
    3.0, hi=5,
    risks=[{"risk": "the strap slips (the line says it doesn't)", "prevented_by": "rigid line; 'no strap sliding/rolling down'"},
           {"risk": "legs warp mid-stride", "prevented_by": "easy walking pace, two steps, HOLD-C + NEG-WARP-C, 'no extra legs'"},
           {"risk": "the camera tracks her", "prevented_by": "locked-off tripod clause, 'no camera movement'"}])
B["B17c"] = clip("B17c",
    "A Black British man's legs seen front-on from ground level on a pavement, walking in long plain navy trousers that cover his knees, "
    "white trainers, a street of semis soft behind.",
    "Already mid-stride on the first frame: he walks towards the lens at an easy walking pace, two steps, about two seconds, and his "
    "legs pass just out of the bottom of the frame. The trouser fabric moves naturally over the knee with the stride — nothing shows "
    "underneath.",
    "no running, no visible strap, no bulge under the trousers, no outline under the fabric, no trousers riding up, no logos on the "
    "trainers, no face, no camera movement, no extra legs",
    3.0, hi=5,
    risks=[{"risk": "an outline of the strap shows through", "prevented_by": "'no bulge, no outline under the fabric, no visible strap'"},
           {"risk": "legs warp mid-stride", "prevented_by": "easy walking pace, two steps, HOLD-C + NEG-WARP-C, 'no extra legs'"},
           {"risk": "the camera tracks him", "prevented_by": "locked-off tripod clause, 'no camera movement'"}])
for _b in ("B17b", "B17c"):
    B[_b][0]["motion"] = B[_b][0]["motion"].replace("hair, fabric and straps lag and keep moving after the body stops", "fabric lags a little with each step")

START = {"B17c": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_180847_021f33a1-6deb-4b77-a0e4-71386a5ef51e.png",
         "B15-BR": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_172430_65c0e88d-6f35-4e1e-8179-c59137a63188.png",
         "B16b": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_172428_cd78f594-03a3-464c-89d0-0bb10b8647fc.png",
         "B17a": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_172428_558e9117-34fa-4372-915b-a77ceed91aad.png",
         "B17b": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_180845_347779b9-c72d-43c5-b420-25576b1b839c.png",
         "B15": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_171207_7f990a90-9ac1-4b71-ae5d-db3100e64d28.png",
         "B16a": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_171208_c47a0262-949a-4916-b2b9-f3a4f299e573.png",
         "B16c": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_181732_31a8a1ec-7792-44d0-8444-46f3d88776ac.png",
         "B16c2": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_181733_a7a7d77c-8e08-4eeb-b086-4c2c542cdba6.png",
         "B16c3": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_181732_555079af-6939-431b-a6be-491d12f6be49.png",
         "B14c": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_163337_ba5e6993-4e59-4bf8-8ec8-9aeb85e5a9de.png",
         "B14a": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_164241_ab6052f5-7c35-44e1-8052-a67bfedf24f7.png",
         "B14b": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_164932_3277f2fd-1eb7-4b05-8d44-8c7529e34946.png",
         "B13": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_164932_18bd9cdf-0960-44c3-a3c1-ef65855dd429.png",
         "B11-BR": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_144242_82c48d6d-785c-454d-91a5-bfea8bd28bcb.png",
         "B12": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_143722_0a389350-3a9a-410e-a56c-5b29e5ee4659.png",
         "B12b": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_143722_c1a15ea6-ad66-4f8b-aeb5-9bb6b3d657b0.png",
         "B10c": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_140203_48b079aa-50b4-48f7-888a-f2c5779f802c.png",
         "B10d": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_140212_e6684a2f-35c2-4d68-91bd-def7c5820b7a.png",
         "B10d2": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_155002_e1a1e449-2ce8-454d-9af0-774d557c78fb.png",
         "B10a2": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_130409_3a6ea112-6592-45b6-bf5b-93efcd5e52d8.png",
         "B10a": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_124139_4d54cb95-4893-4963-aeaa-56169d8697f8.png",
         "B10b": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_123301_214e72ba-2159-428e-bfeb-3619729c8fca.png",
         "B09-BR": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_122112_f986eef2-5bbd-465a-920b-fd552b19e4e5.png",
         "B08-BR2": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_113626_ed25dfaf-eb63-4715-8c55-3f29b1f75f53.png",
         "B06b": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_120637_827d2dc0-4a1e-44f8-a542-35ccb0fd7320.png",
         "B08b": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_115249_bc7a2b7d-06a8-444e-bf7a-4a7e604d9123.png",
         "B08c": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_115249_63775ae4-a1ed-4292-9094-ad0930a4f2d6.png",
         "B08a": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_111706_9b645285-1aef-43ba-99f4-f95ac2ed5c6b.png",
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
         "B06": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_140945_6ede13f8-ffce-4d69-b55d-17a1c9d5ea6f.png",
         "B06-BR": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_215145_b3e86d93-f337-4226-9feb-1ae2a35a886e.png"}

# ── 2026-09-30 "FIX AND CONFIRM": B18b v1 / B19a v1 images confirmed (Kie renders — start frames are the local board copies) ──
B["B18b"] = clip("B18b",
    "A white British woman of sixty-nine with soft white hair, in a sage-green cardigan, white T-shirt and mid-blue denim skirt, coming "
    "DOWN her carpeted stairs towards the camera, facing forwards, her left hand light on the honey oak handrail, a black STRYDE strap "
    "seated just below her right kneecap, white plimsolls.",
    "Already mid-step on the first frame: she comes down one more stair towards the camera, facing forwards, easy and unhurried — her "
    "left foot lands on the stair below, about a second and a half — then her weight settles onto it, her hand sliding lightly along "
    "the rail. The strap stays exactly where it is on her leg — rigid, keeping its shape, size and wordmark, moving only as one piece "
    "with the knee.",
    "no strap moving, no strap sliding, no strap changing shape, no strap on the left leg, no stumbling, no hurrying, no going up the "
    "stairs, no turning sideways, no looking into the lens, no camera movement, no extra legs, no extra hands",
    3.0, hi=5,
    risks=[{"risk": "legs or feet warp on the stair", "prevented_by": "one step at a countable pace, caught mid-step, HOLD-C + NEG-WARP-C"},
           {"risk": "the strap slides or changes", "prevented_by": "rigid line; 'no strap moving/sliding/changing shape'"},
           {"risk": "the camera travels with her", "prevented_by": "locked-off tripod clause, 'no camera movement'"}])
B["B19a"] = clip("B19a",
    "A white British woman of sixty-nine with soft white hair, in a navy-and-white striped T-shirt and a denim skirt, sitting on her "
    "bottom stair seen from above, both knees side by side, a black STRYDE strap seated just below her right kneecap, her left knee "
    "bare, both hands resting on her thighs, white plimsolls on the hall carpet.",
    "Already breathing out on the first frame: one slow, relaxed breath out, about a second and a half — her shoulders drop a little and "
    "settle; her hands stay resting on her thighs and her knees stay still. The strap does not move at all — rigid, keeping its shape, "
    "size and wordmark.",
    "no strap moving, no strap appearing on the left knee, no second strap, no hands moving to the strap, no standing up, no camera "
    "movement, no extra legs, no extra hands, no extra fingers",
    3.0, hi=5,
    risks=[{"risk": "a strap appears on the bare left knee", "prevented_by": "'no strap appearing on the left knee, no second strap'"},
           {"risk": "hands drift and pull the strap", "prevented_by": "hands stay resting; 'no hands moving to the strap'"},
           {"risk": "the face warps", "prevented_by": "one small breath only, HOLD-C + NEG-WARP-C"}])
for _b in ("B18b", "B19a"):
    B[_b][0]["motion"] = B[_b][0]["motion"].replace("hair, fabric and straps lag and keep moving after the body stops", "hair and fabric lag a little; the strap never moves")
START.update({"B18b": str(HERE.parent / "broll/B18b_v1.png"), "B19a": str(HERE.parent / "broll/B19a_v1.png")})

# ── 2026-09-30 "FIX AND CONFIRM" round 2: B18-BR v2 / B18a v2 images confirmed (Kie renders, local start frames) ──
B["B18-BR"] = clip("B18-BR",
    "A white British woman of sixty-nine with soft white hair, in a navy-and-white striped T-shirt, sitting at her pale-oak kitchen "
    "table with a white mug of tea, holding her phone in both hands, its screen turned away from the camera.",
    "Already typing on the first frame: her thumbs tap the screen a few times at an easy pace, about two seconds, and a small warm smile "
    "grows as she writes. The phone stays turned away; the mug stays put.",
    "no screen turning to the camera, no readable text, no looking into the lens, no second person, no camera movement, no extra hands, "
    "no extra fingers",
    3.0, hi=5,
    risks=[{"risk": "the screen turns to camera with text", "prevented_by": "'the phone stays turned away', 'no screen turning to the camera, no readable text'"},
           {"risk": "fingers merge on the phone", "prevented_by": "a few easy taps, HOLD-C + NEG-WARP-C, 'no extra fingers'"},
           {"risk": "she looks into the lens", "prevented_by": "'no looking into the lens'"}])
B["B18a"] = clip("B18a",
    "A Black British man in his sixties with short grey hair and a grey beard, in a navy T-shirt and khaki shorts, crouching at the foot "
    "of his carpeted stairs tying the lace of his white trainer, his right knee deeply bent in front of him with a black STRYDE strap "
    "seated just below the kneecap.",
    "Already moving on the first frame: his hands pull the lace tight in one easy pull, about a second, then finish the bow; he stays "
    "crouched, relaxed, a small easy smile. The strap does not move at all — rigid, keeping its shape, size and wordmark on the knee.",
    "no strap moving, no strap sliding, no strap changing shape, no wordmark changing, no standing up, no wincing, no logos on the "
    "trainers, no camera movement, no extra hands, no extra fingers, no extra legs",
    3.0, hi=5,
    risks=[{"risk": "the strap moves with the bent knee", "prevented_by": "the knee stays bent (no stand-up), rigid line, 'no strap moving/sliding'"},
           {"risk": "hands and laces tangle", "prevented_by": "one easy pull at a countable pace, HOLD-C + NEG-WARP-C"},
           {"risk": "a logo appears on the trainer", "prevented_by": "'no logos on the trainers'"}])
for _b in ("B18-BR", "B18a"):
    B[_b][0]["motion"] = B[_b][0]["motion"].replace("hair, fabric and straps lag and keep moving after the body stops", "hair and fabric lag a little; the strap never moves")
START.update({"B18-BR": str(HERE.parent / "broll/B18-BR_v2.png"), "B18a": str(HERE.parent / "broll/B18a_v2.png")})

# ── 2026-09-30 "FIX AND CONFIRM" round 4: B19b v4, B19-BR2 v4, B19-BR2c v2 confirmed ──
B["B19b"] = clip("B19b",
    "A white British woman of sixty-nine with soft white hair, in a navy-and-white striped T-shirt and a mid-blue denim skirt, at the top "
    "of her carpeted stairs coming DOWN towards the camera, facing forwards, her hand light on the honey oak handrail, a black STRYDE "
    "strap seated just below the kneecap of the leg on the left of the frame, the other knee bare, white plimsolls.",
    "Already stepping on the first frame: she steps down one stair towards the camera, facing forwards, easy and unhurried — her foot "
    "lands on the stair below, about a second and a half — then her weight settles onto it, her hand sliding lightly along the rail. "
    "The strap stays exactly where it is — rigid, keeping its shape, size and wordmark, moving only as one piece with the knee.",
    "no strap moving, no strap sliding, no strap changing shape, no strap appearing on the bare knee, no second strap, no stumbling, no "
    "hurrying, no going up the stairs, no looking into the lens, no camera movement, no extra legs, no extra hands",
    3.0, hi=5,
    risks=[{"risk": "the strap jumps to the other knee", "prevented_by": "the strap placed by leg in subject; 'no strap appearing on the bare knee, no second strap'"},
           {"risk": "legs warp on the stair", "prevented_by": "one step at a countable pace, HOLD-C + NEG-WARP-C"},
           {"risk": "the camera travels with her", "prevented_by": "locked-off tripod clause, 'no camera movement'"}])
B["B19-BR2"] = clip("B19-BR2",
    "A close-up of a white British woman of sixty-nine with soft white hair, in a navy-and-white striped T-shirt, paused partway down her "
    "stairs, one hand on the honey oak handrail, three-quarter on.",
    "Already on the first frame: a quiet look of surprise softens into a small private smile, about two seconds, as if she has just "
    "noticed something; her eyes glance down once towards her knee and back. Her head moves only a little.",
    "no broad grin, no laughing, no talking, no looking into the lens, no camera movement, no face morphing, no extra fingers",
    3.0, hi=5,
    risks=[{"risk": "the face morphs", "prevented_by": "one small expression change, HOLD-C + NEG-WARP-C, 'no face morphing'"},
           {"risk": "she talks or laughs", "prevented_by": "'no talking, no laughing, no broad grin'"},
           {"risk": "she looks into the lens", "prevented_by": "'no looking into the lens'"}])
B["B19-BR2c"] = clip("B19-BR2c",
    "A white British woman of sixty-nine with soft white hair, in a navy-and-white striped T-shirt, standing side-on at her kitchen window "
    "holding a white mug of tea in both hands, looking out at the garden, calm.",
    "Already on the first frame: she lifts the mug a little and takes one small sip, about two seconds, then lowers it slightly, still "
    "looking out of the window, settled and at ease.",
    "no spilling, no mug changing shape, no turning to the camera, no looking into the lens, no talking, no camera movement, no extra "
    "fingers, no extra hands",
    3.0, hi=5,
    risks=[{"risk": "the mug or hands warp", "prevented_by": "one small sip at a countable pace, HOLD-C + NEG-WARP-C"},
           {"risk": "she turns to the camera", "prevented_by": "'no turning to the camera, no looking into the lens'"},
           {"risk": "tea spills", "prevented_by": "'no spilling'"}])
for _b in ("B19b", "B19-BR2", "B19-BR2c"):
    B[_b][0]["motion"] = B[_b][0]["motion"].replace("hair, fabric and straps lag and keep moving after the body stops", "hair and fabric lag a little" + ("; the strap never moves" if _b == "B19b" else ""))
START.update({"B19b": str(HERE.parent / "broll/B19b_v4.png"), "B19-BR2": str(HERE.parent / "broll/B19-BR2_v4.png"), "B19-BR2c": str(HERE.parent / "broll/B19-BR2c_v2.png")})

# ── 2026-10-01 B19-BR2b v3 confirmed → clip (Higgsfield Kling 3.0) ──
B["B19-BR2b"] = clip("B19-BR2b",
    "In a consulting room, a British surgeon of Pakistani heritage in navy scrubs and a grey fleece gilet sits behind a pale wood desk, "
    "pointing with one finger at the joint of a life-size anatomical knee model; a white British woman of sixty-nine with soft white hair "
    "in a navy-and-white striped T-shirt sits across from him, listening.",
    "Already explaining on the first frame: his finger traces once down the inside of the joint on the knee model, about two seconds, "
    "and she gives one small understanding nod. Both stay seated; the knee model stays still on the desk.",
    "no knee model moving, no model changing shape, no talking to the camera, no looking into the lens, no standing up, no third person, "
    "no camera movement, no extra fingers, no extra hands",
    3.0, hi=5,
    risks=[{"risk": "the knee model warps under his finger", "prevented_by": "one light trace, 'no knee model moving, no model changing shape'"},
           {"risk": "faces morph", "prevented_by": "small movements only, HOLD-C + NEG-WARP-C"},
           {"risk": "someone looks into the lens", "prevented_by": "'no looking into the lens'"}])
B["B19-BR2b"][0]["motion"] = B["B19-BR2b"][0]["motion"].replace("hair, fabric and straps lag and keep moving after the body stops", "hair and fabric lag a little")
START.update({"B19-BR2b": str(HERE.parent / "broll/B19-BR2b_v3.png")})

# ── 2026-10-01 "confirm": B19-BR v6 confirmed → clip (Higgsfield Kling 3.0). Product still: only steam and light move. ──
B["B19-BR"] = clip("B19-BR",
    "An open matte-black STRYDE box on a pale-oak kitchen table with a linen runner, its lid with the grey stryde wordmark resting at the "
    "back, two black STRYDE straps with chrome slides lying in the tray, a white mug of tea beside it, a sage-green kitchen behind.",
    "Already moving on the first frame: a thin wisp of steam rises slowly from the tea and drifts, about two seconds, and the soft "
    "daylight from the window shifts very slightly. The box, the lid and both straps do not move at all — rigid, keeping their exact "
    "shape, size and wordmarks.",
    "no box moving, no strap moving, no strap changing shape, no wordmark changing, no lid moving, no hands, no person, no camera "
    "movement, no zoom",
    3.0, hi=5,
    risks=[{"risk": "the straps or wordmarks morph", "prevented_by": "nothing in the box moves; rigid line; 'no strap changing shape, no wordmark changing'"},
           {"risk": "a hand appears", "prevented_by": "'no hands, no person'"},
           {"risk": "the camera drifts", "prevented_by": "locked-off tripod clause, 'no camera movement, no zoom'"}])
B["B19-BR"][0]["motion"] = B["B19-BR"][0]["motion"].replace("hair, fabric and straps lag and keep moving after the body stops", "the steam drifts softly; the straps never move")
START.update({"B19-BR": str(HERE.parent / "broll/B19-BR_v6.png"), "B20": str(HERE.parent / "broll/B20_v1.png"), "B22a": str(HERE.parent / "broll/B22a_v1.png"), "B22c": str(HERE.parent / "broll/B22c_v1.png")})

# ── 2026-10-01 B19b video Fix (gen 2): "not holding the banister because the knee with stryde is okay but in the knee without stryde
# is in pain her hand is on the wall" — frame fixed first (v5, confirmed); now the motion: strapped step easy, bare-knee step hurts. ──
B["B19b"] = clip("B19b",
    "A white British woman of sixty-nine with soft white hair, in a navy-and-white striped T-shirt and a mid-blue denim skirt, at the top "
    "of her carpeted stairs facing down towards the camera, NOT holding the banister, her hand on the right of the frame pressed flat on "
    "the duck-egg blue wall; a black STRYDE strap seated just below the kneecap of the leg on the left of the frame, the other knee bare.",
    "Already stepping on the first frame: she steps down one stair with the strapped leg, easy and sure, about a second; then, as her "
    "weight comes onto the bare knee for the next step, she winces a little, slows, and presses her hand harder against the wall to "
    "steady herself — about two seconds. Her other hand stays free, away from the banister. The strap stays exactly where it is — rigid, "
    "keeping its shape, size and wordmark.",
    "no hand on the banister, no grabbing the handrail, no falling, no stumbling, no strap moving, no strap on the bare knee, no second "
    "strap, no going up the stairs, no exaggerated pain, no looking into the lens, no camera movement, no extra legs, no extra hands",
    4.0, hi=5,
    risks=[{"risk": "her hand goes to the banister", "prevented_by": "hand pressed on the wall in the subject; 'no hand on the banister, no grabbing the handrail'"},
           {"risk": "the pain is overplayed or she falls", "prevented_by": "'winces a little, slows'; 'no falling, no stumbling, no exaggerated pain'"},
           {"risk": "the strap jumps to the bare knee", "prevented_by": "strap placed by leg; 'no strap on the bare knee, no second strap'"}])
B["B19b"][0]["motion"] = B["B19b"][0]["motion"].replace("hair, fabric and straps lag and keep moving after the body stops", "hair and fabric lag a little; the strap never moves")
START.update({"B19b": str(HERE.parent / "broll/B19b_v5.png")})

# ── 2026-10-01 B19-BR2 video Fix (gen 2): "walking up stair" — same frame (face CU on the stairs), the motion now climbs. ──
B["B19-BR2"] = clip("B19-BR2",
    "A close-up of a white British woman of sixty-nine with soft white hair, in a navy-and-white striped T-shirt, on her stairs, one hand "
    "on the honey oak handrail, three-quarter on, a small private smile.",
    "Already moving on the first frame: she walks UP her stairs, taking one easy step up at an unhurried pace, about a second and a "
    "half — her body rises a little in the frame, her hand slides up the oak handrail with her, and her small smile stays as she climbs, "
    "easy and sure. Her head stays inside the frame.",
    "no going down the stairs, no stumbling, no wincing, no head leaving the frame, no looking into the lens, no talking, no camera "
    "movement, no camera following her, no face morphing, no extra fingers, no extra hands",
    3.0, hi=5,
    risks=[{"risk": "her head rises out of a close frame", "prevented_by": "one step only, 'her head stays inside the frame'"},
           {"risk": "the camera follows her up", "prevented_by": "locked-off tripod clause, 'no camera following her'"},
           {"risk": "she goes down instead of up", "prevented_by": "'walks UP', 'no going down the stairs'"}])
B["B19-BR2"][0]["motion"] = B["B19-BR2"][0]["motion"].replace("hair, fabric and straps lag and keep moving after the body stops", "hair and fabric lag a little")

# ── 2026-10-01 B19b video Fix round 3 (user "go"): v2's free hand drifted onto the banister — give the free hand a job (resting on the
# bare thigh above the sore knee) and shorten to ONE bare-knee step, so there is no idle hand and no second step for it to wander in. ──
B["B19b"] = clip("B19b",
    "A white British woman of sixty-nine with soft white hair, in a navy-and-white striped T-shirt and a mid-blue denim skirt, at the top "
    "of her carpeted stairs facing down towards the camera; her hand on the right of the frame pressed flat on the duck-egg blue wall; "
    "a black STRYDE strap seated just below the kneecap of the leg on the left of the frame, the other knee bare.",
    "Already moving on the first frame: her free hand settles onto her bare thigh just above the bare knee and STAYS there, resting, the "
    "whole clip. She steps down one stair onto the bare knee, slowly and carefully, about two seconds — she winces a little as her "
    "weight lands, and leans her other hand harder into the wall. The banister stays untouched at the far edge of the frame. The strap "
    "stays exactly where it is — rigid, keeping its shape, size and wordmark.",
    "no hand on the banister, no hand leaving the thigh, no second step, no falling, no strap moving, no strap on the bare knee, no "
    "exaggerated pain, no feet warping, no shoe changing shape, no extra legs, no extra hands",
    3.0, hi=4,
    risks=[{"risk": "the free hand drifts onto the banister (v2's fault)", "prevented_by": "the free hand is given a job — resting on the bare thigh the whole clip; 'no hand on the banister, no hand leaving the thigh'"},
           {"risk": "feet and shoes warp over two steps (v2)", "prevented_by": "one step only, 4 s; 'no feet warping, no shoe changing shape'"},
           {"risk": "the pain is overplayed", "prevented_by": "'winces a little'; 'no exaggerated pain, no falling'"}])
B["B19b"][0]["motion"] = B["B19b"][0]["motion"].replace("hair, fabric and straps lag and keep moving after the body stops", "hair and fabric lag a little; the strap never moves")

# ── 2026-10-01 "fix and confirm": B20, B22a, B22c images confirmed → clips (Higgsfield Kling 3.0) ──
B["B20"] = clip("B20",
    "A premium 3D anatomical model of a knee seen from a little above and in front on a near-black field, a black STRYDE knee strap with "
    "two rounded peaks, chrome slides and a grey stryde wordmark seated across the front of the leg just below the kneecap.",
    "Already under load on the first frame: one step's load arrives — the knee flexes very slightly and a faint cool pearly pulse passes "
    "through the soft tissue around the strap and fades, about a second, the tendon beneath staying calm with no hot spot. The strap "
    "stays exactly where it is — rigid, its shape, peaks and wordmark unchanged; the kneecap stays uncovered above it.",
    "no strap moving, no strap sliding, no strap changing shape, no wordmark changing, no second strap, no hot spot, no red glow, no "
    "arrows, no text, no labels, no glow spreading down the shin, no second limb, no camera orbit, no zoom",
    3.0, hi=5,
    risks=[{"risk": "the strap warps or the wordmark smears", "prevented_by": "rigid-product line, 'no strap changing shape, no wordmark changing'"},
           {"risk": "a hot spot appears (the wrong message)", "prevented_by": "'tendon calm, no hot spot, no red glow'"},
           {"risk": "the glow spreads or text appears", "prevented_by": "'no glow spreading down the shin, no arrows, no text'"}])
B["B20"][0]["motion"] = B["B20"][0]["motion"].replace("hair, fabric and straps lag and keep moving after the body stops", "the strap never moves")
B["B22a"] = clip("B22a",
    "An open matte-black STRYDE box on a pale-oak kitchen table with a linen runner, two black STRYDE straps with chrome slides lying side "
    "by side in its tray; an older woman's two hands, navy-and-white striped cuffs, hold the box lid just above it.",
    "Already moving on the first frame: her hands lift the lid up and away out of the top of the frame in one smooth movement, about a "
    "second, revealing the two straps in the tray. The box and both straps do not move at all — rigid, keeping their exact shape, size "
    "and wordmarks.",
    "no straps moving, no strap changing shape, no wordmark changing, no box moving, no hands touching the straps, no third strap, no "
    "camera movement, no extra hands, no extra fingers",
    3.0, hi=5,
    risks=[{"risk": "the straps morph as the lid lifts", "prevented_by": "rigid line; 'no straps moving, no strap changing shape'"},
           {"risk": "a hand reaches into the tray", "prevented_by": "'no hands touching the straps'"},
           {"risk": "hands duplicate", "prevented_by": "one movement, HOLD-C + NEG-WARP-C, 'no extra hands'"}])
B["B22a"][0]["motion"] = B["B22a"][0]["motion"].replace("hair, fabric and straps lag and keep moving after the body stops", "the straps never move")
B["B22c"] = clip("B22c",
    "On a pale-oak kitchen table, two older hands with navy-and-white striped cuffs hold a cheap black knee strap by its two ends — a "
    "thin plastic shell with no wordmark and a flat nylon band.",
    "Already pulling on the first frame: the hands draw apart and the cheap nylon band stretches long and thin, then goes limp and slack "
    "as the hands ease back — one pull, about a second and a half. The cheap shell flexes; nothing snaps.",
    "no wordmark appearing, no chrome, no STRYDE strap, no band snapping, no extra hands, no extra fingers, no camera movement",
    3.0, hi=5,
    risks=[{"risk": "the copy gains a wordmark or becomes the hero", "prevented_by": "'no wordmark appearing, no chrome, no STRYDE strap'"},
           {"risk": "hands and band tangle", "prevented_by": "one pull at a countable pace, HOLD-C + NEG-WARP-C"},
           {"risk": "the band snaps (not the line)", "prevented_by": "'goes limp and slack', 'no band snapping'"}])
B["B22c"][0]["motion"] = B["B22c"][0]["motion"].replace("hair, fabric and straps lag and keep moving after the body stops", "the nylon band stretches and sags")

# ── 2026-10-01 "fix & confirm": B21 v2, B22-BR v2, B23b v2 images confirmed → clips (Higgsfield Kling 3.0) ──
START.update({"B21": str(HERE.parent / "broll/B21_v2.png"), "B22-BR": str(HERE.parent / "broll/B22-BR_v2.png"), "B23b": str(HERE.parent / "broll/B23b_v2.png")})
B["B21"] = clip("B21",
    "A Black British man of about seventy in a navy T-shirt, khaki shorts and white trainers on the lawn of his sunny back garden, a "
    "worn brown leather football at his feet, a black STRYDE knee strap with chrome slides seated just below his right kneecap.",
    "Already moving on the first frame: he swings his strapped right leg through and gives the ball one gentle side-foot tap, the ball "
    "rolling slowly away across the grass, then his foot settles back down beside the other — one easy kick, about a second and a half, "
    "his smile widening. The strap stays exactly where it is — rigid, keeping its shape, size and wordmark.",
    "no strap moving, no strap sliding, no strap changing shape, no hard kick, no ball flying up, no second ball, no stumbling, no second "
    "person, no extra legs, no feet warping, no shoe changing shape",
    3.0, hi=4,
    risks=[{"risk": "the strap slides or warps with the kick", "prevented_by": "a gentle side-foot tap, rigid line, 'no strap moving, no strap changing shape'"},
           {"risk": "the kick becomes violent and the ball flies off", "prevented_by": "'one gentle side-foot tap', 'rolling slowly', 'no hard kick, no ball flying up'"},
           {"risk": "legs and feet warp mid-swing", "prevented_by": "one movement, 4 s, HOLD-C + NEG-WARP-C, 'no extra legs, no feet warping'"}])
B["B21"][0]["motion"] = B["B21"][0]["motion"].replace("hair, fabric and straps lag and keep moving after the body stops", "fabric lags a little; the strap never moves")
B["B22-BR"] = clip("B22-BR",
    "A white British woman of sixty-nine with soft white hair, in a navy-and-white striped T-shirt, denim skirt and white plimsolls, "
    "walking along a sunny park path towards the camera, a black STRYDE knee strap seated just below her right kneecap.",
    "Already walking on the first frame: she takes two brisk, easy steps towards the camera at a comfortable walking pace, arms swinging "
    "naturally, her smile bright — about two seconds — and stays fully in frame. The strap stays exactly where it is — rigid, keeping its "
    "shape, size and wordmark.",
    "no strap moving, no strap sliding, no strap changing shape, no running, no limping, no camera moving with her, no second person, "
    "no extra legs, no feet warping, no shoe changing shape",
    3.0, hi=4,
    risks=[{"risk": "the camera travels with her (§27G)", "prevented_by": "locked-off camera, 'no camera moving with her'; two steps only"},
           {"risk": "the strap slides with the stride", "prevented_by": "rigid line, 'no strap moving, no strap sliding'"},
           {"risk": "legs and plimsolls warp in the stride", "prevented_by": "two steps at a counted pace, HOLD-C + NEG-WARP-C"}])
B["B22-BR"][0]["motion"] = B["B22-BR"][0]["motion"].replace("hair, fabric and straps lag and keep moving after the body stops", "hair and fabric lag a little; the strap never moves")
B["B23b"] = clip("B23b",
    "Seen from just behind her on the landing: a white British woman of sixty-nine with soft white hair, in a navy-and-white striped "
    "T-shirt, denim skirt and white plimsolls, standing at the top of her carpeted stairs, the flight going down ahead of her to a sunlit "
    "front door; her hands hang free at her sides.",
    "Already moving on the first frame: she steps forwards and down onto the first stair, facing down the stairs, then the second foot "
    "follows onto the next stair — two easy steps down, about two seconds, steady and unhurried, her hands staying free at her sides. "
    "She stays in frame.",
    "no hand on the banister, no hand on the handrail, no hand on the wall, no turning round, no face to camera, no stumbling, no "
    "camera following her down the stairs, no second person, no extra legs, no feet warping, no shoe changing shape",
    3.0, hi=4,
    risks=[{"risk": "a free hand drifts onto the banister (B19b's fault)", "prevented_by": "'her hands staying free at her sides', 'no hand on the banister, no hand on the handrail'"},
           {"risk": "the camera follows her down (§27G)", "prevented_by": "locked-off camera, 'no camera following her down the stairs'"},
           {"risk": "feet warp on the stairs", "prevented_by": "two steps at a counted pace, HOLD-C + NEG-WARP-C"}])
B["B23b"][0]["motion"] = B["B23b"][0]["motion"].replace("hair, fabric and straps lag and keep moving after the body stops", "hair and fabric lag a little")

# ── 2026-10-01 user "GO": B19b video gen 4 (Fix "DON'T HOLD THE STAIR RAILING") and B19-BR2 video gen 3 (v6 confirmed). Both start from
# frames where both hands already have a job (one flat on the wall, one resting on the bare thigh) — the clip keeps BOTH hands exactly
# where they are and is one calm step, no wince (the lean into the wall was what moved the hands before). ──
START.update({"B19b": str(HERE.parent / "broll/B19b_v7.png"), "B19-BR2": str(HERE.parent / "broll/B19-BR2_v6.png")})
B["B19b"] = clip("B19b",
    "A white British woman of sixty-nine with soft white hair, in a navy-and-white striped T-shirt and a mid-blue denim skirt, at the top "
    "of her carpeted stairs facing down towards the camera; her hand on the right of the frame pressed flat on the duck-egg blue wall, "
    "her other hand resting on her bare thigh; a black STRYDE strap seated just below the kneecap of the leg on the left of the frame, "
    "the other knee bare.",
    "Already moving on the first frame: she steps down one stair, calm and steady, about a second and a half, facing forwards. BOTH "
    "hands stay exactly where they are the whole clip — one flat on the wall, one resting on her thigh; neither hand moves. The banister "
    "stays untouched at the far edge of the frame. The strap stays exactly where it is — rigid, keeping its shape, size and wordmark.",
    "no hand on the banister, no hand on the handrail, no hand reaching across, no hand leaving the wall, no hand leaving the thigh, no "
    "second step, no wincing, no falling, no strap moving, no strap on the bare knee, no feet warping, no shoe changing shape, no extra "
    "legs, no extra hands",
    3.0, hi=4,
    risks=[{"risk": "a hand goes to the banister (v2, v3)", "prevented_by": "both hands given a job in the start frame (wall + thigh) and told not to move; no wince/lean (the lean moved the hands); 'no hand on the banister, no hand reaching across'"},
           {"risk": "feet warp", "prevented_by": "one step only, 4 s"},
           {"risk": "the strap slides", "prevented_by": "rigid line, 'no strap moving'"}])
B["B19b"][0]["motion"] = B["B19b"][0]["motion"].replace("hair, fabric and straps lag and keep moving after the body stops", "hair and fabric lag a little; the strap never moves")
B["B19-BR2"] = clip("B19-BR2",
    "A white British woman of sixty-nine with soft white hair, in a navy-and-white striped T-shirt and a mid-blue denim skirt, partway "
    "down her carpeted stairs facing the camera; her hand on the right of the frame flat on the duck-egg blue wall, her other hand "
    "resting on her thigh; a black STRYDE strap seated just below the kneecap of the leg on the left of the frame, the other knee bare.",
    "Already moving on the first frame: she steps down one more stair, easy and sure, about a second and a half, and as her weight "
    "lands a quiet look of surprise softens into a small smile — she has noticed her knee. BOTH hands stay exactly where they are the "
    "whole clip; neither hand moves. Her head stays inside the frame. The strap stays exactly where it is — rigid, keeping its shape, "
    "size and wordmark.",
    "no hand on the banister, no hand reaching across, no going up the stairs, no second step, no head leaving the frame, no looking "
    "into the lens, no broad grin, no strap moving, no extra hands",
    3.0, hi=4,
    risks=[{"risk": "a hand goes to the banister", "prevented_by": "both hands given a job in the frame and told not to move"},
           {"risk": "her head leaves the frame (v2)", "prevented_by": "going down, not up; 'her head stays inside the frame'"},
           {"risk": "the smile overplays", "prevented_by": "'a small smile', 'no broad grin'"}])
B["B19-BR2"][0]["motion"] = B["B19-BR2"][0]["motion"].replace("hair, fabric and straps lag and keep moving after the body stops", "hair and fabric lag a little; the strap never moves")

# ── 2026-10-01 images B18b v4, B21-BR v3, B22a v2, B23a v3 confirmed → clips (Higgsfield Kling 3.0) ──
START.update({"B18b": str(HERE.parent / "broll/B18b_v4.png"), "B21-BR": str(HERE.parent / "broll/B21-BR_v3.png"),
              "B22a": str(HERE.parent / "broll/B22a_v2.png"), "B23a": str(HERE.parent / "broll/B23a_v3.png")})
B["B18b"] = clip("B18b",
    "Seen from the foot of the stairs: a white British woman of sixty-nine with soft white hair, in a sage-green cardigan, white T-shirt, "
    "denim skirt and white plimsolls, coming down her carpeted stairs facing the camera, a black STRYDE strap just below EACH kneecap, "
    "both arms down at her sides, hands empty, a bright easy smile.",
    "Already moving on the first frame: she steps down one stair towards the camera, light and easy, about a second and a half, her "
    "bright smile staying. Both arms stay down at her sides, hands open and empty, the whole clip — neither hand touches the handrail, "
    "the wall or her clothes. Both straps stay exactly where they are — rigid, keeping their shape, size and wordmarks.",
    "no hand on the banister, no hand on the handrail, no hand on the wall, no hand on her skirt, nothing in her hands, no second step, "
    "no wincing, no stumbling, no strap moving, no third strap, no feet warping, no shoe changing shape, no extra legs, no extra hands",
    3.0, hi=4,
    risks=[{"risk": "a hand goes to the handrail", "prevented_by": "'both arms stay down at her sides, hands open and empty, the whole clip', 'no hand on the banister, no hand on the handrail'"},
           {"risk": "a strap slides or a third appears", "prevented_by": "rigid line, 'no strap moving, no third strap'"},
           {"risk": "feet warp on the step", "prevented_by": "one step only, 4 s"}])
B["B18b"][0]["motion"] = B["B18b"][0]["motion"].replace("hair, fabric and straps lag and keep moving after the body stops", "hair and fabric lag a little; the straps never move")
B["B21-BR"] = clip("B21-BR",
    "A premium 3D anatomical model of a bare knee seen from the front on a near-black field: the kneecap and joint line ringed by a soft "
    "cool blue glow, the patellar tendon just below glowing hot red-orange.",
    "Already pulsing on the first frame: the red-orange glow on the tendon brightens once and eases back, about a second, the load "
    "landing there; the cool blue ring around the joint stays steady and calm. The anatomy itself does not move.",
    "no strap, no brace, no product, no text, no labels, no arrows, no glow spreading to the shin, no blue moving onto the tendon, no "
    "anatomy moving, no camera orbit, no zoom, no second knee",
    3.0, hi=5,
    risks=[{"risk": "the glows swap or spread", "prevented_by": "'the blue ring stays steady', 'no glow spreading to the shin, no blue moving onto the tendon'"},
           {"risk": "a strap or text appears", "prevented_by": "'no strap, no brace, no product, no text, no labels, no arrows'"},
           {"risk": "the model morphs", "prevented_by": "'the anatomy itself does not move', NEG-WARP-C"}])
B["B21-BR"][0]["motion"] = B["B21-BR"][0]["motion"].replace("hair, fabric and straps lag and keep moving after the body stops", "only the glow changes")
B["B22a"] = clip("B22a",
    "Low and close, straight on: an older woman's two bare knees side by side on a carpeted stair, a black STRYDE strap with chrome "
    "slides seated just below EACH kneecap, her denim skirt hem above, white plimsolls below.",
    "Already moving on the first frame: she shifts her weight gently from one leg to the other, one small easy shift, about a second — "
    "the knees ease a little as the weight moves. Both straps stay exactly where they are — rigid, keeping their shape, size and "
    "wordmarks.",
    "no strap moving, no strap sliding, no strap changing shape, no wordmark changing, no third strap, no stepping, no feet lifting, no "
    "hands, no extra legs, no extra knees, no feet warping",
    3.0, hi=4,
    risks=[{"risk": "the straps slide or the wordmarks smear", "prevented_by": "a small weight shift only, rigid line, 'no wordmark changing'"},
           {"risk": "the legs warp in a close frame", "prevented_by": "no step, one small shift, HOLD-C + NEG-WARP-C"},
           {"risk": "a third strap or extra knee", "prevented_by": "'no third strap, no extra knees'"}])
B["B22a"][0]["motion"] = B["B22a"][0]["motion"].replace("hair, fabric and straps lag and keep moving after the body stops", "the skirt hem lags a little; the straps never move")
B["B23a"] = clip("B23a",
    "Low and close on an older woman's legs on her carpeted stairs: a black STRYDE strap seated just below the kneecap of the leg on the "
    "left of the frame, the other knee bare, her denim skirt hem above, white plimsolls, one foot reaching down towards the next stair.",
    "Already moving on the first frame: the reaching foot lands softly on the edge of the next stair and the weight settles onto it, one "
    "step, about a second, steady and sure. The strap stays exactly where it is — rigid, keeping its shape, size and wordmark.",
    "no strap moving, no strap on the bare knee, no second strap, no second step, no slipping, no hand, no face, no feet warping, no shoe "
    "changing shape, no extra legs, no extra feet",
    3.0, hi=4,
    risks=[{"risk": "the foot warps on landing", "prevented_by": "one step at a counted pace, 'no feet warping, no shoe changing shape'"},
           {"risk": "the strap jumps legs", "prevented_by": "'no strap on the bare knee, no second strap'"},
           {"risk": "a slip (wrong message)", "prevented_by": "'lands softly', 'steady and sure', 'no slipping'"}])
B["B23a"][0]["motion"] = B["B23a"][0]["motion"].replace("hair, fabric and straps lag and keep moving after the body stops", "the skirt hem lags a little; the strap never moves")

# ── 2026-10-01 video Fixes (user "GO"): B21 "WILL KICK THEN JUMPING KEEP MOVING" (gen 2); B22a "WALKING DOWN STAIR" (gen 3, user GO);
# B23a "WALKING DOWN STAIR" (gen 2). Same confirmed frames; the motion now carries on. Fixed geography (HT22): she faces down the
# stairs towards the camera and only ever comes down, never turning. ──
B["B21"] = clip("B21",
    "A Black British man of about seventy in a navy T-shirt, khaki shorts and white trainers on the lawn of his sunny back garden, a "
    "worn brown leather football at his feet, a black STRYDE knee strap with chrome slides seated just below his right kneecap.",
    "Already moving on the first frame: he kicks the ball with his strapped right leg, a crisp easy kick, and straight away gives a "
    "small happy hop off both feet and keeps moving — jogging lightly after the ball across the grass, about three seconds, full of "
    "energy, grinning. He stays in frame. The strap stays exactly where it is — rigid, keeping its shape, size and wordmark.",
    "no strap moving, no strap sliding, no strap changing shape, no stumbling, no falling, no wincing, no second ball, no ball flying "
    "up out of frame, no camera following him, no second person, no extra legs, no feet warping, no shoe changing shape",
    4.0, hi=5,
    risks=[{"risk": "he leaves frame chasing the ball (v1 ended with the ball gone)", "prevented_by": "'he stays in frame', a light jog, 'no camera following him'"},
           {"risk": "the strap slides on the hop", "prevented_by": "rigid line, 'no strap moving, no strap sliding'"},
           {"risk": "legs warp mid-jump", "prevented_by": "one small hop, HOLD-C + NEG-WARP-C"}])
B["B21"][0]["motion"] = B["B21"][0]["motion"].replace("hair, fabric and straps lag and keep moving after the body stops", "fabric lags a little; the strap never moves").replace("One small movement, completing inside the clip", "One continuous action, completing inside the clip")
B["B22a"] = clip("B22a",
    "Low and close, straight on: an older woman's two bare legs on a carpeted staircase, facing down the stairs towards the camera, a "
    "black STRYDE strap with chrome slides seated just below EACH kneecap, her denim skirt hem above, white plimsolls below.",
    "Already walking on the first frame: she walks down the stairs towards the camera, two easy steps down, one foot then the other, "
    "about two seconds, steady and sure — her legs coming a little closer. She only ever comes down, facing the camera, never turning. "
    "Both straps stay exactly where they are — rigid, keeping their shape, size and wordmarks.",
    "no strap moving, no strap sliding, no wordmark changing, no third strap, no going up the stairs, no turning round, no hands, no "
    "hand at the edge of the frame, no camera following her, no extra legs, no extra knees, no feet warping, no shoe changing shape",
    3.0, hi=4,
    risks=[{"risk": "a hand edges into the corner (v2)", "prevented_by": "'no hands, no hand at the edge of the frame'"},
           {"risk": "the straps slide or smear as she steps", "prevented_by": "rigid line, 'no strap moving, no wordmark changing'"},
           {"risk": "she turns or goes up", "prevented_by": "fixed geography: facing down the stairs towards the camera, 'only ever comes down', 'no going up the stairs, no turning round'"}])
B["B22a"][0]["motion"] = B["B22a"][0]["motion"].replace("hair, fabric and straps lag and keep moving after the body stops", "the skirt hem lags a little; the straps never move")
B["B23a"] = clip("B23a",
    "Low and close on an older woman's legs on her carpeted staircase, facing down the stairs towards the camera: a black STRYDE strap "
    "seated just below the kneecap of the leg on the left of the frame, the other knee bare, her denim skirt hem above, white plimsolls.",
    "Already walking on the first frame: she walks down the stairs towards the camera, two easy steps down, one foot then the other, "
    "about two seconds, steady and sure. She only ever comes down, facing the camera, never turning. The strap stays exactly where it is "
    "— rigid, keeping its shape, size and wordmark, the same from first frame to last.",
    "no strap moving, no strap changing shape, no strap on the bare knee, no second strap, no going up the stairs, no turning round, no "
    "slipping, no hands, no hand at the edge of the frame, no camera following her, no extra legs, no extra feet, no feet warping",
    3.0, hi=4,
    risks=[{"risk": "the strap changes shape (v1, last second)", "prevented_by": "'the same from first frame to last', 'no strap changing shape'"},
           {"risk": "a hand edges into the corner (v1)", "prevented_by": "'no hands, no hand at the edge of the frame'"},
           {"risk": "she turns or goes up", "prevented_by": "fixed geography, 'only ever comes down', 'no going up the stairs, no turning round'"}])
B["B23a"][0]["motion"] = B["B23a"][0]["motion"].replace("hair, fabric and straps lag and keep moving after the body stops", "the skirt hem lags a little; the strap never moves")

# ── 2026-10-01 B23b v3 confirmed (strap added from behind, Fix "PUT STRYDE PRODUCT") → clip gen 2. ──
START.update({"B23b": str(HERE.parent / "broll/B23b_v3.png")})
B["B23b"] = clip("B23b",
    "Seen from just behind her on the landing: a white British woman of sixty-nine with soft white hair, in a navy-and-white striped "
    "T-shirt, denim skirt and white plimsolls, standing at the top of her carpeted stairs, the flight going down ahead of her to a sunlit "
    "front door; a black STRYDE strap's band round her right leg just below the knee; her hands hang free at her sides.",
    "Already moving on the first frame: she steps forwards and down onto the first stair, facing down the stairs, then the second foot "
    "follows onto the next stair — two easy steps down, about two seconds, steady and unhurried, her hands staying free at her sides. "
    "She only ever goes down, facing away from the camera, never turning. She stays in frame. The strap stays exactly where it is on "
    "her right leg — rigid band, the same from first frame to last.",
    "no hand on the banister, no hand on the handrail, no hand on the wall, no turning round, no face to camera, no stumbling, no "
    "strap moving, no strap on the left leg, no second strap, no camera following her, no extra legs, no feet warping",
    3.0, hi=4,
    risks=[{"risk": "the strap slides or jumps legs", "prevented_by": "'the same from first frame to last', 'no strap on the left leg'"},
           {"risk": "a free hand drifts onto the banister", "prevented_by": "'her hands staying free at her sides', 'no hand on the banister'"},
           {"risk": "the camera follows her down (§27G)", "prevented_by": "locked-off camera, 'no camera following her'"}])
B["B23b"][0]["motion"] = B["B23b"][0]["motion"].replace("hair, fabric and straps lag and keep moving after the body stops", "hair and fabric lag a little; the strap never moves")

# ── 2026-10-01 user "GO": B22a v4 (gen 4) and B23a v6 (gen 3) images confirmed — both carry the approved real-photo strap. The motion
# keeps the user's earlier Fix "WALKING DOWN STAIR"; the straps must not change from the first frame. ──
START.update({"B22a": str(HERE.parent / "broll/B22a_v4.png"), "B23a": str(HERE.parent / "broll/B23a_v6.png")})
B["B22a"] = clip("B22a",
    "Low and close, straight on: an older woman's two pale legs on her carpeted staircase, facing down the stairs towards the camera, a "
    "black STRYDE strap seated just below EACH kneecap — pointed peaks, the kneecap seated in the notch, chrome slides, the grey "
    "lowercase stryde wordmark — her denim skirt hem above, white plimsolls below.",
    "Already walking on the first frame: she walks down the stairs towards the camera, one easy step down with one foot, then the "
    "other, about two seconds, steady and sure, starting straight away. She only ever comes down, facing the camera, never turning. "
    "Both straps stay exactly as they are — rigid, the same shape, size and wordmark from first frame to last.",
    "no standing still, no strap moving, no strap changing shape, no wordmark changing, no third strap, no going up the stairs, no "
    "turning round, no hands, no hand at the edge of the frame, no camera following her, no extra legs, no feet warping",
    3.0, hi=4,
    risks=[{"risk": "she stands still most of the clip (v3)", "prevented_by": "'starting straight away', 'no standing still'"},
           {"risk": "the approved straps get redrawn", "prevented_by": "rigid line, 'the same shape, size and wordmark from first frame to last'"},
           {"risk": "a hand edges into the corner", "prevented_by": "'no hands, no hand at the edge of the frame'"}])
B["B22a"][0]["motion"] = B["B22a"][0]["motion"].replace("hair, fabric and straps lag and keep moving after the body stops", "the skirt hem lags a little; the straps never move")
B["B23a"] = clip("B23a",
    "Close on an older woman's pale strapped leg on her carpeted staircase, facing down the stairs towards the camera, a black STRYDE "
    "strap seated just below the kneecap — pointed peaks, the kneecap seated in the notch, chrome slides, the grey lowercase stryde "
    "wordmark; her other leg stepping down to the stair below; denim skirt hem above, white plimsolls.",
    "Already moving on the first frame: the stepping foot lands softly on the stair below and the weight moves onto it, then the "
    "strapped leg follows down one stair, steady and sure, about two seconds. She only ever comes down, facing the camera, never "
    "turning. The strap stays exactly as it is — rigid, the same shape, size and wordmark from first frame to last.",
    "no strap moving, no strap changing shape, no wordmark changing, no second strap, no going up the stairs, no turning round, no "
    "slipping, no hands, no hand at the edge of the frame, no camera following her, no extra legs, no feet warping",
    3.0, hi=4,
    risks=[{"risk": "the approved strap gets redrawn as the leg moves", "prevented_by": "rigid line, 'from first frame to last'"},
           {"risk": "a hand edges into the corner (v1, v2)", "prevented_by": "'no hands, no hand at the edge of the frame'"},
           {"risk": "a second strap appears on the stepping leg", "prevented_by": "'no second strap'"}])
B["B23a"][0]["motion"] = B["B23a"][0]["motion"].replace("hair, fabric and straps lag and keep moving after the body stops", "the skirt hem lags a little; the strap never moves")

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
