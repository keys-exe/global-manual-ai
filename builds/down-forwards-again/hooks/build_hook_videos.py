#!/usr/bin/env python3
"""Step 6 hook videos — Kling 3.0 Omni I2V (§35 JSON, §27A arc, §27G one action + pace, §22X preflight), routed through Kie
(user override 2026-09-28). Start frames = the user-confirmed hook images (2026-09-29 "confirmed all"). Lengths from
assemble.py --lengths on the locked VO (hooks/plan/*.plan.json). HK2-02a is pin_end → waits for its approved end frame.
Writes hooks/video/<beat>.call.json; preflight.py must PASS before kie_kling.py sends."""
import re, json, pathlib
here = pathlib.Path(__file__).parent
ROOT = here.parents[2]
T = (ROOT / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()
cards = {}
U = "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/"
START = {"HK1-01a": U + "hf_20260929_122456_76034f69-2d2a-4c44-8eb6-6f5cdf19df84.png",
         "HK1-02a": U + "hf_20260929_123622_b6817ac4-bb3e-4664-929d-c9bbff5f4c92.png",
         "HK1-02b": U + "hf_20260929_123623_cac8d27e-8831-4308-ae56-9baa5701182b.png",
         "HK1-02c": U + "hf_20260929_132241_08be9db1-47ba-4f30-b21d-ef207e3261eb.png",
         "HK3-01a": U + "hf_20260929_091945_f282b14c-a926-43ab-9ff2-676a6d6e25ce.png"}
LEN = {"HK1-01a": 3, "HK1-02a": 3, "HK1-02b": 3, "HK1-02c": 4, "HK3-01a": 5}
LINE = {"HK1-01a": "In six weeks, this woman stopped coming down her own stairs backwards.", "HK1-02a": "Without an operation.",
        "HK1-02b": "Without another course of physio.", "HK1-02c": "Without one more brace going in the drawer.",
        "HK3-01a": "Every week somebody brings me a scan of a knee and asks what can be done about the cartilage."}
NEG = lambda *extra: ", ".join([S("NEG-WARP-C"), S("NEG-LIGHT-C"), "no music, no voice, no text appearing", *extra])
def call(beat, motion, framing, extra_neg, sm, risks, product=False):
    j = {"shot": beat.lower().replace("-", "_"), "subject": S("INHERIT-SUBJ"),
         "camera": {"movement": S("RIG-R1C"), "framing": framing},
         "motion": motion + " " + S("HOLD-C") + " " + S("PHYS-MOTION-C"),
         "lighting": S("INHERIT-CAP"), "style": S("INHERIT-ENV"),
         "negatives": NEG(*extra_neg) + (", no bending, no curling, no folding, no melting, no flipping of the product" if product else "")}
    p = json.dumps(j, ensure_ascii=False, separators=(",", ":"))
    return {"beat": beat, "connector": "kling", "mode": 1, "kind": "broll", "prompt": p, "duration": LEN[beat], "resolution": "1080p",
            "aspect_ratio": "9:16", "start_image": START[beat], "start_approved": True, "pinned": False, "end_image": None, "end_approved": False,
            "script_line": LINE[beat], "pace": "brisk" if beat == "HK1-01a" else "unhurried", "subject_motion": sm, "prefer_multi_shots": "false",
            "generation": 1, "rack": None, "risks": risks, "kie_model": "kling-3.0-omni/image-to-video", "route": "kie",
            "route_note": "user override 2026-09-28: Kie AI substitute for the Kling connector",
            "approved_by": "user on the board + chat 2026-09-29 ('confirmed all')", "audio": False}
C = {}
C["HK1-01a"] = call("HK1-01a",
  "She keeps jogging down the station stairs facing forwards: two more light steps, one step every half second, landing on the balls of her feet, "
  "both arms swinging free at her sides and never reaching for the rail, the bag bouncing at her hip, a small smile; still moving down on the last frame. "
  "The wide trousers swing and crease as linen does; both legs stay ordinary covered legs.",
  "WIDE, as in the start frame: her whole body from hair to shoes in frame, steps below her to land on.",
  ["no hand on the handrail, no hand touching the rail or the wall, no stumbling, no falling, no missed step, no feet sliding over the steps, no extra steps appearing",
   "no product visible through the fabric, no bulge at the knee, no rolled trouser leg"],
  "travels",
  [{"risk": "a foot misses or melts into a step", "prevented_by": "two steps only at a countable pace (one per half second), NEG-WARP-C, no missed step"},
   {"risk": "a hand drifts onto the rail (the user's fix)", "prevented_by": "arms swinging free, 'never reaching for the rail' + 'no hand on the handrail'"},
   {"risk": "the camera travels with her", "prevented_by": "RIG-R1C: camera lags the subject, never anticipates; the phone stays at the foot of the stairs"}])
C["HK1-02a"] = call("HK1-02a",
  "The surgeon's hand turns the knee replacement implant slowly a quarter turn towards her so the chrome catches the window, over about two seconds, and holds it there; "
  "she leans back a finger's width and swallows, her hands tightening on the bag handle; she keeps looking at the implant, not at us.",
  "OTS, as in the start frame: over the surgeon's shoulder, soft in the near foreground, the implant sharp, her face across the desk.",
  ["no second implant, no implant changing shape, no surgeon's face, no speaking, no mouth moving, no smiling"],
  "in_place",
  [{"risk": "the implant morphs or duplicates", "prevented_by": "one quarter turn over two seconds, HOLD-C, no implant changing shape, no duplicate objects"},
   {"risk": "her mouth moves as if speaking under the VO", "prevented_by": "no speaking, no mouth moving; the action is a swallow"},
   {"risk": "a face appears on the surgeon", "prevented_by": "no surgeon's face; framing keeps his shoulder soft in the foreground"}])
C["HK1-02b"] = call("HK1-02b",
  "She pushes up onto the low step with her left leg, slow and shaking, over about two and a half seconds, both hands pulling on the parallel bars; "
  "her left knee trembles under the load and straightens only halfway; the physio's hands stay hovering either side of the knee without touching it; "
  "the class keeps stepping behind her, soft; she is still straining on the last frame.",
  "WIDE, as in the start frame: floor level through the near parallel bar, her feet, the step and the floor big in the lower frame.",
  ["no smiling, no speaking, no falling, no physio grabbing her, no extra limbs, no people appearing or vanishing in the class"],
  "in_place",
  [{"risk": "legs or hands fuse with the bars", "prevented_by": "one step-up at a slow countable pace, HOLD-C, NEG-WARP-C"},
   {"risk": "background patients morph or pop in and out", "prevented_by": "class soft and keeps stepping; no people appearing or vanishing"},
   {"risk": "the step is finished too easily (reads as recovery)", "prevented_by": "knee straightens only halfway; still straining on the last frame"}])
C["HK1-02c"] = call("HK1-02c",
  "In the soft background she lowers the grey hinged brace the rest of the way into the black bin bag and lets go of it, over about two seconds, then reaches back towards the open drawer for the next one; "
  "the bag rustles and sags with the weight. In the sharp foreground the knee strap lies still on the table the whole time: it keeps its exact shape, size and wordmark in every frame and does not move at all.",
  "CLOSE on the strap, as in the start frame: the strap sharp in the lower middle, her soft behind it.",
  ["no braces flying or falling through the air, no braces in mid-air, no drawer tipped up, no strap moving, no strap in her hands, no second strap, no strap sliding on the table"],
  "in_place",
  [{"risk": "braces fly into the bag by themselves (the user's fix)", "prevented_by": "her hand lowers the brace and lets go; no braces in mid-air"},
   {"risk": "the strap moves or warps", "prevented_by": "strap lies still, keeps its exact shape, size and wordmark; product negatives"},
   {"risk": "focus jumps to her", "prevented_by": "framing: the strap sharp, her soft; INHERIT-CAP"}], product=True)
C["HK3-01a"] = call("HK3-01a",
  "The knee X-ray film drops the last hand's width onto the heap, lands with a flat slap, slides a little and settles, tilting over the films beneath; "
  "the doctor's hand draws back up and out of the top of the frame; a corner of an envelope under it shifts and settles; everything is still at the end.",
  "OVERHEAD, as in the start frame: straight down on the desk buried under scans.",
  ["no films multiplying, no films vanishing, no writing appearing on the films, no hand re-entering"],
  "in_place",
  [{"risk": "films multiply or merge on impact", "prevented_by": "one film drops, HOLD-C count clause, no films multiplying or vanishing"},
   {"risk": "the film floats or glides", "prevented_by": "PHYS-MOTION-C: mass, flat slap, slides with friction and settles"},
   {"risk": "text appears on films", "prevented_by": "no writing appearing on the films, no text appearing"}])
(here / "video").mkdir(exist_ok=True)
for b, c in C.items():
    (here / "video" / f"{b}.call.json").write_text(json.dumps(c, ensure_ascii=False, indent=1))
    print(f"{b:8s} {len(c['prompt']):5d} chars  {c['duration']}s")
