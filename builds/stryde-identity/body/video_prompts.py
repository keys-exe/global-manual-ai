#!/usr/bin/env python3
"""Body B-roll video prompts — Kling (kling-video-v3_0_omni, image_1 = the confirmed start image).
User rules for this build: Kling only (never Seedance), short plain-text prompts (not JSON), follow the act map.
§27G: one action at a named pace, the strap rigid, the camera sways but never travels with a moving subject.
Writes body/<BEAT>.i2v.txt and body/<BEAT>.call.json (preflight.py input)."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
LEN = {r["beat"]: r["clip_s"] for r in json.loads((HERE.parent / "work/body_lengths.json").read_text())}

STRAP = "The strap stays exactly where it is and keeps its shape; the shell is rigid and never bends."
HELD = "The strap keeps its shape; the shell is rigid and never bends."
END = "No text, no music."
ANAT = ("Stylised 3D anatomy render, slow and smooth. The anatomy keeps its exact form; nothing melts or changes shape. "
        "No text, no labels, no music.")

P = {
 "MECH-01": ("The knee takes a step's weight: the load arrives from above and the small glow on the tendon just below the "
             "kneecap brightens once, then holds. Slow, steady camera drift. " + ANAT, "still"),
 "MECH-02": ("A slow, gentle push in towards the one small glowing spot on the tendon just below the kneecap; the glow pulses "
             "softly once. " + ANAT, "still"),
 "BR-03": ("The surgeon slowly turns the strap a little in the window light, looking at it. " + HELD +
           " The phone stays still on the desk. " + END, "in_place"),
 "BR-04": ("The surgeon's fingertip taps gently twice beside the notch of the strap on the patient's knee. The patient lies "
           "still. " + STRAP + " Handheld phone, steady. " + END, "in_place"),
 "MECH-07": ("The load arrives from above and the pad lights with a soft cool glow that spreads out across the shell to its two "
             "ends; the tendon beneath stays calm. Slow, steady camera drift. " + ANAT, "still"),
 "BR-05": ("A fingertip slowly slides the small cheap copy a little closer to the real strap, then rests. Both stay flat on "
           "the table and keep their shape. Handheld phone, steady. " + END, "in_place"),
 "BR-06": ("The surgeon holds the strap up with its back to the camera and tilts it slowly a little in the light, the pad "
           "catching the window light. " + HELD + " Handheld phone, steady. " + END, "in_place"),
 "BR-08": ("She walks steadily on the treadmill at an easy pace while the scientist watches her knee. " + STRAP +
           " The phone stays still. " + END, "in_place"),
 "BR-09": ("Her knee moves through an easy walking stride on the treadmill, one stride after another. " + STRAP +
           " The phone stays still at knee height. " + END, "in_place"),
 "MECH-10": ("A slow, gentle orbit a little way round the knee joint; the worn gap between the bones glows faintly amber. "
             + ANAT, "still"),
 "MECH-11": ("A slow, gentle push in towards the worn cartilage and the small tear in the meniscus, glowing faintly amber. "
             + ANAT, "still"),
 "BR-12": ("She walks briskly along the path past the green railings with long strides, towards the camera. " + STRAP +
           " The phone stays still beside the path. " + END, "travels"),
 "BR-13": ("She climbs one stair at an easy pace, her hand free of the rail. " + STRAP +
           " The phone stays still at the foot of the stairs. " + END, "travels"),
 "BR-14": ("She pauses on the landing and breathes out, calm, her palm resting on her thigh above the knee. " + STRAP +
           " Handheld phone, steady. " + END, "in_place"),
 "MECH-15": ("The strap on the model holds a soft steady cool glow across the pad as the load passes through; the tendon and "
             "the joint stay calm. Slow, steady camera drift. " + ANAT, "still"),
 "BR-16": ("Both hands, flat on the shell's two sides, slide the closed strap slowly UP the front of his shin in one smooth "
           "move until it stops just below the kneecap. It only moves up. The band stays closed; nothing is opened, threaded "
           "or tightened. Handheld phone, steady. " + END, "in_place"),
 "BR-17": ("He lifts the box from the floor in one slow, steady squat-lift and stands up. " + STRAP +
           " The phone stays still. " + END, "in_place"),
 "BR-18": ("Her hands let the trouser leg fall slowly down over the knee until the fabric covers the strap and lies flat. "
           "Handheld phone, steady. " + END, "in_place"),
 "BR-19": ("He leans on the workbench and takes a slow sip of tea, relaxed. " + STRAP + " The phone stays still. " + END,
           "in_place"),
 "BR-20": ("The surgeon's hand passes the strap slowly across the desk into the patient's open hand, which closes gently "
           "round it. " + HELD + " The phone stays still. " + END, "in_place"),
 "BR-21": ("The group of older walkers walks towards the camera along the path past the railings, chatting, at an easy pace. "
           + STRAP + " The phone stays still beside the path. " + END, "travels"),
 "BR-22": ("Her hands slowly lift the lid off the black box. The box keeps its shape. Handheld phone, steady. " + END,
           "in_place"),
 "BR-23": ("Her fingertips rest on the open box's edge and nudge it slightly towards the camera. The two straps lie still "
           "and flat in the box. Handheld phone, steady. " + END, "in_place"),
 "BR-24": ("She turns the strap slowly in the window light, looking at it. " + HELD + " Handheld phone, steady. " + END,
           "in_place"),
 "BR-25": ("She steps up onto the first stair at an easy pace. " + STRAP + " The phone stays still in the hall. " + END,
           "in_place"),
 "BR-26a": ("Both hands, flat on the shell's two sides, slide the closed strap slowly UP the front of her shin in one smooth "
            "move until it stops just below the kneecap. It only moves up. The band stays closed; nothing is opened, "
            "threaded or tightened. Handheld phone, steady. " + END, "in_place"),
 "BR-26b": ("She climbs one stair towards the camera at an easy pace, her hand free of the rail. " + STRAP +
            " The phone stays still on the landing. " + END, "travels"),
}

RISK = {
 "still": [{"risk": "anatomy melts or morphs", "prevented_by": "slow motion, 'keeps its exact form'"},
           {"risk": "text or labels appear", "prevented_by": "'no text, no labels'"},
           {"risk": "camera move too fast warps the render", "prevented_by": "slow steady drift/push only"}],
 "any": [{"risk": "strap bends or slides", "prevented_by": "rigid-shell clause, strap stays where it is"},
         {"risk": "limbs distort from over-specified motion", "prevented_by": "one plain action at a named easy pace"},
         {"risk": "camera travels with the subject and warps the frame", "prevented_by": "phone still / steady (§27G)"}],
}

if __name__ == "__main__":
    for b, (text, sm) in P.items():
        (HERE / f"{b}.i2v.txt").write_text(text + "\n")
        c = {"beat": b, "connector": "kling", "mode": 1, "kind": "broll", "prompt": text, "duration": LEN[b],
             "resolution": "1080p", "aspect_ratio": "9:16", "start_image": f"{b} confirmed image", "start_approved": True,
             "pinned": False, "prefer_multi_shots": "false", "generation": 1, "subject_motion": sm, "pace": "unhurried",
             "risks": RISK["still" if b.startswith("MECH") else "any"]}
        (HERE / f"{b}.call.json").write_text(json.dumps(c, indent=1, ensure_ascii=False))
    print(len(P), "video prompts")
