"""E6: one assemble.py plan per hook variant (hook rows of that hook + every body row), for --lengths."""
import json, re
rows = json.load(open("work/actmap.json"))
for n in (1, 2, 3):
    br = [dict(r) for r in rows if r["type"] != "TH" and r["act"] in (f"Hook {n}",) + tuple(f"Act {i}" for i in range(1, 7))]
    # rows sharing one script line: each takes the stretch from its key word to the next row's key word
    i = 0
    while i < len(br):
        j = i
        while j + 1 < len(br) and br[j + 1]["line"] == br[i]["line"]: j += 1
        if j > i:
            words = br[i]["line"].split()
            low = [re.sub(r"[^a-z0-9']", "", w.lower()) for w in words]
            starts, pos = [0], 0
            for r in br[i + 1:j + 1]:
                k = re.sub(r"[^a-z0-9']", "", r["key"].lower()); pos = low.index(k, pos + 1); starts.append(pos)
            # start each stretch at the beginning of the sentence/clause that holds the key
            keys = list(starts)
            for n_, st in enumerate(keys[1:], 1):
                b = st
                while b > keys[n_ - 1] + 1 and not re.search(r"[.,?!]$", words[b - 1]): b -= 1
                starts[n_] = b
            for n_, r in enumerate(br[i:j + 1]):
                end = starts[n_ + 1] if n_ + 1 < len(starts) else len(words)
                r["line"] = " ".join(words[starts[n_]:end])
        i = j + 1
    plan = {"audio": f"/home/user/global-manual-ai/builds/stryde-three-regrets/vo/master/HK{n}.wav", "script": f"/home/user/global-manual-ai/builds/stryde-three-regrets/vo/master/HK{n}.script.txt", "base": "/home/user/global-manual-ai/builds/stryde-three-regrets/th/N_TH.mp4",
            "broll": [{"beat": r["beat"], "clip": None, "phrase": r["line"], **({"key": r["key"]} if r.get("key") else {}),
                       **({"max": r["max"]} if r.get("max") else {})} for r in br]}
    json.dump(plan, open(f"edit/plan_HK{n}.json", "w"), indent=1)
    print(n, len(br))
