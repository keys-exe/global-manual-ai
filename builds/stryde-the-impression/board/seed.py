"""Seed the stryde-the-impression boards: builds doc (all four), cast cards (Current), docs/absorption + docs/connectors (Plan + Current)."""
import json, re, time, pathlib
B = "stryde-the-impression"; now = int(time.time()*1000)
boards = {"current": "https://claude.ai/artifact/C7iJiu9zayETRq6wRpHERk", "old": "https://claude.ai/artifact/YHyjDG7UugdwLqpjL2Artq",
          "final": "https://claude.ai/artifact/7jESdNE8iA6sW9qtKVWMJr", "plans": "https://claude.ai/artifact/YR9p35toXVXK1EE1uPywym"}
V = [("N", "Hazel", "West Yorkshire woman, 67, warm, plain, a little husky"), ("C1", "Roy", "West Yorkshire man, 70, soft and practical"),
     ("C2", "Emma", "Yorkshire woman, 39, quick and bright"), ("C3", "Dan", "Leeds man, 41, easy and warm"),
     ("C4", "Oscar", "Yorkshire boy, 4"), ("C5", "Wendy", "Leeds woman, 74, Barbadian lilt, certain and amused"),
     ("X1", "Pharmacy assistant", "Bradford woman, 25, bright shop voice"), ("X2", "Mum with buggy", "Yorkshire woman, 32, friendly"),
     ("X3", "Lollipop lady", "broad West Yorkshire woman, 63, chatty")]
build = {"name": "STRYDE · The Impression", "product": "STRYDE Precision Strap", "mode": "Mode 4 — Realistic Film", "format": "AI Drama VSL",
         "run": "manual", "aspect": "9:16", "kind": "film", "talkingHeads": False, "hooks": 1, "boards": boards, "archiveUrl": boards["old"],
         "folders": {"task": "1myOChLFKSUBiQqn-Z5EoZ7ROwJ9sXeq2"}, "balances": {"Higgsfield": 5592.15, "Kie AI": 99229.6}, "balancesAt": now,
         "connectors": "Images Higgsfield (Sunburst) · Seedance 2.5 Kie AI · voice/music ElevenLabs API · no Drive connector",
         "voices": [{"id": k, "name": n, "needed": True, "status": "missing", "voice": v, "note": "§24I film voice master, after the maps"} for k, n, v in V],
         "updatedAt": now}
urls = json.load(open("cast/urls.json")); jobs = json.load(open("cast/jobs.json"))
assets = {"N-HAZEL": "eb281b4a4f2122c0ebe15e46e7e6e6e0", "C1-ROY": "0b50a226ea08a565bbde676a1ac30a02", "C2-EMMA": "ae7a799cbc81dd7ec9d4b7e9ce9dd4cf",
          "C3-DAN": "620cfa85b6a62c96f2823c9f6e422535", "C4-OSCAR": "0fd24fc231d137f188e6fc103fab0d7e", "C5-WENDY": "af36dde7c2523a61d54a2320bd1ce3cb",
          "X1-ASSISTANT": "f17244a096b620682dceb5f4745e8265", "X2-MUM": "df9da0f39cbf774db68257eb1559bd8a", "X3-LOLLIPOP": "a93fd08b80cb2f00563d4900eefab630"}
titles = {"N-HAZEL": "Hazel, 67 — the lead (every scene)", "C1-ROY": "Roy, 70 — her husband (the lunch, the car, the stairs, 'Say it again')",
          "C2-EMMA": "Emma, 39 — their daughter (the lunch, both hall films, the drawer, the first day)", "C3-DAN": "Dan, 41 — Emma's husband (the lunch, the first day)",
          "C4-OSCAR": "Oscar, 4 — the grandson (the impression, the first day)", "C5-WENDY": "Wendy, 74 — the other grandmother at the gate (the mechanism)",
          "X1-ASSISTANT": "Pharmacy assistant, 25 (the chemist)", "X2-MUM": "Mum with the buggy, 32 (the hill, July and August)",
          "X3-LOLLIPOP": "Lollipop lady, 63 (the school gate)"}
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
summary = [{"label": "Length", "value": "About 6 to 6½ minutes — one film, one opening"},
           {"label": "Pace", "value": "Like a TV drama: quick back-and-forth when people talk, quiet moments held"},
           {"label": "Voice", "value": "Everyone talks on camera in Yorkshire voices; Hazel's thoughts once, on the stairs; she talks to us only at the end"},
           {"label": "On screen", "value": "A family in a Yorkshire hill town: Sunday lunch, the hall and stairs at home, the chemist, the hill with the red postbox, the school gate"},
           {"label": "Opening", "value": "Her four-year-old grandson copies her walk at Sunday lunch, and the laughing stops"},
           {"label": "Ending", "value": "First day of school: she walks him up the hill; he does the walk again — and it's just walking. Then she talks to us at the gate"},
           {"label": "We do better", "value": "We show the strap working on her own stairs, and the boy's walk pays the story off, not just words"},
           {"label": "We leave out", "value": "The lipstick, Paris, and holding the product up at the end; brand and shop names never shown on screen"}]
absorb = {"title": "Absorption Sheet & Film Look Sheet", "step": 1, "order": 1, "source": f"builds/{B}/BUILD_SHEET.md", "build": B,
          "updatedAt": now, "sections": secs, "summary": summary}
json.dump(absorb, open(out/"absorption.json", "w"), ensure_ascii=False)
conn = {"title": "Connector map", "step": 0, "order": 0, "source": f"builds/{B}/work/connectors.md", "build": B, "updatedAt": now,
        "sections": [{"title": "Connector map", "md": pathlib.Path("work/connectors.md").read_text().split("\n", 1)[1].strip()}]}
json.dump(conn, open(out/"connectors.json", "w"), ensure_ascii=False)
print(len(secs), [s["title"] for s in secs])
