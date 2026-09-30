"""User Fix round 4 (2026-09-28): A4-B1 video Fix on its confirmed fix-2 frame, and the clip calls for the fix-4 frames
(A4-M1, A4-P1, A4-P3, A5-B2, A5-B3), sent once the user confirms them. §22X, §27G."""
import json, copy, sys, subprocess
import broll, calls
from fix1_motion import BAND
from fix2 import FX as FX2
from fix4 import FX as FX4
LEN = {x["beat"]: x["call_s"] for x in json.load(open(broll.B / "edit/lengths_v2_HK1.json"))["lengths"]}
GO = "user, 2026-09-28: pressed Fix on the card and said \"fix those\""
SP = "/tmp/claude-0/-home-user-global-manual-ai/0821f8b4-c061-556b-9536-6cf806123315/scratchpad/cur9/generations/"
MF = {
 "A4-B1": ("an older man carrying a laundry basket up his stairs, a strap on his right knee",
   "Already moving on the first frame: basket held high against his chest, clear of the banister, he steps up onto the next stair, one easy step a second, weight onto the strapped right knee; he climbs away from the camera, never into the hall. Still climbing at the cut. The camera stays where it is.", {}),
 "A4-M1": ("a medical animation of a knee in side view, a strap shielding the tendon with a blue glow",
   "Already cycling on the first frame: a warm orange pulse of load travels down the thigh muscle and reaches the blue glow around the strap, where it is stopped and absorbed, fading into the blue; the blue shield brightens as it takes the hit, then settles, and the tendon inside it stays calm and pale. One pulse over about two seconds. The next pulse is travelling down the thigh at the cut.", {}),
 "A4-P1": ("a man's hand holding a black knee strap up by the lower edge of its shell inside a van",
   "Already lifting on the first frame: his one hand raises the strap a little higher by the lower edge of its shell, about two seconds, the wordmark facing the lens; the band hangs free in a loop below and swings loosely, settling as the lift slows. Nothing touches the top of the shell. The band is still swinging at the cut.", {}),
 "A4-P3": ("two black knee straps lying on a workbench",
   "Already drifting on the first frame: the camera eases very slowly along the two straps lying still on the bench, the window light sliding across their shells and chrome slides, about four seconds. Nothing in the frame moves except the light; no hands appear. Still easing along at the cut.", {"camera": "one travelling move on a still subject: slow slide along the bench"}),
 "A5-B2": ("a happy older man coming quickly down his stairs, keys in hand, a strap on his right knee",
   "Already mid-step on the first frame: he comes quickly and happily down, one foot per step, one step every 0.6 seconds, weight on the strapped right knee, smiling, keys in his right hand; he stays on the wall side and neither hand goes near the handrail. The next foot is landing at the cut. The camera stays where it is.", {}),
 "A5-B3": ("an older man coming briskly down his stairs, whole body and face in view",
   "Already mid-stride on the first frame: he comes briskly down toward the camera, one foot per step, one step every 0.6 seconds, weight on the strapped right knee, keys in hand; he stays on the wall side, hands off the handrail, face relaxed. The next foot is landing at the cut. The camera stays where it is.", {}),
}
DIAG = {
 "A4-B1": "motion: he walked out into the hall with the basket against the rail and the strap lost its shape → climbing the stairs, basket high and clear of the banister, strap rigid",
 "A4-M1": "frame: user asked for a new picture where the strap protects the tendon → blue shield frame; motion: the wave stops at the shield",
 "A4-P1": "frame: a second hand held the top of the shell → one hand at the lower edge, top clear",
 "A4-P3": "frame: user asked for new straps → two whole straps on the bench, no hands; motion: light and camera only",
 "A5-B2": "frame: his hand hung beside the rail and the model grabbed it every time → wall side of the flight, keys in the rail-side hand",
 "A5-B3": "frame: his hand hung beside the rail → wall side of the flight, keys in the rail-side hand",
}
NEG = {"A4-B1": "no walking into the hall, no basket on the handrail, no hand on the rail, no misshapen strap",
       "A4-M1": "no orange below the strap, no glow inside the joint, no second leg", "A4-P1": "no second hand, no fingers on the band",
       "A4-P3": "no hands, no straps moving", "A5-B2": "no hand on the handrail, no reaching for the rail, no slow motion",
       "A5-B3": "no hand on the handrail, no reaching for the rail, no slow motion, no face leaving frame"}
NEWFRAME = {"A4-M1", "A4-P1", "A4-P3", "A5-B2", "A5-B3"}
def urls():
    try: return {l.split()[0]: l.split()[2] for l in open(broll.HERE / "fix4_urls.txt")}
    except FileNotFoundError: return {}
def build(b):
    r = copy.deepcopy(broll.ROWS[b])
    if b in FX4: r.update(FX4[b][0])
    elif b in FX2: r.update(FX2[b][0])
    subj, mot, ov = MF[b]; r.update(ov)
    j = json.loads(broll.kling(r, mot, subj))
    if r["product_state"] in ("held", "object"):
        j["motion"] = j["motion"].replace(" The strap keeps its exact shape, size and wordmark in every frame and moves only with what holds it; its rigid shell never bends, flexes or changes proportion.",
                                          " The strap keeps its exact size and wordmark in every frame." + (BAND if r["product_state"] == "held" else ""))
    j["negatives"] += ", " + NEG[b]
    return r, json.dumps(j, ensure_ascii=False, separators=(",", ":"))
def make(b, approved):
    d = json.load(open(SP + f"stryde-cascade__{b}.json")); d = d.get("data", d)
    r, p = build(b)
    (broll.PR / "clips" / f"{b}.fix4.kling.json").write_text(p)
    k = calls.kind(r)
    vv = d.get("videoVersions") or []
    start = urls().get(b) if b in NEWFRAME else d["imageUrl"]
    c = {"beat": b, "connector": "kling", "route": "kie kling-3.0/video (Kling account short, §5)", "mode": 1, "kind": "broll",
         "prompt": p, "duration": LEN[b], "resolution": "1080p", "aspect_ratio": "9:16",
         "start_image": start, "start_approved": approved, "pinned": False, "end_image": None, "end_approved": False,
         "subject_motion": "still" if k == "still" else ("travels" if k == "stairs" else "in_place"), "prefer_multi_shots": "false",
         "generation": (max(v["v"] for v in vv) + 1) if vv else 1, "fix_note": DIAG[b], "risks": calls.RISKS[k]}
    if c["generation"] >= 3: c["user_go"] = GO
    path = broll.B / f"calls/{b}.fix4.json"
    json.dump(c, open(path, "w"), indent=1, ensure_ascii=False)
    out = subprocess.run(["python3", str(broll.B.parents[1] / ".claude/skills/ai-prompt-engineer/scripts/preflight.py"), str(path)], capture_output=True, text=True).stdout
    return len(p), c["generation"], out.strip().splitlines()[-1], [l.strip() for l in out.splitlines() if "FAIL" in l]
if __name__ == "__main__":
    appr = set(sys.argv[1:]) | {"A4-B1"}
    for b in MF: print(b, make(b, b in appr))
