#!/usr/bin/env python3
"""stryde-lost-moments — step 5 act map (E4) for all five variants, one source of truth.

Writes:
  work/actmap_rows.json       every beat, E4 fields (+ §27G motion, §30I angle, §30J focus, §30K light)
  work/angles_<V>.json        each variant's full cut order for scripts/angles.py
  work/actmap.md              the act-map tables (pasted into STEP4_5.md)
Durations stay `pending-master` (E6) until the voice masters exist.
"""
import json, pathlib
HERE = pathlib.Path(__file__).parent

# Board act groups: Hook 1..5 = hooks A..E; Act 1 = shared B-roll (cut into every variant); Act 2..6 = bodies A..E.
ACT = {"A": "Act 2", "B": "Act 3", "C": "Act 4", "D": "Act 5", "E": "Act 6", "S": "Act 1"}
HOOK = {"A": "Hook 1", "B": "Hook 2", "C": "Hook 3", "D": "Hook 4", "E": "Hook 5"}

ROWS = {}
def R(beat, act, line, key, fn, subj, loc, day, framing, action, pace, camera, staging, pin, prod, vis, model,
      h, side, fg, scale, why, plane, dof, src, ks, time, arc, face, ledger="", notes="", layout="full", eg="", mx=6):
    ROWS[beat] = dict(beat=beat, act=act, line=line, key=key, function=fn, subject=subj, location=loc, story_day=day,
        framing=framing, action=action, pace=pace, camera=camera, staging=staging, pin_end=pin, max=mx,
        product=prod, visibility=vis, model=model, layout=layout, eg=eg, ledger=ledger, notes=notes,
        duration="pending-master",
        angle=dict(height=h, side=side, fg=fg, scale=scale, why=why),
        focus=dict(plane=plane, dof=dof, rack=None, moving_subject=False),
        light=dict(source=src, key_side=ks, time=time, arc=arc), face=face)

EVE, THR, PRO, FRO, BEH, OTS = "eye", "three-quarter", "profile", "front", "behind", "ots"
TQB = "three-quarter-back"
STILL, SWAY = "locked off", "sway (handheld, does not travel)"

# ------------------------------------------------------------------ shared set (Act 1)
S = "S"
R("SH-01", ACT[S], "Built over three years with orthopaedic surgeons,", "surgeons", "authority / proof", "C6", "L-CONSULT", "S6-D1",
  "MCU at her desk, the strap held still at chest height in both hands, knee model beside her", "lifts her eyes from the strap to the patient across the desk",
  "one look up, about a second", STILL, "none", "no", "held", "—", "NBP",
  EVE, THR, "clean", "MCU", "", "eyes", "medium", "blind window, west wall", "R", "afternoon", "authority: even daylight", True)
R("SH-02", ACT[S], "to do what sleeves and braces never could.", "sleeves", "objection (F1)", "G-01 hands", "L-KITCHEN", "G-01",
  "CU the open dresser drawer: a grey knit knee sleeve and a black hinged brace lying in it", "her hand pushes the drawer shut on them",
  "one push, about a second", STILL, "hands: large in frame, one movement", "no", "absent", "—", "NB2",
  "high", THR, "clean", "CU", "high = done with them, put away", "hands", "medium", "sink window, north wall", "L", "morning", "everyday", False, ledger="F1")
R("SH-03", ACT[S], "Perfect for bone on bone, arthritis, worn cartilage and meniscus pain.", "bone", "conditions", "C6 hand", "L-CONSULT", "S6-D1",
  "CU the anatomical knee model on the desk, her fingertip on the joint line", "her fingertip traces slowly along the joint line of the model",
  "one slow trace, about two seconds", STILL, "hands: large in frame, one movement", "no", "absent", "—", "NB2",
  "low", PRO, "clean", "CU", "low makes the joint big and important", "hands", "shallow", "blind window, west wall", "R", "afternoon", "authority: even daylight", False)
R("SH-04a", ACT[S], "No slipping.", "slipping", "feature", "G-02", "L-GARDEN-STEP", "G-02",
  "ECU right knee from the side as he steps up one garden step, strap seated", "one step up, weight onto the right leg",
  "one step, about a second", STILL, "stairs: side, waist-down, camera still", "no", "worn", "VISIBLE", "NBP",
  "low", PRO, "clean", "ECU", "low on the working knee", "product", "medium", "open sky, afternoon sun", "L", "afternoon", "after: sun", False)
R("SH-04b", ACT[S], "No sores.", "sores", "feature", "G-03", "L-G03-LIVING", "G-03",
  "CU seated, her fingertips run along the skin at the strap's lower edge — the skin smooth and unmarked", "fingertips slide once along the edge",
  "one slide, about a second", STILL, "hands: large in frame, one movement", "no", "worn", "VISIBLE", "NBP",
  "high", THR, "clean", "CU", "high = looking down at her own knee", "product", "medium", "living-room window, south wall", "R", "afternoon", "after: sun", False)
R("SH-04c", ACT[S], "No rolling down.", "rolling", "feature", "G-04", "L-PARK", "G-04",
  "knee-and-shin only, walking toward the lens, the strap staying put", "three walking steps toward the lens",
  "one step per second, normal walking speed", STILL, "walking toward camera: feet/knee only, 3 steps", "no", "worn", "VISIBLE", "NBP",
  "ground", FRO, "clean", "CU", "ground = steps and legs", "product", "deep", "open sky, afternoon sun", "L", "afternoon", "after: sun", False)
R("SH-05", ACT[S], "Buy one, get one free today at getstryde.co.", "Buy", "offer (EGN05)", "G-05 hands", "L-KITCHEN", "G-05",
  "overhead on the oak table: his hands lift the lid off the box; two straps lie inside side by side", "lifts the lid clear and out of frame",
  "one lift, about a second", STILL, "hands: large in frame; straps do not move", "no", "box open, two units", "—", "NBP",
  "overhead", FRO, "clean", "CU", "overhead = the everyday table, the reveal", "product", "deep", "sink window, north wall", "L", "morning", "offer: bright daylight", False,
  eg="EGN05 offer text in the edit", notes="package_open.jpg + front/back refs")
