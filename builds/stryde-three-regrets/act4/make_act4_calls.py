import json, os
D = "/home/user/global-manual-ai/builds/stryde-three-regrets/act4/"
C = "/tmp/claude-0/-home-user-global-manual-ai/20b2c4f7-1437-5cc0-b561-f96976bb11e8/scratchpad/act4cards3/generations/"

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




import sys; sys.path.insert(0,'/home/user/global-manual-ai/products/stryde'); import stryde_product_sheet as s
GD1 = "THE SAME WOMAN as in the start frame, sixty-two, copper bob, lilac dressing gown, grey T-shirt, navy shorts, sheepskin slippers; unchanged in every respect."
GD2 = "THE SAME LEG, HANDS AND STRAP as in the start frame; unchanged in every respect."
HALL = "Unremarkable phone clip, grey flat daylight from the landing window, no grade."
BED1 = "Unremarkable phone clip, grey late-morning window light from the right, no grade."
BED2 = "Unremarkable phone clip, warm midday sun from the window on the right, no grade."
N = "no glancing at the lens, no talking, no slow motion, no music"
HPC = s.HOLD_PC
NWP = "no shell bending, no peaks becoming uneven, no wordmark changing, no second strap"
def prod(beat, shot, subj, framing, motion, style, negs, risks):
    b = br(beat, shot, subj, framing, motion + " " + HPC, style, negs + ", no shell bending, no extra or fused fingers", risks, hc=False)
    return b
