import json, sys, subprocess
sys.path.insert(0, "work")
import broll
urls = json.load(open("work/frame_urls.json"))
RISKS = {
 "stairs": [{"risk": "feet or legs warp on the step", "prevented_by": "one step at a countable pace, start frame caught mid-step, HOLD-C + NEG-WARP-C"},
            {"risk": "camera travels with the moving subject", "prevented_by": "RIG-R1 sways but lags, never moves with the subject; 'no camera travelling with the subject'"},
            {"risk": "subject changes identity or wardrobe", "prevented_by": "subject line names wardrobe; start frame carries the sheet identity; HOLD-C"}],
 "hands": [{"risk": "fingers fuse or multiply", "prevented_by": "one small hand action at a named pace, HOLD-C, NEG-WARP-C"},
           {"risk": "object in hand morphs", "prevented_by": "HOLD-C: exact form and count kept; product clause where a strap is held"},
           {"risk": "camera drifts off the action", "prevented_by": "RIG-R1 low-amplitude sway only"}],
 "still": [{"risk": "room redraws during the move", "prevented_by": "nothing in the scene moves; one slow camera move only; HOLD-C"},
           {"risk": "objects appear or vanish", "prevented_by": "HOLD-C: exact count kept; NEG-WARP-C"},
           {"risk": "move too fast or resolves", "prevented_by": "slow continuous move, still moving on the final frame"}],
 "anat": [{"risk": "anatomy melts or loses structure", "prevented_by": "HOLD-C + NEG-WARP-C, one load pulse only"},
          {"risk": "labels or text appear", "prevented_by": "T2I ANAT-NEG bans labels; start frame has none"},
          {"risk": "camera orbits away from the tendon", "prevented_by": "RIG-RVD small lateral drift only"}],
}
def kind(r):
    if r["location"] == "ANAT": return "anat"
    if r["subject"] in ("none", "product"): return "still"
    if "STAIR" in r["staging"]: return "stairs"
    return "hands"
def call(b, gen=1, fix=None):
    r = broll.ROWS[b]
    p = open(f"prompts/clips/{b}.kling.json").read()
    k = kind(r)
    c = {"beat": b, "connector": "kling", "mode": 1, "kind": "broll", "prompt": p, "duration": r["duration"], "resolution": "1080p", "aspect_ratio": "9:16",
         "start_image": urls[b], "start_approved": True, "pinned": bool(r["pin_end"]), "end_image": urls.get(b + "_end"), "end_approved": bool(urls.get(b + "_end")),
         "subject_motion": "still" if k in ("still",) else ("travels" if k == "stairs" else "in_place"), "prefer_multi_shots": "false",
         "generation": gen, "risks": RISKS[k]}
    if fix: c["fix_note"] = fix
    json.dump(c, open(f"calls/{b}.json", "w"), indent=1)
    out = subprocess.run(["python3", "../../.claude/skills/ai-prompt-engineer/scripts/preflight.py", f"calls/{b}.json"], capture_output=True, text=True).stdout
    return out.strip().splitlines()[-1], [l for l in out.splitlines() if l.startswith("FAIL")]
if __name__ == "__main__":
    for b in sys.argv[1:]: print(call(b))
