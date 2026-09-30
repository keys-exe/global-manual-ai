#!/usr/bin/env python3
"""stryde-what-changed — step 5 act map (E4): three hooks + one shared body, one source of truth.

Writes:
  work/actmap_rows.json        every beat, E4 fields (+ §27G motion, §30I angle, §30J focus, §30K light, EG layout)
  work/angles_HK<n>.json       each finished variant's cut order (hook + body) for scripts/angles.py
  work/actmap.md               the act-map tables (STEP4_5.md, docs/actmap)
Durations stay `pending-master` (E6) until the VO take exists.
Talking-head rows (TH) are the host on the podcast set (HeyGen, one untrimmed take, cut per line in the edit;
EG01: wide ↔ 1.25× punch-in). They are listed for the cut order; angles.py skips them.
"""
import json, pathlib
HERE = pathlib.Path(__file__).parent

HOOK = {1: "Hook 1", 2: "Hook 2", 3: "Hook 3"}
A1, A2, A3, A4 = "Act 1", "Act 2", "Act 3", "Act 4"   # why it happens · the costly mistake · the product · proof, test, offer

ROWS = {}
def B(beat, act, line, key, fn, subj, loc, day, framing, action, pace, camera, staging, pin, prod, vis, model,
      h, side, fg, scale, why, plane, dof, src, ks, time, arc, kelvin, face, ledger="", notes="", layout="full", eg="", mx=6):
    ROWS[beat] = dict(beat=beat, type="BR", act=act, line=line, key=key, function=fn, subject=subj, location=loc, story_day=day,
        framing=framing, action=action, pace=pace, camera=camera, staging=staging, pin_end=pin, max=mx,
        product=prod, visibility=vis, model=model, layout=layout, eg=eg, ledger=ledger, notes=notes,
        duration="pending-master",
        angle=dict(height=h, side=side, fg=fg, scale=scale, why=why),
        focus=dict(plane=plane, dof=dof, rack=None, moving_subject=False),
        light=dict(source=src, key_side=ks, time=time, arc=arc, kelvin=kelvin), face=face)

def TH(beat, act, line, framing="wide", eg="EG01"):
    ROWS[beat] = dict(beat=beat, type="TH", act=act, line=line, key="", function="talking head", subject="H", location="L-STUDIO",
        story_day="H-D1", framing=framing, layout="full", eg=eg, duration="pending-master", model="HeyGen Avatar V",
        notes="cut from the one HeyGen take; " + ("1.25× punch-in in the edit" if framing == "punch" else "wide seated framing"))

EYE, LOW, HIGH, GROUND, OVER = "eye", "low", "high", "ground", "overhead"
FRO, THR, PRO, BEH, TQB = "front", "three-quarter", "profile", "behind", "three-quarter-back"
STILL, SWAY = "locked off", "sway (handheld, does not travel)"
# light sources, one Kelvin each (§30K/§30L)
M_GREY = ("Maureen's landing window, grey morning", "morning", "problem: grey", 6500)
M_SUN = ("Maureen's front-door glass, afternoon sun", "afternoon", "after: sun", 5600)
D_GREY = ("Desmond's stair window, grey morning", "morning", "problem: grey", 6500)
D_SUN = ("Desmond's front-door glass, afternoon sun", "afternoon", "after: sun", 5600)
STREET_AM = ("open overcast sky, morning", "morning", "problem: grey", 6500)
STREET_PM = ("open sky, afternoon sun", "afternoon", "after: sun", 5600)
KITCH = ("kitchen window over the sink", "morning", "everyday: cool daylight", 6500)
CONS = ("consulting-room blind window", "afternoon", "authority: even daylight", 5600)
ANAT = ("anatomical register (§12A)", "midday", "mechanism", 5600)

def L(src_tuple, ks):
    s, t, a, k = src_tuple
    return dict(src=s, ks=ks, time=t, arc=a, kelvin=k)

def BB(beat, act, line, key, fn, subj, loc, day, framing, action, pace, camera, staging, pin, prod, vis, model,
       h, side, fg, scale, why, plane, dof, light, face, **kw):
    B(beat, act, line, key, fn, subj, loc, day, framing, action, pace, camera, staging, pin, prod, vis, model,
      h, side, fg, scale, why, plane, dof, light["src"], light["ks"], light["time"], light["arc"], light["kelvin"], face, **kw)

# ============================================================ HOOKS (VN01: line 1 as VO over full-screen B-roll, the host on camera for the last line)
BB("HK1-a", HOOK[1], "Your knees have been taking seventeen times your bodyweight on every step", "step", "hook — the hidden number (VN01, EG03)",
   "R1", "L-M-STAIRS", "M-D1", "ECU her feet and bare right knee from the side, coming down one stair", "one step down onto the next stair, weight onto the right leg",
   "one step, about a second and a half", STILL, "stairs: side, waist-down, camera still, hand on the rail visible", "no", "absent", "—", "NB2",
   GROUND, PRO, "through", "CU", "ground through the spindles = steps and knees, watched", "foreground", "medium", L(M_GREY, "L"), False,
   ledger="VN01", eg="EG03 full screen · EG04 caption red box 'seventeen times'")
BB("HK1-b", HOOK[1], "for forty years, and you never felt a thing.", "never", "hook — the hidden number (VN01)",
   "ANAT", "—", "—", "ANAT-A: the knee in profile, a soft pulse of load arriving at the spot just below the kneecap with each step", "one pulse per step",
   "one pulse a second", STILL, "none", "no", "absent", "—", "NB2",
   EYE, PRO, "clean", "CU", "profile shows the load path down the leg", "deep", "deep", L(ANAT, "L"), False, ledger="VN01", eg="EG05 anatomy")
TH("HK1-TH", HOOK[1], "Here is what changed.")

BB("HK2-a", HOOK[2], "There is a band under your kneecap about as wide as your thumb,", "band", "hook — the flattering fact (VN01)",
   "ANAT", "—", "—", "ANAT-A ECU: the patellar tendon laid out as one thick satin band from the lower edge of the kneecap to the top of the shin, the glow one tight spot at its top", "the band draws taut once under load",
   "one tightening, about two seconds", STILL, "none", "no", "absent", "—", "NB2",
   HIGH, THR, "clean", "ECU", "high three-quarter = the band laid out along its length", "deep", "deep", L(ANAT, "R"), False,
   ledger="VN01 · F2", eg="EG03 · EG05",
   notes="user Fixes 2026-09-29: 'GIVE ME DIFFERENT BROLL' then 'I WANT ANATOMY B ROLL HERE' — anatomy, but a band not HK1-b's spot; no thumb shown (F2)")
