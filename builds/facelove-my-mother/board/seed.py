"""Seed the facelove-my-mother boards: builds doc (all four), cast cards (Current), docs/absorption + docs/connectors (Plan + Current)."""
import json, re, time, pathlib
B = "facelove-my-mother"; now = int(time.time()*1000)
boards = {"current": "https://claude.ai/artifact/Gyh667QAbW2fA3GYgjgM23", "old": "https://claude.ai/artifact/KZ2UKhTA7GAysVcfgj7K41",
          "final": "https://claude.ai/artifact/1NUkwd9icgtPGXenBTr5Ah", "plans": "https://claude.ai/artifact/VmUne7ypBrBQa52jVqXRrs"}
build = {"name": "FACELOVE · You Look Like My Mother", "product": "FACELOVE Changing Foundation Stick", "mode": "Mode 4 — Realistic Film", "format": "AI Drama VSL",
         "run": "manual", "aspect": "9:16", "kind": "film", "talkingHeads": False, "hooks": 1, "boards": boards, "archiveUrl": boards["old"],
         "folders": {"task": "1M1DbzCv_DwDnXnhwkztLtgEB69yjBUiZ", "cast": "1__Tfn0-oRlpOnPL9ev8zfii2Q9vAcqT0"}, "balances": {"Higgsfield": 7880.55}, "balancesAt": now,
         "connectors": {"images": "Higgsfield (Sunburst, ODAQ B.V.)", "seedance": "Higgsfield (rung 2 — no Kie key)", "voice": "ElevenLabs API", "music": "ElevenLabs API"},
         "voices": [{"id": k, "name": n, "needed": True, "status": "missing", "voice": v, "note": "§24I film voice master, after the maps"} for k, n, v in [
            ("N", "Susan (narrator)", "American woman, 49, low, warm, slightly smoky, Midwest"), ("C1", "Greg", "American man, 52, warm baritone loosened by drink"),
            ("C2", "Paula", "American woman, 49, warm, low, a little husky"), ("C3", "Beth", "American woman, 49, bright, easy, honest"),
            ("C5", "Friend A", "American woman, 51, low and quick"), ("C6", "Friend B", "American woman, 50, soft and gentle")]],
         "updatedAt": now}
assets = {"N-SUSAN": "9c7a6a05384c26f8774c1a98e156ffe4", "N-SUSAN-AFTER": "6b92b2774f9852a5ffc61b33a30dd04f", "C1-GREG": "45aaf6609426ad275f9c80b8f33b680f",
          "C2-PAULA": "2de0678a362c7d55fb6f2f30c54e087a", "C3-BETH": "7801a81a6e6b14f9c6faaa991bcdb4ef", "C4-DAUGHTER": "646b05fe0499d12da20a0947638857f3",
          "C5-FRIEND-A": "798c09362223c99eccc976722f23a6e9", "C6-FRIEND-B": "5e69c61a280c1ee67a6fdf0c5908b000"}
refs = {"N-SUSAN": ("SUSAN OLD (your cast picture)", "53a938f866b107f7544d5ff57f73de04"), "N-SUSAN-AFTER": ("SUSAN NEW (your cast picture)", "d8e03887b18df0c36dbe5dfa6a49c81b"),
        "C1-GREG": ("GREG (your cast picture)", "b787e545eef12cba559302e67ef6fdc0"), "C2-PAULA": ("PAULA (your cast picture)", "235eb099fe80b3ace00066875df49de3"),
        "C3-BETH": ("BETH (your cast picture)", "ac80ec9630442c995d137df8d66f66df")}
titles = {"N-SUSAN": "Susan — 49, before (every scene to SC05)", "N-SUSAN-AFTER": "Susan — after: foundation on, every line kept (SC05 end → SC09)",
          "C1-GREG": "Greg — the husband, 52 (the toast, the redirect)", "C2-PAULA": "Paula — 49, a friend's wife (the toast, the boomerang)",
          "C3-BETH": "Beth — 49, the friend who helps (SC05–SC07)", "C4-DAUGHTER": "The daughter, 26 (the family gathering, SC04)",
          "C5-FRIEND-A": "Friend A, 51 — “…that was awful of him.” (the whisper, the return)", "C6-FRIEND-B": "Friend B, 50 — “She did kind of stop trying.” (the whisper, the return)"}
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
           "imageRefs": ([{"label": refs[k][0], "role": "Image 1 · face to copy", "kind": "character", "asset": refs[k][1], "type": "image/png"}] if k in refs else []),
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
summary = [{"label": "Length", "value": "About 3½ minutes — a short live-action drama with real-looking actors"},
           {"label": "Pace", "value": "Like a TV drama: shots of 2–4 seconds, people talking to each other, a few long held silences"},
           {"label": "Voice", "value": "Susan, 49, tells her own story over the scenes after the party; everyone else speaks on camera"},
           {"label": "On screen", "value": "A backyard anniversary party under string lights, her house, her bathroom mirror, her bedroom vanity, then the same party yard again"},
           {"label": "Opening", "value": "Her husband's toast turns cruel in front of thirty friends: “You look like my mother.” The camera stays on her face"},
           {"label": "Ending", "value": "She walks back into the same yard; Paula asks her what she's doing; “Go enjoy the party, Greg.” Then the stick, the offer and the free primer"},
           {"label": "We do better", "value": "A public wound instead of a private one, a friend doing her make-up with her own hands, the colour change in one unbroken shot, the cake left untouched then shared"},
           {"label": "We leave out", "value": "Real beauty brands on screen (the inspo's La Mer counter), the phone call, the inspo's own offer and guarantee wording"}]
absorb = {"title": "Absorption Sheet & Film Look Sheet", "step": 1, "order": 1, "source": f"builds/{B}/BUILD_SHEET.md", "build": B,
          "updatedAt": now, "sections": secs, "summary": summary}
json.dump(absorb, open(out/"absorption.json", "w"), ensure_ascii=False)
conn = pathlib.Path("connectors.md").read_text().split("\n", 1)[1]
json.dump({"title": "Connector Map", "step": 0, "order": 0, "source": f"builds/{B}/connectors.md", "build": B, "updatedAt": now,
           "sections": [{"title": "Connector map (§5)", "md": conn.strip()}]}, open(out/"connectors.json", "w"), ensure_ascii=False)
print(len(secs), [s["title"] for s in secs])