R("SH-06", ACT[S], "Sixty-day money-back guarantee.", "guarantee", "guarantee", "G-05", "L-KITCHEN", "G-05",
  "MCU at the table, the open box in front of him, he sips his tea and looks at the straps", "lowers his mug to the table",
  "one lowering, about a second", STILL, "none", "no", "box open, two units", "—", "NBP",
  EVE, THR, "clean", "MCU", "", "eyes", "medium", "sink window, north wall", "L", "morning", "offer: bright daylight", True, eg="EGN05")
R("MECH-01", ACT[S], "…seventeen times your bodyweight goes through one small spot below your kneecap.", "seventeen", "mechanism — load (EGN04)", "—", "—", "—",
  "ANAT-A: the knee in the anatomical register, load arriving down the leg to the spot below the kneecap", "load pulses down with a walking cadence",
  "one pulse per second", STILL, "none", "no", "absent", "—", "NB2",
  EVE, PRO, "clean", "CU", "profile shows the load path down the leg", "deep", "deep", "anatomical register (§12A)", "L", "—", "mechanism", False, eg="EGN04 · 17× overlay", notes="one clip, cut into all five at each variant's span")
R("MECH-02", ACT[S], "This strap redirects the load away from the worn spot. (A C E) · catches the weight before it hits the knee. (B) · takes the weight off it. (D)", "strap", "mechanism — protection (EGN04, F2)", "—", "—", "—",
  "ANAT-A: the strap seated below the kneecap, the pad taking the load, the worn spot calming", "the red at the spot fades as the pad takes the load",
  "one fade, about two seconds", STILL, "none", "no", "worn (anatomical)", "—", "NB2",
  "low", THR, "clean", "CU", "low = the fix, resolve", "deep", "deep", "anatomical register (§12A)", "L", "—", "mechanism", False, eg="EGN04", ledger="F2")
R("NS-03a", ACT[S], "Adjustable, breathable, (A B C E)", "Adjustable", "SEAT (fit, never adjusting — F6)", "G-06", "L-G06-BEDROOM", "G-06",
  "CU seated on the edge of a bed, both hands slide the closed strap up the shin to seat it", "slides up the last few centimetres and stops at contact",
  "one slide, about a second", STILL, "hands: start mid-movement, end on contact", "no", "seated", "VISIBLE", "NBP",
  "high", THR, "clean", "CU", "high = his own view of his knee", "product", "medium", "bedroom window, east wall", "R", "morning", "after: fresh daylight", False, ledger="F6")
R("NS-03b", ACT[S], "with a silicone pad that locks the pressure right where you need it. (A C)", "pad", "product — the pad (PAD_BACK_SHOT)", "G-06 hands", "L-G06-BEDROOM", "G-06",
  "CU hands hold the strap and tip it so the inner pad faces the lens", "one tilt of the strap toward the lens",
  "one tilt, about a second", STILL, "turning the product: pin the end frame", "yes", "held — the pad", "—", "NBP",
  EVE, FRO, "clean", "CU", "", "product", "medium", "bedroom window, east wall", "R", "morning", "after: fresh daylight", False, ledger="F8", notes="prompt says 'the pad', never 'silicone'")
R("NS-04b", ACT[S], "light enough you forget it's there. (B E)", "forget", "feature", "G-07", "L-G07-GARDEN", "G-07",
  "MEDIUM at a garden table doing a crossword, strap on her knee under the table edge", "fills in one word with her pen",
  "a few pen strokes, about two seconds", STILL, "none", "no", "worn", "VISIBLE", "NBP",
  "low", THR, "clean", "MEDIUM", "low keeps the knee and her face in one frame", "deep", "deep", "open sky, afternoon sun", "R", "afternoon", "after: sun", True)
R("NS-05", ACT[S], "Recommended by orthopaedic surgeons for lasting relief. (A C E)", "Recommended", "recommendation (F3)", "C6", "L-CONSULT", "S6-D1",
  "MCU over the patient's shoulder: C6 hands the strap across the desk", "passes the strap into the patient's hand",
  "one pass, about a second", STILL, "hands: one grip change", "no", "held", "—", "NBP",
  EVE, OTS, "through", "MCU", "over the shoulder puts us in the patient's chair", "eyes", "medium", "blind window, west wall", "R", "afternoon", "authority: even daylight", True, ledger="F3")
R("NS-06", ACT[S], "Sits flat under your trousers. (C D)", "trousers", "REVEAL→CONCEALED (§9D)", "G-09", "L-G09-HALL", "G-09",
  "CU from the side: he lets his chino leg drop over the strap; the fabric lies flat", "the trouser leg falls and settles",
  "one drop, about a second", STILL, "none", "no", "worn", "REVEAL", "NBP",
  EVE, PRO, "clean", "CU", "profile shows the flat line of the trouser", "product", "medium", "hall door glass, north wall", "L", "morning", "after: fresh daylight", False, ledger="F10")
R("NS-07", ACT[S], "Over two hundred thousand people wear one now. (B D)", "people", "social proof", "G-10 group", "L-PARK", "G-10",
  "MEDIUM four walkers side by side on the park path, a strap on the nearest knee", "three steps toward the lens",
  "one step per second", STILL, "walking toward camera: waist-down, 3 steps", "no", "worn", "VISIBLE", "NBP",
  "low", THR, "clean", "MEDIUM", "low = many, strong", "deep", "deep", "open sky, afternoon sun", "L", "afternoon", "after: sun", False, eg="200,000+ overlay")

SHARED_A = ["SH-01", "SH-02", "SH-03"]
SH04 = ["SH-04a", "SH-04b", "SH-04c"]

