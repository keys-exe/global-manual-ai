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

# B14b image v2 (user Fix 'too big, fix size', then 'confirm'): the strap upright in her one hand, the grey pad to the lens. One small
# tilt through the window light — the pad stays to the lens, so no pinned end frame (act map pin 'no').
B["B14b"] = clip("B14b",
    "An older woman's hand holding a small black knee strap upright, its inside turned to the lens: a grey grooved pad with one smooth "
    "comma-shaped ridge inside a thin black rim, a chrome slide at each end, a pale kitchen soft behind.",
    "Already on the first frame: her wrist turns the strap a few degrees to one side and back, slowly, over about two seconds, so the "
    "window light slides across the grooves and the ridge of the pad; the pad stays facing the lens the whole time and the strap keeps "
    "its size and shape.",
    "no strap turning round, no front of the shell showing, no wordmark, no strap changing size, no pad changing shape, no ridge moving, "
    "no second hand, no extra fingers, no strap dropped",
    4.0, hi=5,
    risks=[{"risk": "the pad pattern swims as it tilts", "prevented_by": "a few degrees only, 'no pad changing shape, no ridge moving', HOLD-C"},
           {"risk": "the strap turns right round to its front", "prevented_by": "'the pad stays facing the lens', 'no strap turning round, no front of the shell showing'"},
           {"risk": "the strap grows in the hand (the Fix was size)", "prevented_by": "'keeps its size and shape', 'no strap changing size'"}])

# B14c image v3 (user Fix 'FIX SIZE BIGGER', then 'GO'): ANAT front-on, the real strap seated below the kneecap spanning the leg.
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

START = {"B14c": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_163337_ba5e6993-4e59-4bf8-8ec8-9aeb85e5a9de.png",
         "B14a": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_164241_ab6052f5-7c35-44e1-8052-a67bfedf24f7.png",
         "B14b": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_160315_ab4a6700-d742-40b1-8b0d-6eb4c68382da.png",
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
