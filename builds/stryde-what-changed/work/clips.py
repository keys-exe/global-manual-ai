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

# Hook 2 — E6 from the trimmed HK2 variant: HK2-a 0–3.36 s ("and" at 3.36), HK2-b 3.36–6.80 s ("it" at 6.80)
B["HK2-a"] = clip("HK2-a",   # v3 image (user Fixes: different B-roll, then anatomy) — the tendon as a band, high three-quarter ECU
    "A premium 3D anatomical model of a knee seen close from a high three-quarter angle, near-black field: the lower edge of the kneecap at "
    "the top and the patellar tendon running down from it as one thick satin band to the top of the shin, a tight bright spot glowing at its top.",
    "Already under load on the first frame: the band draws taut once as [TARGET JOINT] takes a step's load — it straightens and firms "
    "along its length over about a second — and the spot at [SITE] brightens once and eases back as the load passes; the band stays in place.",
    "no arrows, no text, no labels, no numbers, no thumb, no hand, no ruler, no glow on the shin bone, no glow spreading down the band, "
    "no second limb, no product, no camera orbit, no zoom",
    3.36, hi=5, anat=True,
    risks=[{"risk": "the glow spreads down the band onto the shin", "prevented_by": "tight spot in subject + motion, negatives on spread and shin"},
           {"risk": "the model swims or the band warps", "prevented_by": "HOLD-C + NEG-WARP-C, one tightening only, 'the band stays in place'"},
           {"risk": "a thumb or scale object appears (F2)", "prevented_by": "'no thumb, no hand, no ruler'"}])
B["HK2-b"] = clip("HK2-b",   # v4 image (user Fixes) — side-on, cropped at the waist, lifting a box from a deep squat
    "A Black British man of sixty-six seen side-on from low, cropped at the waist: dark grey jogging shorts, a bare bent right knee in side "
    "profile nearest the lens, both hands under the bottom corners of a plain taped cardboard box just off the hall floor, plain white trainers.",
    "Already at the bottom of the squat on the first frame: his knees straighten and he rises steadily, lifting the box up in front of his "
    "shins to thigh height — one smooth lift in about two seconds, feet staying flat — then he holds, standing with the box.",
    "no face in frame, no head entering the frame, no second person, no knee strap, no knee brace, no writing on the box, no logos, "
    "no dropping the box, no box floating, no extra legs, no extra hands",
    3.44, risks=[{"risk": "hands or box warp during the lift", "prevented_by": "one lift at a countable pace, start frame caught mid-lift, HOLD-C + NEG-WARP-C"},
                 {"risk": "his head rises into the frame as he stands", "prevented_by": "rise only to thigh height with the box, 'no head entering the frame', locked-off tripod"},
                 {"risk": "camera travels with the moving subject", "prevented_by": "locked-off tripod clause, 'no camera travelling with the subject'"}])

START = {"HK1-a": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_140551_661eba13-ffd8-4a6f-8b1c-2bfca7beddcc.png",
         "HK1-b": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_140550_bca03c1b-07b2-4580-8709-6f3a74007ee7.png",
         "HK2-a": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_173257_512cb5a0-c05b-4ab8-af5f-723322275d70.png",
         "HK2-b": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_174627_a9e02dbb-2d91-4a3d-a960-2a053cdfef10.png"}

if __name__ == "__main__":
    out = HERE / "clips"; out.mkdir(exist_ok=True)
    for b in sys.argv[1:] or B:
        d, dur, risks = B[b]
        s = json.dumps(d, ensure_ascii=False, separators=(",", ":"))
        (out / f"{b}.kling.json").write_text(s)
        call = {"beat": b, "connector": "kling", "mode": 1, "kind": "broll", "prompt": s, "duration": dur, "resolution": "1080p", "aspect_ratio": "9:16",
                "start_image": START[b], "start_approved": True, "pinned": False, "end_image": None, "end_approved": False,
                "subject_motion": "in_place" if "ANAT" in d["subject"] or "anatomical" in d["subject"] else "travels",
                "prefer_multi_shots": "false", "generation": 1, "risks": risks, "approved_by": "user: board Confirm + 'confirm' / 'CONFIRM' (2026-09-29)"}
        (out / f"{b}.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
        print(b, dur, "s", len(s), "chars")
