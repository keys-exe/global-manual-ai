import json, os
D = "/home/user/global-manual-ai/builds/stryde-three-regrets/act3/"
C = "/tmp/claude-0/-home-user-global-manual-ai/20b2c4f7-1437-5cc0-b561-f96976bb11e8/scratchpad/act3cards2/generations/"

R1C = "Already drifting on frame one. Low breath sway throughout, vertical with slight roll. Brief focus hunt at entry. One late partial reframe. Camera lags the subject, never anticipates. Still drifting at the cut."
RVC = "Virtual camera already orbiting on frame one. Slow unbroken lateral orbit with a gentle push, constant rate, mechanically smooth, no handheld physics. Narrow arc, target centred. Still moving at the cut."
RVF = "Virtual camera already moving fast on the first frame. Rapid push toward the target structure, short and hard, with a slight lateral arc across it. Mechanically smooth at speed — no sway, no bounce, no handheld physics, no whip. Still travelling on the final frame, the cut landing mid-move."
RVD = "Virtual camera already drifting on the first frame, never static at entry. A slow steady lateral travel across the subject, single direction, constant unhurried speed, mechanically smooth — no rotation, no orbit, no push, no sway, no handheld physics. Total travel roughly a tenth of frame width. Still drifting on the final frame."
HOLD_C = "Everything in frame keeps the exact form, proportion and count it has in the start frame, first frame to last — nothing melts, merges, splits, grows or becomes something else. One small movement, completing inside the clip, subject fully in frame throughout, nothing leaving frame and returning."
HOLD_HC = "Same person, face and wardrobe every frame; five separate fingers on each hand, never fusing or passing through anything; limbs keep their length and bend only as real joints bend."
PHYS = "Mass and momentum in all movement: heavy starts and settles slow, nothing at uniform speed, nothing stops instantly — motions decelerate into a settle or small overshoot; actions travel through the body, weight transferring first, hands arriving last; hair, fabric and straps lag and keep moving after the body stops; objects drag with friction, never glide."
CAP = "Capture characteristics exactly as in the start frame — same tone-mapping, same noise, same colour temperature. No grading change across the clip."
NEGW = "no morphing, no warping, no melting, no shape shifting, no merging, no splitting, no parts detaching, no proportions changing, no duplicate objects, no background bending, no texture swimming, no smearing, no flickering geometry, no flickering light, no exposure pumping"
BEDLIGHT = "Unremarkable phone clip, grey flat late-morning daylight from the bedroom window on the right, no grade."
CONLIGHT = "Unremarkable phone clip, grey flat daylight from the consulting-room window on the right, no grade."
GAIL = "THE SAME WOMAN as in the start frame, early sixties, big-boned, auburn chin-length bob, lilac dressing gown, grey T-shirt, navy pyjama shorts; exactly as in the start frame, unchanged in every respect."

# anatomy
PHYS_A = "The structures behave mechanically: muscle bellies shorten and thicken as they contract; the patellar tendon draws taut as tension arrives and softens as it passes; the knee keeps correct joint spacing. Small, controlled deformations, never soft rubber."
HOLD_A = "The anatomy keeps its structure every frame: bones hold shape, length and spacing, joints never separate or pass through each other, muscle keeps constant volume, and the layer order holds — bone deepest, muscle over it, translucent contour outermost."
RENDER = "Render exactly as in the start frame, same rim light and colour. No grading change across the clip."
ASTYLE = "Premium 3D anatomical visualisation for medical education, clean broadcast-quality render, as in the start frame."
NEGF = "no flowing energy, no river of light, no glow moving along the limb away from the site, no emission migrating, no fog, no mist, no crossfade, no arrows"
NEGX = "no lasers, no energy bolts, no projectiles, no fire, no flames, no sparks, no beams, no external energy attacking the body, no shattering, no fragments, no cracks, no shockwave, no explosion"
ASUBJ = "The same anatomical knee model as in the start frame, unchanged in every respect."

def br(beat, shot, subj, framing, motion, style, negs, risks, hc=True, sm="in_place"):
    return dict(beat=beat, shot=shot, subject=subj, camera={"movement": R1C, "framing": framing},
                motion=motion + " " + HOLD_C + (" " + HOLD_HC if hc else "") + " " + PHYS,
                lighting=CAP, style=style, negatives=NEGW + ", " + negs, risks=risks, sm=sm)

