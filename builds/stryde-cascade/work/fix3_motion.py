"""User Fix round 3 (2026-09-28): new §35 Kling JSON for video Fixes on confirmed frames (A4-M1, A4-P3, A5-B2), and the
clip calls for the fix-3 frames (A2-B2, A4-P1, A4-P2), sent once the user confirms those frames. §22X, §27G."""
import json, copy, sys, subprocess, glob
import broll, calls
from fix1_motion import BAND, MF as MF1
from fix1 import FX as FX1
from fix3 import FX as FX3
LEN = {x["beat"]: x["call_s"] for x in json.load(open(broll.B / "edit/lengths_v2_HK1.json"))["lengths"]}
GO = "user, 2026-09-28: pressed Fix on the card and said \"fix those\""
SP = "/tmp/claude-0/-home-user-global-manual-ai/0821f8b4-c061-556b-9536-6cf806123315/scratchpad/cur4/generations/"
MF = {
 "A4-M1": ("a medical animation of a knee in side view wearing a strap on the patellar tendon",
   "Already cycling on the first frame: a warm orange pulse of load travels down the thigh muscle as a glowing wave and reaches the strap, where the strap's pad lights up a soft cool BLUE and absorbs the whole wave — the orange is drawn into the blue glow and fades there, and nothing passes below the strap: the tendon and the shin beneath stay calm and pale. One pulse over about two seconds, then the blue glow softens. The next pulse is travelling down the thigh at the cut.", {}),
 "A4-P3": ("a man's weathered hand setting a second black knee strap down beside another on a workbench",
   "Already lowering on the first frame: his hand sets the strap down by its shell beside the first one and lets go, then draws back, about two seconds; the band drops onto the wood and settles. Nothing is pulled, stretched or unfastened. Both straps lie still at the cut.", {}),
 "A5-B2": ("an older man walking down his stairs, a black strap on his right knee, hands off the rail",
   "Already mid-step on the first frame: he steps down onto the next stair, weight onto the strapped right knee, one step a second; arms loose at his sides, his right hand a hand's width off the handrail throughout, never touching it. The next step is beginning at the cut. The camera stays where it is.", {}),
 "A2-B2": ("an older man sitting on a stair, one fingertip pressing the tendon just below his right kneecap, seen from above",
   "Already pressing on the first frame: his fingertip presses slowly into the tendon just below the kneecap on the front of the leg, the skin dimpling under it, holds, and his knee flinches very slightly, about two seconds in all. The finger stays on the midline below the kneecap. Still pressing at the cut.", {}),
 "A4-P1": ("a man's weathered hand holding a black knee strap up by the lower edge of its shell inside a van",
   "Already lifting on the first frame: his hand raises the strap a little higher by the lower edge of its shell, about two seconds, the wordmark facing the lens; the band hangs free in a loop below and swings loosely, settling as the lift slows. The band is still swinging at the cut.", {}),
 "A4-P2": ("a man's hands holding a knee strap turned over, the smooth pad on its back",
   "Already moving on the first frame: he turns the strap slowly a little in his hands, about two seconds, so the window light slides across the smooth silicone pad on its back, then his thumb presses gently into the pad, which gives softly and springs back smooth. Turning again at the cut.", {"camera": "sway"}),
}
DIAG = {
 "A4-M1": "motion: the load wave passed on down the shin → the strap glows blue and absorbs the whole wave, nothing below it",
 "A4-P3": "motion: the hands stripped the band off the shell → the strap is only set down by its shell and left",
 "A5-B2": "motion: his right hand drifted onto the handrail → hands held a hand's width off the rail, never rising to it",
 "A2-B2": "frame: fingers at the side of the knee → fingertip on the midline below the kneecap",
 "A4-P1": "frame: the product drew as a rounded clip → held by the lower edge so the two-peak shell reads whole",
 "A4-P2": "frame: the thumb press drew holes in the pad → pad smooth and unbroken, thumb resting",
}
NEG = {"A4-M1": "no wave passing below the strap, no orange glow on the shin, no glow inside the joint", "A4-P3": "no pulling, no stretching, no unfastening, no band taken off the shell",
       "A5-B2": "no hand on the handrail, no hand touching the rail, no reaching for the rail", "A2-B2": "no finger at the side of the knee",
       "A4-P1": "no fingers on the band", "A4-P2": "no holes in the pad, no zoom-only shot"}
FRAME3 = {"A2-B2", "A4-P1", "A4-P2"}
def urls3():
    try: return {l.split()[0]: l.split()[2] for l in open(broll.HERE / "fix3_urls.txt")}
    except FileNotFoundError: return {}
def build(b):
    r = copy.deepcopy(broll.ROWS[b])
    if b in FX3: r.update(FX3[b][0])
    elif b in FX1: r.update(FX1[b][0])
    subj, mot, ov = MF[b]; r.update(ov)
    if b == "A2-B2": r["product_state"] = "absent"
    j = json.loads(broll.kling(r, mot, subj))
    if r["product_state"] in ("held", "object"):
        j["motion"] = j["motion"].replace(" The strap keeps its exact shape, size and wordmark in every frame and moves only with what holds it; its rigid shell never bends, flexes or changes proportion.",
                                          (" The strap keeps its exact size; the back of the shell stays plain." if b == "A4-P2" else " The strap keeps its exact size and wordmark in every frame.") + BAND)
        j["negatives"] = j["negatives"].replace("no bending, no curling, no folding, no melting, no flipping of the product", "no bending of the rigid shell, no melting, no flipping of the product, no stiff frozen band")
    j["negatives"] += ", " + NEG[b]
    return r, json.dumps(j, ensure_ascii=False, separators=(",", ":"))
def make(b, approved):
    d = json.load(open(SP + f"stryde-cascade__{b}.json")); d = d.get("data", d)
    r, p = build(b)
    (broll.PR / "clips" / f"{b}.fix3.kling.json").write_text(p)
    k = calls.kind(r)
    vv = [v for v in (d.get("videoVersions") or [])]
    start = urls3().get(b) if b in FRAME3 else d["imageUrl"]
    c = {"beat": b, "connector": "kling", "route": "kie kling-3.0/video (Kling account short, §5)", "mode": 1, "kind": "broll",
         "prompt": p, "duration": LEN[b], "resolution": "1080p", "aspect_ratio": "9:16",
         "start_image": start, "start_approved": approved, "pinned": False, "end_image": None, "end_approved": False,
         "subject_motion": "still" if k == "still" else ("travels" if k == "stairs" else "in_place"), "prefer_multi_shots": "false",
         "generation": max(v["v"] for v in vv) + 1 if vv else 1, "fix_note": DIAG[b], "risks": calls.RISKS[k]}
    if c["generation"] >= 3: c["user_go"] = GO
    path = broll.B / f"calls/{b}.fix3.json"
    json.dump(c, open(path, "w"), indent=1, ensure_ascii=False)
    out = subprocess.run(["python3", str(broll.B.parents[1] / ".claude/skills/ai-prompt-engineer/scripts/preflight.py"), str(path)], capture_output=True, text=True).stdout
    return len(p), c["generation"], out.strip().splitlines()[-1], [l.strip() for l in out.splitlines() if "FAIL" in l]
if __name__ == "__main__":
    appr = set(sys.argv[1:]) | {"A4-M1", "A4-P3", "A5-B2"}   # the video-only fixes start from confirmed frames
    for b in MF: print(b, make(b, b in appr))
