"""Seed the facelove-paint-wall boards: builds doc (all four), cast cards (Current), docs/absorption + docs/connectors (Plan + Current)."""
import json, re, time, pathlib
B = "facelove-paint-wall"; now = int(time.time()*1000)
boards = {"current": "https://claude.ai/artifact/UnrHuRnaF86L7SNs4E2BX5", "old": "https://claude.ai/artifact/7ZBom126noUB8XknY5bNoq",
          "final": "https://claude.ai/artifact/7Do26Wwn8PBN3v9YUG6VZu", "plans": "https://claude.ai/artifact/FFh624b555mGJhZmNDk73Q"}
build = {"name": "FACELOVE · Paint Wall", "product": "FACELOVE Changing Foundation Stick", "mode": "Mode 1 — Photorealistic", "format": "UGC Ad",
         "run": "manual", "aspect": "9:16", "kind": "narration", "talkingHeads": True, "hooks": 3, "boards": boards, "archiveUrl": boards["old"],
         "folders": {"task": "1_OhMLzSEs_ftxQG1Np6NDBy2npGQ_iCP"}, "balances": {"Higgsfield": 1487.19}, "balancesAt": now,
         "connectors": {"images": "Higgsfield (Sunburst, ODAQ B.V.)", "kling": "Higgsfield (rung 3 — no Kling connector)", "voice": "ElevenLabs API", "talking": "HeyGen Avatar V"},
         "voices": [{"id": "N", "name": "The narrator", "needed": True, "status": "missing",
                     "voice": "American woman, 57, warm low-middle voice, bold and knowing, dry humour, clear and unhurried", "note": "§22U after the maps"}],
         "updatedAt": now}
assets = {"N-BEFORE": "3a764057cbd56aac5ac555b75da8e3fc", "N-AFTER": "baf9890c32611199d624f0559d7d393f"}
titles = {"N-BEFORE": "The narrator — bare tired face, before (Scene 2 mirror, Scene 3 macros)",
          "N-AFTER": "The narrator — the stick blended in, every line kept (presenter scenes, after, CTA)"}
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
           "imageRefs": [{"label": "AVATAR.png (your narrator picture)", "role": "Image 1 · face to copy", "kind": "character", "asset": "eabf276da0e6f564b3172fdf86c4219a", "type": "image/png"}],
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
summary = [{"label": "Length", "value": "About 2½ minutes — one woman in her late fifties talking to the camera in a bright, clean room, with close-ups"},
           {"label": "Pace", "value": "Calm and confident, like a clever teacher; the pictures change every 2–3 seconds"},
           {"label": "Voice", "value": "Her own voice — a warm, knowing American woman of 57, a little dry and funny"},
           {"label": "On screen", "value": "Her shelf of expensive foundations, her tired face in a mirror, foundation caking in the lines, a wall painted the wrong beige, the white stick turning her shade"},
           {"label": "Opening", "value": "“You could throw out every expensive foundation on your shelf right now…” — holding a bottle in one hand and the stick in the other"},
           {"label": "Ending", "value": "The offer in her voice, the stick turning in soft light — “Stop paying for a color that was never yours.”"},
           {"label": "We do better", "value": "A real wall and real paint for the analogy, the wall's cracks matching her skin's lines, the colour change in one unbroken close-up, three hooks"},
           {"label": "We leave out", "value": "The inspo's shirtless men and door, the injections part, the big words on the wall"}]
absorb = {"title": "Absorption Sheet", "step": 1, "order": 1, "source": f"builds/{B}/BUILD_SHEET.md", "build": B,
          "updatedAt": now, "sections": secs, "summary": summary}
json.dump(absorb, open(out/"absorption.json", "w"), ensure_ascii=False)
conn = pathlib.Path("connectors.md").read_text().split("\n", 1)[1]
json.dump({"title": "Connector Map", "step": 0, "order": 0, "source": f"builds/{B}/connectors.md", "build": B, "updatedAt": now,
           "sections": [{"title": "Connector map (§5)", "md": conn.strip()}]}, open(out/"connectors.json", "w"), ensure_ascii=False)
print(len(secs), [s["title"] for s in secs])
