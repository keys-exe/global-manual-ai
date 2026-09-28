"""User Fix round 1: preflight calls (generation 2, diagnosed fix) for every fixed beat."""
import json, sys, subprocess, copy
import broll, calls
from fix1_motion import build
S = "/tmp/claude-0/-home-user-global-manual-ai/ea15d283-9935-5994-9efa-ae7c21b1ec32/scratchpad/board2/generations/"
LEN = {x["beat"]: x["call_s"] for h in ("HK1","HK2","HK3") for x in json.load(open(broll.B / f"edit/lengths_v2_{h}.json"))["lengths"]}
DIAG = {  # user note -> source of the fault -> change
 "A1-B2": "motion: prompt asked for alternating steps → step-to, both feet land on the same step each time",
 "A1-B4": "motion: steady grip read as easy → hesitant hovering foot, clenched grip, hunched shoulders",
 "A1-B5": "motion: smooth descent → laboured step-to on both rails, arms taking the weight",
 "A2-B1": "frame: wide view showed the whole flight → tight frame, one tread and one riser only",
 "A2-B2": "frame: wrong stairs and finger on the wrong spot → C2's oak stairs, fingertip on the patellar tendon below the kneecap",
 "A3-B2": "frame: distorted knee in an awkward overhead crop → clean close-up of one normal bent knee, one hand",
 "A4-B1": "frame: wide seated shot → product close-up, the strap the hero of the frame, wordmark readable",
 "A4-B2": "frame: fingers hid the product → product close-up, finger pointing at the notch",
 "A4-M1": "frame + motion: the mechanism was faint → large pad/tendon view, the load wave visibly caught and spread at the pad",
 "A4-P1": "motion: rigid-product clause froze the band → rigid shell only, band swings and settles with weight",
 "A4-P2": "frame + motion: still object + push-in read as an image zoom → his thumb presses the pad and it squashes",
 "A4-P3": "frame + motion: still object + push-in read as an image zoom → his hand sets the second strap down, band drops",
 "A5-B1": "frame: dropping straps in a box → lifting a heavy toolbox in work shorts, strap on the right knee",
 "A5-B2": "frame + motion: hand on the rail → both arms loose, hands never touch the rail",
 "A5-B3": "frame + motion: standing weight shift → brisk descent, one foot per step every 0.6s",
 "A5-B4": "frame + motion: slow step → brisk descent every 0.6s, frame caught mid-step",
 "A5-B5": "frame: stair geometry distorted → straight even flight, parallel rails, new frame",
 "A5-F1": "frame + motion: copy worn on the leg → held in her lap, band stretched out slack by both hands",
}
def make(b, start_url):
    d = json.load(open(S + f"stryde-cascade__{b}.json"))
    vv = d.get("videoVersions") or []
    r, p = build(b)
    (broll.PR / "clips" / f"{b}.v2.kling.json").write_text(p)
    k = calls.kind(r)
    c = {"beat": b, "connector": "kling", "route": "kie kling-3.0/video (Kling account short, §5)", "mode": 1, "kind": "broll",
         "prompt": p, "duration": LEN[b], "resolution": "1080p", "aspect_ratio": "9:16",
         "start_image": start_url, "start_approved": True, "pinned": False, "end_image": None, "end_approved": False,
         "subject_motion": "still" if k == "still" else ("travels" if k == "stairs" else "in_place"), "prefer_multi_shots": "false",
         "generation": len(vv) + 1, "fix_note": f"user Fix '{d.get('fault')}' — {DIAG[b]}", "risks": calls.RISKS[k]}
    path = broll.B / f"calls/{b}.v2.json"
    json.dump(c, open(path, "w"), indent=1, ensure_ascii=False)
    out = subprocess.run(["python3", str(broll.B.parents[1] / ".claude/skills/ai-prompt-engineer/scripts/preflight.py"), str(path)], capture_output=True, text=True).stdout
    return out.strip().splitlines()[-1], [l for l in out.splitlines() if "FAIL" in l]
if __name__ == "__main__":
    jobs = json.load(open("work/fix1_jobs.json")) if len(sys.argv) < 2 or sys.argv[1] != "--old" else {}
    for b in DIAG:
        d = json.load(open(S + f"stryde-cascade__{b}.json"))
        url = jobs.get(b, {}).get("url") or d["imageUrl"]
        print(b, "new" if b in jobs else "old", make(b, url))