BB("HK2-b", HOOK[2], "and for its size it is one of the strongest things in your body.", "strongest", "hook — the flattering fact (VN01)",
   "R2", "L-D-STAIRS", "D-D1", "MS side-on, waist-down: Desmond lifting a heavy box off his hall floor from a deep squat, knees taking the load", "one lift up out of the squat",
   "one lift, about two seconds", STILL, "hall floor by the foot of the stairs, cropped at the waist, side-on, camera still", "no", "absent", "—", "NB2",
   LOW, PRO, "clean", "MS", "low profile = the bent knee and the load read at once", "foreground", "medium", L(D_GREY, "L"), False, ledger="VN01",
   notes="user Fixes 2026-09-29 'GIVE ME DIFFERENT BROLL HERE' (was one step up onto the stair), 'FIX THIS', 'FIX THE BROLL' (face kept creeping in front-on → side-on, waist-down)")
TH("HK2-TH", HOOK[2], "It is so good at its job that nobody ever thinks to check it. Not even the person who read your scan.")

BB("HK3-a", HOOK[3], "Five thousand steps a day. Forty years.", "Five", "hook — the arithmetic (VN01)",
   "R1", "L-STREET", "M-D1", "ground-level: Maureen's feet walking along the pavement towards the lens", "three walking steps towards the lens",
   "one step per second, normal walking speed", STILL, "walking toward camera: feet/knee only, 3 steps", "no", "absent", "—", "NB2",
   GROUND, FRO, "clean", "CU", "ground = steps", "deep", "deep", L(STREET_AM, "L"), False, ledger="VN01", eg="EG03 · captions '5,000 a day' '40 years'")
BB("HK3-b", HOOK[3], "That is about seventy million times your full bodyweight has gone through one spot below your kneecap.", "seventy", "hook — the arithmetic (VN01, F4)",
   "ANAT", "—", "—", "ANAT-A: low front three-quarter, the knee bent mid-step as the foot lands, the one spot below the kneecap burning brighter with each landing", "the spot flares with each landing",
   "one landing a second", STILL, "none", "no", "absent", "—", "NB2",
   LOW, THR, "clean", "CU", "low = the weight coming down onto the one spot", "deep", "deep", L(ANAT, "R"), False, ledger="VN01 · F4",
   eg="EG05 · '70,000,000' overlay (post)",
   notes="user Fixes 2026-09-29: 'GIVE ME BETTER DIFFERENT BROLL' (whole leg) → worn stairs → 'ANATOMY BROLL HERE'; a fourth anatomy look: low, knee bent under a landing (HK1-b profile, HK2-a band ECU are the others)")
TH("HK3-TH", HOOK[3], "Here is what happens when that spot stops being able to take it.")

# ============================================================ ACT 1 — why it happens (shared body)
BB("B01a", A1, "That band is the patellar tendon.", "tendon", "anatomy",
   "ANAT", "—", "—", "ANAT-A: the knee three-quarter front, the patellar tendon traced from the kneecap down to the shin", "the tendon lights from top to bottom",
   "one trace, about two seconds", STILL, "none", "no", "absent", "—", "NB2",
   EYE, THR, "clean", "CU", "", "deep", "deep", L(ANAT, "L"), False, eg="EG05")
BB("B01b", A1, "It sits two centimetres below your kneecap, on the front of the joint,", "centimetres", "where it is",
   "R2", "L-D-STAIRS", "D-D1", "ECU from the front: Desmond standing in his hall, his bare right knee straight, the band of the tendon standing out as a ridge under the skin just below the kneecap", "the knee straightens a touch, the ridge firms",
   "one small straighten, about a second", STILL, "hall: knee only, from the front, camera still", "no", "absent", "—", "NB2",
   EYE, FRO, "clean", "ECU", "front = the spot shown straight on", "foreground", "medium", L(D_GREY, "L"), False,
   notes="user 2026-09-29 'PUT DIFFERENT BROLLS HERE' — line split in two (was Desmond stepping down, side-on)")
BB("B01c", A1, "and every step you take lands on it.", "step", "every step lands on it",
   "R1", "L-STREET", "M-D1", "ground level, side-on: Maureen's plimsoll steps down off the kerb and lands on the road, the knee taking it", "one step down off the kerb",
   "one step, about a second", STILL, "street: feet and shins only, camera still at ground level", "no", "absent", "—", "NB2",
   GROUND, PRO, "clean", "CU", "ground level = the step landing", "foreground", "medium", L(STREET_AM, "L"), False,
   notes="user 2026-09-29 'PUT DIFFERENT BROLLS HERE' — second half of the B01b line")
TH("B01-TH", A1, "Put your finger there now and press.", framing="punch")
BB("B02", A1, "That is the one.", "one", "participation",
   "R1", "L-M-STAIRS", "M-D1", "CU front-on: seated on her bottom stair, the front of her bare right knee square to the lens, her fingertip on the tendon straight below the kneecap", "her fingertip presses in once and holds",
   "one press, about a second", STILL, "hands: large in frame, one movement", "no", "absent", "—", "NB2",
   EYE, FRO, "clean", "CU", "front-on = the tendon below the kneecap shown straight on", "hands", "shallow", L(M_GREY, "R"), False)
TH("B03-TH", A1, "It is not a big thing. It is about as wide as your thumb, and it has been quietly taking your whole bodyweight, multiplied, since you were a teenager.")
BB("B04a", A1, "Going up the stairs, your muscles lift you.", "up", "the climb is hard work (problem state)",
   "R2", "L-D-STAIRS", "D-D1", "MEDIUM three-quarter on the stairs: Desmond struggling up, one hand gripping the handrail, the other pushing down on his thigh to lever himself up the next step, his face set with effort", "he levers himself up one step",
   "one slow, effortful step, about two seconds", STILL, "stairs: three-quarter from the hall, full figure from head to the treads below, camera still", "no", "absent", "—", "NB2",
   EYE, THR, "clean", "MEDIUM", "three-quarter = his effort and his face together", "deep", "deep", L(D_GREY, "R"), True,
   notes="user Fix 2026-09-29 'NEGATIVE BROLL, STRUGGLING TO Going up the stairs.' (was from behind, climbing easily)")
BB("B04b", A1, "Going down, nothing lifts you. You are catching yourself on every step,", "catching", "the careful descent",
   "R1", "L-M-STAIRS", "M-D1", "MEDIUM from the lower stairs looking up: Maureen near the top of her flight coming down, gripping the oak handrail, her other hand braced on the wall, struggling a little", "one careful step down, holding the rail",
   "one careful step, about two seconds", STILL, "stairs: from the foot of the flight looking up, camera still", "no", "absent", "—", "NB2",
   LOW, FRO, "clean", "MEDIUM", "low front = her coming down to us, every step a catch", "deep", "deep", L(M_GREY, "L"), True,
   notes="user Fix 2026-09-29 'GOING DOWN WHILE HOLDING THE BANISTER, CHANGE THE BROLL' (was Desmond stepping down through the spindles)")
