import json, os
D = "/home/user/global-manual-ai/builds/stryde-three-regrets/act1/"
C = "/tmp/claude-0/-home-user-global-manual-ai/20b2c4f7-1437-5cc0-b561-f96976bb11e8/scratchpad/act1cards3/generations/"

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

B = [
 br("BR-003","act1_gail_drawer_pull",GAIL,"MEDIUM as in the start frame: eye height, three-quarter from behind, past the soft door edge. FOCUS: her hands on the drawer are sharp; the room falls soft.",
    "CONTINUING: her hands are already pulling the half-open top drawer of the pine chest. COMPLETING: one pull, about two seconds — the drawer sticks for an instant, jolts, then gives and slides out a few centimetres more on its runners, her shoulders leaning back slightly with it. UNRESOLVED: she looks down into the drawer, hands still on its front.",
    BEDLIGHT,"no drawer closing, no contents flying out, no talking, no slow motion, no music",
    [{"risk":"the drawer slides smoothly with no stick","prevented_by":"motion: sticks for an instant, jolts, then gives; PHYS-MOTION-C friction clause"},
     {"risk":"drawer comes fully out or the chest morphs","prevented_by":"a few centimetres only; HOLD-C; no drawer falling out"},
     {"risk":"her face or gown drift","prevented_by":"subject unchanged in every respect; HOLD-HC"}]),
 br("BR-004","act1_gail_rub_knee",GAIL,"MCU as in the start frame: high angle, three-quarter, sitting on the bed edge. FOCUS: her hands on the right knee are sharp; the bed falls soft.",
    "CONTINUING: both hands are already on her right knee. COMPLETING: two slow rubs, about three seconds — her fingers press and rub the outside of the knee in small circles, the skin moving under them, her brow tightening as she frowns down at it. UNRESOLVED: her hands keep resting on the knee, eyes still on it.",
    BEDLIGHT,"no standing up, no glancing at the lens, no smiling, no crying, no talking, no slow motion, no music",
    [{"risk":"rubbing turns into a massage montage or fast repetitive motion","prevented_by":"two slow rubs; PHYS-MOTION-C"},
     {"risk":"fingers fuse with the knee","prevented_by":"HOLD-HC five separate fingers; NEG-WARP-C"},
     {"risk":"she looks at the lens","prevented_by":"eyes stay on the knee; no glancing at the lens"}]),
 br("BR-005","act1_gail_sleeve",GAIL,"CU as in the start frame: eye height, profile, leg raised, hands at the knee. FOCUS: her hands and the black sleeve are sharp; the window falls soft.",
    "CONTINUING: both hands are already gripping the top edge of the plain black stretchy sleeve over her right knee. COMPLETING: one pull, about three seconds — she draws the sleeve a few centimetres up over the knee, the knit stretching, then settling snug. UNRESOLVED: her hands smooth the top edge, the leg still raised.",
    BEDLIGHT,"no logo on the sleeve, no sleeve changing colour or length, no glancing at the lens, no talking, no slow motion, no music",
    [{"risk":"the sleeve grows a brand or changes shape","prevented_by":"plain black sleeve; no logo; HOLD-C"},
     {"risk":"hands pass through the fabric","prevented_by":"HOLD-HC never passing through anything"},
     {"risk":"the raised leg drops or bends wrongly","prevented_by":"UNRESOLVED leg still raised; HOLD-HC joints"}]),
 br("BR-006","act1_gail_brace_strap","THE SAME HANDS AND FOREARMS as in the start frame, an older woman's, navy sleeve, and the same plain grey hinged knee brace with metal side bars on her right knee; exactly as in the start frame, unchanged in every respect.",
    "CU as in the start frame: low angle, three-quarter, the brace on the knee. FOCUS: her hands and the strap are sharp; the chest of drawers falls soft.",
    "CONTINUING: her left hand is already drawing the grey strap across the front of the brace. COMPLETING: one fasten, about two seconds — she pulls the strap round and presses its hook-and-loop end flat onto the brace, fingers pressing. UNRESOLVED: her fingers rest on the fastened strap. The metal side bars stay rigid and never bend.",
    BEDLIGHT,"no logo, no metal bars bending, no brace changing shape, no talking, no slow motion, no music",
    [{"risk":"the metal side bars bend or the brace warps","prevented_by":"side bars stay rigid; no metal bars bending; HOLD-C"},
     {"risk":"strap passes through the hand","prevented_by":"HOLD-HC never passing through anything"},
     {"risk":"a logo appears on the brace","prevented_by":"plain brace; no brand, no logo"}]),
 br("BR-007","act1_drawer_drop","THE SAME HANDS as in the start frame, an older woman's with a gold ring, green fleece sleeves, holding a beige wrap and a blue gel pad over the open drawer full of supports; exactly as in the start frame, unchanged in every respect.",
    "CU as in the start frame: overhead, looking down into the drawer. FOCUS: the pile in the drawer is sharp; the carpet falls soft.",
    "CONTINUING: her hands are already opening over the drawer. COMPLETING: one drop, about two seconds — the beige wrap and the blue gel pad fall onto the pile, landing with weight, the wrap's strap flopping over, the gel pad settling with a slight slump. UNRESOLVED: her hands hover above the drawer, empty.",
    BEDLIGHT,"no items floating, no items multiplying, no items vanishing, no slow falling, no talking, no slow motion, no music",
    [{"risk":"items float or fall in slow motion","prevented_by":"landing with weight; no items floating; no slow falling"},
     {"risk":"the pile multiplies or morphs","prevented_by":"HOLD-C exact count; no items multiplying"},
     {"risk":"fingers fuse with the gel pad","prevented_by":"HOLD-HC five separate fingers"}]),
 br("BR-008","act1_gail_shrug",GAIL,"MCU as in the start frame: eye height, three-quarter, standing by the open drawer. FOCUS: her face is sharp; the bedroom falls soft.",
    "CONTINUING: she is already looking down at the full drawer. COMPLETING: one small tired shrug, about two seconds — her shoulders lift a little and drop, a slow breath out, her eyes staying on the drawer. UNRESOLVED: she keeps looking at it, arms loose at her sides.",
    BEDLIGHT,"no walking, no touching the drawer, no glancing at the lens, no smiling, no crying, no talking, no slow motion, no music",
    [{"risk":"overacted shrug","prevented_by":"one small shrug, shoulders lift a little"},
     {"risk":"she walks off or looks at the lens","prevented_by":"no walking; eyes stay on the drawer"},
     {"risk":"face drifts","prevented_by":"subject unchanged; HOLD-HC"}]),
 br("BR-009","act1_xray_trace","THE SAME MAN'S HAND as in the start frame, navy shirt cuff, at the same white-framed wall lightbox with the same knee X-ray; exactly as in the start frame, unchanged in every respect.",
    "CU as in the start frame: screen height, front of the lightbox. FOCUS: the X-ray is sharp; the hand falls slightly soft.",
    "CONTINUING: his forefinger is already on the dark joint line between the thigh bone and the shin bone. COMPLETING: one trace, about two seconds — the fingertip slides along the joint line, following its curve, just touching the film. UNRESOLVED: the finger rests at the end of the line.",
    CONLIGHT,"no X-ray image changing, no bones moving on the film, no second hand, no face, no text, no talking, no slow motion, no music",
    [{"risk":"the X-ray image changes or animates","prevented_by":"HOLD-C; no X-ray image changing, no bones moving"},
     {"risk":"finger passes into the lightbox","prevented_by":"just touching the film; HOLD-HC"},
     {"risk":"extra hand appears","prevented_by":"no second hand; HOLD-C count"}]),
 br("BR-012","act1_gail_press",GAIL,"ECU as in the start frame: over her right shoulder, looking down her arm to the knee. FOCUS: the fingertip under the kneecap is sharp; the bed falls soft.",
    "CONTINUING: her right forefinger is already pressed under her right kneecap. COMPLETING: one press, about two seconds — she presses a little deeper, the skin dimpling, her fingers tensing, then a small wince through her shoulders, her head dipping slightly. UNRESOLVED: the finger stays pressed in.",
    BEDLIGHT,"no second person, no other hand, no face turning to the lens, no bruise, no talking, no slow motion, no music",
    [{"risk":"a second person's hand appears","prevented_by":"her own right hand; no second person, no other hand"},
     {"risk":"finger sinks unnaturally into the knee","prevented_by":"skin dimpling only; HOLD-HC"},
     {"risk":"she turns to the lens","prevented_by":"no face turning to the lens"}]),
 br("BR-015","act1_brace_tilt","THE SAME MAN'S HAND as in the start frame, navy shirt cuff, holding the same plain grey hinged knee brace upright over the desk; exactly as in the start frame, unchanged in every respect.",
    "CU as in the start frame: low, looking past the desk to the lightbox. FOCUS: the brace and hand are sharp; the room falls soft.",
    "CONTINUING: his hand is already holding the brace upright by its lower cuff. COMPLETING: one slow tilt, about three seconds — he tilts the whole brace to one side and back, the metal side bars and hinge staying rigid and never folding sideways. UNRESOLVED: he holds the brace upright again, still.",
    CONLIGHT,"no brace bending sideways, no hinge folding, no brace floating, no brand, no logo, no face, no talking, no slow motion, no music",
    [{"risk":"the hinge folds sideways, contradicting the line","prevented_by":"bars and hinge rigid; no hinge folding; no brace bending sideways"},
     {"risk":"the brace floats out of the hand","prevented_by":"held by its lower cuff; no brace floating"},
     {"risk":"6s clip over-animates","prevented_by":"one slow tilt then UNRESOLVED hold; HOLD-C"}]),
 br("BR-016","act1_drawer_wont_shut",GAIL,"MEDIUM as in the start frame: eye height, from behind her at the chest of drawers. FOCUS: her hand on the drawer is sharp; the window falls soft.",
    "CONTINUING: her hand is already on the front of the overfilled top drawer. COMPLETING: one push, about two seconds — the drawer slides in a few centimetres and jams on the stuffed supports, the grey strap hanging out bunching; it will not shut. UNRESOLVED: her hand stays on it, her head dropping slightly.",
    BEDLIGHT,"no drawer closing fully, no contents vanishing, no strap disappearing, no photos changing, no turning to the lens, no talking, no slow motion, no music",
    [{"risk":"the drawer shuts anyway","prevented_by":"jams; no drawer closing fully"},
     {"risk":"the stuffed contents vanish to let it close","prevented_by":"HOLD-C count; no contents vanishing"},
     {"risk":"6s clip over-animates","prevented_by":"one push then UNRESOLVED hold"}], hc=False),
 mech("MECH-010","act1_tendon_step",RVC,"CU as in the start frame: true lateral profile, the leg mid-stride, the knee off-centre. FOCUS: the tendon below the kneecap is sharp.",
    "CONTINUING: the leg is already mid-stride, the patellar tendon immediately below the patella already glowing warm. COMPLETING: one walking step lands, about three seconds — the foot plants, the knee bends a few degrees under the load, the quadriceps shorten and the patellar tendon draws taut, its glow brightening to near-white at that one site, then easing a little as the step passes. UNRESOLVED: the band keeps glowing, still warm.",
    "no leg leaving frame, no second leg appearing, no glow spreading to the bone shafts, no slow motion, no music",
    [{"risk":"a still model with light played over it","prevented_by":"knee bends, quadriceps shorten, tendon draws taut; PHYS_A"},
     {"risk":"glow travels along the limb","prevented_by":"at that one site; NEG-FLOW"},
     {"risk":"bones interpenetrate or limb stretches","prevented_by":"HOLD-AC"}]),
 mech("MECH-011","act1_heel_strike",RVF,"MCU as in the start frame: low three-quarter, the knee dominant. FOCUS: the patellar tendon below the kneecap is sharp.",
    "CONTINUING: the knee is already under load, the patellar tendon already glowing. COMPLETING: one heel strike, a single hard arrival — the quadriceps compress and the patellar tendon draws taut as the load arrives, once; a near-white flash ignites at the tendon immediately below the patella and the structure compresses fractionally, then decays back to a hot glowing core. UNRESOLVED: still glowing at the cut, never going out.",
    "no rhythm, no repeated flashes, no glow on the whole limb, no slow motion, no music",
    [{"risk":"repeated pulsing instead of one arrival","prevented_by":"one heel strike, once; no rhythm, no repeated flashes"},
     {"risk":"external energy hitting the knee","prevented_by":"NEG-EXTERNAL subset; load from the body"},
     {"risk":"anatomy morphs under the fast push","prevented_by":"HOLD-AC; NEG-WARP-C"}]),
 mech("MECH-013","act1_tight_spot",RVC,"ECU as in the start frame: front, the kneecap and tendon filling the frame. FOCUS: the tight spot on the tendon is sharp.",
    "CONTINUING: one tight spot on the patellar tendon immediately below the patella is already glowing. COMPLETING: one slow pulse, about two seconds — the spot brightens and tightens inward, the tendon fibres around it drawing taut, then easing back. UNRESOLVED: the spot stays lit, the only bright point in frame.",
    "no second hotspot, no glow spreading, no glow on the kneecap, no slow motion, no music",
    [{"risk":"glow spreads over the whole knee","prevented_by":"the only bright point; no glow spreading"},
     {"risk":"lit diagram with no mechanical event","prevented_by":"fibres drawing taut; PHYS_A"},
     {"risk":"kneecap or tendon morphs","prevented_by":"HOLD-AC; NEG-WARP-C"}]),
 mech("MECH-014","act1_sleeve_squeeze",RVD,"MCU as in the start frame: high three-quarter, the dark sleeve round the knee. FOCUS: the tendon below the kneecap is sharp.",
    "CONTINUING: the plain dark knit sleeve is already round the whole knee, the patellar tendon immediately below the patella already glowing. COMPLETING: one squeeze, about three seconds — the sleeve tightens a fraction evenly all round the joint, compressing the whole knee equally, while the band below the kneecap stays loaded, its glow unchanged. UNRESOLVED: the band keeps glowing under the sleeve.",
    "no glow fading at the site, no logo on the sleeve, no slow motion, no music",
    [{"risk":"the sleeve relieves the glow, contradicting the line","prevented_by":"glow unchanged; no glow fading at the site"},
     {"risk":"sleeve grows a logo or changes shape","prevented_by":"plain dark knit sleeve; no logo; HOLD-C"},
     {"risk":"lit diagram","prevented_by":"sleeve tightens, knee compresses; PHYS_A"}]),
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
