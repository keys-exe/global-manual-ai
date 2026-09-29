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
   "ANAT", "—", "—", "ANAT-A: the knee from the side, the one spot below the kneecap glowing warmer as the pulses stack up", "the spot warms with each pulse",
   "one pulse a second", STILL, "none", "no", "absent", "—", "NB2",
   HIGH, THR, "clean", "CU", "high = the one spot, looked down on", "deep", "deep", L(ANAT, "R"), False, ledger="VN01 · F4", eg="EG05 · '70,000,000' overlay (post)")
TH("HK3-TH", HOOK[3], "Here is what happens when that spot stops being able to take it.")

# ============================================================ ACT 1 — why it happens (shared body)
BB("B01a", A1, "That band is the patellar tendon.", "tendon", "anatomy",
   "ANAT", "—", "—", "ANAT-A: the knee three-quarter front, the patellar tendon traced from the kneecap down to the shin", "the tendon lights from top to bottom",
   "one trace, about two seconds", STILL, "none", "no", "absent", "—", "NB2",
   EYE, THR, "clean", "CU", "", "deep", "deep", L(ANAT, "L"), False, eg="EG05")
BB("B01b", A1, "It sits two centimetres below your kneecap, on the front of the joint, and every step you take lands on it.", "step", "anatomy → life",
   "R2", "L-D-STAIRS", "D-D1", "ECU from the side: Desmond's bare right knee bending as he steps down one stair", "one step down",
   "one step, about a second and a half", STILL, "stairs: side, waist-down, camera still, hand on the rail visible", "no", "absent", "—", "NB2",
   EYE, PRO, "clean", "ECU", "profile shows the knee bending and the spot below it", "foreground", "medium", L(D_GREY, "L"), False)
TH("B01-TH", A1, "Put your finger there now and press.", framing="punch")
BB("B02", A1, "That is the one.", "one", "participation",
   "R1", "L-M-STAIRS", "M-D1", "CU sitting on the bottom stair, her fingertip pressing just below her right kneecap", "her fingertip presses in once and holds",
   "one press, about a second", STILL, "hands: large in frame, one movement", "no", "absent", "—", "NB2",
   HIGH, THR, "clean", "CU", "high = her own view of her knee", "hands", "shallow", L(M_GREY, "R"), False)
TH("B03-TH", A1, "It is not a big thing. It is about as wide as your thumb, and it has been quietly taking your whole bodyweight, multiplied, since you were a teenager.")
BB("B04a", A1, "Going up the stairs, your muscles lift you.", "up", "mechanism — up",
   "R2", "L-D-STAIRS", "D-D1", "from behind and below: Desmond climbs two stairs, thigh muscles working, hand on the rail", "two steps up",
   "one step a second", STILL, "stairs: from behind, camera still, 2 steps", "no", "absent", "—", "NB2",
   LOW, BEH, "clean", "MEDIUM", "behind and low = the climb, the muscles doing the lifting", "deep", "deep", L(D_GREY, "R"), False)
BB("B04b", A1, "Going down, nothing lifts you. You are catching yourself on every step,", "catching", "mechanism — down",
   "R2", "L-D-STAIRS", "D-D1", "from the side, waist-down: Desmond comes down one stair, the knee bending and taking the landing, hand on the rail", "one step down, the knee absorbing it",
   "one step, about a second and a half", STILL, "stairs: side, waist-down, camera still, hand on the rail visible", "no", "absent", "—", "NB2",
   EYE, PRO, "through", "MEDIUM", "through the spindles: the step watched closely", "deep", "deep", L(D_GREY, "L"), False)
BB("B04c", A1, "so coming down puts more through that band than going up does.", "more", "mechanism (F5)",
   "ANAT", "—", "—", "ANAT-A: the knee on a down step, the tendon glowing stronger as the foot lands", "one landing pulse, stronger than the last",
   "one pulse, about a second", STILL, "none", "no", "absent", "—", "NB2",
   HIGH, THR, "clean", "CU", "high = the drop onto the step", "deep", "deep", L(ANAT, "R"), False, ledger="F5", eg="EG05")
BB("B05", A1, "And inside the joint there is a layer of cartilage doing the absorbing. And over the years that layer thins.", "thins", "anatomy — cartilage",
   "ANAT", "—", "—", "ANAT-A: the joint cut away, the pale cartilage layer between the bones slowly thinning", "the cartilage thins by a fraction",
   "one slow change over four seconds", STILL, "none", "no", "absent", "—", "NB2",
   EYE, PRO, "clean", "CU", "profile: the layer seen edge-on", "deep", "deep", L(ANAT, "L"), False, eg="EG05")
