import json, math, re, sys
sys.path.insert(0, "work")
from judge_takes import norm
B = "."
am = json.load(open("act_map.json"))
def words_of(judgefile):
    return json.load(open(judgefile))[0]["words"]
def span(words, phrase):
    ws = [(norm(w)[0] if norm(w) else "", a, b) for w, a, b in words]
    flat = []
    i = 0
    while i < len(words):
        w, a, b = words[i]
        if w.strip() == "200" and i + 1 < len(words) and words[i+1][0].strip().startswith(",000"):
            for t in ["two", "hundred", "thousand"]: flat.append((t, a, words[i+1][2]))
            i += 2; continue
        for t in norm(w): flat.append((t.replace("orthopedic", "orthopaedic"), a, b))
        i += 1
    m = []
    for t in flat:
        if m and m[-1][0] == "body" and t[0] == "weight": m[-1] = ("bodyweight", m[-1][1], t[2])
        else: m.append(t)
    flat = m
    target = norm(phrase)
    toks = [t for t, _, _ in flat]
    for i in range(len(toks) - len(target) + 1):
        if toks[i:i + len(target)] == target:
            return flat[i][1], flat[i + len(target) - 1][2]
    raise ValueError(phrase)
body = words_of("voice/Identity.judge.json")
hooks = {f"HK{i}-01": f"voice/Identity_HK{i}_master.mp3" for i in (1, 2, 3)}
out = {}
for r in am:
    if r["beat_id"].startswith("HK"): continue
    a, b = span(body, r["phrase"])
    d = min(15, max(3, math.ceil(b - a + 0.5)))
    r["span"] = [round(a, 2), round(b, 2)]; r["duration"] = d; out[r["beat_id"]] = (round(a, 2), round(b, 2), d)
json.dump(am, open("act_map.json", "w"), indent=1)
for k, v in out.items(): print(k, v)
