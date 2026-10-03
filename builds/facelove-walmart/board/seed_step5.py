"""Step-5 docs (Plan + Current) and the 16 planned take cards (Current)."""
import json, time, pathlib, os, re
os.chdir(pathlib.Path(__file__).resolve().parents[1])
B = "facelove-walmart"; now = int(time.time()*1000)
rows = json.load(open("step5/act_rows.json")); md = pathlib.Path("STEP4_5.md").read_text()
def secs(text):
    out = []
    for chunk in re.split(r"\n(?=### )", text):
        chunk = chunk.strip()
        if not chunk.startswith("### "): continue
        t, _, b = chunk.partition("\n"); out.append({"title": t[4:].strip(), "md": b.strip()})
    return out
p4 = md.split("## 5. Act map")[0].split("## 4. Property and location maps (§30G, §30C)")[1]
p5 = "### " + md.split("## 5. Act map, takes, wardrobe, music\n")[1].split("\n### ", 1)[1]
docs = {
 "locations": {"title": "Locations & product cards", "step": 4, "order": 3, "sections": secs(p4)},
 "actmap": {"title": "Act map", "step": 5, "order": 4, "sections": [s for s in secs(p5) if s["title"].startswith(("Story spine", "Act map"))]},
 "takes": {"title": "Takes", "step": 5, "order": 5, "sections": secs(pathlib.Path("step5/takes.md").read_text())},
 "blocking": {"title": "Set maps & blocking", "step": 5, "order": 6, "sections": [{"title": "Blocking (§24P)", "md": pathlib.Path("step5/blocking.md").read_text()}]},
 "visualplan": {"title": "Visual pitch", "step": 5, "order": 7, "sections": [{"title": "Visual pitch (§30M)", "md": pathlib.Path("step5/visual_plan.md").read_text()}]},
 "wardrobe": {"title": "Wardrobe map", "step": 5, "order": 8, "sections": [{"title": "Wardrobe per story day (§21)", "md": pathlib.Path("step5/wardrobe.md").read_text()}]},
 "music": {"title": "Music register map", "step": 5, "order": 9, "sections": secs(pathlib.Path("step5/music.md").read_text())},
 "budget": {"title": "Credit cap", "step": 5, "order": 2, "sections": [s for s in secs(p5) if s["title"].startswith("Credit cap")]},
}
for k, d in docs.items():
    d.update(source=f"builds/{B}/STEP4_5.md", build=B, updatedAt=now)
    assert d["sections"], k
REF = {"N": "N-MICHELLE", "C1": "C1-PETER", "C2": "C2-YOUNGER", "C3": "C3-ROSA"}
AFTER_DAYS = {"P1", "P2", "A1", "A2"}
takes = {}
for r in rows: takes.setdefault(r["take"], []).append(r)
gens = {}
for t, rs in takes.items():
    sc = int(rs[0]["group"][2:]); hook = sc == 1
    ing = []
    for c in sorted({c for r in rs for c in r.get("cast", [])}):
        ref = ("N-MICHELLE-AFTER" if rs[0]["story_day"] in AFTER_DAYS else "N-MICHELLE") if c == "N" else REF[c]
        ing.append({"label": ref, "role": "@ref · character", "kind": "character", "ref": f"{B}__{ref}"})
    loc = {"L-HALL": "P-HOUSE"}.get(rs[0]["location"], rs[0]["location"])
    ing.append({"label": loc, "role": "@ref · location", "kind": "location", "ref": f"{B}__{loc}"})
    if rs[0]["location"] == "L-AISLE": ing.append({"label": "L-AISLE-REV", "role": "@ref · location (reverse)", "kind": "location", "ref": f"{B}__L-AISLE-REV"})
    if any(r.get("product_beat") for r in rs):
        ing.append({"label": "PROD-CLOSED", "role": "@ref · product", "kind": "product", "ref": f"{B}__PROD-CLOSED"})
        if t.startswith("SC06"):
            ing.append({"label": "PROD-HAND-CARD", "role": "@ref · info", "kind": "info", "ref": f"{B}__PROD-HAND-CARD", "note": "held low, a little longer than her hand is wide"})
            ing.append({"label": "COLOUR-FRONT-CARD", "role": "@ref · info", "kind": "info", "ref": f"{B}__COLOUR-FRONT-CARD", "note": "white ahead of the brush, her shade behind; lines unchanged"})
    words = " / ".join(x for r in rs for x in [r.get("dialogue")] if x)
    gens[t] = {"build": B, "act": "Hook 1" if hook else f"Act {sc-1}", "stage": "hooks" if hook else "broll", "scene": sc, **({"hook": 1} if hook else {}),
               "beat": t, "title": f"{t} — " + {1: "the carts hit", 2: "the divorce", 3: "the undoing", 4: "nothing worked", 5: "the sister", 6: "the reveal",
                                                7: "the change", 8: "back in the photos", 9: "the payoff", 10: "out through the doors", 11: "the text", 12: "the close"}[sc]
               + " (" + ", ".join(r["beat"].split("-", 1)[1] for r in rs) + ")",
               "line": words or " ".join(r.get("vo", "") for r in rs).strip(), "covers": [r["beat"] for r in rs], "duration": sum(r["duration"] for r in rs),
               "status": "planned", "model": "kling3_0 · first+last frame (pinned)" if rs[0].get("pinned") else "seedance_2_5 · omni_reference · 720p · 9:16",
               "videoConnector": "Higgsfield", "flow": ["video"], "updatedAt": now,
               "motionPlan": " → ".join(r["action"] for r in rs), "ingredients": ing,
               "note": "Waits for the plates, the cards and the voice masters to be confirmed, then one call (§24K part 5)."}
out = pathlib.Path("board/json")
for k, d in docs.items(): json.dump(d, open(out / f"doc_{k}.json", "w"), ensure_ascii=False)
for k, d in gens.items(): json.dump(d, open(out / f"gen_{k}.json", "w"), ensure_ascii=False)
b = json.load(open(out / "build.json")); b["budget"] = {"Higgsfield": 18950, "ElevenLabs": 14200, "from": "step-5 estimate (act map, 262 s of takes)"}; b["balances"] = {"Higgsfield": 3988.35}; b["balancesAt"] = now; b["updatedAt"] = now
json.dump(b, open(out / "build.json", "w"), ensure_ascii=False)
W = lambda col, k, f: {"op": "set", "collection": col, "doc_id": k, "file_path": str((out / f).resolve())}
plan = [W("docs", k, f"doc_{k}.json") for k in docs]
cur = plan + [W("generations", f"{B}__{k}", f"gen_{k}.json") for k in gens]
json.dump(plan, open(out / "step5_plan.json", "w")); json.dump(cur, open(out / "step5_current.json", "w"))
print(len(docs), "docs,", len(gens), "takes")
