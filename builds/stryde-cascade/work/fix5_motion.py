"""User Fix round 5 (2026-09-28): clip calls for the fix-5 frames (A4-B1, A4-P2, A4-P3), sent once the user confirms them. §22X, §27G."""
import json, copy, sys, subprocess
import broll, calls
from fix5 import FX as FX5
LEN = {x["beat"]: x["call_s"] for x in json.load(open(broll.B / "edit/lengths_v2_HK1.json"))["lengths"]}
GO = "user, 2026-09-28: pressed Fix on the card and said \"fix those\""
SP = "/tmp/claude-0/-home-user-global-manual-ai/0821f8b4-c061-556b-9536-6cf806123315/scratchpad/cur9/generations/"
SLIDE = "one travelling move on a still subject: slow slide along the bench"
MF = {
 "A4-B1": ("an older man carrying a laundry basket on his right hip up his stairs, a strap on his right knee",
   "Already moving on the first frame: basket on his right hip, he steps up onto the next stair, one step a second, weight onto the strapped right knee; he climbs away from the camera, the basket clear of the handrail. Still climbing at the cut. The camera stays where it is.", {}),
 "A4-P2": ("the back of a black knee strap lying on a workbench",
   "Already drifting on the first frame: the camera eases very slowly along the strap lying still on the bench, the window light sliding across the smooth back of the shell and its chrome slides, about four seconds. Nothing in the frame moves except the light; no hands appear. Still easing along at the cut.", {"camera": SLIDE}),
 "A4-P3": ("two black knee straps lying on a workbench",
   "Already drifting on the first frame: the camera eases very slowly along the two straps lying still on the bench, the window light sliding across their shells and chrome slides, about four seconds. Nothing in the frame moves except the light; no hands appear. Still easing along at the cut.", {"camera": SLIDE}),
}
DIAG = {
 "A4-B1": "frame: the basket was on the banister side → carried on his right hip, away from the rail",
 "A4-P2": "frame: the back drew as a rectangular watch pad → the real back (two-peak outline) from the back reference, lying on the bench, no hands",
 "A4-P3": "frame: the bands drew as cut open straps → each band one closed loop slide to slide",
}
NEG = {"A4-B1": "no basket on the handrail, no hand on the rail, no walking into the hall, no misshapen strap",
       "A4-P2": "no hands, no strap moving, no wordmark appearing, no rectangular pad", "A4-P3": "no hands, no straps moving, no cut bands"}
def urls():
    try: return {l.split()[0]: l.split()[2] for l in open(broll.HERE / "fix5_urls.txt")}
    except FileNotFoundError: return {}
def build(b):
    r = copy.deepcopy(broll.ROWS[b]); r.update(FX5[b][0])
    subj, mot, ov = MF[b]; r.update(ov)
    j = json.loads(broll.kling(r, mot, subj))
    if r["product_state"] == "object":
        j["motion"] = j["motion"].replace(" The strap keeps its exact shape, size and wordmark in every frame and moves only with what holds it; its rigid shell never bends, flexes or changes proportion.",
                                          " The strap keeps its exact shape and size in every frame" + ("; its back stays plain." if b == "A4-P2" else " and its wordmark stays readable."))
    j["negatives"] += ", " + NEG[b]
    return r, json.dumps(j, ensure_ascii=False, separators=(",", ":"))
def make(b, approved):
    d = json.load(open(SP + f"stryde-cascade__{b}.json")); d = d.get("data", d)
    r, p = build(b)
    (broll.PR / "clips" / f"{b}.fix5.kling.json").write_text(p)
    k = calls.kind(r)
    vv = d.get("videoVersions") or []
    c = {"beat": b, "connector": "kling", "route": "kie kling-3.0/video (Kling account short, §5)", "mode": 1, "kind": "broll",
         "prompt": p, "duration": LEN[b], "resolution": "1080p", "aspect_ratio": "9:16",
         "start_image": urls().get(b), "start_approved": approved, "pinned": False, "end_image": None, "end_approved": False,
         "subject_motion": "still" if k == "still" else ("travels" if k == "stairs" else "in_place"), "prefer_multi_shots": "false",
         "generation": (max(v["v"] for v in vv) + 1) if vv else 1, "fix_note": DIAG[b], "risks": calls.RISKS[k]}
    if c["generation"] >= 3: c["user_go"] = GO
    path = broll.B / f"calls/{b}.fix5.json"
    json.dump(c, open(path, "w"), indent=1, ensure_ascii=False)
    out = subprocess.run(["python3", str(broll.B.parents[1] / ".claude/skills/ai-prompt-engineer/scripts/preflight.py"), str(path)], capture_output=True, text=True).stdout
    return len(p), c["generation"], out.strip().splitlines()[-1], [l.strip() for l in out.splitlines() if "FAIL" in l]
if __name__ == "__main__":
    appr = set(sys.argv[1:])
    for b in MF: print(b, make(b, b in appr))
