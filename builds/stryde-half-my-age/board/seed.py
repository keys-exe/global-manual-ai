"""Seed the stryde-half-my-age boards: builds doc (all four), cast cards (Current), docs/absorption (Plan + Current)."""
import json, re, time, pathlib
B = "stryde-half-my-age"; now = int(time.time()*1000)
boards = {"current": "https://claude.ai/artifact/RrQR9jKnsbqT6v8uJMbqR2", "old": "https://claude.ai/artifact/SXWuEkNiYcdetxvhetCFaZ",
          "final": "https://claude.ai/artifact/FH22SWdaLRACaGTyS92KpH", "plans": "https://claude.ai/artifact/UK75G7UMCa1sSmvwJQFWJo"}
build = {"name": "STRYDE · Half My Age", "product": "STRYDE Precision Strap", "mode": "Mode 4 — Realistic Film", "format": "AI Drama VSL",
         "run": "manual", "aspect": "9:16", "kind": "film", "talkingHeads": False, "hooks": 4, "boards": boards, "archiveUrl": boards["old"],
         "folders": {"task": "1R1jJrUhMjPzbIsbM3fmXdJUpxnu48iOT"}, "balances": {"Higgsfield": 12735.65}, "balancesAt": now,
         "voices": [{"id": k, "name": n, "needed": True, "status": "missing", "voice": v, "note": "§24I film voice master, after the maps"} for k, n, v in [
            ("N", "Her (narrator)", "Northern English woman, 71, light, dry, a little gravel"), ("C1", "Barbara", "Midlands, 74, bright and certain"),
            ("C2", "Daughter", "northern, 46, quick and warm"), ("C3", "Husband", "northern, 74, gruff and soft"),
            ("C4", "Sister", "northern, 68, soft and careful"), ("C5", "Friend 1", "British Indian, 70, crisp and dry"),
            ("C6", "Friend 2", "Black British (Jamaican), 72, warm London"), ("X1", "Tannoy", "station announcer (one-off)"),
            ("X2", "Commuter", "southern man, 20s (one-off)"), ("X3", "Cashier", "young, northern (one-off)")]],
         "updatedAt": now}
urls = json.load(open("cast/urls.json")); jobs = json.load(open("cast/jobs.json"))
assets = {"N-HER": "36907b659eab1979815f57a97ab4f6ce", "C1-BARBARA": "64712384eec47cd3d751b62a974d02b7", "C2-DAUGHTER": "ff63f9f46833bcb9dbf910f8db9784b0",
          "C3-HUSBAND": "850c95c61279150703343ad61e4152a6", "C4-SISTER": "669ce851cfc595d65d82a6567c121831", "C5-FRIEND1": "06d3b486faeda9066062569b11832655",
          "C6-FRIEND2": "6367ae61b52b27d4fc4668ac6f932d5b"}
titles = {"N-HER": "Her — narrator, 71 (every scene)", "C1-BARBARA": "Barbara — the cousin, 74 (wedding, the strap, the mechanism)",
          "C2-DAUGHTER": "The daughter, 46 (all four hooks)", "C3-HUSBAND": "The husband, 74 (rock bottom, the drawer, the wedding, 'You were gone a long time')",
          "C4-SISTER": "The sister, 68 (the phone, the door, the stairs)", "C5-FRIEND1": "Friend 1, 70 (the café)", "C6-FRIEND2": "Friend 2, 72 (the café)"}
out = pathlib.Path("board/json"); out.mkdir(exist_ok=True)
json.dump(build, open(out/"build.json", "w"), ensure_ascii=False)
for k in assets:
    p = pathlib.Path(f"cast/{k}.prompt.txt").read_text(); size = pathlib.Path(f"cast/{k}_v1.png").stat().st_size
    doc = {"build": B, "act": "Cast", "stage": "cast", "beat": k, "title": titles[k], "line": "", "imagePrompt": p,
           "imageModel": "gpt_image_2_5 · sunburst · high · 2k · 9:16", "imageStatus": "review", "status": "review", "imageRegens": 0,
           "imageAsset": assets[k], "imageType": "image/png", "imageConnector": "Higgsfield", "imageUrl": urls[k], "imageJob": jobs[k],
           "imageRes": "1520×2688", "imageAt": now, "updatedAt": now, "flow": ["image"],
           "imageVersions": [{"v": 1, "asset": assets[k], "type": "image/png", "url": urls[k], "model": "gpt_image_2_5 sunburst", "connector": "Higgsfield",
                              "size": size, "at": now, "note": ""}]}
    json.dump(doc, open(out/f"gen_{k}.json", "w"), ensure_ascii=False)
# absorption doc: one section per ### heading of sections 1 and 1b
md = pathlib.Path("BUILD_SHEET.md").read_text()
part = md.split("## 1. Absorption Sheet (§42)")[1].split("## 2. Script")[0]
secs = []
for chunk in re.split(r"\n(?=### |## 1b)", part):
    chunk = chunk.strip().strip("-").strip()
    if not chunk: continue
    title, _, body = chunk.partition("\n")
    secs.append({"title": title.lstrip("#").strip(), "md": body.strip().rstrip("-").strip()})
summary = [{"label": "Length", "value": "About 5 to 5½ minutes per film — four films, one per opening"},
           {"label": "Pace", "value": "Unhurried, like a TV drama: shots of about 4–5 seconds, people talking to each other"},
           {"label": "Voice", "value": "Her, 71, northern English, telling her own story over the scenes; everyone else speaks on camera"},
           {"label": "On screen", "value": "A British family drama: her house and stairs, a station, a wedding, the town, a café"},
           {"label": "Opening", "value": "Four openings: station stairs, the lift queue, the broken escalator, getting up off the floor — each ends 'When did that happen?'"},
           {"label": "Ending", "value": "Her sister comes Sunday and walks up the stairs on her own; the offer is said inside the story"},
           {"label": "We do better", "value": "Richer, darker film look; we show the strap working on her own stairs instead of only talking about it"},
           {"label": "We leave out", "value": "The lipstick and the narrator talking to camera at the end; brand and shop names are never shown on screen"}]
absorb = {"title": "Absorption Sheet & Film Look Sheet", "step": 1, "order": 1, "source": f"builds/{B}/BUILD_SHEET.md", "build": B,
          "updatedAt": now, "sections": secs, "summary": summary}
json.dump(absorb, open(out/"absorption.json", "w"), ensure_ascii=False)
print(len(secs), [s["title"] for s in secs])
