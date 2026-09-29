"""User Fix round 2 (2026-09-28): §35 Kling JSON + preflight call per beat, from the fix-2 start frames (§22X, §27G).
The calls are written now; each is sent only after the user confirms its new frame (start_approved)."""
import json, copy, sys, subprocess
import broll, calls
from fix2 import FX
from fix1_motion import BAND
LEN = {x["beat"]: x["call_s"] for x in json.load(open(broll.B / "edit/lengths_v2_HK1.json"))["lengths"]}
GO = "user, 2026-09-28: pressed Fix on the card and said \"fix those\""
MF = {
 "A1-B3": ("an older woman in a lilac cardigan sitting on the second stair of a straight carpeted flight, rubbing her right knee",
   "Already rubbing on the first frame: her right hand rubs slowly over her right knee, one stroke every two seconds, her left hand resting on the left knee. The staircase behind her stays exactly as it is, rising straight to its landing. Still rubbing at the cut.", {}),
 "A2-M4": ("a translucent anatomical model of ONE knee in strict side view on a descending step",
   "Already descending on the first frame: the thigh muscle lengthens as it brakes and the load snaps down onto the patellar tendon below the kneecap, which flares red, one catch over about one and a half seconds. Only the narrow strap of tendon running from the bottom tip of the kneecap down to the top of the shin bone lights up; the kneecap itself, the joint space behind it and the thigh stay their own colour. There is only ever one leg, one outline, first frame to last. The motion runs continuously the whole clip, never pausing. The next catch is arriving at the cut.", {}),
 "A4-B1": ("a heavyset older man in shorts carrying a full laundry basket up his stairs, a black knee strap on his right knee",
   "Already mid-step on the first frame: basket in both arms, he steps up onto the next stair, weight onto the strapped right knee, one step a second, steady, never touching the rail. The next step is beginning at the cut. The camera stays where it is.", {}),
 "A4-P1": ("a man's weathered hand lifting a black knee strap out of a clear box on a van shelf, holding it by its shell",
   "Already lifting on the first frame: his hand lifts the strap out of the box by its shell alone, about two seconds, wordmark to the lens; the band hangs free from both ends and swings below his hand. The band is still swinging at the cut.", {}),
 "A4-P2": ("a man's hands holding a knee strap turned over, the pad on its back",
   "Already pressing on the first frame: his thumb presses into the silicone pad on the back of the shell, which squashes, then springs back as he eases off; twice, two seconds a press, the strap turning slightly in the light. Pressing again at the cut.", {"camera": "sway"}),
 "A5-B3": ("a heavyset older man in shorts coming briskly down his stairs, his whole body and face in view, a black knee strap on his right knee",
   "Already mid-stride on the first frame: he comes briskly down toward the camera, one foot per step, one step every 0.6 seconds, weight landing on the strapped right knee, hands off the rail, face relaxed. The next foot is landing at the cut. The camera stays where it is.", {}),
 "A5-F1": ("an older woman's hands stretching the band of a cheap unbranded copy strap in her lap",
   "Already pulling on the first frame: her hands pull the cheap copy's band apart and it stretches out long and slack with no spring in it, then as she eases her hands together it stays baggy and limp, drooping in a loose loop, about three seconds. The copy stays in her hands, never on her leg. The band is hanging slack at the cut.", {}),
}
DIAG = {
 "A1-B3": "frame: the flight in the start image ran into a wall → new frame, a straight flight rising to a proper landing",
 "A2-M4": "frame: the start image had two overlapping leg outlines (the base prompt asked for a three-quarter view against a side-view beat) → new frame in strict profile, one leg",
 "A4-B1": "frame: a seated product close-up did not show the strap earning its keep → new frame, carrying laundry up the stairs, strap below the kneecap",
 "A4-P1": "frame: his hand held the band → new frame, held by the rigid shell only, band hanging free",
 "A4-P2": "frame: the start image showed the front of the strap → new frame from the back reference, thumb in the silicone pad; motion: two presses and a slight turn so it never reads as a still zoom",
 "A5-B3": "frame: waist-down framing cut his face off → new frame, whole body from the hall, face lit",
 "A5-F1": "frame: the copy was a buckle webbing strap → new frame, an unbranded copy of the same shape, band stretched in her hands",
}
NEG = {"A1-B3": "no stairs running into a wall, no staircase changing shape", "A2-M4": "no second leg, no overlapping legs, no double outline",
       "A4-B1": "no hand on the rail, no dropping the basket", "A4-P1": "no fingers on the band",
       "A4-P2": "no still image, no zoom-only shot", "A5-B3": "no slow motion, no hand on the rail, no face leaving frame",
       "A5-F1": "no strap worn on the leg, no wordmark on the copy"}
URLS = {l.split()[0]: l.split()[2] for l in open(broll.HERE / "fix2_urls.txt")}
def build(b):
    r = copy.deepcopy(broll.ROWS[b])
    if b in FX: r.update(FX[b][0])
    subj, mot, ov = MF[b]; r.update(ov)
    if b == "A5-F1": r["product_state"] = "absent"
    if b == "A4-P2": r["product_state"] = "held"
    j = json.loads(broll.kling(r, mot, subj))
    if r["product_state"] == "held":
        j["motion"] = j["motion"].replace(" The strap keeps its exact shape, size and wordmark in every frame and moves only with what holds it; its rigid shell never bends, flexes or changes proportion.",
                                          (" The strap keeps its exact size in every frame; the back of the shell stays plain, no wordmark." if b == "A4-P2" else " The strap keeps its exact size and wordmark in every frame.") + BAND)
        j["negatives"] = j["negatives"].replace("no bending, no curling, no folding, no melting, no flipping of the product", "no bending of the rigid shell, no melting, no flipping of the product, no stiff frozen band, no band hanging rigid in mid-air")
    j["negatives"] += ", " + NEG[b]
    return r, json.dumps(j, ensure_ascii=False, separators=(",", ":"))
def make(b, gen, approved=False):
    r, p = build(b)
    (broll.PR / "clips" / f"{b}.fix2.kling.json").write_text(p)
    k = calls.kind(r)
    c = {"beat": b, "connector": "kling", "route": "kie kling-3.0/video (Kling account short, §5)", "mode": 1, "kind": "broll",
         "prompt": p, "duration": LEN[b], "resolution": "1080p", "aspect_ratio": "9:16",
         "start_image": URLS[b], "start_approved": approved, "pinned": False, "end_image": None, "end_approved": False,
         "subject_motion": "still" if k == "still" else ("travels" if k == "stairs" else "in_place"), "prefer_multi_shots": "false",
         "generation": gen, "fix_note": DIAG[b], "risks": calls.RISKS[k]}
    if gen >= 3: c["user_go"] = GO
    path = broll.B / f"calls/{b}.fix2.json"
    json.dump(c, open(path, "w"), indent=1, ensure_ascii=False)
    out = subprocess.run(["python3", str(broll.B.parents[1] / ".claude/skills/ai-prompt-engineer/scripts/preflight.py"), str(path)], capture_output=True, text=True).stdout
    return len(p), out.strip().splitlines()[-1], [l.strip() for l in out.splitlines() if "FAIL" in l]
GEN = {"A1-B3": 2, "A2-M4": 3, "A4-B1": 3, "A4-P1": 3, "A4-P2": 3, "A5-B3": 3, "A5-F1": 3}
if __name__ == "__main__":
    appr = set(sys.argv[1:])
    for b in MF: print(b, make(b, GEN[b], b in appr))