TH("B06-TH", A1, "That part is ordinary. It happens to everybody. But here is what nobody explains. The load does not thin with it.")
BB("B06", A1, "Seventeen times your bodyweight is still arriving, every step, in exactly the same place.", "Seventeen", "mechanism — load (pip)",
   "ANAT", "—", "—", "ANAT-A: the thinner joint, the load pulses still arriving at the same spot below the kneecap", "one pulse per second, unchanged",
   "one pulse a second", STILL, "none", "no", "absent", "—", "NB2",
   LOW, THR, "clean", "CU", "low = the weight coming down on it", "deep", "deep", L(ANAT, "L"), False,
   layout="pip", eg="EG02 host cut-out bottom-left · EG04 red box 'Seventeen times' · 17× overlay")
TH("B07-TH", A1, "The cushion gets thinner. The weight stays exactly the same.", framing="punch")
BB("B07", A1, "That is why it feels like it arrived overnight.", "overnight", "problem — the feeling",
   "R1", "L-M-STAIRS", "M-D1", "MCU at the top of her stairs, hand on the rail, she looks down the flight and stops", "she draws one breath and doesn't step",
   "one breath, about a second", STILL, "none", "no", "absent", "—", "NB2",
   HIGH, THR, "clean", "MCU", "high = the drop in front of her, small", "eyes", "medium", L(M_GREY, "R"), True)
TH("B08-TH", A1, "Nothing about the way you walk changed, so you assume nothing changed. And here is the part that catches people out. You do not have to have done anything to your knees for this to happen.")
BB("B08a", A1, "Some of the people it happens to have never run a mile in their life.", "mile", "not what you did",
   "R1", "L-M-STAIRS", "M-D1", "MEDIUM in her hall: Maureen picks her keys out of the bowl on the half-moon table", "lifts the keys from the bowl",
   "one lift, about a second", STILL, "hands: one grip change", "no", "absent", "—", "NB2",
   EYE, THR, "clean", "MEDIUM", "", "eyes", "medium", L(M_GREY, "L"), True)
BB("B08b", A1, "Others played sport for thirty years.", "sport", "not what you did",
   "R2", "L-D-STAIRS", "D-D1", "CU over Desmond's shoulder: his hand straightens one black-framed team photograph on the stair wall", "his fingertips level the frame",
   "one small nudge, about a second", STILL, "hands: one movement", "no", "absent", "—", "NB2",
   EYE, "ots", "through", "CU", "over his shoulder: his own memory", "hands", "shallow", L(D_GREY, "R"), False)
TH("B08-TH2", A1, "It makes almost no difference, because the load is not coming from what you did.", framing="punch")
BB("B08c", A1, "It is coming from standing up and walking.", "standing", "the cause — ordinary life",
   "R2", "L-D-STAIRS", "D-D1", "MEDIUM: Desmond sitting on the bottom stair tying a trainer, already rising — ends standing", "rises to standing",
   "about a second and a half", STILL, "standing up: start mid-movement, end on contact, 3s", "no", "absent", "—", "NB2",
   LOW, THR, "clean", "MEDIUM", "low = the effort of standing", "eyes", "deep", L(D_GREY, "L"), True, mx=3)

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

HOOKS = {1: ["HK1-a", "HK1-b", "HK1-TH"], 2: ["HK2-a", "HK2-b", "HK2-TH"], 3: ["HK3-a", "HK3-b", "HK3-TH"]}
BODY = ["B01a", "B01b", "B01-TH", "B02", "B03-TH", "B04a", "B04b", "B04c", "B05", "B06-TH", "B06", "B07-TH", "B07", "B08-TH", "B08a", "B08b", "B08-TH2", "B08c",
        "B09-TH", "B10a", "B10b", "B10c", "B10d", "B11-TH", "B12",
        "B13", "B14a", "B14b", "B14c", "B15-TH", "B15", "B16a", "B16b", "B16c", "B17a", "B17b", "B17c",
        "B18-TH", "B18a", "B18b", "B19-TH", "B19a", "B19b", "B19-TH2", "B20", "B21-TH", "B21", "B22a", "B22-TH", "B22c", "B23a", "B23b"]

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
