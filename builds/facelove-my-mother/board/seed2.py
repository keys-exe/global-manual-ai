"""Steps 4–5 board writes: plate cards (Current) + plan docs (Plan + Current, text only) + build doc balance."""
import json, re, time, pathlib
B = "facelove-my-mother"; now = int(time.time()*1000); out = pathlib.Path("board/json"); out.mkdir(exist_ok=True)
assets = {"P-HOUSE": "49d14ae498b0515fa9051693a8deb25d", "L-YARD": "e1faab6f3e8b06e00d56f0fc26b6d7f5", "L-GATHERING": "fbd4270aa191336a7fd2cce2f97f3ef8",
          "L-VANITY": "4a674a38302e4e8ea40fb3e3b6c90427", "L-YARD-REV": "39ee502d52712a896c886964780980d0", "L-PORCH-IN": "4485df5afc200e5fe41041c7dad46c38",
          "L-HOSTS-FRONT": "09a47791c22123bba22507ea8f5255f5", "L-VANITY-REV": "e829edff5ff1af3acecf59ed553cda24"}
titles = {"P-HOUSE": "Susan's house — the front hall and kitchen (property plate; SC04 invite)", "L-YARD": "The hosts' back yard — the long table, the cake, the bulbs (SC01, SC02, SC07–SC09)",
          "L-GATHERING": "The daughter's family room — the birthday (SC04)", "L-VANITY": "Susan's bedroom — the dressing table and mirror (SC04 mirror, SC05, SC06)",
          "L-YARD-REV": "The yard from the deck — reverse (SC07, SC09)", "L-PORCH-IN": "Inside the hosts' back door at dusk (SC03)",
          "L-HOSTS-FRONT": "The hosts' house from the street (SC07 — the car)", "L-VANITY-REV": "Susan's bedroom toward the door — reverse (SC05 Beth comes in)"}
ref = {"L-VANITY": "P-HOUSE", "L-YARD-REV": "L-YARD", "L-PORCH-IN": "L-YARD", "L-HOSTS-FRONT": "L-YARD", "L-VANITY-REV": "L-VANITY"}
urls = {l.split()[0]: (l.split()[1], l.split()[2]) for l in open("plates/urls.txt").read().splitlines()}
prompts = json.load(open("plates/prompts.json"))
cr = round(24.92 / 8, 2)
writes = []
for k, a in assets.items():
    size = pathlib.Path(f"plates/{k}_v1.png").stat().st_size
    doc = {"build": B, "act": "Locations", "stage": "locations", "beat": k, "title": titles[k], "line": "", "imagePrompt": prompts[k]["prompt"],
           "imageModel": "gpt_image_2_5 · sunburst · high · 2k · 16:9", "imageStatus": "review", "status": "review", "imageRegens": 0,
           "imageAsset": a, "imageType": "image/png", "imageConnector": "Higgsfield", "imageUrl": urls[k][0], "imageJob": urls[k][1],
           "imageRes": "2688×1520", "imageCredits": cr, "imageAt": now, "updatedAt": now, "flow": ["image"],
           "imageRefs": ([{"label": f"{ref[k]} plate", "role": "Image 1 · the same place", "kind": "location", "ref": f"{B}__{ref[k]}"}] if k in ref else []),
           "imageVersions": [{"v": 1, "asset": a, "type": "image/png", "url": urls[k][0], "model": "gpt_image_2_5 sunburst", "connector": "Higgsfield", "credits": cr, "size": size, "at": now, "note": ""}]}
    if k == "L-PORCH-IN": doc["note"] = "F17: through the glass this render shows the back of a house, not the party yard — your call"
    json.dump(doc, open(out / f"gen_{k}.json", "w"), ensure_ascii=False); writes.append(("generations", f"{B}__{k}", f"gen_{k}.json"))
md = pathlib.Path("STEP4_5.md").read_text()
def secs(text):
    s = []
    for chunk in re.split(r"\n(?=### )", text.strip()):
        t, _, body = chunk.partition("\n"); s.append({"title": t.lstrip("#").strip(), "md": body.strip()})
    return s
part4 = md.split("## 4. Property and location maps (§30G, §30C)")[1].split("## 5.")[0]
part5 = "## 5." + md.split("## 5.")[1]
spine = part5.split("### Story spine (§24I part 9)")[1].split("### Act map")[0]
actm = part5.split("### Act map (E4)")[1].split("### Takes")[0]
takes = part5.split("### Takes (§24K part 5)")[1].split("### Wardrobe map")[0]
music = part5.split("### Music Register Map")[1].split("### Visual Instruction Ledger")[0]
vil = part5.split("### Visual Instruction Ledger — assigned")[1].split("### Ingredient ledger")[0]
ing = part5.split("### Ingredient ledger")[1].split("## Flags added")[0]
flags = part5.split("## Flags added at steps 4–5")[1].split("## Next")[0]
docs = {
 "locations": {"title": "Property & Location Sheets", "step": 4, "order": 2, "sections": secs(part4)},
 "actmap": {"title": "Act map", "step": 5, "order": 3, "sections": [{"title": "Story spine", "md": spine.strip()}, {"title": "Act map (E4) " + actm.split("\n")[0].strip(), "md": "\n".join(actm.split("\n")[1:]).strip()},
            {"title": "Visual Instruction Ledger — assigned", "md": vil.strip()}, {"title": "Ingredient ledger", "md": ("Ingredient ledger" + ing).split("\n", 1)[1].strip()}, {"title": "Flags added at steps 4–5", "md": flags.strip()}]},
 "takes": {"title": "Takes — one Seedance call each", "step": 5, "order": 4, "sections": [{"title": "Takes", "md": takes.split("\n", 1)[1].strip()}, {"title": "takes.py report", "md": pathlib.Path("step5/takes.md").read_text()}]},
 "wardrobe": {"title": "Wardrobe map — per story day", "step": 5, "order": 5, "sections": [{"title": "Wardrobe map (§14A, §21)", "md": pathlib.Path("step5/wardrobe.md").read_text()}]},
 "visualplan": {"title": "Visual Pitch", "step": 5, "order": 6, "sections": [{"title": "Visual Pitch (§30M)", "md": pathlib.Path("step5/visual_plan.md").read_text()}]},
 "music": {"title": "Music Register Map", "step": 5, "order": 7, "sections": [{"title": "Music Register Map (§40A)", "md": ("Music Register Map" + music).split("\n", 1)[1].strip()}]},
}
for k, d in docs.items():
    d.update({"source": f"builds/{B}/STEP4_5.md", "build": B, "updatedAt": now})
    json.dump(d, open(out / f"doc_{k}.json", "w"), ensure_ascii=False); writes.append(("docs", k, f"doc_{k}.json"))
json.dump([{"op": "set", "collection": c, "doc_id": d, "file_path": str((out / f).resolve())} for c, d, f in writes], open(out / "batch2_current.json", "w"))
json.dump([{"op": "set", "collection": c, "doc_id": d, "file_path": str((out / f).resolve())} for c, d, f in writes if c == "docs"], open(out / "batch2_plans.json", "w"))
print(len(writes), [len(d["sections"]) for d in docs.values()])
