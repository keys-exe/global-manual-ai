import json, pathlib
import broll
from scenes import SC, ANAT
OUT = broll.PR / "frames"; OUT.mkdir(exist_ok=True)
L = {}
for h in ["HK1","HK2","HK3"]:
    for x in json.load(open(broll.B/f"edit/lengths_{h}.json"))["lengths"]: L.setdefault(x["beat"], x)
man = []
for b, r in broll.ROWS.items():
    if r["location"] == "ANAT":
        p = broll.t2i(r, "", ANAT[b]); model = "nano_banana_pro"
    else:
        scene, campos = SC[b]
        p = broll.t2i(r, campos, broll.s("SEED-CANDID").split("[")[0] + scene if False else "A snapshot, " + scene[0].lower() + scene[1:] if not scene.startswith("A ") else scene)
        model = "gpt_image_2_5" if r["subject"] in ("none", "product") else "nano_banana_pro"
    (OUT / f"{b}.txt").write_text(p)
    r["duration"] = L[b]["call_s"]; r["cut_s"] = L[b]["cut_s"]; r["on_screen_s"] = L[b]["on_screen_s"]
    man.append({"beat": b, "model": model, "refs": broll.refs(r), "chars": len(p), "call_s": r["duration"]})
json.dump(man, open(broll.B/"prompts/frames/manifest.json","w"), indent=1)
json.dump(list(broll.ROWS.values()), open(broll.B/"actmap.json","w"), indent=1, ensure_ascii=False)
for m in man: print(m["beat"], m["model"], len(m["refs"]), m["chars"], m["call_s"])