BB("B04c", A1, "so coming down puts more through that band than going up does.", "more", "mechanism (F5)",
   "ANAT", "—", "—", "ANAT-C: the silhouette figure, waist-down, walking down a short flight of steps, the leading foot landing, the spot glowing", "one landing pulse, stronger than the last",
   "one pulse, about a second", STILL, "none", "no", "absent", "—", "NB2",
   HIGH, THR, "clean", "MEDIUM", "high = the drop onto the step", "deep", "deep", L(ANAT, "R"), False, ledger="F5", eg="EG05")
BB("B05", A1, "And inside the joint there is a layer of cartilage doing the absorbing. And over the years that layer thins.", "thins", "anatomy — cartilage",
   "ANAT", "—", "—", "ANAT-A: the joint cut away, the pale cartilage layer between the bones slowly thinning", "the cartilage thins by a fraction",
   "one slow change over four seconds", STILL, "none", "no", "absent", "—", "NB2",
   EYE, PRO, "clean", "CU", "profile: the layer seen edge-on", "deep", "deep", L(ANAT, "L"), False, eg="EG05")
TH("B06-TH", A1, "That part is ordinary. It happens to everybody. But here is what nobody explains. The load does not thin with it.")
BB("B06", A1, "Seventeen times your bodyweight is still arriving, every step, in exactly the same place.", "Seventeen", "mechanism — load (pip)",
   "ANAT", "—", "—", "ANAT-A detailed: the thinner joint — worn cartilage, menisci, ligaments, fat pad, tendon fibres — the load pulses still arriving at the same spot below the kneecap", "one pulse per second, unchanged",
   "one pulse a second", STILL, "none", "no", "absent", "—", "NB2",
   LOW, THR, "clean", "CU", "low = the weight coming down on it", "deep", "deep", L(ANAT, "L"), False,
   layout="pip", eg="EG02 host cut-out bottom-left · EG04 red box 'Seventeen times' · 17× overlay")
TH("B07-TH", A1, "The cushion gets thinner. The weight stays exactly the same.", framing="punch")
BB("B07", A1, "That is why it feels like it arrived overnight.", "overnight", "problem — the feeling",
   "R1", "L-KITCHEN", "M-D1", "MCU in her kitchen first thing in the morning: Maureen half-risen from her chair at the oak table, a cup of tea in front of her, she stops and puts a hand to her knee, a small surprised frown", "she straightens, stops, hand to her knee",
   "one slow rise, about two seconds", STILL, "kitchen: three-quarter at the table, camera still", "no", "absent", "—", "NB2",
   EYE, THR, "clean", "MCU", "eye-level three-quarter = the small surprise on her face", "eyes", "medium", L(KITCH, "L"), True,
   notes="v2 — user Fix 'GIVE ME DIFFERENT BROLL HERE' (v1: top of her stairs, stopping)")
TH("B08-TH", A1, "Nothing about the way you walk changed, so you assume nothing changed. And here is the part that catches people out. You do not have to have done anything to your knees for this to happen.")
BB("B08a", A1, "Some of the people it happens to have never run a mile in their life.", "mile", "not what you did",
   "R1", "L-STREET", "M-D1", "MEDIUM at the bus stop on her street: Maureen sits on the shelter bench with her handbag on her lap, waiting for the bus, calm and still", "she settles her handbag and glances up the road",
   "one small settle, about two seconds", STILL, "street: three-quarter to the shelter, full figure seated, camera still", "no", "absent", "—", "NB2",
   EYE, THR, "clean", "MEDIUM", "three-quarter = an unhurried, unsporty life", "eyes", "medium", L(STREET_AM, "L"), True,
   notes="v4 — user Fix 'CREATE NEW IMAGE FOR THIS LINE' (v1 keys; v2 tartan trolley; v3 unworn trainers in the cupboard)")
BB("B08b", A1, "Others played sport for thirty years.", "sport", "not what you did",
   "extras", "L-PARK", "D-D1", "MEDIUM on a grass park pitch: a veterans' Sunday football game, a fit grey-haired man in his sixties in a plain kit strikes the ball, other older players around him", "he strikes the ball and follows through",
   "one kick, about a second", STILL, "pitch: low three-quarter, the kicker full figure, camera still", "no", "absent", "—", "NB2",
   LOW, THR, "clean", "MEDIUM", "low three-quarter = a lifetime of sport, still playing", "eyes", "medium", L(STREET_AM, "L"), True,
   notes="v5 — user Fix 'GIVE ME DIFFERENT IMAGE HERE' (v1 team photo; v2 football; v3 trophies; v4 Desmond jogging); one-off extras, no sheets (§19B)")
TH("B08-TH2", A1, "It makes almost no difference, because the load is not coming from what you did.", framing="punch")
BB("B08c", A1, "It is coming from standing up and walking.", "standing", "the cause — ordinary life",
   "R1", "L-KITCHEN", "M-D1", "side-on, waist-down, low: Maureen pushes up from her kitchen chair, both knees straightening under her weight, and takes the first step away", "she rises and steps off",
   "one rise and one step, about two seconds", STILL, "standing up: side-on, waist-down, camera still", "no", "absent", "—", "NB2",
   LOW, PRO, "clean", "MS", "low profile = the knees doing the work of standing", "foreground", "shallow", L(KITCH, "L"), False, mx=3,
   notes="v2 — user Fix 'GIVE ME DIFFERENT IMAGE HERE' (v1 Desmond rising from his bottom stair)")

# ============================================================ ACT 2 — the costly mistake
TH("B09-TH", A2, "Which is why most of what gets sold for this cannot work.", framing="punch")
BB("B10a", A2, "A sleeve squeezes the whole knee and leaves that band carrying everything.", "sleeve", "the mistake (F6)",
   "hands", "L-KITCHEN", "K-D1", "overhead on the oak table: a plain grey knit knee sleeve; a hand slides it aside", "one slide aside",
   "one slide, about a second", STILL, "hands: large in frame, one movement", "no", "absent", "—", "NB2",
   OVER, FRO, "clean", "CU", "overhead = laid out, examined", "hands", "deep", L(KITCH, "L"), False, ledger="F6", notes="unbranded")
BB("B10b", A2, "A hinged brace stops the knee going sideways, and it was never going sideways.", "brace", "the mistake (F6)",
   "hands", "L-KITCHEN", "K-D1", "CU a black hinged knee brace lying on the table; a hand flexes its hinge once sideways", "one flex of the hinge",
   "one flex, about a second", STILL, "hands: one movement", "no", "absent", "—", "NB2",
   HIGH, THR, "clean", "CU", "high = looking down at it, done with it", "hands", "medium", L(KITCH, "L"), False, ledger="F6", notes="unbranded")
