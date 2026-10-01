#!/usr/bin/env python3
"""The body edit (step 9, §30H) — user 2026-10-01: "confirm proceed, use the latest bgm update"; layouts by the current rule (the user's pick
over the act map's EDIT-DFA): full screen by default, a 60/40 split (B-roll on top) on five mechanism shots, never two in a row (~1 in 8).
  base   = TH-A1…A5 trims joined (th/TH-BODY.trim.mp4), its audio the master (edit/body/BODY.master.wav) — wall to wall, never cut
  B-roll = every Act 1–5 act-map row with a card, its current confirmed clip, its phrase = its line in acts/plan/lengths.json (verbatim script),
           its key = the act map's key word. BR-03b and BR-22a3 have no card (the doctor stays on screen).
Writes edit/body/BODY.plan.json; then: assemble.py edit/body/BODY.plan.json --out edit/body/BODY.rough.mp4"""
import json, glob, os, subprocess, pathlib
import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
B = pathlib.Path(__file__).parents[1]
G = "/tmp/claude-0/-home-user-global-manual-ai/33ac0ea1-56e5-53d2-9765-ab6fc866d4ca/scratchpad/g32/generations/"
SPLIT = set()   # user 2026-10-01: "DONT USE SPLIT SCREEN" — every B-roll full screen
# user 2026-10-01: "SOME OF THE BROLLS ARE MISSING" — no row is dropped; a line under 2 s holds its clip over the next words (assemble.py HOLD)
DROP = {}
# base + master
lst = B / "edit/body/th_list.txt"
lst.write_text("".join(f"file '{B}/th/TH-{a}.trim.mp4'\n" for a in ["A1", "A2", "A3", "A4", "A5"]))
base = B / "th/TH-BODY.trim.mp4"
if not base.exists():
    subprocess.run([FF, "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(base)], check=True)
master = B / "edit/body/BODY.master.wav"
subprocess.run([FF, "-y", "-v", "error", "-i", str(base), "-vn", "-ac", "1", "-ar", "48000", str(master)], check=True)
A = json.load(open(B / "work/actmap.json")); L = json.load(open(B / "acts/plan/lengths.json"))
rows = []
for r in A:
    b = r["beat"]
    if not r["act"].startswith("Act") or b.startswith("TH") or b in DROP or not os.path.exists(G + f"down-forwards-again__{b}.json"): continue
    c = json.load(open(G + f"down-forwards-again__{b}.json")); assert c["status"] == "use", b
    v = [x for x in c["videoVersions"] if x.get("asset") == c["videoAsset"]][0]["v"]
    clip = B / f"acts/video/clips/{b}.v{v}.mp4"; assert clip.exists(), clip
    row = {"beat": b, "clip": str(clip), "phrase": L[b]["line"].rstrip("."),
           "layout": {"type": "split", "broll_pos": "top", "ratio": 0.6} if b in SPLIT else {"type": "full"}}
    # no key anchors (dry run 1: keys at the end of a line — "stairs", "surgeons", "landing", "walk" — cut the B-roll in late and squeezed it
    # under 2 s); every B-roll starts on its line's first word
    rows.append(row)
plan = {"audio": str(master), "script": str(B / "work/BODY.lines.txt"), "base": str(base), "broll": rows}
json.dump(plan, open(B / "edit/body/BODY.plan.json", "w"), ensure_ascii=False, indent=1)
print(len(rows), "rows;", sum(1 for x in rows if x["layout"]["type"] != "full"), "split")
