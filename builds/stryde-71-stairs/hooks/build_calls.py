"""Hook video calls (§35 JSON, §27G natural motion, §22X preflight) — Kling 3.0 on Kie (user: USE KIE FOR KLING)."""
import json, sys
CAM = {"movement": "Propped, not held, not tripod. Small settle at entry, then near-stillness with a slow unresolved drift. Slightly off-level and never corrected.",
       "framing": "PROPPED as in the start frame."}
MASS = ("Everything in frame keeps the exact form, proportion and count it has in the start frame, first frame to last — nothing melts, merges, splits, grows or becomes something else. "
        "One small movement, completing inside the clip, subject fully in frame throughout, nothing leaving frame and returning. Mass and momentum in all movement: heavy starts and settles slow, "
        "nothing at uniform speed, nothing stops instantly — motions decelerate into a settle or small overshoot; actions travel through the body, weight transferring first, hands arriving last; "
        "hair, fabric and straps lag and keep moving after the body stops.")
LIGHT = "Capture characteristics exactly as in the start frame — same tone-mapping, same noise, same colour temperature. No grading change across the clip."
NEG = ("no morphing, no warping, no melting, no shape shifting, no merging, no splitting, no parts detaching, no proportions changing, no duplicate objects, no background bending, "
       "no texture swimming, no smearing, no flickering geometry, no camera travelling with the subject, no music, no speech, no slow motion")
CALLS = {
 "HK-01a": dict(img="https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260928_205427_a7a09cb6-b4ba-48cd-a9e7-d44db13f24d9.png", dur=5,
   subject="A Black American woman of seventy-one in an emerald-green church dress climbing her own family-photo staircase briskly, her daughter in a grey sweatshirt and jeans two steps behind her. Exactly as in the start frame.",
   motion="Already mid-climb on the first frame: the mother takes two brisk steps up, one step per second, her hand only brushing the rail; two steps behind, the daughter climbs one step and grips the rail, falling a little further behind. The camera stays where it is at the foot of the stairs.",
   neg=", no third person, no turning around, no one coming down the stairs, no running, no knee strap visible",
   risks=[("legs or feet warp on the stairs","two steps at a countable pace, start frame caught mid-step, camera still"),
          ("camera travels up the stairs with them","propped camera, 'the camera stays where it is', 'no camera travelling with the subject'"),
          ("the two women merge or swap faces","each described by wardrobe in subject; 'no merging, no duplicate objects, no third person'")]),
 "HK-02a": dict(img="https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260928_205426_af12fdf3-74a2-41c1-aa2b-ce333c0c7b54.png", dur=4,
   subject="A Black American woman in her mid-forties with long box braids, in a grey sweatshirt and jeans, three steps from the top of the stairs, seen from the landing. Exactly as in the start frame.",
   motion="Already mid-step on the first frame: she climbs one step toward the camera in about a second, her hand sliding on the rail, then lifts her face to the lens with a surprised, delighted look and her lips part as if about to speak. The camera stays where it is at the top of the stairs.",
   neg=", no second person, no speaking, no lip sync, no turning around, no walking past the camera",
   risks=[("face distorts as she comes closer","one step only, she stays three steps below the lens, framing held"),
          ("camera travels down the stairs","propped camera at the top, 'the camera stays where it is'"),
          ("mouth animates as speech (no dialogue on this beat)","'lips part as if about to speak', negatives 'no speaking, no lip sync'")]),
}
def build(k, gen=1, fix=None):
    c = CALLS[k]
    p = {"shot": k.lower().replace("-", "_"), "subject": c["subject"], "camera": CAM, "motion": c["motion"] + " " + MASS,
         "lighting": LIGHT, "style": "As in the start frame.", "negatives": NEG + c["neg"]}
    ps = json.dumps(p, ensure_ascii=False, separators=(",", ":"))
    call = {"beat": k, "connector": "kling", "mode": 1, "kind": "broll", "prompt": ps, "duration": c["dur"], "resolution": "1080p", "aspect_ratio": "9:16",
            "start_image": c["img"], "start_approved": True, "pinned": False, "end_image": None, "end_approved": False,
            "subject_motion": "travels", "prefer_multi_shots": "false", "generation": gen,
            "risks": [{"risk": a, "prevented_by": b} for a, b in c["risks"]], "approved_by": "user: CONFIRMED PROCEED TO HOOK VIDEOS (2026-09-28)"}
    if fix: call["fix_note"] = fix
    json.dump(call, open(f"calls/{k}.call.json", "w"), indent=1, ensure_ascii=False)
    open(f"calls/{k}.prompt.txt", "w").write(ps)
    print(k, len(ps))
if __name__ == "__main__":
    for k in sys.argv[1:] or CALLS: build(k)