# ------------------------------------------------------------------ A — Forwards (Gloria)
V = "A"
R("A-HKa", HOOK[V], "Too bad you can't go down the stairs forwards.", "", "hook — the loss (EGN01)", "C1", "L-G-STAIRS", "G-D1",
  "from the side, waist-down: she comes down sideways, both hands on the rail", "one sideways step down",
  "one step, about a second and a half", STILL, "stairs: side, waist-down, camera still, hands on the rail visible", "no", "absent", "—", "NB2",
  EVE, PRO, "through", "MEDIUM", "through the spindles: we watch her struggle", "deep", "deep", "landing window, south wall", "L", "morning", "problem: grey", False, ledger="VN02", eg="EGN01")
R("A-HKb", HOOK[V], "Thanks to these life-changing knee straps, not for much longer.", "straps", "hook — the fix (EGN01)", "C1", "L-G-STAIRS", "G-D1",
  "CU sitting on the bottom stair, both hands slide the strap up her right shin to seat it", "slides up the last few centimetres, stops at contact",
  "one slide, about a second", STILL, "hands: start mid-movement, end on contact", "no", "seated", "VISIBLE", "NBP",
  "high", THR, "clean", "CU", "high = her own view of her knee", "product", "medium", "front-door glass, west wall", "R", "morning", "turn: window side", False, ledger="VN02", eg="whoosh on the cut")
R("A-01", ACT[V], "On every step down,", "step", "problem", "C1", "L-G-STAIRS", "G-D1",
  "MCU at the top of the stairs, looking down the flight, hand on the rail", "she draws one breath before the first step",
  "one breath, about a second", STILL, "none", "no", "absent", "—", "NB2",
  "high", THR, "clean", "MCU", "high = the drop in front of her, small", "eyes", "medium", "landing window, south wall", "R", "morning", "problem: grey", True)
R("A-02", ACT[V], "That's why you turn sideways.", "sideways", "problem", "C1", "L-G-STAIRS", "G-D1",
  "ECU her slippers turned sideways on the stair runner", "one foot slides down to the next step, sideways",
  "one step, about a second and a half", STILL, "stairs: side, feet only", "no", "absent", "—", "NB2",
  "ground", THR, "clean", "ECU", "ground = feet and steps", "foreground", "shallow", "landing window, south wall", "L", "morning", "problem: grey", False)
R("A-03", ACT[V], "That's why you grip the railing.", "railing", "problem", "C1 hand", "L-G-STAIRS", "G-D1",
  "CU her hand clamped white-knuckled on the mahogany rail", "her grip tightens as her weight comes down",
  "one squeeze, about a second", STILL, "hands: large in frame", "no", "absent", "—", "NB2",
  EVE, PRO, "clean", "CU", "profile runs the rail across the frame", "hands", "shallow", "landing window, south wall", "L", "morning", "problem: grey", False)
R("A-04", ACT[V], "And the pain just lifts.", "lifts", "turn — relief", "C1", "L-G-STAIRS", "G-D2",
  "MCU on the landing, her face easing, the strap on (below frame)", "her shoulders drop as she breathes out",
  "one breath out, about two seconds", STILL, "none", "no", "worn (out of frame)", "—", "NB2",
  EVE, THR, "clean", "MCU", "", "eyes", "medium", "landing window, south wall", "L", "afternoon", "turn: the window side of the face", True)
R("A-05", ACT[V], "So you come down facing forwards.", "forwards", "after-state", "C1", "L-G-STAIRS", "G-D2",
  "from the side, waist-down: she comes down facing forwards, one hand resting lightly on the rail, strap on her right knee", "one step down, facing forwards",
  "one step, about a second", STILL, "stairs: side, waist-down, camera still", "no", "worn", "VISIBLE", "NBP",
  EVE, PRO, "clean", "MEDIUM", "profile answers the hook's side view", "product", "medium", "front-door glass, west wall", "R", "afternoon", "after: sun through the door glass", False, eg="mirror of A-HKa", notes="mirror_of A-HKa")
R("A-06", ACT[V], "One foot per step.", "foot", "after-state (EGN03 punch-in)", "C1", "L-G-STAIRS", "G-D2",
  "ECU from the hall floor: her feet come down the last two steps, one foot per step, toward the lens", "two steps down",
  "one step per second", STILL, "stairs: feet only, two steps", "no", "worn (knee at top of frame)", "VISIBLE", "NBP",
  "ground", FRO, "clean", "ECU", "ground = the steps themselves", "foreground", "medium", "front-door glass, west wall", "R", "afternoon", "after: sun through the door glass", False, eg="EGN03")
R("A-07", ACT[V], "Like a normal person again.", "normal", "after-state", "C1", "L-G-STAIRS", "G-D2",
  "MEDIUM from behind, waist-up: she walks away down the hall towards the bright kitchen doorway", "three steps away from the lens",
  "one step per second", STILL, "walking away: waist-up, 3 steps", "no", "worn (out of frame)", "—", "NB2",
  EVE, BEH, "clean", "MEDIUM", "behind = we let her go, she doesn't need us", "deep", "deep", "kitchen window, east (far end)", "back", "afternoon", "after: the bright doorway ahead", False, notes="backlit on purpose: walking into the light; face not in frame")
R("A-08", ACT[V], "Put one on.", "", "SEAT — callback", "C1", "L-G-STAIRS", "G-D1",
  "reuse A-HKb (the seat), second half", "—", "—", STILL, "reuse", "no", "seated", "VISIBLE", "reuse",
  "high", THR, "clean", "CU", "high = her own view of her knee", "product", "medium", "front-door glass, west wall", "R", "morning", "turn: window side", False, notes="reuse A-HKb — no new generation")