BB("B10c", A2, "Gel sits on the skin.", "Gel", "the mistake (F6)",
   "hands", "L-KITCHEN", "K-D1", "CU a plain white tube; clear gel squeezed onto two fingertips", "one squeeze",
   "one squeeze, about a second", STILL, "hands: one movement", "no", "absent", "—", "NB2",
   EYE, PRO, "clean", "CU", "profile: the gel sitting on the fingertip", "hands", "shallow", L(KITCH, "R"), False, ledger="F6", notes="unbranded, no label")
BB("B10d", A2, "A painkiller turns the alarm off and leaves the load exactly where it was.", "painkiller", "the mistake (F6)",
   "hands", "L-KITCHEN", "K-D1", "CU a plain blister pack of white tablets beside a glass of water; a thumb pops one tablet out", "one tablet popped",
   "one press, about a second", STILL, "hands: one movement", "no", "absent", "—", "NB2",
   LOW, THR, "clean", "CU", "low = the small pill made big", "hands", "shallow", L(KITCH, "L"), False, ledger="F6", notes="unbranded, no print")
TH("B11-TH", A2, "None of them are aimed at the spot.", framing="punch")
BB("B12", A2, "What that band actually needs is for less of your weight to land on it.", "less", "the need (pip)",
   "ANAT", "—", "—", "ANAT-A: the knee in profile, the load pulse at the spot below the kneecap dimming to a soft glow", "the pulse softens",
   "one fade, about two seconds", STILL, "none", "no", "absent", "—", "NB2",
   EYE, PRO, "clean", "CU", "profile shows the load path down the leg", "deep", "deep", L(ANAT, "L"), False,
   layout="pip", eg="EG02 host cut-out bottom-left")

# ============================================================ ACT 3 — the product
BB("B13", A3, "That is what this does. It is called Stryde.", "Stryde", "reveal — the product, wordmark",
   "hands", "L-KITCHEN", "K-D1", "CU two hands hold the strap up at chest height above the kitchen table, the front of the shell and the wordmark to the lens", "the hands lift it a few centimetres into the light",
   "one small lift, about a second", STILL, "hands: one movement; the strap does not turn", "no", "held", "VISIBLE", "NBP",
   EYE, FRO, "clean", "CU", "", "product", "medium", L(KITCH, "R"), False, eg="EG04 red box 'Stryde'", notes="WORDMARK-LOCK")
BB("B14a", A3, "It sits two centimetres below the kneecap, on the tendon, and never crosses the joint.", "below", "SEAT (§9B) — placement",
   "R1", "L-M-STAIRS", "M-D2", "CU sitting on the bottom stair, both hands slide the strap up her right shin and stop at contact under the kneecap", "slides up the last few centimetres and stops at contact",
   "one slide, about a second", STILL, "hands: start mid-movement, end on contact", "no", "seated", "VISIBLE", "NBP",
   HIGH, THR, "clean", "CU", "high = her own view of her knee", "product", "medium", L(M_SUN, "R"), False, notes="PLACE-LOCK")
BB("B14b", A3, "A silicone pad inside holds pressure on that one band instead of spreading it round the whole knee.", "pad", "product — the pad (PAD_BACK_SHOT)",
   "hands", "L-KITCHEN", "K-D1", "CU hands hold the strap and tip it so the inner pad faces the lens", "one tilt of the strap toward the lens",
   "one tilt, about a second", STILL, "turning the product: pin the end frame", "yes", "held — the pad", "—", "NBP",
   EYE, THR, "clean", "ECU", "", "product", "medium", L(KITCH, "L"), False, notes="prompt says 'the pad', never 'silicone'; inner_face.jpg attached")
BB("B14c", A3, "Your weight gets caught and moved off the worn part before it reaches the joint.", "caught", "mechanism — protection (F7)",
   "ANAT", "—", "—", "ANAT-A: the strap seated below the kneecap, the pad pressing on the tendon, the glow at the worn spot calming", "the red at the spot fades as the pad takes the load",
   "one fade, about two seconds", STILL, "none", "no", "worn (anatomical)", "—", "NB2",
   LOW, THR, "clean", "CU", "low = the fix, resolve", "deep", "deep", L(ANAT, "R"), False, ledger="F7", eg="EG05")
TH("B15-TH", A3, "The placement is the whole thing.", framing="punch")
BB("B15", A3, "A centimetre too high and it is a sleeve again.", "high", "placement",
   "R1", "L-M-STAIRS", "M-D2", "ECU from the side: the strap seated on her right knee, the kneecap's lower edge sitting in the notch", "her knee flexes a little and straightens",
   "one flex, about a second", STILL, "none", "no", "worn", "VISIBLE", "NBP",
   EYE, PRO, "clean", "ECU", "profile: the kneecap in the notch", "product", "medium", L(M_SUN, "L"), False, notes="PLACE-LOCK, contact")
BB("B16a", A3, "Thirty four percent less strain. Measured.", "Thirty", "proof — held (34%)",
   "R2", "L-D-STAIRS", "D-D2", "from the side, waist-down: Desmond comes down one stair easily, the strap on his right knee", "one easy step down",
   "one step, about a second", STILL, "stairs: side, waist-down, camera still, hand on the rail visible", "no", "worn", "VISIBLE", "NBP",
   EYE, PRO, "clean", "MEDIUM", "profile: the knee working with the strap on", "product", "medium", L(D_SUN, "L"), False, eg="34% overlay (post)")
BB("B16b", A3, "Three years with orthopedic surgeons.", "surgeons", "authority — held",
   "S1", "L-CONSULT", "S1-D1", "MCU at his desk, the knee model beside him, he holds the strap still at chest height and looks up from it", "lifts his eyes from the strap to the patient",
   "one look up, about a second", STILL, "none", "no", "held", "—", "NBP",
   EYE, THR, "clean", "MCU", "", "eyes", "medium", L(CONS, "L"), True, notes="APPROACH-PRO")
BB("B16c", A3, "Two hundred thousand people wearing one.", "thousand", "social proof — held",
   "R2", "L-STREET", "D-D2", "knee-and-shin only, walking toward the lens on the pavement, the strap staying put", "three walking steps toward the lens",
   "one step per second, normal walking speed", STILL, "walking toward camera: feet/knee only, 3 steps", "no", "worn", "VISIBLE", "NBP",
   GROUND, FRO, "clean", "CU", "ground = steps and legs", "product", "deep", L(STREET_PM, "L"), False, eg="200,000+ overlay (post)")
