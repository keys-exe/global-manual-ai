#!/usr/bin/env python3
"""stryde-what-changed — Kling clip calls (§35 minified JSON, §27G natural motion, §22X preflight) for confirmed start images.

Kling account short (3 credits) → Kie `kling-3.0/video` (pro 1080x1920, 9:16, single shot, sound off) per §5 / V7.65.0.
E6 lengths: screen time (cut to next cut, from the trimmed variant's word timestamps, cut 3 frames before the anchor word)
+ 0.4 s skip + 0.5 s, rounded up, 3–15 s; §27G human motion 3–6 s.
Usage: clips.py HK1-a HK1-b  → work/clips/<beat>.kling.json + <beat>.call.json
"""
import json, re, sys, pathlib, math

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
T = (ROOT / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
sys.path.insert(0, str(ROOT / "products/stryde"))
import stryde_product_sheet as P  # noqa: E402


def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S)
    if not m: raise KeyError(i)
    return m.group(1).strip()


ROWS = {r["beat"]: r for r in json.loads((HERE / "actmap_rows.json").read_text())}
ANAT_SLOTS = {"[REGION]": "knee", "[STACK]": "quadriceps, hamstrings and calf", "[BONES]": "femur, patella and tibia",
              "[TARGET]": "the patellar tendon", "[TARGET JOINT]": "the knee joint", "[SITE]": "the patellar tendon immediately below the kneecap"}
STILL_CAM = "Locked off on a small tripod: the camera does not move at all, no pan, no tilt, no push, no drift."
NEG_CAM = "no camera travelling with the subject, no camera movement, no zoom"


def length(screen_s, lo=3, hi=6):
    return max(lo, min(hi, math.ceil(screen_s + 0.9)))


def clip(beat, subject, motion, neg, screen_s, hi=6, anat=False, risks=()):
    r = ROWS[beat]
    mot = motion + " " + S("HOLD-C") + " " + (S("ANAT-LOAD") if anat else S("PHYS-MOTION-C"))
    for k, v in ANAT_SLOTS.items():
        mot = mot.replace(k, v)
    d = {"shot": beat.lower().replace("-", "_"), "subject": subject + " Exactly as in the start frame.",
         "camera": {"movement": STILL_CAM, "framing": "As in the start frame."},
         "motion": mot, "lighting": S("INHERIT-CAP"), "style": "As in the start frame.",
         "negatives": ", ".join([S("NEG-WARP-C"), NEG_CAM, neg, "no music, no speech, no slow motion"])}
    return d, length(screen_s, hi=hi), list(risks)


B = {}
B["HK1-a"] = clip("HK1-a",
    "A white British woman of sixty-nine, seen from the side waist-down through the white stair spindles, coming DOWN her stairs forwards: "
    "a navy A-line skirt ending just above the knee, bare knees and shins, white canvas plimsolls, her left hand on the honey oak handrail.",
    "Already mid-step on the first frame: her right foot is planted and taking her weight, the right knee bends a little further under the load "
    "as her left foot comes down onto the next stair below — one careful step in about a second and a half — then her weight settles onto it.",
    "no second person, no face in frame, no knee strap, no knee brace, no walking stick, no going up the stairs, no turning sideways, no extra legs",
    4.28, risks=[{"risk": "legs or feet warp on the stair", "prevented_by": "one step at a countable pace, start frame caught mid-step, HOLD-C + NEG-WARP-C"},
                 {"risk": "camera travels with the moving subject", "prevented_by": "locked-off tripod clause, 'no camera travelling with the subject'"},
                 {"risk": "a strap or brace appears on the bare knee (the before state)", "prevented_by": "'no knee strap, no knee brace' + bare knees in subject"}])
B["HK1-b"] = clip("HK1-b",
    "A premium 3D anatomical model of a single knee seen from the side, near-black field, the patellar tendon just below the kneecap glowing as one tight bright spot.",
    "Already under load on the first frame: one step lands — [STACK] shortens and the glow at [SITE] pulses once brighter and eases back, "
    "about one pulse a second, the glow staying one tight spot on the tendon.",
    "no arrows, no text, no labels, no numbers, no glow on the shin bone, no glow spreading down the leg, no second limb, no product, no camera orbit",
    3.36, hi=5, anat=True,
    risks=[{"risk": "the glow spreads down the shin or across the joint", "prevented_by": "'one tight spot' in subject + motion, negatives on shin and spread"},
           {"risk": "the model swims or melts", "prevented_by": "HOLD-C + NEG-WARP-C, one pulse only"},
           {"risk": "text or arrows appear", "prevented_by": "'no arrows, no text, no labels, no numbers'"}])

START = {"HK1-a": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_140551_661eba13-ffd8-4a6f-8b1c-2bfca7beddcc.png",
         "HK1-b": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_140550_bca03c1b-07b2-4580-8709-6f3a74007ee7.png"}

if __name__ == "__main__":
    out = HERE / "clips"; out.mkdir(exist_ok=True)
    for b in sys.argv[1:] or B:
        d, dur, risks = B[b]
        s = json.dumps(d, ensure_ascii=False, separators=(",", ":"))
        (out / f"{b}.kling.json").write_text(s)
        call = {"beat": b, "connector": "kling", "mode": 1, "kind": "broll", "prompt": s, "duration": dur, "resolution": "1080p", "aspect_ratio": "9:16",
                "start_image": START[b], "start_approved": True, "pinned": False, "end_image": None, "end_approved": False,
                "subject_motion": "in_place" if "ANAT" in d["subject"] or "anatomical" in d["subject"] else "travels",
                "prefer_multi_shots": "false", "generation": 1, "risks": risks, "approved_by": "user: board Confirm + 'confirm' (2026-09-29)"}
        (out / f"{b}.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
        print(b, dur, "s", len(s), "chars")