B = [
 br("BR-032","act4_stair_down",GD1,"FULL as in the start frame: low at the foot of the narrow stairwell, looking up. FOCUS: deep; the stairs and her stay sharp.",
    "CONTINUING: her left foot is already lowering onto the next stair, her right hand gripping the rail. COMPLETING: one step down, about two seconds — the left foot lands, her weight drops onto it heavily through the rail, the stiff right leg stays braced and straight behind, her face tight. UNRESOLVED: she pauses on the step, gathering herself, right leg still straight.",
    HALL,"no running, no second step, no falling, no hand off the rail, no knee support, "+N,
    [{"risk":"she walks down several steps","prevented_by":"one step down then a pause; no second step"},
     {"risk":"the right knee bends normally","prevented_by":"stiff right leg stays braced and straight"},
     {"risk":"she falls","prevented_by":"no falling; weight through the rail"}], sm="in_place"),
 br("BR-033","act4_stair_up",GD1,"FULL as in the start frame: eye height from behind at the foot of the stairs. FOCUS: deep.",
    "CONTINUING: her right foot is already on the next stair, her weight rising onto it. COMPLETING: one easy step up, about two seconds — she rises onto the right foot, the left foot comes up to the stair above, her hand light on the rail. UNRESOLVED: she keeps climbing, back to the lens, the landing window ahead.",
    HALL,"no turning round, no face, no stumbling, no knee support, no slow motion, no music",
    [{"risk":"she turns to the lens","prevented_by":"back to the lens; no turning round, no face"},
     {"risk":"stairs warp","prevented_by":"HOLD-C; NEG-WARP-C"},
     {"risk":"legs lengthen on the step","prevented_by":"HOLD-HC limbs keep length"}], sm="in_place"),
 br("BR-035","act4_sleeve_off",GD1,"CU as in the start frame: knee height, three-quarter, her hands and knee. FOCUS: her hands and the sleeve are sharp.",
    "CONTINUING: both hands are already rolling the black sleeve down below her kneecap. COMPLETING: one peel, about two seconds — the sleeve rolls down her shin over itself, the knee skin pink and creased where it was. UNRESOLVED: the sleeve bunched at mid-shin, her hands resting on it.",
    BED1,"no logo on the sleeve, no strap, no brace, no face, "+N,
    [{"risk":"the sleeve turns into another product","prevented_by":"plain black sleeve; no strap, no brace, no logo"},
     {"risk":"fingers fuse with the fabric","prevented_by":"HOLD-HC"},
     {"risk":"sleeve vanishes","prevented_by":"HOLD-C; bunched at mid-shin"}]),
 mech("MECH-034","act4_catch_on_band",RVC,"MCU as in the start frame: lateral close-up, the knee bent as in a step down. FOCUS: the tendon band is sharp.",
    "CONTINUING: the knee is already bent under the step-down, the tendon band below the kneecap glowing. COMPLETING: one catch, about three seconds — the thigh muscles lengthen and tighten to catch the lowering weight, the knee bends a few degrees more, and the pull lands on the band: it draws taut and its glow flares near-white at that one spot. UNRESOLVED: still glowing, held under load.",
    "no walking, no foot, no second leg, no hands, no glow spreading",
    [{"risk":"a still model with light","prevented_by":"muscles lengthen and tighten, knee bends; PHYS_A"},
     {"risk":"extra limbs appear","prevented_by":"no foot, no second leg, no hands"},
     {"risk":"glow spreads along the shin","prevented_by":"at that one spot; NEG-FLOW"}]),
 mech("MECH-036","act4_down_to_band",RVD,"CU as in the start frame: front, low, the kneecap and band. FOCUS: the band below the kneecap is sharp.",
    "CONTINUING: a dim warmth lies on the joint line, the band below the kneecap already brighter. COMPLETING: about two seconds — the joint-line warmth fades away while the band below the kneecap brightens to near-white, the attention settling on it. UNRESOLVED: the band glows, the joint line dark.",
    "no glow on the joint line at the end, no glow spreading, no walking, no extra limbs",
    [{"risk":"both glow equally","prevented_by":"joint-line warmth fades while the band brightens"},
     {"risk":"crossfade look","prevented_by":"NEG-FLOW crossfade"},
     {"risk":"anatomy morphs","prevented_by":"HOLD-AC"}]),
 prod("PR-037","act4_first_look","THE SAME HAND and strap as in the start frame; unchanged in every respect.",
    "CU as in the start frame: level, front, the strap by the bright window. FOCUS: the shell and wordmark are sharp.",
    "CONTINUING: her hand is already holding the strap up in a bottom-edge pinch. COMPLETING: one small slow tilt of the wrist, about two seconds — the shell turns a little towards the light so the chrome slides catch it, then back, the wordmark staying readable. UNRESOLVED: held up, still, facing the lens.",
    BED2,"no fingers over the peaks or notch, no hand on the band, no strap swinging, no face, "+N,
    [{"risk":"the shell reshapes as it turns","prevented_by":"small tilt only; HOLD-PC; shell never bends"},
     {"risk":"the wordmark garbles","prevented_by":"wordmark staying readable; no wordmark changing letters"},
     {"risk":"fingers cover the peaks","prevented_by":"no fingers over the peaks or notch"}]),
 prod("BR-038","act4_worn_breath",GD2,"CU as in the start frame: knee height, three-quarter, the strap on the knee. FOCUS: the strap and kneecap are sharp.",
    "CONTINUING: she sits with the right leg straight, the strap seated under the kneecap, hands resting on her thigh. COMPLETING: one slow breath, about two seconds — her thigh and hands rise and settle slightly, the strap staying exactly in place, the notch cupping the kneecap. UNRESOLVED: still, the strap untouched.",
    BED2,"no hands on the strap, no strap sliding, no strap on the kneecap, no face, "+N,
    [{"risk":"the strap slides or climbs the kneecap","prevented_by":"strap staying exactly in place; no strap sliding"},
     {"risk":"shell warps","prevented_by":"HOLD-PC; no shell bending"},
     {"risk":"leg skin smooths","prevented_by":"INHERIT-CAP; capture unchanged"}]),
 prod("BR-039","act4_pad_back","THE SAME HANDS and strap as in the start frame, the pad facing the lens; unchanged in every respect.",
    "CU as in the start frame: level, front, the ring over the quilt. FOCUS: the pad and peaks are sharp.",
    "CONTINUING: her hands already hold the ring with the pad facing the lens. COMPLETING: one small tilt, about two seconds — the shell tips a little back towards the light so the pad's matte curve and the chrome slides catch it, then settles. UNRESOLVED: held still, the pad facing the lens.",
    BED2,"no turning the strap round, no wordmark appearing, no glossy pad, no band being stretched, no face, "+N,
    [{"risk":"the strap spins and the back changes","prevented_by":"small tilt only; no turning the strap round"},
     {"risk":"the pad goes glossy or silicone","prevented_by":"matte curve; no glossy pad"},
     {"risk":"the grey half of the shell grows","prevented_by":"HOLD-PC; HOLD-C"}]),
 prod("BR-041","act4_seat_up",GD2,"CU as in the start frame: knee height, profile of the leg, the strap in her hands. FOCUS: her hands and the strap are sharp.",
    "CONTINUING: both hands hold the strap on her leg just below the knee. COMPLETING: one slide up, about three seconds — her palms flat on the shell move it up the last short way until the notch meets the underside of the kneecap and stops there, the kneecap uncovered above. UNRESOLVED: her fingers lift away, the strap seated.",
    BED2,"no strap moving down, no strap climbing onto the kneecap, no band being pulled or tightened, no threading, no face, "+N,
    [{"risk":"the strap climbs onto the kneecap","prevented_by":"stops at the kneecap; no strap climbing onto the kneecap"},
     {"risk":"it reads as tightening","prevented_by":"palms flat on the shell; no band being pulled or tightened"},
     {"risk":"the strap moves down","prevented_by":"only up; no strap moving down"}]),
 prod("BR-042","act4_tap_notch",GD2,"ECU as in the start frame: above, three-quarter, the kneecap and notch. FOCUS: the fingertip and notch are sharp.",
    "CONTINUING: her forefinger rests at the shell's top edge in the notch. COMPLETING: one light tap, about two seconds — the fingertip lifts and taps the top edge once where the kneecap sits in the notch, then rests there. UNRESOLVED: her finger rests at the notch, the strap unmoved.",
    BED2,"no strap moving, no trousers over the strap, no finger pressing the kneecap, no face, "+N,
    [{"risk":"the strap moves under the tap","prevented_by":"strap unmoved; no strap moving"},
     {"risk":"trouser hem slides over the strap","prevented_by":"no trousers over the strap"},
     {"risk":"finger fuses with the shell","prevented_by":"HOLD-HC"}]),
 mech("MECH-040","act4_pad_catches",RVC,"MCU as in the start frame, lateral. FOCUS: the strap and tendon are sharp.",
    "CONTINUING: the strap sits on the tendon below the kneecap, a step's load arriving. COMPLETING: one catch, about three seconds — the knee flexes a little, the shell meets the load and settles a fraction deeper, its pad glowing cool pale blue, the tendon beneath staying cool and unlit. UNRESOLVED: the cool glow holds."+HPC,
    "no orange glow at the site, no strap sliding, no strap on the kneecap, no shell bending",
    [{"risk":"the site lights warm","prevented_by":"tendon stays cool and pale; no orange glow at the site"},
     {"risk":"the strap slides through the joint","prevented_by":"holds station; no strap sliding"},
     {"risk":"product morphs","prevented_by":"HOLD-PC; NEG-WARP-P"}]),
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
