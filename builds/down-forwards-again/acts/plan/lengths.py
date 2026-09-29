#!/usr/bin/env python3
"""Body B-roll lengths from the locked VO (TH-A1…A5 trimmed audio) — each B-roll runs from the first word of its own script span to the first
word of the next B-roll's span (the last one to the end of the act's audio). Script spans = work/actmap.json `line` (BLINE, asserted to rebuild
each phrase). Word times = acts/plan/words.json (faster-whisper medium.en). Script words are aligned to the heard words with difflib, so a
numeral heard as "17" still lands. Kling length = ceil(span), 3–15 s. Writes acts/plan/lengths.json.
Usage: lengths.py [A1 A2 …]"""
import json, math, re, sys, difflib, pathlib
HERE = pathlib.Path(__file__).resolve().parent
B = HERE.parents[1]
rows = json.load(open(B / "work/actmap.json")); rows = rows if isinstance(rows, list) else rows["rows"]
W = json.load(open(HERE / "words.json"))
NUM = {"17": "seventeen", "2": "two", "60": "sixty", "9": "nine", "6": "six"}
norm = lambda w: NUM.get(re.sub(r"[^a-z0-9]", "", w.lower()), re.sub(r"[^a-z0-9]", "", w.lower()))
out = {}
for a in (sys.argv[1:] or ["A1", "A2", "A3", "A4", "A5"]):
    act = "Act " + a[1:]
    br = [r for r in rows if r["act"] == act and r["type"] != "TH"]
    heard = [(norm(w), s, e) for w, s, e in W[a]["words"]]
    script, owner = [], []
    for i, r in enumerate(br):
        for t in r["line"].split():
            if norm(t): script.append(norm(t)); owner.append(i)
    sm = difflib.SequenceMatcher(None, script, [h[0] for h in heard], autojunk=False)
    s2h = {}
    for blk in sm.get_matching_blocks():
        for k in range(blk.size): s2h[blk.a + k] = blk.b + k
    first, last, firsti, lasti = [], [], [], []
    for i in range(len(br)):
        idx = [j for j, o in enumerate(owner) if o == i]
        hits = [s2h[j] for j in idx if j in s2h]
        assert hits, (br[i]["beat"], "no heard word matched")
        # the first B-roll of an act opens on the act's first word (a numeral heard as "34" would otherwise start it late)
        h0 = min(hits); matched = set(s2h.values())
        back = 0  # up to 3 unmatched heard words just before (a numeral heard as "200 ,000") belong to this span
        numeric = lambda k: any(ch.isdigit() for ch in W[a]["words"][k][0]) or W[a]["words"][k][0].strip() in ("%", ",000")
        while back < 3 and h0 - back - 1 >= 0 and (h0 - back - 1) not in matched and numeric(h0 - back - 1): back += 1
        h0 = 0 if i == 0 and h0 - back <= 3 else h0 - back
        first.append(heard[h0][1]); last.append(heard[max(hits)][2]); firsti.append(h0); lasti.append(max(hits))
    end = heard[-1][2]
    for i, r in enumerate(br):
        t0, t1 = first[i], (first[i + 1] if i + 1 < len(br) else end)
        # a talking-head-only stretch after this span (the doctor to camera, no B-roll written for it): end 0.4 s after the span's own last word
        gap_words = (firsti[i + 1] if i + 1 < len(br) else len(heard)) - lasti[i] - 1
        if gap_words >= 5: t1 = round(last[i] + 0.4, 2)
        span = round(t1 - t0, 2)
        out[r["beat"]] = {"act": act, "in": t0, "out": t1, "span": span, "kling": min(15, max(3, math.ceil(span))), "line": r["line"]}
        print(f"{r['beat']:8s} {t0:6.2f} → {t1:6.2f}  {span:5.2f}s  kling {out[r['beat']]['kling']}s  | {r['line'][:70]}")
    print(f"{a}: {len(br)} B-rolls, audio ends {end:.2f}s, match ratio {sm.ratio():.3f}")
old = json.load(open(HERE / "lengths.json")) if (HERE / "lengths.json").exists() else {}
old.update(out); json.dump(old, open(HERE / "lengths.json", "w"), indent=1)
