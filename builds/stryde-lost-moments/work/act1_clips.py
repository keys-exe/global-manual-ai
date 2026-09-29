#!/usr/bin/env python3
"""stryde-lost-moments — Act 1 clip calls (§35 Kling JSON, §27G staging, §22X preflight call.json).
One action at a named pace, camera locked off (propped phone), rigid product, prefer_multi_shots false.
Writes hooks/calls-style files to work/clips/<beat>.v1.kling.json + .call.json. Usage: act1_clips.py <urls.txt>
"""
import json, sys, pathlib
from beats import S, PS
HERE = pathlib.Path(__file__).parent
OUT = HERE / "clips"; OUT.mkdir(exist_ok=True)
URL = dict(l.split() for l in open(sys.argv[1]) if l.strip())
LEN = {b: v["call_s"] for b, v in json.load(open(HERE / "broll_lengths.json")).items()}

CAM = {"movement": "Propped, not held, not tripod. Small settle at entry, then near-stillness with a slow unresolved drift. Slightly off-level and never corrected.",
       "framing": "PROPPED as in the start frame."}
LIGHT = "Capture characteristics exactly as in the start frame — same tone-mapping, same noise, same colour temperature. No grading change across the clip."
HOLD = ("Everything in frame keeps the exact form, proportion and count it has in the start frame, first frame to last — nothing melts, merges, splits, "
        "grows or becomes something else. Mass and momentum: weight transfers first, hands arrive last, fabric lags and settles.")
RIGID = ("The strap keeps its exact shape, size and wordmark in every frame and moves only with the body it sits on; its rigid shell never bends.")
NEG = "no morphing, no warping, no melting, no merging, no splitting, no duplicate objects, no background bending, no texture swimming, no camera travelling with the subject, no slow motion, no music, no speech"
NEGP = "no bending, no curling, no folding, no melting, no flipping of the product, no strap sliding on the leg, no product covering the kneecap, no second unit"
NEGH = "no extra fingers, no fused fingers, no melted hands"

def slots(s):
    for k, v in PS.SLOTS.items():
        if isinstance(v, str): s = s.replace("[" + k.replace("_", " ") + "]", v).replace("[" + k + "]", v).replace("[" + k.replace("_", "-") + "]", v)
    return s.replace("[LOAD-CADENCE]", "a walking cadence")

