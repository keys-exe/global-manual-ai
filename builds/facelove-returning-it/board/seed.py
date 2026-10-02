"""Seed the facelove-returning-it boards: builds doc (all four), cast cards (Current), docs/absorption + docs/connectors (Plan + Current)."""
import json, re, time, pathlib
B = "facelove-returning-it"; now = int(time.time()*1000)
boards = {"current": "https://claude.ai/artifact/XvBf5D1NNmCN9XAkq4pDfs", "old": "https://claude.ai/artifact/TtJDHH94bKokmwcYsVCgqK",
          "final": "https://claude.ai/artifact/Ryuk4diTvt4cmAkjn6kKss", "plans": "https://claude.ai/artifact/7HqDH14C4dtjNtJSddmF1C"}
build = {"name": "FACELOVE · Returning It", "product": "FACELOVE Changing Foundation Stick", "mode": "Mode 1 — Photorealistic", "format": "UGC Ad",
         "run": "manual", "aspect": "9:16", "kind": "narration", "talkingHeads": True, "hooks": 3, "boards": boards, "archiveUrl": boards["old"],
         "folders": {"task": "1PvwdhVU13RI6M1GQi9GKy-aEdx_4XZSa"}, "balances": {"Higgsfield": 4548.14}, "balancesAt": now,
         "connectors": {"images": "Higgsfield (Sunburst, ODAQ B.V.)", "kling": "Higgsfield (rung 3 — no Kling connector)", "voice": "ElevenLabs API", "talking": "HeyGen Avatar V"},
         "voices": [{"id": "N", "name": "The creator (narrator)", "needed": True, "status": "missing",
                     "voice": "American woman, mid-40s, light Latina-American lilt, warm, quick, exasperated then delighted, conversational", "note": "§22U after the maps"}],
         "updatedAt": now}
assets = {"N-BEFORE": "ee03aee43fb55bcbe1bdfcdb724746c4", "N-AFTER": "0f42b94ed10f3bd9a7852c3161789e74"}
titles = {"N-BEFORE": "The creator — bare skin, before the stick (talking heads, application start)",
          "N-AFTER": "The creator — after: the stick blended in, every line kept (after beats, CTA)"}
urls = dict(l.split() for l in open("cast/urls.txt").read().splitlines())
jobs = json.load(open("cast/jobs.json"))
out = pathlib.Path("board/json"); out.mkdir(exist_ok=True)
json.dump(build, open(out/"build.json", "w"), ensure_ascii=False)
for k in assets:
    p = pathlib.Path(f"cast/{k}.prompt.txt").read_text(); size = pathlib.Path(f"cast/{k}_v1.png").stat().st_size
    doc = {"build": B, "act": "Cast", "stage": "cast", "beat": k, "title": titles[k], "line": "", "imagePrompt": p,
           "imageModel": "gpt_image_2_5 · sunburst · high · 2k · 9:16", "imageStatus": "review", "status": "review", "imageRegens": 0,
           "imageAsset": assets[k], "imageType": "image/png", "imageConnector": "Higgsfield", "imageUrl": urls[k], "imageJob": jobs[k],
           "imageRes": "1520×2688", "imageCredits": 2.75, "imageAt": now, "updatedAt": now, "flow": ["image"],
           "imageRefs": [{"label": "avatar.png (your creator picture)", "role": "Image 1 · face to copy", "kind": "character", "asset": "eb5451456bec860b918bc32801f02556", "type": "image/png"}],
           "imageVersions": [{"v": 1, "asset": assets[k], "type": "image/png", "url": urls[k], "model": "gpt_image_2_5 sunburst", "connector": "Higgsfield",
                              "credits": 2.75, "size": size, "at": now, "note": ""}]}
    json.dump(doc, open(out/f"gen_{k}.json", "w"), ensure_ascii=False)
md = pathlib.Path("BUILD_SHEET.md").read_text()
part = md.split("## 1. Absorption Sheet (§42)")[1].split("## 2. Script")[0]
secs = []
for chunk in re.split(r"\n(?=### )", part):
    chunk = chunk.strip().strip("-").strip()
    if not chunk: continue
    title, _, body = chunk.partition("\n")
    secs.append({"title": title.lstrip("#").strip(), "md": body.strip().rstrip("-").strip()})
rest = md.split("## 2. Script")[1]
for t in ["## 2. Script" + rest.split("## 3.")[0], "## 3." + rest.split("## 3.")[1].split("## 4.")[0], "## 4." + rest.split("## 4.")[1].split("## 5.")[0], "## 6." + rest.split("## 6.")[1]]:
    title, _, body = t.strip().partition("\n"); secs.append({"title": title.lstrip("#").strip(), "md": body.strip().strip("-").strip()})
summary = [{"label": "Length", "value": "About 1½ minutes — one woman talking to her phone in her bathrobe, with close-ups of the stick on her face"},
           {"label": "Pace", "value": "Fast and chatty, like a real TikTok: she barely stops talking; the close-ups change every 2–3 seconds"},
           {"label": "Voice", "value": "Her own voice — a warm, quick American woman in her mid-40s, annoyed at first, then clearly delighted"},
           {"label": "On screen", "value": "Her face to the camera, the white stick going on her cheek and turning her shade, her skin before and after, the sale bundle"},
           {"label": "Opening", "value": "“I am so mad…” — she sounds furious and says she's returning the stick"},
           {"label": "Ending", "value": "The twist: she only returns it to buy the 2-for-1 deal — “It was never your skin. It was the formula.”"},
           {"label": "We do better", "value": "The colour change shown clearly up close, her real skin problems before, the offer items shown, three different hooks"},
           {"label": "We leave out", "value": "The knife, the other brand's pink box, the inspo's laser-treatment line"}]
absorb = {"title": "Absorption Sheet", "step": 1, "order": 1, "source": f"builds/{B}/BUILD_SHEET.md", "build": B,
          "updatedAt": now, "sections": secs, "summary": summary}
json.dump(absorb, open(out/"absorption.json", "w"), ensure_ascii=False)
conn = pathlib.Path("connectors.md").read_text().split("\n", 1)[1]
json.dump({"title": "Connector Map", "step": 0, "order": 0, "source": f"builds/{B}/connectors.md", "build": B, "updatedAt": now,
           "sections": [{"title": "Connector map (§5)", "md": conn.strip()}]}, open(out/"connectors.json", "w"), ensure_ascii=False)
print(len(secs), [s["title"] for s in secs])