R("A-09", ACT[V], "Go to your own stairs.", "stairs", "close — callback", "C1", "L-G-STAIRS", "G-D1",
  "MEDIUM from the hall: she stands at the foot of the stairs, hand on the newel, and looks up the flight", "she lifts her eyes up the stairs",
  "one look up, about a second", STILL, "none", "no", "worn", "VISIBLE", "NBP",
  "low", THR, "clean", "MEDIUM", "low = resolve, she's ready", "eyes", "medium", "front-door glass, west wall", "R", "morning", "turn: window side", True)
R("A-10", ACT[V], "Nothing to lose but the pain.", "pain", "close", "C1", "L-G-STAIRS", "G-D2",
  "MCU on the landing, a small smile as she starts down", "she starts to smile",
  "one smile, about a second", STILL, "none", "no", "worn (out of frame)", "—", "NB2",
  "high", THR, "clean", "MCU", "high = the stairs below her, beaten", "eyes", "medium", "landing window, south wall", "L", "afternoon", "after: sun", True)
ORDER_A = ["A-HKa", "A-HKb"] + SHARED_A + ["A-01", "MECH-01", "A-02", "A-03", "MECH-02", "A-04", "A-05", "A-06", "A-07",
           "NS-03a", "NS-03b"] + SH04 + ["NS-05", "SH-05", "SH-06", "A-08", "A-09", "A-10"]

# ------------------------------------------------------------------ B — Walk far (Sheila)
V = "B"
R("B-HKa", HOOK[V], "Too bad you can't walk far without stopping anymore.", "", "hook — the loss (EGN01)", "C2", "L-HIGHST", "S2-D1",
  "MEDIUM: she sinks onto the high-street bench, shopping bag at her feet, hand to her knee", "sits down — hips already moving, ends on contact",
  "about a second and a half", STILL, "sitting down: start mid-movement, end on contact, 3s", "no", "absent", "—", "NB2",
  EVE, THR, "clean", "MEDIUM", "", "eyes", "deep", "overcast sky", "L", "morning", "problem: grey", True, ledger="VN03", eg="EGN01", mx=3)
R("B-HKb", HOOK[V], "Thanks to these life-changing knee straps, that's about to change.", "straps", "hook — the fix (EGN01)", "C2", "L-HIGHST", "S2-D1",
  "CU on the bench, both hands slide the strap up her right shin to seat it", "slides up the last few centimetres, stops at contact",
  "one slide, about a second", STILL, "hands: start mid-movement, end on contact", "no", "seated", "VISIBLE", "NBP",
  "high", THR, "clean", "CU", "high = her own view of her knee", "product", "medium", "overcast sky", "L", "morning", "turn", False, ledger="VN03", eg="whoosh on the cut")
R("B-01", ACT[V], "Every stride puts", "stride", "problem", "C2", "L-HIGHST", "S2-D1",
  "her grey trainers mid-stride on the paving, feet only, from the side", "two strides across the frame",
  "one step per second", STILL, "walking: feet only", "no", "absent", "—", "NB2",
  "ground", PRO, "clean", "CU", "ground = strides", "foreground", "medium", "overcast sky", "L", "morning", "problem: grey", False)
R("B-02", ACT[V], "By the end of the road, that spot has had enough.", "end", "problem", "C2", "L-HIGHST", "S2-D1",
  "MEDIUM waist-up: she slows to a stop by the lamppost", "two slowing steps, then stops",
  "slowing, about two seconds", STILL, "walking toward camera: waist-up, 2 steps", "no", "absent", "—", "NB2",
  EVE, THR, "clean", "MEDIUM", "", "eyes", "deep", "overcast sky", "R", "morning", "problem: grey", True)
R("B-03", ACT[V], "So you stop.", "stop", "problem", "C2 hand", "L-HIGHST", "S2-D1",
  "CU her hand on the lamppost, the other pressing just below her kneecap", "her hand presses the knee",
  "one press, about a second", STILL, "hands: large in frame", "no", "absent", "—", "NB2",
  "high", THR, "clean", "CU", "high = small, stopped", "hands", "shallow", "overcast sky", "R", "morning", "problem: grey", False)
R("B-04", ACT[V], "The pain is pressure. Nothing more.", "pressure", "product — placement", "C2", "L-HIGHST", "S2-D1",
  "ECU the strap seated on her right knee on the bench, her palm resting just above the kneecap", "her palm settles on the knee",
  "one settle, about a second", STILL, "none", "no", "worn", "VISIBLE", "NBP",
  EVE, FRO, "clean", "ECU", "", "product", "medium", "overcast sky", "L", "morning", "turn", False)
R("B-05", ACT[V], "Take the pressure off, and you keep going.", "going", "turn", "C2", "L-HIGHST", "S2-D1",
  "MEDIUM: she rises from the bench, weight already forward, and sets off", "stands up — already rising — then one step",
  "about two seconds", STILL, "standing up: start mid-movement, end on contact, 3s", "no", "worn", "VISIBLE", "NBP",
  "low", PRO, "clean", "MEDIUM", "low = resolve", "deep", "deep", "overcast sky", "L", "morning", "turn", True, mx=3)
R("B-06", ACT[V], "To the shops and back.", "shops", "after-state", "C2", "L-HIGHST", "S2-D2",
  "MEDIUM waist-up: she walks out of the greengrocer's toward the lens, a full bag in hand", "three steps toward the lens",
  "one step per second", STILL, "walking toward camera: waist-up, 3 steps", "no", "worn (out of frame)", "—", "NB2",
  EVE, THR, "clean", "MEDIUM", "", "eyes", "deep", "sun, south-west", "R", "afternoon", "after: sun", True)
R("B-07", ACT[V], "Round the park, the long way.", "park", "after-state (EGN03 punch-in)", "C2", "L-PARK", "S2-D2",
  "WIDE: a small figure walking away along the long branch of the path under the plane trees", "she walks on, small in the frame",
  "one step per second", STILL, "walking away: wide, small figure", "no", "worn (too small to read)", "—", "NB2",
  "high", BEH, "clean", "WIDE", "high and behind: the long way ahead of her", "deep", "deep", "sun, south-west", "back", "afternoon", "after: sun", False, eg="EGN03", notes="backlit on purpose: into the sun; no face")