BB("B17a", A3, "Ten seconds to put on.", "Ten", "feature (F8)",
   "R2", "L-D-STAIRS", "D-D3", "CU sitting on the bottom stair, his tracksuit leg rolled up, both hands slide the strap up to contact under the kneecap", "slides up and stops at contact",
   "one slide, about a second", STILL, "hands: start mid-movement, end on contact", "no", "seated", "VISIBLE", "NBP",
   HIGH, THR, "clean", "CU", "high = his own view of his knee", "product", "medium", L(D_SUN, "R"), False, ledger="F8")
BB("B17b", A3, "No sores, no rolling down,", "sores", "feature (F8)",
   "R1", "L-M-STAIRS", "M-D2", "CU seated, her fingertips run along the skin at the strap's lower edge — the skin smooth and unmarked", "fingertips slide once along the edge",
   "one slide, about a second", STILL, "hands: large in frame, one movement", "no", "worn", "VISIBLE", "NBP",
   LOW, PRO, "clean", "CU", "low profile: the edge against the skin", "product", "medium", L(M_SUN, "L"), False, ledger="F8")
BB("B17c", A3, "and nobody can see it.", "nobody", "REVEAL→CONCEALED (§9D, F8)",
   "R2", "L-D-STAIRS", "D-D3", "CU from the side: he lets his tracksuit leg drop over the strap; the fabric lies flat", "the trouser leg falls and settles",
   "one drop, about a second", STILL, "none", "no", "worn", "REVEAL", "NBP",
   EYE, PRO, "clean", "CU", "profile shows the flat line of the trouser", "product", "medium", L(D_SUN, "L"), False, ledger="F8")

# ============================================================ ACT 4 — proof, the test, the offer, the close
TH("B18-TH", A4, "The thing people write to us about most is not the pain.")
BB("B18a", A4, "It is that the knee stops feeling like a rusty hinge.", "hinge", "outcome (F9)",
   "R2", "L-D-STAIRS", "D-D2", "CU Desmond's strapped right knee bending smoothly as he sits down onto the bottom stair — already lowering, ends seated", "sits down, ends on contact",
   "about a second and a half", STILL, "sitting down: start mid-movement, end on contact, 3s", "no", "worn", "VISIBLE", "NBP",
   EYE, THR, "clean", "CU", "", "product", "medium", L(D_SUN, "R"), False, ledger="F9", mx=3)
BB("B18b", A4, "They stop planning the stairs before they get to them.", "stairs", "outcome (F9)",
   "R1", "L-M-STAIRS", "M-D2", "WIDE from the foot of the stairs: Maureen at the top starts straight down, facing forwards, hand light on the rail", "one step down, facing forwards",
   "one step, about a second and a half", STILL, "stairs: facing forwards, full figure small in frame, camera still at the foot", "no", "worn", "VISIBLE", "NBP",
   LOW, FRO, "clean", "WIDE", "low from the foot = she comes down to us, resolve", "deep", "deep", L(M_SUN, "L"), True, ledger="F9")
TH("B19-TH", A4, "And you do not have to take my word for any of it.")
BB("B19a", A4, "Put one on one knee only. Leave the other bare.", "bare", "the self-test",
   "R1", "L-M-STAIRS", "M-D2", "CU seated on the bottom stair: both knees side by side, the strap on the right, the left bare", "her hands rest on her thighs; she breathes out",
   "one breath, about a second", STILL, "none", "no", "worn (one knee)", "VISIBLE", "NBP",
   HIGH, FRO, "clean", "CU", "high = her own view, the comparison", "product", "medium", L(M_SUN, "R"), False, notes="one strapped knee, one bare — the script's test (SIDE_RULE)")
BB("B19b", A4, "Go to your own stairs and come down forwards.", "forwards", "the self-test",
   "R1", "L-M-STAIRS", "M-D2", "from the side, waist-down: Maureen comes down one stair facing forwards, hand light on the rail", "one step down, facing forwards",
   "one step, about a second and a half", STILL, "stairs: side, waist-down, camera still, hand on the rail visible", "no", "worn", "VISIBLE", "NBP",
   EYE, PRO, "through", "MEDIUM", "through the spindles: the same view as the hook, now forwards", "product", "medium", L(M_SUN, "L"), False, notes="mirror_of HK1-a")
TH("B19-TH2", A4, "You will know in a minute. Not because the arthritis has gone. It is still there, and nothing here changes that.", framing="punch")
BB("B20", A4, "Because the weight is not landing on that band any more.", "weight", "mechanism — protection (pip)",
   "ANAT", "—", "—", "ANAT-A: the strap seated, the step pulse arriving and spreading off the tendon, the spot staying calm", "one step pulse, the spot stays cool",
   "one pulse, about a second", STILL, "none", "no", "worn (anatomical)", "—", "NB2",
   HIGH, FRO, "clean", "CU", "high = the whole knee calm", "deep", "deep", L(ANAT, "L"), False, layout="pip", eg="EG02 host cut-out bottom-left")
TH("B21-TH", A4, "So here is the choice. Keep aiming at the joint, which is where it hurts but not where the load is.")
BB("B21", A4, "Or move the load off the one spot that has been taking it since you were a teenager.", "spot", "the choice",
   "R2", "L-D-STAIRS", "D-D2", "CU Desmond's strapped right knee as he steps down one stair, one of the old team photos on the wall behind", "one step down",
   "one step, about a second and a half", STILL, "stairs: side, knee-down, camera still", "no", "worn", "VISIBLE", "NBP",
   LOW, THR, "clean", "CU", "low = resolve", "product", "medium", L(D_SUN, "R"), False)
BB("B22a", A4, "Two for one, so you can do both knees.", "Two", "offer — pair pack",
   "hands", "L-KITCHEN", "K-D1", "overhead on the oak table: hands lift the lid off the box; two straps lie inside side by side", "lifts the lid clear and out of frame",
   "one lift, about a second", STILL, "hands: large in frame; straps do not move", "no", "box open, two units", "—", "NBP",
   OVER, FRO, "clean", "CU", "overhead = the everyday table, the reveal", "product", "deep", L(KITCH, "L"), False, eg="EG04 · 'BUY 1 GET 1 FREE' in the edit", notes="package_open.jpg + front/back refs")
TH("B22-TH", A4, "Sixty days, and you keep the straps. From the Stryde site.", eg="EG01 · '60 days' in the edit (F10)")
BB("B22c", A4, "The copies stretch, and a stretched strap stops holding the spot.", "stretch", "anti-copy (F11)",
   "hands", "L-KITCHEN", "K-D1", "CU on the table: two hands pull a cheap copy's thin frayed band and it stretches slack", "one pull, the band goes slack",
   "one pull, about a second", STILL, "hands: one movement", "no", "copy only (FAKE-BASE + 'wide webbing')", "—", "NB2",
   HIGH, PRO, "clean", "CU", "high profile = examined and judged", "hands", "medium", L(KITCH, "R"), False, ledger="F11", notes="FAKE-BASE, no wordmark; the hero never damaged")
