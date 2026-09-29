#!/usr/bin/env python3
"""Step 7 · Act 1 body videos — Kling 3.0 Omni I2V (§35 JSON, §27A arc, §27G one action + pace, §22X preflight), routed through Kie
(user override 2026-09-28, Kling at 3 credits). Start frames = the user-confirmed body images (2026-09-29 "all confirmed").
Lengths from acts/plan/lengths.py on the locked VO (TH-A1 trimmed): each clip covers its own script span to the next B-roll's first word.
Mechanism beats (§12A): each is the entry of its own mechanism run (a B-roll sits either side) → RIG-RVF; HOLD-C + HOLD-AC; NEG-CAM-RV +
selected ANAT-NEG clauses (§37 budget); lighting carried from the render (exempt from INHERIT-CAP).
Writes acts/video/<beat>.call.json; preflight.py must PASS before voice/kie_kling.py sends."""
import re, json, pathlib
here = pathlib.Path(__file__).parent
ROOT = here.parents[2]
T = (ROOT / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()
L = json.load(open(here / "plan/lengths.json"))
CARD = {}
U = "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/"
START = {"BR-01": U + "hf_20260929_153713_1dadd868-8315-4cfd-9d9e-c4de39f8eee4.png",
         "MECH-01": U + "hf_20260929_145606_a1f58ac4-2f47-4d79-9733-f1ae7dab5521.png",
         "BR-02": U + "hf_20260929_160352_f5737d15-5f22-4e4e-8afe-40b36c92b22f.png",
         "MECH-03": U + "hf_20260929_160352_3c5a033f-cfb1-4ece-ac7e-28fb9a762936.png",
         "BR-04": U + "hf_20260929_190321_7527b4ef-2b3e-43c6-b59f-5e39cb223893.png",
         "BR-05a": U + "hf_20260929_160353_a5c721f5-2fe3-459b-a43d-ba2a0f9c5665.png",
         "BR-05b": U + "hf_20260929_153713_1da6919a-a58f-4ca6-a104-9884873fb62d.png",
         "MECH-05": U + "hf_20260929_145606_54d936e8-fbab-4f15-8645-dfc2101a1535.png"}
NEG = lambda *extra: ", ".join([S("NEG-WARP-C"), S("NEG-LIGHT-C"), "no music, no voice, no text appearing", *extra])
ANAT_SEL = ("no crossfade, no glow fading in place, no gradual onset, no static anatomy, no arrows, no motion lines, no text overlays, no labels, "
            "no numbers, no individual muscle fibres, no second limb, no clothing, no hands, "
            "no people, no x-ray look, no flat illustration, no cartoon look, no vignette")
PIP = "Framed for a picture-in-picture crop: one subject, large and centred, readable at a third of the width."
def base(beat, pace, sm, risks, kind="broll"):
    return {"beat": beat, "connector": "kling", "mode": 1, "kind": kind, "duration": L[beat]["kling"], "resolution": "1080p",
            "aspect_ratio": "9:16", "start_image": START[beat], "start_approved": True, "pinned": False, "end_image": None, "end_approved": False,
            "script_line": L[beat]["line"], "pace": pace, "subject_motion": sm, "prefer_multi_shots": "false", "generation": 1, "rack": None,
            "risks": risks, "kie_model": "kling-3.0-omni/image-to-video", "route": "kie",
            "route_note": "user override 2026-09-28: Kie AI substitute for the Kling connector",
            "approved_by": "user on the board + chat 2026-09-29 ('all confirmed')", "audio": False}
def broll(beat, motion, framing, extra_neg, pace, sm, risks):
    j = {"shot": beat.lower().replace("-", "_"), "subject": S("INHERIT-SUBJ"),
         "camera": {"movement": S("RIG-R1C"), "framing": framing + " " + PIP},
         "motion": motion + " " + S("HOLD-C") + " " + S("PHYS-MOTION-C"),
         "lighting": S("INHERIT-CAP"), "style": S("INHERIT-ENV"), "negatives": NEG(*extra_neg)}
    c = base(beat, pace, sm, risks); c["prompt"] = json.dumps(j, ensure_ascii=False, separators=(",", ":")); return c
def mech(beat, motion, framing, extra_neg, risks):
    j = {"shot": beat.lower().replace("-", "_"), "subject": S("INHERIT-SUBJ"),
         "camera": {"movement": S("RIG-RVF"), "framing": framing + " " + PIP},
         "motion": motion + " " + S("HOLD-C") + " " + S("HOLD-AC"),
         "lighting": "As in the start frame.",
         "style": S("INHERIT-ENV"), "negatives": ", ".join([S("NEG-WARP-C"), S("NEG-CAM-RV"), ANAT_SEL, *extra_neg])}
    c = base(beat, "brisk", "in_place", risks); c["prompt"] = json.dumps(j, ensure_ascii=False, separators=(",", ":")); return c
C = {}
C["BR-01"] = broll("BR-01",
  "She sits at the kitchen table looking down, her right hand round the mug; her left hand rubs slowly down over her left knee once and back up, "
  "over about two seconds, then rests there; she lets out a slow breath and her shoulders drop a little; still, hand on the knee, on the last frame.",
  "MEDIUM, as in the start frame: her seated at the kitchen table, head to feet.",
  ["no standing up, no drinking, no mug moving by itself, no speaking, no mouth moving, no strap, no brace"],
  "unhurried", "in_place",
  [{"risk": "the mug slides or melts into her hand", "prevented_by": "her right hand stays round the mug; no mug moving by itself; HOLD-C"},
   {"risk": "she speaks under the VO", "prevented_by": "no speaking, no mouth moving; the action is a breath"},
   {"risk": "the rub repeats as a loop", "prevented_by": "one rub down and back over two seconds, then rests"}])
C["MECH-01"] = mech("MECH-01",
  "The virtual camera pushes in on the worn LEFT knee joint: where bone meets bone the orange-red glow flares brighter once, on the push, and "
  "stays hot; behind it the right knee's joint warms to a faint red, beginning; the bones do not move.",
  "MEDIUM-CLOSE, as in the start frame: both knee joints, the left one in front.",
  ["no joints moving, no bones sliding"],
  [{"risk": "bones bend or separate", "prevented_by": "HOLD-AC; the bones do not move"},
   {"risk": "the glow fades in slowly and reads as ambient", "prevented_by": "flares once on the push; no gradual onset, no crossfade"},
   {"risk": "the camera orbits away from the left joint", "prevented_by": "RIG-RVF push toward the target; NEG-CAM-RV"}])
C["BR-02"] = broll("BR-02",
  "His right hand pushes the knee X-ray film up the last centimetre into the lightbox clip and lets go; the clip closes on it with a small snap; the "
  "film settles flat against the lit glass; his hands draw back down and out of the bottom of the frame, over about two seconds; the X-ray hangs still at the end.",
  "CLOSE, as in the start frame: his hands and the X-ray on the lit glass.",
  ["no film sliding off, no second film, no writing appearing on the film, no face"],
  "unhurried", "in_place",
  [{"risk": "the film warps or duplicates", "prevented_by": "one push and let go; no second film; HOLD-C"},
   {"risk": "text appears on the film", "prevented_by": "no writing appearing on the film, no text appearing"},
   {"risk": "the film falls", "prevented_by": "the clip closes on it; no film sliding off"}])
C["MECH-03"] = mech("MECH-03",
  "The leg takes one step's load: the thigh muscle tightens and the knee gives a little, and at that moment the band of tendon under the kneecap "
  "flashes bright red along its whole length, as one band; the red holds hot while the load stays on; the kneecap and shin bone keep their places.",
  "CLOSE, as in the start frame: the knee, the kneecap and the band of tendon below it.",
  ["no red spreading over the whole knee, no second band"],
  [{"risk": "the red spreads over the whole knee", "prevented_by": "the band of tendon under the kneecap flashes as one band; no red spreading"},
   {"risk": "the leg bends too far and the anatomy breaks", "prevented_by": "the knee gives a little; HOLD-AC"},
   {"risk": "the glow fades in gently", "prevented_by": "flashes at the moment of load; no gradual onset"}])
C["BR-04"] = broll("BR-04",
  "Her right forefinger presses into the soft spot directly under the centre of her kneecap: one slow firm press over about a second, the skin "
  "dimpling round the fingertip, held, then eased a little; the fingertip never leaves that spot and never slides to the side of the knee; her left "
  "hand stays on the hem; still pressing on the last frame.",
  "CLOSE, as in the start frame: her bent knee head-on, the kneecap and the fingertip under it.",
  ["no finger sliding to the side of the knee, no finger moving onto the kneecap, no second hand pressing, no skirt moving over the knee"],
  "unhurried", "in_place",
  [{"risk": "the fingertip drifts to the side of the knee (the user's many fixes)", "prevented_by": "never leaves that spot; no finger sliding to the side"},
   {"risk": "fingers fuse or multiply", "prevented_by": "one press; NEG-WARP-C; HOLD-C"},
   {"risk": "the skirt hem drops over the knee", "prevented_by": "her left hand stays on the hem; no skirt moving over the knee"}])
C["BR-05a"] = broll("BR-05a",
  "She pulls herself up onto the next stair: both hands tighten on the newel post, her left foot lifts slowly onto the tread above and her weight "
  "follows it, over about two seconds, her back bent with the effort; she stops there, gripping the post, on the last frame.",
  "WIDE, as in the start frame: the hall and the foot of the stairs, her whole body side-on on the bottom steps.",
  ["no second step, no stumbling, no falling, no feet sliding over the steps, no extra steps appearing, no hand leaving the post"],
  "unhurried", "travels",
  [{"risk": "a foot melts into or misses the tread", "prevented_by": "one step up at a slow countable pace; NEG-WARP-C; no feet sliding"},
   {"risk": "she climbs several steps and leaves frame", "prevented_by": "one step, then she stops; no second step"},
   {"risk": "the camera travels with her", "prevented_by": "RIG-R1C: the phone stays in the hall, sways but never travels"}])
C["BR-05b"] = broll("BR-05b",
  "She comes down one stair: gripping the rails either side, she lowers her right foot onto the next stair down, slowly, over about two seconds; as "
  "her weight drops onto it her left knee bends stiffly and braces to catch her, her shoulders tensing; she stays there, both hands gripping, on the last frame.",
  "WIDE, as in the start frame: her whole body on the stairs, the flight between her and the lens.",
  ["no second step, no stumbling, no falling, no feet sliding over the steps, no extra steps appearing, no hands leaving the rails"],
  "unhurried", "travels",
  [{"risk": "a foot misses or melts into the step", "prevented_by": "one step down at a slow countable pace; NEG-WARP-C"},
   {"risk": "she walks down several steps", "prevented_by": "one stair, then she stays there; no second step"},
   {"risk": "the camera climbs towards her", "prevented_by": "RIG-R1C: the phone stays at the foot of the stairs"}])
C["MECH-05"] = mech("MECH-05",
  "The leg steps down: the foot lands on the step below and the thigh muscle lengthens to catch the weight; at the catch the band of tendon under "
  "the kneecap flashes bright red once, hard, and stays hot as the weight settles; the bones keep their shape.",
  "MEDIUM-CLOSE, as in the start frame: the whole leg stepping down, the knee in the middle.",
  ["no second step, no foot sliding through the step"],
  [{"risk": "the leg distorts through the step", "prevented_by": "one step down; HOLD-AC; no foot sliding through the step"},
   {"risk": "the flash lands before the catch", "prevented_by": "the flash comes at the catch, once, and stays hot"},
   {"risk": "the camera wanders off the knee", "prevented_by": "RIG-RVF push toward the target; NEG-CAM-RV"}])
(here / "video").mkdir(exist_ok=True)
for b, c in C.items():
    (here / "video" / f"{b}.call.json").write_text(json.dumps(c, ensure_ascii=False, indent=1))
    print(f"{b:8s} {len(c['prompt']):5d} chars  {c['duration']}s  span {L[b]['span']}s")