R("B-08", ACT[V], "Two miles, if you fancy it.", "miles", "after-state (F7)", "C2", "L-PARK", "S2-D2",
  "her trainers and knees walking on the path, feet only, the strap on", "two strides",
  "one step per second", STILL, "walking: feet only", "no", "worn", "VISIBLE", "NBP",
  "ground", THR, "clean", "CU", "ground = strides", "product", "medium", "sun, south-west", "L", "afternoon", "after: sun", False, ledger="F7")
R("B-09", ACT[V], "Go the long way round.", "long", "close — callback", "C2", "L-PARK", "S2-D2",
  "MEDIUM from behind at the fork: she takes the long branch", "three steps onto the long branch",
  "one step per second", STILL, "walking away: waist-up, 3 steps", "no", "worn", "VISIBLE", "NBP",
  EVE, TQB, "clean", "MEDIUM", "three-quarter-back: we see her choose", "deep", "deep", "sun, south-west", "R", "afternoon", "after: sun", False)
R("B-10", ACT[V], "Nothing to lose but the pain.", "pain", "close", "C2", "L-PARK", "S2-D2",
  "MCU on the path, face lifted to the sun, a small smile", "she smiles",
  "one smile, about a second", STILL, "none", "no", "worn (out of frame)", "—", "NB2",
  "low", THR, "clean", "MCU", "low = she's won", "eyes", "medium", "sun, south-west", "L", "afternoon", "after: sun", True)
ORDER_B = ["B-HKa", "B-HKb"] + SHARED_A + ["B-01", "MECH-01", "B-02", "B-03", "MECH-02", "B-04", "B-05", "B-06", "B-07", "B-08",
           "NS-03a", "NS-04b"] + SH04 + ["NS-07", "SH-05", "SH-06", "B-09", "B-10"]

# ------------------------------------------------------------------ C — Dog (Winston)
V = "C"
R("C-HKa", HOOK[V], "Too bad someone else walks your dog now.", "", "hook — the loss (EGN01)", "C3 + G-12 neighbour + DOG", "L-W-FRONTROOM", "W-D1",
  "over his shoulder through the bay window: a neighbour walks Bramble past the front gate", "the neighbour and the dog cross the window",
  "normal walking speed", STILL, "walking across frame, outside, small", "no", "absent", "—", "NB2",
  EVE, OTS, "through", "MEDIUM", "over his shoulder: we watch with him", "background", "medium", "bay window, south-east", "back", "morning", "problem: grey", False,
  ledger="VN04", eg="EGN01", notes="backlit on purpose: he watches through the window; his face not in frame")
R("C-HKb", HOOK[V], "Thanks to these life-changing knee straps, not for much longer.", "straps", "hook — the fix (EGN01)", "C3", "L-W-FRONTROOM", "W-D1",
  "CU in the armchair, both hands slide the strap up his right shin to seat it", "slides up the last few centimetres, stops at contact",
  "one slide, about a second", STILL, "hands: start mid-movement, end on contact", "no", "seated", "VISIBLE", "NBP",
  "high", THR, "clean", "CU", "high = his own view of his knee", "product", "medium", "bay window, south-east", "L", "morning", "turn", False, ledger="VN04", eg="whoosh on the cut")
R("C-01", ACT[V], "Here's why the walks got shorter.", "shorter", "problem", "C3 + DOG", "L-W-GATE", "W-D1",
  "MEDIUM at his front gate, Bramble pulling ahead on the lead, he holds back, hand on his knee", "the dog leans on the lead; he stays put",
  "about two seconds", STILL, "none", "no", "absent", "—", "NB2",
  EVE, THR, "clean", "MEDIUM", "", "eyes", "deep", "overcast sky", "R", "morning", "problem: grey", True)
R("C-02", ACT[V], "Every stride,", "stride", "problem", "C3 + DOG", "L-BLOCK", "W-D1",
  "his boots and the dog's paws on the pavement, feet only, from the side", "two strides",
  "one step per second", STILL, "walking: feet only", "no", "absent", "—", "NB2",
  "ground", PRO, "clean", "CU", "ground = strides", "foreground", "medium", "overcast sky", "L", "morning", "problem: grey", False)
R("C-03", ACT[V], "And the pain just lifts.", "lifts", "turn — relief", "C3", "L-FIELD", "W-D2",
  "MCU in the field, his face easing as he breathes out", "shoulders drop on one breath out",
  "about two seconds", STILL, "none", "no", "worn (out of frame)", "—", "NB2",
  EVE, THR, "clean", "MCU", "", "eyes", "medium", "sun, south", "L", "afternoon", "turn: the window side of the face", True)
R("C-04", ACT[V], "So you take the lead back.", "lead", "after-state", "C3 hand + G-12 hand", "L-W-GATE", "W-D2",
  "CU hands at the gate: the neighbour's hand passes the red lead into his big hand", "the lead passes from her hand to his",
  "one pass, about a second", STILL, "hands: one grip change", "no", "absent", "—", "NB2",
  EVE, PRO, "clean", "CU", "profile: the handover across the frame", "hands", "shallow", "sun, south", "R", "afternoon", "after: sun", False)
R("C-05", ACT[V], "Round the block first.", "block", "after-state", "C3 + DOG", "L-BLOCK", "W-D2",
  "MEDIUM waist-up: he walks toward the lens along the residential street, the dog at heel", "three steps toward the lens",
  "one step per second", STILL, "walking toward camera: waist-up, 3 steps", "no", "worn (out of frame)", "—", "NB2",
  EVE, THR, "clean", "MEDIUM", "", "eyes", "deep", "sun, south", "L", "afternoon", "after: sun", True)