BB("B23a", A4, "The next step is going to land in the same place either way.", "step", "close",
   "R1", "L-M-STAIRS", "M-D2", "ECU her foot, the strap just in frame above it, on the edge of the top stair", "her foot settles on the edge",
   "one small settle, about a second", STILL, "stairs: feet only, camera still", "no", "worn", "VISIBLE", "NBP",
   GROUND, THR, "clean", "ECU", "ground = the next step", "foreground", "medium", L(M_SUN, "R"), False)
BB("B23b", A4, "Go and do it forwards.", "forwards", "close — callback",
   "R1", "L-M-STAIRS", "M-D2", "MEDIUM from below: Maureen comes down towards us facing forwards, a small smile", "one step down, facing forwards",
   "one step, about a second and a half", STILL, "stairs: facing forwards, waist-up, camera still at the foot", "no", "worn (out of frame)", "—", "NB2",
   LOW, FRO, "clean", "MEDIUM", "low from the foot = resolve", "eyes", "medium", L(M_SUN, "L"), True, notes="callback to HK1")


# ============================================================ B-roll on every line (user, 2026-09-29: "BROLL FOR EVERY LINE")
# One B-roll per host line: the talking head stays as audio and on the timeline, the B-roll covers its line.
BB("B01-BR", A1, "Put your finger there now and press.", "press", "the self-test, shown",
   "R2", "L-D-STAIRS", "D-D1", "CU seated on his bottom stair: Desmond's fingertip slides down over his kneecap and stops in the soft spot below it", "fingertip slides down and stops",
   "one slide, about two seconds", STILL, "seated, knee-down, face out of frame, camera still", "no", "absent", "—", "NB2",
   LOW, THR, "clean", "CU", "low = his own finger finding it", "hands", "shallow", L(D_GREY, "R"), False, notes="covers B01-TH")
BB("B03a", A1, "It is not a big thing. It is about as wide as your thumb,", "big", "how small it is",
   "ANAT", "—", "—", "ANAT-A low front MS: the big thigh muscle filling the top of the frame and narrowing down into the one small band under the kneecap, glowing", "the small band's glow pulses once",
   "one pulse, about a second", STILL, "none", "no", "absent", "—", "NB2",
   LOW, FRO, "clean", "MEDIUM", "low front = the big muscle above, the small band below", "deep", "deep", L(ANAT, "L"), False, ledger="F2", eg="EG05",
   notes="user 2026-09-29 'PUT DIFFERENT BROLLS HERE' — B03 line split in three; no thumb against anything (F2)")
BB("B03b", A1, "and it has been quietly taking your whole bodyweight, multiplied,", "multiplied", "everyday load",
   "R1", "L-KITCHEN", "M-D1", "MEDIUM in the kitchen: Maureen bends at the knees to lift a heavy cast-iron casserole pot from a low cupboard, her knees taking the load", "she rises with the pot",
   "one lift, about two seconds", STILL, "kitchen: three-quarter, camera still, her face turned to the cupboard", "no", "absent", "—", "NB2",
   EYE, THR, "clean", "MEDIUM", "three-quarter = an ordinary moment, the knees working", "deep", "deep", L(KITCH, "L"), False,
   notes="user 2026-09-29 'PUT DIFFERENT BROLLS HERE' — B03 line split in three")
BB("B03c", A1, "since you were a teenager.", "teenager", "since you were a teenager",
   "hands", "L-KITCHEN", "K-D1", "overhead on the oak table: a photo album open at a faded 1970s snapshot of a teenage girl mid-stride on a seaside promenade; Maureen's hand at the page", "one page turned",
   "one turn, about two seconds", STILL, "hands only, camera still", "no", "absent", "—", "NB2",
   OVER, FRO, "clean", "CU", "overhead = the album laid open, looked back on", "hands", "medium", L(KITCH, "L"), False, ledger="F2",
   notes="was B03-BR (the album) — now the third part of the B03 line")
BB("B06-BR", A1, "That part is ordinary. It happens to everybody. But here is what nobody explains. The load does not thin with it.", "everybody", "it happens to everybody",
   "extras", "L-STREET", "M-D1", "MEDIUM on the pavement at a bus stop: three people of different ages, each with a knee problem — a man in his seventies on the shelter bench rubbing his knee, a woman in her forties leaning on the shelter post easing her knee, a young man in his twenties in running gear walking past with a slight limp, a hand on his thigh", "the walker limps through, the man on the bench rubs his knee",
   "an ordinary, slightly slow pace", STILL, "street: three-quarter on to the bus stop, camera still, nobody looks at the lens", "no", "absent", "—", "NB2",
   EYE, THR, "clean", "MEDIUM", "three-quarter = several people, one ordinary street, the same trouble", "deep", "deep", L(STREET_AM, "L"), True,
   notes="user 2026-09-29 'It happens to everybody. (2 OR 3 PEOPLE HAVING PROBLEM IN THEIR KNEE) BROLL HERE' + 'NOT SAME AGE'; one-off extras, no sheets (§19B)")
BB("B06-BR2", A1, "The load does not thin with it.", "load", "the load stays full",
   "R2", "L-STREET", "D-D1", "ECU knee-height, side-on on the pavement: Desmond's right knee fills the frame as his foot lands, the knee bending under his whole weight, the tendon standing out below the kneecap", "one heavy step lands",
   "one step, about a second, ordinary walking pace", STILL, "street: side-on, knee-height, legs only, camera still, he walks through the frame", "no", "absent", "—", "NB2",
   LOW, PRO, "clean", "ECU", "low profile, close = the full weight landing on the knee", "foreground", "shallow", L(STREET_AM, "L"), False,
   notes="user 2026-09-29 'The load does not thin with it — BROLL HERE'; v2 Fix 'FOCUS ON KNEE'")
BB("B07-BRa", A1, "The cushion gets thinner.", "thinner", "the cushion in the knee wears thin",
   "ANAT", "—", "—", "ANAT-B front-on close-up of the joint gap: the pale cartilage cushion between thigh bone and shin bone, visibly thin and worn, the bones sitting close", "the cushion thins a little further",
   "one slow change over three seconds", STILL, "none", "no", "absent", "—", "NB2",
   EYE, FRO, "clean", "CU", "front = the gap between the bones seen straight on, the cushion's thickness readable", "deep", "deep", L(ANAT, "R"), False,
   notes="user 2026-09-29 'The cushion gets thinner. (CUSHION IN KNEE GETS THINNER)'; B05 is the profile cutaway, this is front-on and closer")
