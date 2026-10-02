"""Seed the stryde-her-dad boards: builds doc (all four), cast cards (Current), docs/absorption + docs/connectors (Plan + Current)."""
import json, re, time, pathlib
B = "stryde-her-dad"; now = int(time.time()*1000)
boards = {"current": "https://claude.ai/artifact/Ki6d6eeXAgujWT1vAKTu8B", "old": "https://claude.ai/artifact/KnhxtqiFtKW7x4AJXdDtmQ",
          "final": "https://claude.ai/artifact/FTaYbfPdGNzgvtW7H5D3V9", "plans": "https://claude.ai/artifact/GGfqqXJgZNEKzVmicQv5Ps"}
build = {"name": "STRYDE · Her Dad", "product": "STRYDE Precision Strap", "mode": "Mode 4 — Realistic Film", "format": "AI Drama VSL",
         "run": "manual", "aspect": "9:16", "kind": "film", "talkingHeads": False, "hooks": 1, "boards": boards, "archiveUrl": boards["old"],
         "folders": {"task": "1HiQYsCmreGmcdUU2a-HF0hmxW68gFfz8"}, "balances": {"Higgsfield": 5855.90}, "balancesAt": now,
         "connectors": "Images Higgsfield · Seedance 2.5 Kie AI API · voice ElevenLabs API · music/SFX ElevenLabs API (see docs/connectors)",
         "voices": [{"id": k, "name": n, "needed": True, "status": "missing", "voice": v, "note": "§24I film voice master, after the maps"} for k, n, v in [
            ("C1", "Tony (and his inner VO)", "Kent, 64, low, rough, gravel, flat"), ("C2", "Sue (and her inner VO once)", "south-east, 52, quick, clear, warm"),
            ("C3", "Gary", "Essex, 70, dry, amused, certain"), ("C4", "The lad", "south London, 19, quick and kind"),
            ("C5", "GP", "Midlands, 48, calm and measured"), ("N", "Narrator (offer)", "English man, 60s, warm and plain — F2"),
            ("X1", "Labourer", "30s, south-east, cheeky (one-off)"), ("X2", "Neighbour", "older woman, friendly (one-off)")]],
         "updatedAt": now}
urls = json.load(open("cast/urls.json")); jobs = json.load(open("cast/jobs.json"))
assets = {"C1-TONY": "7d06fb8176f4d733345af64aaac98d27", "C2-SUE": "86b4e5a27e785955f8d23a2bbb110307", "C3-GARY": "d13af404ed788f9465c2bf54861996e1",
          "C4-LAD": "8302128decce000da57d35d4853c99c6", "C5-GP": "f74b6063e59d7578b071c274a7daddae"}
titles = {"C1-TONY": "Tony — 64, the hero (every scene)", "C2-SUE": "Sue — 52, his wife (the van, the car, the strap, the garden, the payoff)",
          "C3-GARY": "Gary — 70, the mentor (the builders' yard)", "C4-LAD": "The lad — 19, garden-centre worker (the van and the payoff)",
          "C5-GP": "The GP — 48 (the surgery)"}
out = pathlib.Path("board/json"); out.mkdir(exist_ok=True)
json.dump(build, open(out/"build.json", "w"), ensure_ascii=False)
for k in assets:
    p = pathlib.Path(f"cast/{k}.prompt.txt").read_text(); size = pathlib.Path(f"cast/{k}_v1.png").stat().st_size
    doc = {"build": B, "act": "Cast", "stage": "cast", "beat": k, "title": titles[k], "line": "", "imagePrompt": p,
           "imageModel": "gpt_image_2_5 · sunburst · high · 2k · 9:16", "imageStatus": "review", "status": "review", "imageRegens": 0,
           "imageAsset": assets[k], "imageType": "image/png", "imageConnector": "Higgsfield", "imageUrl": urls[k], "imageJob": jobs[k],
           "imageCredits": 2.75, "imageRes": "1520×2688", "imageAt": now, "updatedAt": now, "flow": ["image"],
           "imageVersions": [{"v": 1, "asset": assets[k], "type": "image/png", "url": urls[k], "model": "gpt_image_2_5 sunburst", "connector": "Higgsfield",
                              "credits": 2.75, "size": size, "at": now, "note": ""}]}
    json.dump(doc, open(out/f"gen_{k}.json", "w"), ensure_ascii=False)
md = pathlib.Path("BUILD_SHEET.md").read_text()
part = md.split("## 1. Absorption Sheet (§42)")[1].split("## 2. Script")[0]
secs = []
for chunk in re.split(r"\n(?=### |## 1b)", part):
    chunk = chunk.strip().strip("-").strip()
    if not chunk: continue
    title, _, body = chunk.partition("\n")
    secs.append({"title": title.lstrip("#").strip(), "md": body.strip().rstrip("-").strip()})
summary = [{"label": "Length", "value": "About 7 minutes — one film (the script has one opening)"},
           {"label": "Pace", "value": "Like a TV drama: short shots on faces, people talking to each other, a few quiet held moments"},
           {"label": "Voice", "value": "Everyone speaks on camera; Tony's thoughts (and Sue's once) are heard over his face; a narrator only for the offer"},
           {"label": "On screen", "value": "A British family drama: a garden-centre car park, their car, his stairs, the doctor, a builders' yard, their garden"},
           {"label": "Opening", "value": "A van reverses at Sue; Tony's knee gives way; a young lad saves her and asks 'Is your dad alright?'"},
           {"label": "Ending", "value": "Same car park weeks later: Tony gets to her in three strides; the lad calls him 'sir'; then the offer"},
           {"label": "We do better", "value": "A richer film look, and we show the change — forwards down his stairs, laying their patio — not only talk about it"},
           {"label": "We leave out", "value": "The inspo's assault and shirtless mirror scene, its drops and labels; shop and brand names are never shown"}]
absorb = {"title": "Absorption Sheet & Film Look Sheet", "step": 1, "order": 1, "source": f"builds/{B}/BUILD_SHEET.md", "build": B,
          "updatedAt": now, "sections": secs, "summary": summary}
json.dump(absorb, open(out/"absorption.json", "w"), ensure_ascii=False)
conn = pathlib.Path("work/connectors.md").read_text().split("\n", 1)[1].strip()
json.dump({"title": "Connector map", "step": 0, "order": 0, "source": f"builds/{B}/work/connectors.md", "build": B, "updatedAt": now,
           "sections": [{"title": "Connector map (§5)", "md": conn}]}, open(out/"connectors.json", "w"), ensure_ascii=False)
print(len(secs), [s["title"] for s in secs])
