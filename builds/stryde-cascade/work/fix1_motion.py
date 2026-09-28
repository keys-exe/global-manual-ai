"""User Fix round 1 (2026-09-28): new §35 Kling JSON per fixed beat — fault fixed at its source (§22X), §27G motion."""
import json, copy, sys
import broll
from fix1 import FX
BAND = " Rigid shell; the elastic band is soft and heavy: it hangs, swings, lags and settles with real weight."
# beat -> (subject line, motion, row overrides)
MF = {
 "A1-B2": ("an older woman's legs and navy slippers climbing carpeted stairs one step at a time, both feet meeting on each step",
   "Already moving on the first frame: her left foot comes up and lands on the SAME step as her right foot, the two slippers side by side on one tread, and she pauses there a moment with both feet together; then her right foot lifts first onto the next step and the left comes up to join it on that same step again. Step-to, both feet on every step, about two seconds per step. Her right foot is lifting again at the cut.", {}),
 "A1-B4": ("an older woman in a navy cardigan at the top of carpeted stairs, struggling to start down, gripping a short oak rail",
   "Already gripping on the first frame: her hand clenches tight on the rail and her shoulders hunch as she leans her weight onto it; she lowers her first foot toward the top step down, hesitates halfway with the foot hovering, pulls it back a little, then lowers it again, very slowly and unsteadily, the whole attempt taking about three seconds. The foot is still hovering, not yet down, at the cut.", {}),
 "A1-B5": ("an older woman in a navy cardigan struggling down carpeted stairs, a hand on each rail, taking her weight on her arms",
   "Already mid-step on the first frame: leaning heavily on both rails, her arms taking her weight, she lowers one stiff leg down to the next tread with a small wobble, then brings the other foot down to the SAME tread beside it, both feet together, pausing to steady herself; one laboured step taking about three seconds. She is steadying on the rails at the cut.", {}),
 "A2-B1": ("an older man's bare right knee and shin in khaki shorts on one light oak stair tread",
   "Already mid-step on the first frame: his right foot settles flat on the tread and the knee bends under his weight, the skin just below the kneecap tightening, one step taking about one and a half seconds. The knee is still bending under the weight at the cut.", {}),
 "A2-B2": ("an older man in khaki shorts sitting on the bottom stair, pressing a fingertip into the tendon just below his right kneecap",
   "Already pressing on the first frame: his fingertip presses slowly into the tendon just below the kneecap, the skin dimpling under it, holds, and his knee flinches very slightly, about two seconds in all. Still pressing at the cut.", {}),
 "A3-B2": ("an older woman's bare right knee and one hand spreading clear gel over the kneecap",
   "Already rubbing on the first frame: her fingertips spread the gel in slow small circles over the front of the kneecap, one circle every second, the gel shining wet on the skin; the knee itself stays completely still and keeps its exact shape. Still rubbing at the cut.", {}),
 "A4-B1": ("a close-up of a black knee strap worn on an older man's right knee as he sits on a stair",
   "Already moving on the first frame: he slowly straightens his right leg a little forward, about two seconds, the strap moving with the knee and staying exactly in place below the kneecap, the chrome slide catching the light as the leg turns. The leg is still easing out at the cut.", {}),
 "A4-B2": ("a close-up looking down at a black knee strap on an older man's right knee, his finger pointing at its notch",
   "Already still on the first frame: his index finger taps the top edge of the strap's shell twice, right at the notch under the kneecap, about one second, marking the spot. His finger is resting on the notch at the cut.", {}),
 "A4-P1": ("a man's weathered hand lifting a black knee strap out of a clear box on a van shelf",
   "Already lifting on the first frame: his hand lifts the strap up out of the box, about two seconds, the shell's front and wordmark facing the lens; the band slides over the box edge and swings loose below his hand. The band is still swinging at the cut.", {}),
 "A4-P2": ("a man's weathered hands holding a black knee strap turned to show the pad inside the shell, on a workbench",
   "Already pressing on the first frame: his thumb presses slowly into the soft black pad, which squashes under it, then springs back smooth as he eases off, about two seconds. His thumb is pressing in again at the cut.", {}),
 "A4-P3": ("a man's weathered hand setting a second black knee strap down beside another on a workbench",
   "Already lowering on the first frame: his hand sets the second strap down beside the first and lets go, its band dropping onto the wood in a loose curl, about two seconds. His hand is drawing back at the cut.", {}),
 "A5-B1": ("a stocky grey-haired man in work shorts lifting a heavy steel toolbox inside a van, a black knee strap on his right knee",
   "Already lifting on the first frame: he straightens up with the heavy toolbox in both hands, the weight pulling at his arms, about three seconds, the strap staying in place below his right kneecap. He is still rising at the cut.", {}),
 "A5-B2": ("an older man in khaki shorts walking down his stairs, arms loose at his sides, a black knee strap on his right knee",
   "Already mid-step on the first frame: he steps down onto the next stair and his weight moves easily onto the strapped right knee, one step every second, both arms swinging loose at his sides and both hands never touching the handrail. The next step is beginning at the cut. The camera stays where it is.", {}),
 "A5-B3": ("an older man's legs coming quickly down light oak stairs, a black knee strap on his right knee",
   "Already mid-stride on the first frame: he comes down the stairs briskly, one foot on every step, alternating feet, a quick even rhythm of one step every 0.6 seconds, weight landing firmly on the strapped right knee each time, hands off the rail. The next foot is landing at the cut. The camera stays where it is.", {}),
 "A5-B4": ("an older man in khaki shorts coming quickly down his stairs forwards, arms loose, a black knee strap on his right knee",
   "Already mid-step on the first frame: he comes down briskly, one foot per step, alternating, one step every 0.6 seconds, arms loose, not holding the rail. The next foot is landing at the cut. The camera stays where it is.", {}),
 "A5-B5": ("an older woman in a navy cardigan climbing a straight carpeted flight, a hand on each rail, seen from behind",
   "Already mid-step on the first frame: she pulls herself up onto the next step with both hands on the rails, slowly, about three seconds for the one step; the stairs, the banister and the wall rail stay perfectly straight and still. Her back foot is lifting at the cut. The camera stays where it is.", {}),
 "A4-M1": ("a medical animation of a knee in side view wearing a strap on the patellar tendon",
   "Already cycling on the first frame: a bright pulse of load travels down the thigh muscle as a glowing wave and hits the strap's pad, where it splits and spreads out sideways across the shell in soft rings, while the tendon beneath stays calm and pale; one pulse over about two seconds. The next pulse is travelling down the thigh at the cut.", {}),
 "A5-F1": ("an older woman's hands stretching the band of a cheap knee strap in her lap",
   "Already pulling on the first frame: her hands pull the cheap strap's band apart and it stretches out long and slack with no spring in it, then as she eases her hands together it stays baggy and limp, drooping in a loose loop, about three seconds. The band is hanging slack at the cut.", {}),
}
def build(b):
    r = copy.deepcopy(broll.ROWS[b])
    if b in FX: r.update(FX[b][0])
    subj, mot, ov = MF[b]; r.update(ov)
    j = json.loads(broll.kling(r, mot, subj))
    if r["product_state"] in ("held", "object") or b in ("A5-F1",):
        j["motion"] = j["motion"].replace(" The strap keeps its exact shape, size and wordmark in every frame and moves only with what holds it; its rigid shell never bends, flexes or changes proportion.",
                                          " The strap keeps its exact size and wordmark in every frame." + BAND)
        j["negatives"] = j["negatives"].replace("no bending, no curling, no folding, no melting, no flipping of the product", "no bending of the rigid shell, no melting, no flipping of the product, no stiff frozen band, no band hanging rigid in mid-air")
    if b in ("A1-B4", "A1-B5"):
        j["negatives"] += ", no smooth confident stride, no easy walking"
    if b in ("A5-B3", "A5-B4"):
        j["negatives"] += ", no slow motion, no hesitation, no hand on the rail"
    if b == "A5-B2":
        j["negatives"] += ", no hand on the handrail, no hand touching the rail"
    return r, json.dumps(j, ensure_ascii=False, separators=(",", ":"))
if __name__ == "__main__":
    for b in (sys.argv[1:] or MF):
        r, p = build(b)
        (broll.PR / "clips" / f"{b}.v2.kling.json").write_text(p)
        print(b, len(p), r["camera"][:30])