BB("B07-BRb", A1, "The weight stays exactly the same.", "same", "the load does not change",
   "R1", "L-M-STAIRS", "M-D1", "waist-down from the front, low at the foot of her stairs: Maureen comes down carrying a full laundry basket on her hip, one foot landing on the tread nearest the lens, the knee bending under her whole weight", "one step down onto the tread",
   "one step, about a second and a half", STILL, "stairs: front, waist-down, basket at her hip, camera still", "no", "absent", "—", "NB2",
   LOW, FRO, "clean", "MCU", "low front = the weight coming straight down at the lens", "foreground", "shallow", L(M_GREY, "L"), False,
   notes="user 2026-09-29 'The weight stays exactly the same. MAKE ME A BROLL HERE'; replaces the planned worn-plimsoll B07-BR")
BB("B08-BR", A1, "Nothing about the way you walk changed, so you assume nothing changed.", "changed", "ordinary walking",
   "R1", "L-M-STAIRS", "M-D1", "MEDIUM from behind: Maureen walks down her hall towards the front door, ordinary and unhurried", "four ordinary steps away from the lens",
   "an ordinary walking pace", STILL, "hall: from behind, full figure small in frame, camera still", "no", "absent", "—", "NB2",
   EYE, BEH, "clean", "MEDIUM", "from behind = her ordinary day, unobserved", "deep", "deep", L(M_GREY, "R"), False, notes="first sentence of B08-TH (user Fix 2026-09-29)")
BB("B08-BRb", A1, "And here is the part that catches people out.", "catches", "it catches you out",
   "R2", "L-D-STAIRS", "D-D1", "MCU from the landing above: Desmond halfway down his stairs stops short, one hand on the rail, the other going to his knee, looking down at it, caught out", "he stops mid-flight and his hand goes to his knee",
   "one stop, about a second", STILL, "stairs: from above, head and shoulders to the knee, camera still", "no", "absent", "—", "NB2",
   HIGH, THR, "clean", "MCU", "high three-quarter = looking down on the man caught out mid-step", "eyes", "medium", L(D_GREY, "R"), True,
   notes="user 2026-09-30 'give me brolls here' — first sentence of the rest of B08-TH")
BB("B08-BRc", A1, "You do not have to have done anything to your knees for this to happen.", "anything", "nothing you did",
   "R1", "L-KITCHEN", "M-D1", "MEDIUM side-on in her kitchen: Maureen at the worktop filling the kettle at the sink, an ordinary quiet morning", "she fills the kettle and turns off the tap",
   "one ordinary action, about two seconds", STILL, "kitchen: side-on at the sink, waist up, camera still", "no", "absent", "—", "NB2",
   EYE, PRO, "clean", "MEDIUM", "profile = an ordinary life, nothing sporty", "eyes", "medium", L(KITCH, "L"), True,
   notes="user 2026-09-30 'give me brolls here' — second sentence; replaces the planned plimsolls shot (too close to B08-BR2's boots)")
BB("B08-BR2", A1, "It makes almost no difference,", "difference", "what you did doesn't matter",
   "R2", "L-D-STAIRS", "D-D1", "CU Desmond's hand sets a pair of old black football boots, dried mud on the studs, down on the shoe rack by his front door", "the boots set down on the rack",
   "one set-down, about a second", STILL, "hall by the door, hand and boots only, camera still", "no", "absent", "—", "NB2",
   HIGH, THR, "clean", "CU", "high = the old boots looked down on, put away", "hands", "shallow", L(D_GREY, "L"), False, notes="first half of B08-TH2 (user 'BROLLS HERE'); no logos on the boots")
BB("B08-BR3", A1, "because the load is not coming from what you did.", "load", "the load comes from every step",
   "R1", "L-M-STAIRS", "M-D1", "ECU at floor level, side-on: Maureen's plimsoll steps over her front doorstep from the hall, the bare knee above bending as it takes her weight", "one step over the doorstep",
   "one step, about a second", STILL, "doorway: ground level side-on, feet and knee only, camera still", "no", "absent", "—", "NB2",
   GROUND, PRO, "clean", "ECU", "ground profile = one ordinary step taking the load", "foreground", "shallow", L(M_GREY, "R"), False, notes="second half of B08-TH2 (user 'BROLLS HERE')")
BB("B09-BR", A2, "Which is why most of what gets sold for this cannot work.", "sold", "the pile of things that didn't work",
   "hands", "L-KITCHEN", "K-D1", "on the oak table: a grey knit knee sleeve, a black hinged brace, a plain white gel tube and a blister pack of tablets laid out together; a hand sets the last one down", "the last item set down",
   "one set-down, about a second", STILL, "table top, hands only, camera still", "no", "absent", "—", "NB2",
   HIGH, THR, "clean", "MEDIUM", "high = everything tried, laid out", "hands", "deep", L(KITCH, "L"), False, ledger="F6", notes="covers B09-TH; all unbranded, no print")
BB("B11-BR", A2, "None of them are aimed at the spot.", "spot", "the sleeve misses the spot",
   "ANAT", "—", "—", "ANAT-C: the knee as a dark silhouette wrapped in a faint grey knit sleeve over the whole joint, the one spot below the kneecap still glowing untouched", "the spot pulses once, the sleeve does nothing",
   "one pulse", STILL, "none", "no", "absent", "—", "NB2",
   EYE, FRO, "clean", "CU", "front = the sleeve round everything, the spot still lit", "deep", "deep", L(ANAT, "L"), False, eg="EG05", notes="covers B11-TH; generic unbranded sleeve")
BB("B15-BR", A3, "The placement is the whole thing.", "placement", "placement, measured",
   "R1", "L-M-STAIRS", "M-D2", "ECU seated on her bottom stair: two fingers laid flat just below her kneecap, measuring the spot, the strap held ready in her other hand", "the strap's pad lowers onto the measured spot",
   "one placement, about two seconds", STILL, "seated, knee and hands only, camera still", "no", "held", "the pad and shell", "NBP",
   HIGH, THR, "clean", "ECU", "high = her own view, measuring", "hands", "shallow", L(M_SUN, "R"), False, notes="covers B15-TH; PLACE-LOCK")
BB("B18-BR", A4, "The thing people write to us about most is not the pain.", "write", "the letters",
   "hands", "L-KITCHEN", "K-D1", "overhead on the oak table: a small pile of handwritten cards and letters, the handwriting too soft to read; a hand spreads them out", "the letters spread out",
   "one spread, about two seconds", STILL, "table top, hands only, camera still", "no", "absent", "—", "NB2",
   OVER, FRO, "clean", "CU", "overhead = the letters laid out, read", "hands", "medium", L(KITCH, "R"), False, notes="covers B18-TH; no readable handwriting")