R("C-06", ACT[V], "Then the field.", "field", "after-state", "C3 + DOG", "L-FIELD", "W-D2",
  "WIDE: man and dog small on the field path, the dog bounding ahead", "they walk on along the path",
  "normal walking speed", STILL, "wide, small figures", "no", "worn (too small to read)", "—", "NB2",
  "high", THR, "clean", "WIDE", "high = the whole field open to them", "deep", "deep", "sun, south", "R", "afternoon", "after: sun", False)
R("C-07", ACT[V], "Then the long loop you both miss.", "loop", "after-state (EGN03 punch-in)", "C3 + DOG", "L-FIELD", "W-D2",
  "MEDIUM from behind along the hedge path, the dog trotting ahead, his knee strap on", "three steps away along the path",
  "one step per second", STILL, "walking away: waist-down, 3 steps", "no", "worn", "VISIBLE", "NBP",
  "low", TQB, "clean", "MEDIUM", "low and behind: the path ahead, resolve", "deep", "deep", "sun, south", "R", "afternoon", "after: sun", False, eg="EGN03")
R("C-08", ACT[V], "Get the lead.", "lead", "close — callback", "C3 hand + DOG", "L-W-HALL", "W-D2",
  "CU his hand lifts the red lead off the hook in the hall, Bramble's head at his knee", "lifts the lead off the hook",
  "one lift, about a second", STILL, "hands: one movement", "no", "absent", "—", "NB2",
  "low", THR, "clean", "CU", "low = the dog's-eye view, ready", "hands", "shallow", "front-door glass, south-east", "L", "afternoon", "after: sun", False)
R("C-09", ACT[V], "Nothing to lose but the pain.", "pain", "close", "C3 + DOG", "L-FIELD", "W-D2",
  "MCU in the field, the dog at his side, he laughs", "he laughs once",
  "one laugh, about a second", STILL, "none", "no", "worn (out of frame)", "—", "NB2",
  EVE, THR, "clean", "MCU", "", "eyes", "medium", "sun, south", "L", "afternoon", "after: sun", True)
ORDER_C = ["C-HKa", "C-HKb"] + SHARED_A + ["C-01", "C-02", "MECH-01", "MECH-02", "C-03", "C-04", "C-05", "C-06", "C-07",
           "NS-03a", "NS-03b"] + SH04 + ["NS-06", "NS-05", "SH-05", "SH-06", "C-08", "C-09"]

# ------------------------------------------------------------------ D — Golf (Graham)
V = "D"
R("D-HKa", HOOK[V], "Too bad your golf clubs are still in the garage.", "", "hook — the loss (EGN01)", "C4", "L-GARAGE", "Gr-D1",
  "MEDIUM: he stands in the garage looking at the golf bag under its dust sheet", "a slow push-in on him, he stays still",
  "one slow push-in over the clip", "one slow push-in (subject still)", "none", "no", "absent", "—", "NB2",
  EVE, TQB, "through", "MEDIUM", "past the covered bag: what he's lost is in the foreground", "background", "medium", "garage door, north", "R", "morning", "problem: grey", False,
  ledger="VN05", eg="EGN01")
R("D-HKb", HOOK[V], "Thanks to these life-changing knee straps, not for much longer.", "straps", "hook — the fix (EGN01)", "C4", "L-GARAGE", "Gr-D1",
  "CU on the step stool, both hands slide the strap up his right shin to seat it", "slides up the last few centimetres, stops at contact",
  "one slide, about a second", STILL, "hands: start mid-movement, end on contact", "no", "seated", "VISIBLE", "NBP",
  "high", THR, "clean", "CU", "high = his own view of his knee", "product", "medium", "garage door, north", "L", "morning", "turn", False, ledger="VN05", eg="whoosh on the cut")
R("D-01", ACT[V], "A round is hours on your feet.", "hours", "problem", "C4 + G-13 partner", "L-COURSE", "Gr-D2",
  "WIDE: two golfers walking up a long fairway, small in frame", "they walk on up the fairway",
  "normal walking speed", STILL, "wide, small figures", "no", "absent", "—", "NB2",
  "high", BEH, "clean", "WIDE", "high and behind: the long way to go", "deep", "deep", "overcast sky", "back", "afternoon", "problem: grey", False)
R("D-02", ACT[V], "Every stride,", "stride", "problem", "C4", "L-COURSE", "Gr-D2",
  "his golf shoes walking on fairway grass, feet only, from the side", "two strides",
  "one step per second", STILL, "walking: feet only", "no", "absent", "—", "NB2",
  "ground", PRO, "clean", "CU", "ground = strides", "foreground", "medium", "overcast sky", "L", "afternoon", "problem: grey", False)
R("D-03", ACT[V], "By the back nine, that spot is finished.", "finished", "problem", "C4", "L-COURSE", "Gr-D2",
  "MEDIUM: he's stopped on the fairway, leaning on a club, other hand on his knee", "he shifts his weight onto the club",
  "one shift, about a second", STILL, "none", "no", "absent", "—", "NB2",
  "high", THR, "clean", "MEDIUM", "high = small, beaten", "eyes", "deep", "overcast sky", "R", "afternoon", "problem: grey", True)
R("D-04", ACT[V], "This strap sits two centimetres below the kneecap", "kneecap", "product — placement (F5)", "C4", "L-COURSE", "Gr-D3",
  "ECU his right knee, the strap seated, the kneecap sitting in the notch (PLACE-LOCK, contact)", "his fingertip taps once below the notch",
  "one tap", STILL, "none", "no", "worn", "VISIBLE", "NBP",
  EVE, FRO, "clean", "ECU", "", "product", "medium", "sun, south-west", "L", "afternoon", "after: sun", False, ledger="F5")
R("D-05", ACT[V], "And the pain just lifts.", "lifts", "turn — relief", "C4", "L-COURSE", "Gr-D3",
  "MCU on the tee, his face easing, club in hand", "shoulders drop on one breath out",
  "about two seconds", STILL, "none", "no", "worn (out of frame)", "—", "NB2",
  EVE, THR, "clean", "MCU", "", "eyes", "medium", "sun, south-west", "L", "afternoon", "turn: the window side of the face", True)
