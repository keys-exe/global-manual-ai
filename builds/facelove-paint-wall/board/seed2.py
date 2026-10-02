"""Steps 4–5 onto the boards: plate + prop cards (Current, To check), planned beat cards, Plan docs (Plan + Current)."""
import json, re, time, pathlib
B = "facelove-paint-wall"; now = int(time.time()*1000)
out = pathlib.Path("board/json"); jobs = json.load(open("plates/jobs.json"))
urls = dict(l.split() for l in open("plates/urls.txt"))
A = {"L-SHELF": "7eeaeb1e4c7165e474011cde0cee4b0a", "L-WALL": "0652fe0e0b0bf613e04f6234dce2eb57",
     "PROP-BOTTLE": "a522c5615227481cd620b566394916ea", "PROP-PAINT": "695837ad04a584c18d588ca32e9e8f5a"}
T = {"L-SHELF": "Her dressing room — the shelf of ~40 foundation bottles (the talking-head set)",
     "L-WALL": "The same room turned round — the bare warm plaster wall prepared for painting",
     "PROP-BOTTLE": "Prop card — the one ordinary foundation bottle she holds (no label)",
     "PROP-PAINT": "Prop card — the plain paint can, tray and roller (no label)"}
writes = []
for k, a in A.items():
    plate = k.startswith("L-")
    p = pathlib.Path(f"plates/{k}.prompt.txt").read_text(); size = pathlib.Path(f"plates/{k}_v1.png").stat().st_size
    doc = {"build": B, "act": "Locations", "stage": "locations", "beat": k, "title": T[k], "line": "",
           "imagePrompt": p, "imageModel": f"gpt_image_2_5 · sunburst · high · 2k · {'16:9' if plate else '9:16'}", "imageStatus": "review", "status": "review",
           "imageRegens": 0, "imageAsset": a, "imageType": "image/png", "imageConnector": "Higgsfield", "imageUrl": urls[k], "imageJob": jobs[k],
           "imageRes": "2688×1520" if plate else "1520×2688", "imageCredits": 2.75, "imageAt": now, "updatedAt": now, "flow": ["image"], "imageRefs": [],
           "imageVersions": [{"v": 1, "asset": a, "type": "image/png", "url": urls[k], "model": "gpt_image_2_5 sunburst", "connector": "Higgsfield",
                              "credits": 2.75, "size": size, "at": now, "note": ""}]}
    json.dump(doc, open(out/f"gen_{k}.json", "w"), ensure_ascii=False); writes.append(("generations", f"{B}__{k}", f"gen_{k}.json"))
R = json.load(open("step5/act_map.json"))
for r in R:
    th = r["type"] == "TH"
    doc = {"build": B, "act": r["act"], "stage": "talking" if th else "broll", "beat": r["beat"], "title": (r["line"] if th else r["action"])[:140],
           "line": r["line"], "status": "planned", "updatedAt": now, "flow": ["video"] if th else ["image", "video"]}
    if not th:
        doc.update({"imageStatus": "planned", "location": r["location"], "storyDay": r["story_day"],
                    "motionPlan": "From this frame: " + r["action"] + f" — {r['pace']}; {r['camera']}."})
    json.dump(doc, open(out/f"gen_{r['beat']}.json", "w"), ensure_ascii=False); writes.append(("generations", f"{B}__{r['beat']}", f"gen_{r['beat']}.json"))
def secs(md, level="### "):
    out_ = []
    for chunk in re.split(r"\n(?=%s)" % re.escape(level), "\n" + md):
        chunk = chunk.strip()
        if not chunk.startswith(level.strip()): continue
        t, _, b = chunk.partition("\n"); out_.append({"title": t.lstrip("#").strip(), "md": b.strip().strip("-").strip()})
    return out_
s45 = pathlib.Path("STEP4_5.md").read_text()
step4 = s45.split("## Step 4")[1].split("## Step 5")[0]; step5 = s45.split("## Step 5")[1]
n_br = sum(r["type"] == "BR" for r in R); n_th = len(R) - n_br
docs = {
 "locations": {"title": "Locations, property & light", "step": 4, "order": 2, "sections": secs(step4)},
 "actmap": {"title": "Act map", "step": 5, "order": 3, "sections": [{"title": f"Act map ({len(R)} rows · {n_br} B-roll · {n_th} talking heads)", "md": pathlib.Path("step5/act_map.md").read_text()}]},
 "wardrobe": {"title": "Wardrobe map — per story day", "step": 5, "order": 4, "sections": [{"title": "Wardrobe map", "md": pathlib.Path("step5/wardrobe.md").read_text().split("\n", 1)[1].strip()}]},
 "visualplan": {"title": "Visual Pitch", "step": 5, "order": 5, "sections": [{"title": "Visual Pitch (§30M)", "md": pathlib.Path("step5/visual_plan.md").read_text()}]},
 "music": {"title": "Music register map", "step": 5, "order": 6, "sections": [s for s in secs(step5) if s["title"].startswith("Music")]},
}
for k, d in docs.items():
    d.update({"build": B, "source": f"builds/{B}/STEP4_5.md", "updatedAt": now})
    json.dump(d, open(out/f"doc_{k}.json", "w"), ensure_ascii=False); writes.append(("docs", k, f"doc_{k}.json"))
json.dump(writes, open(out/"writes2.json", "w"))
print(len(writes), [len(d["sections"]) for d in docs.values()])