BB("B19-BR", A4, "And you do not have to take my word for any of it.", "word", "try it yourself",
   "R1", "L-M-STAIRS", "M-D2", "MEDIUM from behind at the foot of her stairs: Maureen holds one strap in her hand and looks up the flight", "she lifts her eyes up the stairs",
   "one look up, about two seconds", STILL, "hall: from behind, the strap in her hand, camera still", "no", "held", "the strap in her hand", "NBP",
   EYE, BEH, "clean", "MEDIUM", "from behind = her test, her stairs", "deep", "deep", L(M_SUN, "L"), False, notes="covers B19-TH")
BB("B19-BR2", A4, "You will know in a minute. Not because the arthritis has gone. It is still there, and nothing here changes that.", "minute", "coming down with ease",
   "R1", "L-M-STAIRS", "M-D2", "CU side-on: her hand lets go of the oak handrail as she comes down the stairs steadily", "her hand lifts off the rail mid-step",
   "one step, about a second and a half", STILL, "stairs: side-on, hand and rail, camera still", "no", "absent", "—", "NB2",
   EYE, PRO, "clean", "CU", "profile = the hand leaving the rail", "hands", "shallow", L(M_SUN, "L"), False, ledger="F9", notes="covers B19-TH2; no claim shown beyond ease")
BB("B21-BR", A4, "So here is the choice. Keep aiming at the joint, which is where it hurts but not where the load is.", "joint", "aiming at the joint",
   "R2", "L-D-STAIRS", "D-D1", "CU seated on his bottom stair: Desmond's hand rubs clear gel in slow circles over his whole kneecap", "two slow circles of the hand",
   "two circles, about two seconds", STILL, "seated, knee and hand only, camera still", "no", "absent", "—", "NB2",
   HIGH, THR, "clean", "CU", "high = his own view, rubbing the wrong place", "hands", "shallow", L(D_GREY, "R"), False, ledger="F6", notes="covers B21-TH; plain unbranded gel")
BB("B22-BR", A4, "Sixty days, and you keep the straps. From the Stryde site.", "Sixty", "the offer, delivered",
   "R1", "L-M-STAIRS", "M-D2", "CU on her doormat: the STRYDE box, just delivered; Maureen's hand picks it up", "the box lifted off the mat",
   "one lift, about a second", STILL, "hall doormat, hand and box only, camera still", "no", "box", "the box and wordmark", "NBP",
   HIGH, FRO, "clean", "CU", "high = looking down at what arrived", "product", "medium", L(M_SUN, "L"), False, eg="EG04 '60 days' (post)", notes="covers B22-TH; WORDMARK-LOCK")

HOOKS = {1: ["HK1-a", "HK1-b", "HK1-TH"], 2: ["HK2-a", "HK2-b", "HK2-TH"], 3: ["HK3-a", "HK3-b", "HK3-TH"]}
BODY = ['B01a', 'B01b', 'B01c', 'B01-TH', 'B01-BR', 'B02', 'B03-TH', 'B03a', 'B03b', 'B03c', 'B04a', 'B04b', 'B04c', 'B05', 'B06-TH', 'B06-BR', 'B06-BR2', 'B06', 'B07-TH', 'B07-BRa', 'B07-BRb', 'B07', 'B08-TH', 'B08-BR', 'B08-BRb', 'B08-BRc', 'B08a', 'B08b', 'B08-TH2', 'B08-BR2', 'B08-BR3', 'B08c', 'B09-TH', 'B09-BR', 'B10a', 'B10b', 'B10c', 'B10d', 'B11-TH', 'B11-BR', 'B12', 'B13', 'B14a', 'B14b', 'B14c', 'B15-TH', 'B15-BR', 'B15', 'B16a', 'B16b', 'B16c', 'B17a', 'B17b', 'B17c', 'B18-TH', 'B18-BR', 'B18a', 'B18b', 'B19-TH', 'B19-BR', 'B19a', 'B19b', 'B19-TH2', 'B19-BR2', 'B20', 'B21-TH', 'B21-BR', 'B21', 'B22a', 'B22-TH', 'B22-BR', 'B22c', 'B23a', 'B23b']

def angles_rows(order):
    out = []
    for b in order:
        r = ROWS[b]
        if r["type"] == "TH":
            out.append(dict(beat=b, group=r["act"], type="TH", subject="H")); continue
        a = r["angle"]; lt = r["light"]
        out.append(dict(beat=b, group=r["act"], type="BR", subject=r["subject"], height=a["height"], side=a["side"], scale=a["scale"],
            fg=a["fg"], why=a["why"], mirror_of="HK1-a" if "mirror_of HK1-a" in r["notes"] else None, mode=1,
            product_beat=r["focus"]["plane"] == "product", focus=r["focus"], story_day=r["story_day"], face=r["face"],
            light=dict(source=lt["source"], key_side=lt["key_side"], time=lt["time"], arc=lt["arc"], kelvin=lt["kelvin"], why="")))
    return out

def md():
    lines = ["| Beat | Act | Line | Subject · location · day | Framing / action | Angle · focus · light | Layout · EG | Product · model | Ledger |",
             "|---|---|---|---|---|---|---|---|---|"]
    for b in [x for h in HOOKS.values() for x in h] + BODY:
        r = ROWS[b]
        if r["type"] == "TH":
            lines.append(f"| {b} | {r['act']} | {r['line']} | H · L-STUDIO · H-D1 | talking head ({'1.25× punch-in' if r['framing']=='punch' else 'wide'}) | — | full · {r['eg']} | — · HeyGen Avatar V | |")
        else:
            a, f, lt = r["angle"], r["focus"], r["light"]
            lines.append(f"| {b} | {r['act']} | {r['line']} | {r['subject']} · {r['location']} · {r['story_day']} | {r['framing']} — {r['action']} ({r['pace']}) | "
                         f"{a['height']} {a['side']} {a['scale']}{' '+a['fg'] if a['fg']!='clean' else ''} · {f['plane']}/{f['dof']} · {lt['source']} {lt['key_side']} {lt['kelvin']}K | "
                         f"{r['layout']}{' · '+r['eg'] if r['eg'] else ''} | {r['visibility']} · {r['model']} | {r['ledger']} |")
    return "\n".join(lines)

if __name__ == "__main__":
    used = {b for h in HOOKS.values() for b in h} | set(BODY)
    assert used == set(ROWS), set(ROWS) ^ used
    json.dump(list(ROWS.values()), open(HERE / "actmap_rows.json", "w"), indent=1, ensure_ascii=False)
    for n, h in HOOKS.items():
        json.dump(angles_rows(h + BODY), open(HERE / f"angles_HK{n}.json", "w"), indent=1)
    (HERE / "actmap.md").write_text(md() + "\n")
    br = [b for b in ROWS if ROWS[b]["type"] == "BR"]
    pip = [b for b in br if ROWS[b]["layout"] != "full"]
    print(len(ROWS), "rows;", len(br), "B-roll,", len(ROWS) - len(br), "talking head;", "pip:", pip)