R("D-06", ACT[V], "So you walk the course instead of watching it.", "walk", "after-state", "C4", "L-COURSE", "Gr-D3",
  "MEDIUM waist-up: he walks past the parked buggy toward the lens, bag on his shoulder", "three steps toward the lens",
  "one step per second", STILL, "walking toward camera: waist-up, 3 steps", "no", "worn (out of frame)", "—", "NB2",
  "low", THR, "clean", "MEDIUM", "low = resolve", "eyes", "deep", "sun, south-west", "R", "afternoon", "after: sun", True)
R("D-07", ACT[V], "All eighteen.", "eighteen", "after-state (EGN03 punch-in)", "C4 hands", "L-COURSE", "Gr-D3",
  "CU his hand drops the flag back into the hole on the last green", "the flagstick slides into the cup",
  "one drop, about a second", STILL, "hands: one movement", "no", "absent", "—", "NB2",
  "high", THR, "clean", "CU", "high = the hole, done", "hands", "shallow", "sun, south-west", "L", "afternoon", "after: sun", False, eg="EGN03")
R("D-08", ACT[V], "No buggy.", "buggy", "after-state", "C4", "L-COURSE", "Gr-D3",
  "WIDE from behind: he walks off the green carrying his bag, the empty buggy parked", "he walks away across the green",
  "normal walking speed", STILL, "wide, small figure", "no", "worn (too small to read)", "—", "NB2",
  EVE, BEH, "clean", "WIDE", "behind = he's walking on, we watch him go", "deep", "deep", "sun, south-west", "back", "afternoon", "after: sun", False, notes="backlit on purpose: evening-side sun; no face")
R("D-09", ACT[V], "Sports doctors recommend it.", "doctors", "recommendation (F4)", "G-11 sports doctor", "L-SPORTSMED", "G-11",
  "MCU in a sports-medicine room, he holds the strap up and looks from it to his patient", "lifts his eyes from the strap to the patient",
  "one look up, about a second", STILL, "none", "no", "held", "—", "NBP",
  EVE, THR, "clean", "MCU", "", "eyes", "medium", "clinic window, west", "L", "afternoon", "authority: even daylight", True, ledger="F4")
R("D-10", ACT[V], "One for each knee.", "each", "product (F12)", "C4", "L-COURSE", "Gr-D3",
  "ECU seated on the course bench: a strap on each knee", "he rests both hands on his thighs",
  "one settle, about a second", STILL, "none", "no", "worn ×2", "VISIBLE", "NBP",
  EVE, FRO, "clean", "ECU", "", "product", "medium", "sun, south-west", "R", "afternoon", "after: sun", False, ledger="F12")
R("D-11", ACT[V], "Book the tee time.", "tee", "close — callback", "C4", "L-GARAGE", "Gr-D3",
  "MEDIUM: he swings the uncovered golf bag onto his shoulder in the open garage door", "the bag settles on his shoulder",
  "one swing, about a second", STILL, "none", "no", "worn", "VISIBLE", "NBP",
  "low", THR, "clean", "MEDIUM", "low = resolve; mirror of the covered bag", "eyes", "deep", "garage door, north", "R", "afternoon", "after: sun on the drive", True, notes="mirror_of D-HKa")
R("D-12", ACT[V], "Nothing to lose but the pain.", "pain", "close", "C4", "L-COURSE", "Gr-D3",
  "MCU on the first tee, a small smile", "he smiles",
  "one smile, about a second", STILL, "none", "no", "worn (out of frame)", "—", "NB2",
  "high", THR, "clean", "MCU", "high = the course laid out below him", "eyes", "medium", "sun, south-west", "L", "afternoon", "after: sun", True)
ORDER_D = ["D-HKa", "D-HKb"] + SHARED_A + ["D-01", "D-02", "MECH-01", "D-03", "D-04", "MECH-02", "D-05", "D-06", "D-07", "D-08",
           "NS-06"] + SH04 + ["D-09", "NS-07", "SH-05", "D-10", "SH-06", "D-11", "D-12"]

# ------------------------------------------------------------------ E — Floor (Clifton)
V = "E"
R("E-HKa", HOOK[V], "Too bad you can't get down on the floor with the grandkids.", "", "hook — the loss (EGN01)", "C5 + GK1 + GK2", "L-C-LIVING", "Cl-D1",
  "MEDIUM from above: he sits on the sofa edge, hands on his knees, the kids playing with the train on the rug below", "he leans forward, then stops",
  "one lean, about a second", STILL, "none", "no", "absent", "—", "NB2",
  "high", THR, "clean", "MEDIUM", "high = small, stuck on the sofa", "eyes", "deep", "patio doors, south", "L", "morning", "problem: grey", True, ledger="VN06", eg="EGN01")
R("E-HKb", HOOK[V], "Thanks to these life-changing knee straps, it doesn't have to stay that way.", "straps", "hook — the fix (EGN01)", "C5", "L-C-LIVING", "Cl-D1",
  "CU on the sofa, both hands slide the strap up his right shin to seat it", "slides up the last few centimetres, stops at contact",
  "one slide, about a second", STILL, "hands: start mid-movement, end on contact", "no", "seated", "VISIBLE", "NBP",
  EVE, PRO, "clean", "CU", "profile: the shin and the hands in one line", "product", "medium", "patio doors, south", "L", "morning", "turn", False, ledger="VN06", eg="whoosh on the cut")
R("E-01", ACT[V], "It's not getting down that stops you.", "down", "problem", "C5", "L-C-LIVING", "Cl-D1",
  "MCU on the sofa, looking down at the rug, not moving", "he looks down at the kids",
  "one look down, about a second", STILL, "none", "no", "absent", "—", "NB2",
  EVE, THR, "clean", "MCU", "", "eyes", "medium", "patio doors, south", "R", "morning", "problem: grey", True)
