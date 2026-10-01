"""User Fix round 7 (2026-09-28): A4-B1 motion Fix on the confirmed fix-6 frame — "he should just be getting up, not tying", sent once the user confirms them. §22X, §27G."""
import json, copy, sys, subprocess
import broll, calls
from fix6 import FX as FX5
LEN = {x["beat"]: x["call_s"] for x in json.load(open(broll.B / "edit/lengths_v2_HK1.json"))["lengths"]}
GO = "user, 2026-09-28: pressed Fix on the card and said \"fix those\""
SP = "/tmp/claude-0/-home-user-global-manual-ai/0821f8b4-c061-556b-9536-6cf806123315/scratchpad/cur13/generations/"
SLIDE = "one travelling move on a still subject: slow slide along the bench"
MF = {
 "A4-B1": ("an older man in his hall rising from a crouch to standing, a black knee strap on his right knee",
   "Already rising on the first frame: from the crouch he pushes up and stands, weight driving through the strapped right knee, hands leaving the boot, about three seconds, one smooth easy rise; he is upright at the end. No tying, no laces. He is standing at the cut. The camera stays where it is.", {}),
}
DIAG = {"A4-B1": "motion: he tied his laces → he just gets up from the crouch, one easy rise on the strapped knee"}
NEG = {"A4-B1": "no tying, no hands on the laces, no stairs, no strap slipping, no misshapen strap"}
def urls():
    try: return {l.split()[0]: l.split()[2] for l in open(broll.HERE / "fix6_urls.txt")}
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
    (broll.PR / "clips" / f"{b}.fix7.kling.json").write_text(p)
    k = calls.kind(r)
    vv = d.get("videoVersions") or []
    c = {"beat": b, "connector": "kling", "route": "kie kling-3.0/video (Kling account short, §5)", "mode": 1, "kind": "broll",
         "prompt": p, "duration": LEN[b], "resolution": "1080p", "aspect_ratio": "9:16",
         "start_image": urls().get(b), "start_approved": approved, "pinned": False, "end_image": None, "end_approved": False,
         "subject_motion": "still" if k == "still" else ("travels" if k == "stairs" else "in_place"), "prefer_multi_shots": "false",
         "generation": (max(v["v"] for v in vv) + 1) if vv else 1, "fix_note": DIAG[b], "risks": calls.RISKS[k]}
    if c["generation"] >= 3: c["user_go"] = GO
    path = broll.B / f"calls/{b}.fix7.json"
    json.dump(c, open(path, "w"), indent=1, ensure_ascii=False)
    out = subprocess.run(["python3", str(broll.B.parents[1] / ".claude/skills/ai-prompt-engineer/scripts/preflight.py"), str(path)], capture_output=True, text=True).stdout
    return len(p), c["generation"], out.strip().splitlines()[-1], [l.strip() for l in out.splitlines() if "FAIL" in l]
if __name__ == "__main__":
    appr = set(sys.argv[1:])
    for b in MF: print(b, make(b, b in appr))
