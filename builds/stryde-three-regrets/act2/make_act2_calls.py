import json, os
D = "/home/user/global-manual-ai/builds/stryde-three-regrets/act2/"
C = "/tmp/claude-0/-home-user-global-manual-ai/20b2c4f7-1437-5cc0-b561-f96976bb11e8/scratchpad/act2cards2/generations/"

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


KENS = "THE SAME MAN as in the start frame, flat cap, tan golf jacket, stone shorts, navy socks, brown brogues; unchanged in every respect."
STREET = "Unremarkable phone clip, flat grey overcast daylight from the left, no grade."
BGN = "no bus arriving, no traffic crossing close, no glancing at the lens, no talking, no slow motion, no music"
B = [
 br("BR-017","act2_ken_weight_shift",KENS,"FULL as in the start frame: eye height, three-quarter, beside the shelter. FOCUS: deep; he and the street stay sharp.",
    "CONTINUING: he stands with his hands in his jacket pockets, his weight already easing to the left. COMPLETING: one shift, about two seconds — his hip settles to the left, the left leg takes his weight straight and planted, the right knee softens and the right heel lifts a little. UNRESOLVED: he stands on the left leg, looking up the road. People far behind keep walking.",
    STREET,"no walking, no stepping, no sitting, "+BGN,
    [{"risk":"he walks off instead of shifting","prevented_by":"one weight shift in place; no walking, no stepping"},
     {"risk":"the shift reads on the wrong leg","prevented_by":"left leg takes the weight, right heel lifts; HOLD-HC joints"},
     {"risk":"background people morph","prevented_by":"HOLD-C; NEG-WARP-C"}]),
 br("BR-018","act2_ken_knees",KENS,"CU as in the start frame: knee height, front, his legs from the shorts hem to his brogues. FOCUS: his knees are sharp; the shelter falls soft.",
    "CONTINUING: he stands at the kerb, weight already more on his left leg. COMPLETING: a small sway, about two seconds — his weight settles further onto the straight left leg, the left knee staying locked, while the right knee bends a touch more and the right heel lifts off the pavement. UNRESOLVED: he holds that uneven stance.",
    STREET,"no face, no upper body, no walking, no stepping off the kerb, no both knees bending, "+BGN,
    [{"risk":"both legs load evenly","prevented_by":"left knee locked, right knee bends and heel lifts; no both knees bending"},
     {"risk":"he steps off the kerb","prevented_by":"held stance; no walking, no stepping off the kerb"},
     {"risk":"legs lengthen or socks change","prevented_by":"HOLD-HC limbs keep length; HOLD-C"}]),
 br("BR-019","act2_ken_glance",KENS,"MCU as in the start frame: eye height, profile from his right side. FOCUS: his near eye is sharp; the road falls soft.",
    "CONTINUING: his head is already turning toward the road. COMPLETING: one glance, about two seconds — he looks down the road for the bus, eyes narrowing a little, a small breath out; his body stays still, weight left, right knee soft. UNRESOLVED: he keeps looking down the road.",
    STREET,"no walking, no waving, no smiling, "+BGN,
    [{"risk":"he looks at the lens","prevented_by":"glance down the road; no glancing at the lens"},
     {"risk":"face drifts from the sheet","prevented_by":"subject unchanged; HOLD-HC"},
     {"risk":"a bus arrives and steals the shot","prevented_by":"no bus arriving"}]),
 br("BR-020","act2_ken_kerb_step",KENS,"FULL as in the start frame: low, near the road, the kerb and his leading foot nearest the lens. FOCUS: deep; kerb, shoes and him sharp.",
    "CONTINUING: his left brogue is already landing on the road below the kerb, his right hand on the lamp post. COMPLETING: one step down, about two seconds — the left foot settles flat, his weight drops onto it, then the stiff right leg follows down and lands beside it. UNRESOLVED: he stands at the crossing edge.",
    STREET,"no jump, no both feet in the air, no stumbling, no fall, "+BGN,
    [{"risk":"he jumps or both feet leave the ground","prevented_by":"one step down, left foot lands first; no jump, no both feet in the air"},
     {"risk":"the right knee bends normally, losing the point","prevented_by":"stiff right leg follows; HOLD-HC"},
     {"risk":"he walks out of frame","prevented_by":"UNRESOLVED: stands at the crossing edge; HOLD-C in frame"}], sm="in_place"),
 br("BR-022","act2_ken_rub_left",KENS,"MCU as in the start frame: high, three-quarter, on the red perch bench. FOCUS: his hands on the left knee are sharp; the street falls soft.",
    "CONTINUING: both hands are already on his LEFT knee. COMPLETING: one slow rub, about three seconds — his fingers knead just below the kneecap in small circles, pressing in, his head bowed and mouth tight. UNRESOLVED: his hands rest on the left knee.",
    STREET,"no rubbing the right knee, no standing up, "+BGN,
    [{"risk":"rubs the wrong knee","prevented_by":"both hands on his LEFT knee; no rubbing the right knee"},
     {"risk":"fingers fuse with the knee","prevented_by":"HOLD-HC five separate fingers"},
     {"risk":"he stands up","prevented_by":"no standing up; HOLD-C"}]),
 mech("MECH-021","act2_two_bands",RVC,"MCU as in the start frame: three-quarter front, both legs from the hips down. FOCUS: the brightly glowing knee is sharp.",
    "CONTINUING: both legs stand, one knee's tendon band already glowing bright under a doubled load, the other knee's band only faint. COMPLETING: the weight of one step settles onto the loaded leg, about three seconds — that knee takes it, the quadriceps tighten, its band draws taut and its glow brightens to near-white at that one spot, while the other knee's band stays faint and dim. UNRESOLVED: the loaded band keeps glowing; the legs never walk.",
    "no walking, no stepping, no torso, no hands, no second glow brightening, no glow swapping sides",
    [{"risk":"both knees glow equally","prevented_by":"the other band stays faint; no second glow brightening"},
     {"risk":"the model animates walking","prevented_by":"legs never walk; no walking, no stepping"},
     {"risk":"the glow swaps to the other knee","prevented_by":"no glow swapping sides; HOLD-C"}]),
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