C = {  # beat: (subject, motion, extra negatives, product?, subject_motion, risks)
 "SH-01": ("Medium close-up of a white British woman surgeon of fifty-six in navy scrubs at her desk, holding the knee strap still at chest height in both hands. Exactly as in the start frame.",
   "Already moving on the first frame: she lifts her eyes from the strap to the patient across the desk, one look up in about a second, then holds the look with a small, calm, professional nod. Her hands and the strap stay still. " + RIGID,
   NEGH + ", no white coat, no speaking, no mouth moving", True, "still",
   [("face drifts or changes", "one small eye-line change only; HOLD clause; 'no speaking'"), ("strap bends in her hands", "hands and strap stay still; rigid clause; product negatives"), ("fingers fuse on the shell", "hands do not move; 'no fused fingers'")]),
 "SH-02": ("Close-up looking down into an open wooden dresser drawer holding a grey knee sleeve and a black hinged brace, a woman's hand on the drawer front. Exactly as in the start frame.",
   "Already moving on the first frame: her hand pushes the drawer shut in one firm push, about a second, the sleeve and the brace sliding out of sight as it closes; the drawer front meets the dresser and her hand rests on it. The camera stays where it is.",
   NEGH + ", no drawer bouncing open, no items flying, no face in frame", False, "in_place",
   [("drawer or items warp as it closes", "one push, about a second; HOLD clause; 'no items flying'"), ("hand fuses with the drawer", "hand large in frame, one movement; 'no melted hands'"), ("camera follows the drawer", "camera propped, stays where it is")]),
 "SH-03": ("Close-up of an anatomical knee model on a desk, a surgeon's fingertip on its joint line. Exactly as in the start frame.",
   "Already moving on the first frame: her fingertip traces slowly along the joint line of the model, one slow trace across about two seconds, then rests at the tendon below the kneecap. The model does not move.",
   NEGH + ", no model moving, no labels, no face in frame", False, "still",
   [("the model deforms under the finger", "'the model does not move'; HOLD clause"), ("finger multiplies", "one fingertip, one trace; hand negatives"), ("focus hunts", "camera propped, near-still")]),
 "SH-04a": ("Extreme close-up from the side of a man's right leg stepping up a York-stone garden step, the black knee strap snug just under his kneecap. Exactly as in the start frame.",
   "Already stepping on the first frame: he steps up onto the next stone step, one step in about a second, weight rolling onto the right leg, the knee straightening under it with no hesitation; the left foot follows past the lens. " + RIGID + " " + S("AFTER-EASE"),
   NEGP + ", " + S("NEG-EFFORT") + ", no stumble, no slipping foot, no hand on anything", True, "in_place",
   [("legs blend mid-step", "§27G stairs staging: side, one step, camera still; HOLD clause"), ("strap slides as the knee straightens", "rigid clause; 'no strap sliding on the leg'"), ("step reads as effort", "AFTER-EASE; NEG-EFFORT")]),
 "SH-04b": ("Close-up looking down at a woman's right knee as she sits on a sofa, the black knee strap snug under her kneecap, her fingertips at the skin below its lower edge. Exactly as in the start frame.",
   "Already moving on the first frame: her fingertips slide once along the smooth skin just below the strap's lower edge, one slow slide in about a second, then rest. Fingertips touch only skin, never the strap. " + RIGID,
   NEGP + ", " + NEGH + ", no redness appearing, no marks on the skin, no fingers on the strap, no face in frame", True, "still",
   [("fingers merge with the strap", "'fingertips touch only skin, never the strap'; hand negatives"), ("skin changes colour", "'no redness appearing, no marks'"), ("strap shifts", "rigid clause; product negatives")]),
 "SH-04c": ("Ground-level shot up a park path at a woman's legs from the knees down, walking toward the lens, the black knee strap snug under her right kneecap. Exactly as in the start frame.",
   "Already walking on the first frame: three easy steps toward the lens, one step per second, normal walking speed, the strap riding exactly in place on the moving knee; she stops just short of the lens. Feet and knees only, the camera stays where it is. " + RIGID,
   NEGP + ", " + S("NEG-EFFORT") + ", no strap rolling down, no face in frame, no extra legs, no feet merging", True, "travels",
   [("legs blend walking at the lens", "§27G: feet/knee only, three steps; 'no extra legs, no feet merging'"), ("strap rolls down", "rigid clause; 'no strap rolling down, no strap sliding'"), ("she walks into the lens", "'stops just short of the lens'")]),
 "SH-05": ("Overhead on an oak kitchen table: a man's hands lifting the lid off a matte-black box that holds two straps side by side. Exactly as in the start frame.",
   "Already moving on the first frame: his hands lift the lid clear and carry it up and out of frame, one lift in about a second; the two straps stay exactly where they lie in their wells, then the open box rests on the table. The straps never move. The camera stays where it is.",
   NEGP + ", " + NEGH + ", no straps moving, no third strap, no text appearing on the box, no face in frame", True, "in_place",
   [("straps change shape or number", "'the straps never move'; 'no third strap'; product negatives"), ("lid morphs", "one lift out of frame; HOLD clause"), ("text appears on the box", "'no text appearing on the box'")]),
 "SH-06": ("Medium close-up of a Black British man of seventy-two at a kitchen table, an open box with two straps in front of him, a mug of tea in his hand. Exactly as in the start frame.",
   "Already moving on the first frame: he lowers his mug to the table, one lowering in about a second, and settles back with a quiet, satisfied half-smile at the straps. The box and the straps do not move.",
   NEGP + ", " + NEGH + ", no tea spilling, no speaking, no mouth moving, no second mug", True, "still",
   [("mug or hand warps", "one lowering, about a second; hand negatives"), ("face drifts", "small expression only; HOLD clause"), ("straps move", "'the box and the straps do not move'")]),
 "MECH-01": ("A stylised anatomical knee in true lateral profile against a near-black field, a tight glowing spot on the patellar tendon below the kneecap. Exactly as in the start frame.",
   slots(S("ANAT-STRESS-PC")),
   "no arrows, no motion lines, no labels, no numbers, no text overlays, no UI, no static anatomy, no anatomy holding still, no flat ambient lighting, no x-ray look, no cartoon look, no second limb, no hands, no people, no vignette" + ", " + "no lasers, no energy bolts, no fire, no sparks, no beams, no external energy, no orange fog, no emission outside the structures, no shattering, no cracks" + ", no product", False, "in_place",
   [("glow spreads or floats outside the body", "ANAT-STRESS-P holds heat inside the tissue; NEG-EXTERNAL"), ("the limb holds still like a diagram", "load cycles one per second, the structure compresses and recovers"), ("labels or arrows appear", "ANAT-NEG")]),
 "MECH-02": ("A stylised anatomical knee from a low three-quarter angle against a near-black field, the strap seated below the kneecap taking the load. Exactly as in the start frame.",
   slots(S("ANAT-STRESS-SC")),
   "no arrows, no motion lines, no labels, no numbers, no text overlays, no UI, no static anatomy, no anatomy holding still, no flat ambient lighting, no x-ray look, no cartoon look, no second limb, no hands, no people, no vignette" + ", " + "no lasers, no energy bolts, no fire, no sparks, no beams, no external energy, no orange fog, no emission outside the structures, no shattering, no cracks" + ", no emission crossing the product line, no load reaching the tendon, no product moving, no product failing", True, "in_place",
   [("the strap slides or rotates under load", "'the product holds station under every arrival'; NEG-PROT"), ("glow crosses the product line", "NEG-PROT; ember stays dim"), ("labels or arrows appear", "ANAT-NEG")]),
 "NS-03a": ("Close-up looking down at a man's right shin as he sits on the edge of a bed, both hands sliding the closed knee strap up toward his kneecap. Exactly as in the start frame.",
   "Already moving on the first frame: both hands slide the strap up the last few centimetres in one smooth slide, about a second, and stop at contact with it seated snug directly under the kneecap, the notch against its lower edge; the hands rest there. Fitting it, never adjusting it. " + RIGID,
   NEGP + ", " + NEGH + ", " + PS.NEG_ADJUST + ", no strap passing over the kneecap, no face in frame", True, "in_place",
   [("strap overshoots onto the kneecap", "'stop at contact … snug directly under the kneecap'; 'no strap passing over the kneecap'"), ("hands fuse with the strap", "hands on the shell's edges, one movement; hand negatives"), ("reads as adjusting", "NEG_ADJUST")]),
 "NS-03b": ("Close-up of two hands holding the knee strap up toward the lens with its smooth inner pad facing the camera. Exactly as in the start frame.",
   "The hands hold the strap still toward the lens; only a small natural settle of the hands in the first second, then stillness. The strap does not turn or rotate — the pad stays facing the camera the whole time. " + RIGID,
   NEGP + ", " + NEGH + ", no strap rotating, no turning the strap, no wordmark appearing on the pad, no second strap", True, "still",
   [("the strap turns and changes shape", "§27G: don't animate the turn — the frame is already turned; 'no strap rotating'"), ("fingers merge with the band", "hands still; hand negatives"), ("pad gains texture or text", "'no wordmark appearing on the pad'")]),
 "NS-04b": ("Medium shot of a Black British woman of about seventy at a garden table doing a crossword, the black knee strap on her right knee in the lower frame. Exactly as in the start frame.",
   "Already writing on the first frame: she fills in one word with her pen, a few pen strokes across about two seconds, then taps the pen once on the paper, absorbed and relaxed. Her legs do not move. " + RIGID,
   NEGP + ", " + NEGH + ", no looking at the knee, no hand on the knee, no readable text", True, "still",
   [("hand and pen warp", "small pen strokes only; hand negatives"), ("strap shifts while she sits", "'her legs do not move'; rigid clause"), ("face drifts", "absorbed, small movement; HOLD clause")]),
 "NS-05": ("Medium close-up over a patient's shoulder: a surgeon in navy scrubs hands the knee strap across the desk. Exactly as in the start frame.",
   "Already moving on the first frame: she passes the strap into the patient's hand, one pass in about a second — one grip change, her fingers opening as the patient's close on the shell's edge — then she sits back with a small reassuring nod. " + RIGID,
   NEGP + ", " + NEGH + ", no dropping the strap, no speaking, no mouth moving, no white coat", True, "in_place",
   [("two hands fuse on the strap", "one grip change only (§27G); hand negatives"), ("strap bends in the hand-off", "rigid clause; product negatives"), ("face drifts", "HOLD clause; 'no speaking'")]),
 "NS-06": ("Close-up from the side of a man's right leg in stone chinos, the trouser leg falling down over his knee. Exactly as in the start frame.",
   "Already falling on the first frame: the chino leg drops the rest of the way down over the knee and settles, one drop in about a second, the fabric lying flat over the knee with no bulge and breaking softly at the shoe. The leg does not move.",
   NEGP + ", no bulge under the fabric, no strap outline, no hand in frame after the first frame, no face in frame", True, "still",
   [("fabric shows a bulge", "'lying flat … no bulge'; 'no strap outline'"), ("fabric morphs", "one drop, about a second; HOLD clause"), ("hand stays and fuses", "'no hand in frame after the first frame'")]),
 "NS-07": ("Medium shot of four friends in their sixties and seventies walking toward the lens along a park path, the black knee strap on the nearest woman's right knee. Exactly as in the start frame.",
   "Already walking on the first frame: three easy steps toward the lens, one step per second, normal walking speed, chatting and laughing, arms swinging; they stay in frame and never reach the lens. The camera stays where it is. " + RIGID,
   NEGP + ", " + S("NEG-EFFORT") + ", no fifth person, no extra legs, no feet merging, no faces changing", True, "travels",
   [("people's legs blend", "three steps at one per second; 'no extra legs, no feet merging'"), ("faces drift", "HOLD clause; 'no faces changing'"), ("strap slides on the nearest knee", "rigid clause; product negatives")]),
}

for b, (subj, motion, neg, prod, sm, risks) in C.items():
    p = {"shot": b.lower().replace("-", "_"), "subject": subj, "camera": CAM, "motion": motion + " " + HOLD,
         "lighting": LIGHT if not b.startswith("MECH") else "As in the start frame: three-source render lighting, near-black field, no change across the clip.",
         "style": "As in the start frame.", "negatives": NEG + ", " + neg}
    s = json.dumps(p, ensure_ascii=False, separators=(",", ":"))
    call = dict(beat=b, connector="kling", mode=1, kind="broll", prompt=s, duration=LEN[b], resolution="1080p", aspect_ratio="9:16",
                start_image=URL[b], start_approved=True, approved_by="user: 'I'VE CONFIRM PROCEED' (2026-09-29) on the Act 1 images",
                pinned=False, end_image=None, end_approved=False, subject_motion=sm, prefer_multi_shots="false", generation=1,
                risks=[dict(risk=r, prevented_by=v) for r, v in risks])
    (OUT / f"{b}.v1.kling.json").write_text(s)
    (OUT / f"{b}.v1.call.json").write_text(json.dumps(call, indent=1))
    print(b, LEN[b], "s", len(s), "chars")