def mech(beat, shot, rig, framing, motion, negs, risks):
    return dict(beat=beat, shot=shot, subject=ASUBJ, camera={"movement": rig, "framing": framing},
                motion=motion + " " + PHYS_A + " " + HOLD_A, lighting=RENDER, style=ASTYLE,
                negatives=NEGW + ", " + NEGF + ", " + NEGX + ", " + negs, risks=risks, sm="in_place")



JIN = "THE SAME WOMAN as in the start frame, seventy-nine, white pixie crop, heather-purple twinset, grey pleated skirt; unchanged in every respect."
JOUT = "THE SAME WOMAN as in the start frame, seventy-nine, white pixie crop, camel wool coat, grey pleated skirt; unchanged in every respect."
LNG = "Unremarkable phone clip, grey even afternoon light through the net curtains from the left, no grade."
STR = "Unremarkable phone clip, flat grey overcast daylight, no grade."
N = "no glancing at the lens, no talking, no slow motion, no music"
B = [
 br("BR-024","act3_phone_rings",JIN,"MEDIUM as in the start frame: eye height, three-quarter, the chair and side table. FOCUS: her eyes are sharp; the window falls soft.",
    "CONTINUING: the cream phone beside her is ringing and her head is already turning to it. COMPLETING: one look, about two seconds — her eyes settle on the phone, a small still pause, her hands stay in her lap. UNRESOLVED: she keeps looking at the ringing phone, not reaching for it.",
    LNG,"no picking up the phone, no standing up, no sad face, "+N,
    [{"risk":"she answers the phone","prevented_by":"not reaching for it; no picking up the phone"},
     {"risk":"face drifts from the sheet","prevented_by":"subject unchanged; HOLD-HC"},
     {"risk":"phone morphs","prevented_by":"HOLD-C; NEG-WARP-C"}]),
 br("BR-025","act3_polite_no",JIN,"MCU as in the start frame: eye height, profile, the receiver at her ear. FOCUS: her near eye is sharp; the window falls soft.",
    "CONTINUING: she holds the cream receiver to her ear, already starting a gentle shake of the head. COMPLETING: one slow shake, about three seconds — a small polite smile, her eyes lowered, saying no kindly. UNRESOLVED: she listens, the smile fading a little.",
    LNG,"no laughing, no crying, no putting the phone down, no mobile phone, no glancing at the lens, no slow motion, no music",
    [{"risk":"overacted sadness","prevented_by":"small polite smile; no crying"},
     {"risk":"receiver or cord morphs","prevented_by":"HOLD-C; NEG-WARP-C"},
     {"risk":"lip-sync words invented","prevented_by":"a shake and a smile only; she listens"}]),
 br("BR-026","act3_walkers_pass",JIN,"MEDIUM as in the start frame: from behind her chair, through the net curtain. FOCUS: the walkers outside are sharp; her head is soft.",
    "CONTINUING: outside, the walking group in bright anoraks is already passing along the path, poles swinging. COMPLETING: the group walks on across the window, about three seconds, left to right at an easy pace; she stays still, only her head turning slightly to follow them. UNRESOLVED: the last walker nears the window edge.",
    LNG,"no walkers entering the room, no window opening, no faces of the walkers, no turning to the lens, no slow motion, no music",
    [{"risk":"walkers morph or multiply","prevented_by":"HOLD-C exact count; NEG-WARP-C"},
     {"risk":"she moves too much","prevented_by":"she stays still, only her head turning slightly"},
     {"risk":"net curtain flickers","prevented_by":"NEG-WARP-C flickering light"}], hc=False),
 br("BR-027","act3_receiver_down","THE SAME HANDS as in the start frame, small and thin-skinned, a gold wedding ring, over the teak side table with the cream phone; unchanged in every respect.",
    "CU as in the start frame: high, three-quarter, her hands and the table. FOCUS: her hand and the receiver are sharp; the carpet falls soft.",
    "CONTINUING: her right hand is already lowering the cream receiver towards its cradle. COMPLETING: one set-down, about two seconds — the receiver settles into the cradle with a small click, her fingers resting on it a moment, the curly cord settling slack. UNRESOLVED: her hand lifts slowly away.",
    LNG,"no dropping the receiver, no receiver floating, no face, no mobile phone, no slow motion, no music",
    [{"risk":"receiver misses the cradle or floats","prevented_by":"settles into the cradle; no receiver floating"},
     {"risk":"fingers fuse with the receiver","prevented_by":"HOLD-HC five separate fingers"},
     {"risk":"cord tangles or morphs","prevented_by":"HOLD-C; NEG-WARP-C"}]),
 br("BR-028","act3_foot_of_steps",JOUT,"FULL as in the start frame: high, from up the steps looking down at her at the foot. FOCUS: deep; the steps and her stay sharp.",
    "CONTINUING: she stands at the foot of the steps, her left hand on the railing. COMPLETING: one quiet breath, about two seconds — her eyes lift up the flight towards the door, her shoulders rise and settle. UNRESOLVED: she stays at the foot, both feet on the pavement, not climbing.",
    STR,"no climbing, no foot on the step, no walking, no waving, "+N,
    [{"risk":"she climbs the steps","prevented_by":"not climbing; no climbing, no foot on the step"},
     {"risk":"railing or steps warp","prevented_by":"HOLD-C; NEG-WARP-C"},
     {"risk":"she smiles at the lens","prevented_by":"eyes lift up the flight to the door; no glancing at the lens"}]),
 br("BR-029","act3_covering_smile",JOUT,"CU as in the start frame: eye height, three-quarter, close. FOCUS: her eyes are sharp; the steps behind fall soft.",
    "CONTINUING: a small smile is already forming, her eyes lowered to the pavement. COMPLETING: one small covering smile, about two seconds — it reaches her cheeks but not her eyes, a tiny nod to herself. UNRESOLVED: the smile fades a little, eyes still down.",
    STR,"no crying, no laughing, no looking at the camera, no talking, no slow motion, no music",
    [{"risk":"overacted emotion","prevented_by":"one small smile; no crying, no laughing"},
     {"risk":"she looks at the lens","prevented_by":"eyes stay down; no looking at the camera"},
     {"risk":"face drifts","prevented_by":"subject unchanged; HOLD-HC"}]),
 br("BR-030","act3_she_leaves","THE SAME PEOPLE as in the start frame: the woman with the raised hand and the boy in the red sweatshirt in the foreground, and the old woman in the camel coat on the steps beyond them; unchanged in every respect.",
    "MEDIUM as in the start frame: behind the family, over their shoulders, looking at the old woman. FOCUS: deep; everyone stays sharp.",
    "CONTINUING: the woman's hand is already raised in a wave. COMPLETING: one wave, about two seconds — the old woman gives a small smile, then turns away and takes two slow steps off to the side down the pavement. UNRESOLVED: she walks on, her back half to them, the wave ending.",
    STR,"no hug, no running, no family faces to the lens, no one falling, no extra people appearing, no slow motion, no music",
    [{"risk":"extra people appear or merge","prevented_by":"HOLD-C exact count; no extra people appearing"},
     {"risk":"she walks towards the camera","prevented_by":"turns away down the pavement; back half to them"},
     {"risk":"family turn to the lens","prevented_by":"no family faces to the lens"}], sm="in_place"),
]

for b in B:
    card = json.load(open(C + f"stryde-three-regrets__{b['beat']}.json"))
    prompt = json.dumps({k: b[k] for k in ("shot","subject","camera","motion","lighting","style","negatives")}, ensure_ascii=False, separators=(",", ":"))
    call = {"beat": b["beat"], "connector": "kling", "mode": 1, "kind": "broll", "prompt": prompt,
            "duration": card["duration"], "resolution": "1080p", "aspect_ratio": "9:16",
            "start_image": card["imageUrl"], "start_approved": card["imageStatus"] == "confirmed",
            "pinned": False, "subject_motion": b["sm"], "prefer_multi_shots": "false", "generation": 1, "risks": b["risks"]}
    json.dump(call, open(D + f"{b['beat']}.call.json", "w"), ensure_ascii=False, indent=1)
    open(D + f"{b['beat']}.kie_prompt.txt", "w").write(prompt)
    print(b["beat"], card["duration"], len(prompt))
