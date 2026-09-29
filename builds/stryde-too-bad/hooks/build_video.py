#!/usr/bin/env python3
"""Step 6 hook clips for stryde-too-bad — §35 Kling JSON per confirmed start image (§27G, §37 ≤ 2,500 chars).
Route: Kling 3.0 on Kie (`kie.py kling`, 9:16, multi_shots false, no sound) — the Kling connector holds 3 credits (§5 fallback).
Lengths are E6: the part's time on screen in the locked T8 VO + 0.4 s + 0.5 s, rounded up. Pattern from stryde-thirty-years/broll/build_video.py.
Writes hooks/video/<BEAT>.call.json (for preflight.py) and <BEAT>.prompt.txt (the minified JSON sent to Kling).
Usage: build_video.py BEAT [BEAT ...]"""
import json, math, re, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent; BUILD = HERE.parent; ROOT = BUILD.parents[1]
T = (ROOT / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
def S(i):
    return re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S).group(1).strip()
HANDHELD = S("RIG-R1C")
NEG_BASE = S("NEG-WARP-C")
NEG_MOT = "no held pose, no looping motion, no reversed motion, no slow motion, no two separate actions in one clip"
NEG_TAIL = "no music, no voice, no text, no captions"
# on-screen seconds of each hook part in the locked VO (vo/cut/T8_V1.mp3 = HK1 order, T8_V2.mp3 = HK2 order; split cuts)
ON = {"HK1-01": 3.01, "HK2-01": 2.61}
START = {"HK1-01": "hooks/HK1-01_v2.png", "HK2-01": "hooks/HK2-01_v1.png"}
PIN_END = {"HK1-01": "hooks/HK1-01-END_v1.png"}   # act map pin_end: the product turns (§27G rule 5)
sys.path.insert(0, str(ROOT / "products/stryde")); import stryde_product_sheet as P  # noqa: E402
PRODUCT = "The strap keeps its exact shape, size and wordmark in every frame and moves only with the hand that holds it; " + P.HOLD_PC
NEG_PROD = "no bending, no curling, no folding, no melting, no flipping of the product, no shell turning side-on, no second strap"
# beat: (framing, rig, motion, extra negatives, subject_motion, risks)
V = {
 "HK1-01": ("CLOSE, high three-quarter as in the start frame: her hand, the strap, the grey brace.",
   HANDHELD,
   "Her wrist turns slowly a little, about twenty degrees, over about two seconds, already turning on the first frame, the shell "
   "coming round to the end frame, the near chrome slide catching the window light; same pinch grip throughout. The brace never "
   "moves. The camera sways where it is.",
   "no brace moving, no fingers moving on the shell, no grip change, no face", "in_place",
   [("the shell bends or turns into a different shape as it turns (§27G product rigid)", "pinned end frame + HOLD_PC + product negatives"),
    ("fingers slide over the wordmark or peaks during the turn", "same pinch grip stated + no grip change + HOLD-HC"),
    ("the turn overshoots to side-on or loops back", "about twenty degrees, one turn, pinned end; no looping / reversed motion")]),
 "HK2-01": ("CLOSE overhead as in the start frame, looking straight down into the open kitchen drawer.", HANDHELD,
   "His right hand pulls the drawer the last few centimetres open towards the camera in one short pull over about two seconds, "
   "already moving on the first frame; the tangle of old supports inside jolts a little with the pull and settles, the strap over the "
   "front edge swinging once. Then his fingers stay hooked on the handle. The camera sways where it is.",
   "no drawer closing, no drawer sliding by itself, no supports climbing out, no new objects in the drawer, no stryde strap, no face",
   "in_place",
   [("supports in the drawer morph, merge or multiply", "HOLD-C + 'no new objects' + NEG-WARP-C"),
    ("fingers fuse with the steel handle", "HOLD-HC + finger negatives, fingers stated hooked on the handle"),
    ("drawer keeps sliding or closes (second action)", "one short pull, then fingers stay; no drawer closing / no two actions")]),
}
def build(beat):
    framing, rig, motion, extra, sm, risks = V[beat]; prod = beat in PIN_END
    j = {"shot": beat.lower().replace("-", "_"), "subject": S("INHERIT-SUBJ") + (" " + PRODUCT if prod else ""),
         "camera": {"movement": rig, "framing": framing},
         "motion": motion + " " + S("HOLD-C") + " " + S("HOLD-HC"),
         "lighting": S("INHERIT-CAP"), "style": S("INHERIT-ENV"),
         "negatives": ", ".join([NEG_BASE, extra] + ([NEG_PROD] if prod else []) + [NEG_MOT, NEG_TAIL])}
    return json.dumps(j, ensure_ascii=False, separators=(",", ":"))
if __name__ == "__main__":
    (HERE / "video").mkdir(exist_ok=True)
    for beat in sys.argv[1:]:
        prompt = build(beat); framing, rig, motion, extra, sm, risks = V[beat]
        dur = max(3, math.ceil(ON[beat] + 0.4 + 0.5))
        call = {"beat": beat, "connector": "kling", "route": "Kling 3.0 on Kie (kie.py kling), Kling connector out of credits",
                "mode": 1, "kind": "broll", "prompt": prompt, "duration": dur, "resolution": "1080p", "aspect_ratio": "9:16",
                "start_image": START[beat], "start_approved": True, "pinned": beat in PIN_END, "end_image": PIN_END.get(beat), "end_approved": False,
                "pace": "unhurried", "subject_motion": sm, "prefer_multi_shots": "false", "generation": 1,
                "risks": [{"risk": a, "prevented_by": b} for a, b in risks]}
        (HERE / f"video/{beat}.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
        (HERE / f"video/{beat}.prompt.txt").write_text(prompt)
        print(beat, dur, "s", len(prompt), "chars")
