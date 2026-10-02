"""Steps 4–5 onto the boards: plate cards + C1/C2 sheets (Current, To check), planned beat cards, Plan docs (Plan + Current)."""
import json, re, time, pathlib
B = "facelove-returning-it"; now = int(time.time()*1000)
out = pathlib.Path("board/json"); jobs = json.load(open("work/step5_jobs.json"))
urls = {}
for f in ["plates/urls.txt", "cast/urls.txt"]:
    for l in open(f): k, u = l.split(); urls[k] = u
A = {"P-HOME": "bdc4a4f7120ce18244ea6ddf00f1b673", "L-VANITY": "51da1dc3ea4cd1be25f42ef3f5e381b0", "L-COUNTER": "2b7cc207a199abd054cdb96df21524fc",
     "L-CAFE": "7164204a1c157c41edf09de29584e1c7", "L-FRONT": "643bcac1aac96d5d847b9c5333d6c61b",
     "C1-COUNTER": "e2379fd33f48303f3f7b6f142e890ffc", "C2-FRIEND": "7f60699ea4cafb3a818b0ebc513058e5"}
T = {"P-HOME": "Her front hall — the brass mirror and the walnut door (property plate)", "L-VANITY": "Her bedroom from the vanity — the talking-head set",
     "L-COUNTER": "The department-store makeup counter (flashback)", "L-CAFE": "The café table by the window (this week)", "L-FRONT": "The front of her house — the path and the drive",
     "C1-COUNTER": "The makeup-counter saleswoman (B04–B05)", "C2-FRIEND": "The friend who asks what she's using (B09–B10)"}
writes = []
for k, a in A.items():
    plate = not k.startswith("C")
    d = "plates" if plate else "cast"
    p = pathlib.Path(f"{d}/{k}.prompt.txt").read_text(); size = pathlib.Path(f"{d}/{k}_v1.png").stat().st_size
    doc = {"build": B, "act": "Locations" if plate else "Cast", "stage": "locations" if plate else "cast", "beat": k, "title": T[k], "line": "",
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
docs = {
 "locations": {"title": "Locations, property & light", "step": 4, "order": 2, "sections": secs(step4)},
 "actmap": {"title": "Act map", "step": 5, "order": 3, "sections": [{"title": "Act map (24 rows · 16 B-roll · 8 talking heads)", "md": pathlib.Path("step5/act_map.md").read_text()}]},
 "wardrobe": {"title": "Wardrobe map — per story day", "step": 5, "order": 4, "sections": [{"title": "Wardrobe map", "md": pathlib.Path("step5/wardrobe.md").read_text().split("\n", 1)[1].strip()}]},
 "visualplan": {"title": "Visual Pitch", "step": 5, "order": 5, "sections": [{"title": "Visual Pitch (§30M)", "md": pathlib.Path("step5/visual_plan.md").read_text()}]},
 "music": {"title": "Music register map", "step": 5, "order": 6, "sections": [s for s in secs(step5) if s["title"].startswith("Music")]},
}
for k, d in docs.items():
    d.update({"build": B, "source": f"builds/{B}/STEP4_5.md", "updatedAt": now})
    json.dump(d, open(out/f"doc_{k}.json", "w"), ensure_ascii=False); writes.append(("docs", k, f"doc_{k}.json"))
json.dump(writes, open(out/"writes2.json", "w"))
print(len(writes), [len(d["sections"]) for d in docs.values()])