R("E-02", ACT[V], "It's getting back up.", "up", "problem", "C5 hand", "L-C-LIVING", "Cl-D1",
  "CU his hand pushing down hard on the sofa arm, knuckles straining", "his hand presses down",
  "one press, about a second", STILL, "hands: large in frame", "no", "absent", "—", "NB2",
  "high", THR, "clean", "CU", "high = the weight he has to lift", "hands", "shallow", "patio doors, south", "L", "morning", "problem: grey", False)
R("E-03", ACT[V], "And the pain just lifts.", "lifts", "turn — relief", "C5", "L-C-LIVING", "Cl-D2",
  "MCU kneeling on the rug, his face easing", "shoulders drop on one breath out",
  "about two seconds", STILL, "none", "no", "worn (out of frame)", "—", "NB2",
  "low", THR, "clean", "MCU", "low = down at the kids' level now", "eyes", "medium", "patio doors, south", "L", "afternoon", "turn: the window side of the face", True)
R("E-04", ACT[V], "So you get down among the toys.", "toys", "after-state", "C5 + GK1 + GK2", "L-C-LIVING", "Cl-D2",
  "MEDIUM: he lowers onto one knee on the rug beside the kids — hips already moving, ends on contact", "kneels down, ends on contact",
  "about a second and a half", STILL, "sitting down: start mid-movement, end on contact, 3s", "no", "worn", "VISIBLE", "NBP",
  "high", THR, "clean", "MEDIUM", "high = down among the toys, the whole kneel", "deep", "deep", "patio doors, south", "L", "afternoon", "after: sun", False, mx=3)
R("E-05", ACT[V], "And you get back up on your own.", "own", "after-state (EGN03 punch-in)", "C5", "L-C-LIVING", "Cl-D2",
  "MEDIUM: he rises from the kneel with no hands — already rising — to standing", "stands up, ends upright",
  "about a second and a half", STILL, "standing up: start mid-movement, end on contact, 3s", "no", "worn", "VISIBLE", "NBP",
  "low", THR, "clean", "MEDIUM", "low = resolve, he rises into the frame", "eyes", "deep", "patio doors, south", "R", "afternoon", "after: sun", True, eg="EGN03", mx=3)
R("E-06", ACT[V], "No hand on the sofa.", "hand", "after-state", "C5 hands", "L-C-LIVING", "Cl-D2",
  "CU his hands holding a wooden engine, the empty sofa arm behind", "he turns the engine over in his fingers once",
  "one turn, about a second", STILL, "hands: one movement", "no", "absent", "—", "NB2",
  EVE, THR, "clean", "CU", "", "hands", "shallow", "patio doors, south", "L", "afternoon", "after: sun", False)
R("E-07", ACT[V], "Nobody hauling you up.", "Nobody", "after-state", "C5 + GK1 + GK2", "L-C-LIVING", "Cl-D2",
  "WIDE: he stands on the rug, the kids reaching up to take his hands", "the kids take his hands",
  "about a second", STILL, "none", "no", "worn", "VISIBLE", "NBP",
  "high", THR, "clean", "WIDE", "high = the whole room, the family", "deep", "deep", "patio doors, south", "R", "afternoon", "after: sun", False)
R("E-08", ACT[V], "They won't be little for long.", "little", "close — callback", "GK1 + GK2 + C5", "L-C-LIVING", "Cl-D2",
  "MEDIUM from behind the kids: they build the track, Clifton kneeling beside them", "the girl clicks one piece of track into place",
  "one click, about a second", STILL, "hands: one movement", "no", "worn", "VISIBLE", "NBP",
  "ground", TQB, "clean", "MEDIUM", "ground = their level, their world", "background", "medium", "patio doors, south", "L", "afternoon", "after: sun", False)
R("E-09", ACT[V], "Nothing to lose but the pain.", "pain", "close", "C5", "L-C-LIVING", "Cl-D2",
  "MCU on the rug, laughing with the kids", "he laughs once",
  "one laugh, about a second", STILL, "none", "no", "worn (out of frame)", "—", "NB2",
  EVE, THR, "clean", "MCU", "", "eyes", "medium", "patio doors, south", "L", "afternoon", "after: sun", True)
ORDER_E = ["E-HKa", "E-HKb"] + SHARED_A + ["E-01", "E-02", "MECH-01", "MECH-02", "E-03", "E-04", "E-05", "E-06", "E-07",
           "NS-03a", "NS-04b"] + SH04 + ["NS-05", "SH-05", "SH-06", "E-08", "E-09"]

ORDERS = {"A": ORDER_A, "B": ORDER_B, "C": ORDER_C, "D": ORDER_D, "E": ORDER_E}

def angles_rows(v):
    out = []
    for b in ORDERS[v]:
        r = ROWS[b]; a = r["angle"]
        out.append(dict(beat=b, group=v, type="MECH" if b.startswith("MECH") else "BR", subject=r["subject"].split(" ")[0],
            height=a["height"], side=a["side"], scale=a["scale"], fg=a["fg"], why=a["why"], mirror_of=None, mode=1,
            product_beat=r["focus"]["plane"] == "product", focus=r["focus"], story_day=r["story_day"], face=r["face"],
            light=dict(source=r["light"]["source"], key_side=r["light"]["key_side"], time=r["light"]["time"],
                       arc=r["light"]["arc"], why=r["notes"] if r["light"]["key_side"] == "back" else "")))
    return out

if __name__ == "__main__":
    used = {b for o in ORDERS.values() for b in o}
    assert used == set(ROWS), set(ROWS) ^ used
    json.dump(list(ROWS.values()), open(HERE / "actmap_rows.json", "w"), indent=1)
    for v in ORDERS:
        json.dump(angles_rows(v), open(HERE / f"angles_{v}.json", "w"), indent=1)
    print(len(ROWS), "beats;", {v: len(o) for v, o in ORDERS.items()}, "cuts per variant")
