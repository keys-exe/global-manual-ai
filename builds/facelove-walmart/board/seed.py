"""Seed the facelove-walmart boards: builds doc (all four), cast cards (Current), docs/absorption + docs/connectors (Plan + Current)."""
import json, re, time, pathlib, os
os.chdir(pathlib.Path(__file__).resolve().parents[1])
B = "facelove-walmart"; now = int(time.time()*1000)
boards = {"current": "https://claude.ai/artifact/KDWnrhSUGd5cTmrB28MBcW", "old": "https://claude.ai/artifact/JCGVnxgDJ1wb4ijcTj5Yhn",
          "final": "https://claude.ai/artifact/MJYSNxQs8zmZauvGD9yAfM", "plans": "https://claude.ai/artifact/RgnvPVq64gwcwwqheqg9BY"}
build = {"name": "FACELOVE · Walmart — Too Busy Glowing", "product": "FACELOVE Changing Foundation Stick", "mode": "Mode 5 — Pixar Film", "format": "AI Drama VSL",
         "run": "manual", "aspect": "9:16", "kind": "film", "talkingHeads": False, "hooks": 1, "boards": boards, "archiveUrl": boards["old"],
         "folders": {"task": "1Xvl_PR2jCEe3WJk177Vn5T-1efS1gt80"}, "balances": {"Higgsfield": 4006.35}, "balancesAt": now,
         "connectors": {"images": "Higgsfield (nano_banana_pro, private workspace)", "seedance": "Higgsfield (rung 2 — no Kie key)", "voice": "ElevenLabs API", "music": "ElevenLabs API"},
         "budget": {"Higgsfield": 16500, "ElevenLabs": 14200, "from": "draft (564 words)"},
         "voices": [{"id": k, "name": n, "needed": True, "status": "missing", "voice": v, "note": "§24I film voice master, after the maps"} for k, n, v in [
            ("N", "Michelle (narrator)", "Latina American woman, 63, warm, low, slightly husky, composed"), ("C1", "Peter", "American man, 65, confident baritone, salesman's ease"),
            ("C2", "The woman, 41", "American woman, 41, bright, clipped, guarded → urgent"), ("C3", "Rosa", "Latina American woman, 67, warm, husky, fierce and loving")]],
         "updatedAt": now}
assets = {"N-MICHELLE": "cfc484a2fb13481c71a99d6ebad97bb3", "N-MICHELLE-AFTER": "5744b410b34dae901ca6cd38ed82797b", "C1-PETER": "371c9add67dff289c2d18a3d096c5a03",
          "C2-YOUNGER": "5c4b5afa0a1dedf1564de9032f131aaf", "C3-ROSA": "0aa65e2ecf168292b2941c984c366467"}
titles = {"N-MICHELLE": "Michelle — 63, before (the flashback: divorce → the sister)", "N-MICHELLE-AFTER": "Michelle — after: foundation on, every line kept (hook, payoff, epilogue, CTA)",
          "C1-PETER": "Peter — the ex-husband, 65 (the divorce, the aisle)", "C2-YOUNGER": "The woman he left her for, 41 (the aisle)",
          "C3-ROSA": "Rosa — Michelle's older sister, 67 (the door, the reveal)"}
urls = dict(l.split() for l in open("cast/urls.txt").read().splitlines())
jobs = json.load(open("cast/jobs.json"))
out = pathlib.Path("board/json"); out.mkdir(exist_ok=True)
json.dump(build, open(out/"build.json", "w"), ensure_ascii=False)
for k in assets:
    p = pathlib.Path(f"cast/{k}.prompt.txt").read_text(); size = pathlib.Path(f"cast/{k}_v1.png").stat().st_size
    doc = {"build": B, "act": "Cast", "stage": "cast", "beat": k, "title": titles[k], "line": "", "imagePrompt": p,
           "imageModel": "nano_banana_pro (logged nano_banana_2) · 2k · 9:16", "imageStatus": "review", "status": "review", "imageRegens": 0,
           "imageAsset": assets[k], "imageType": "image/png", "imageConnector": "Higgsfield", "imageUrl": urls[k], "imageJob": jobs[k],
           "imageRes": "1536×2752", "imageCredits": 2, "imageAt": now, "updatedAt": now, "flow": ["image"],
           "imageRefs": ([{"label": "Michelle — before sheet (v1)", "role": "Image 1 · face to copy", "kind": "character", "ref": "N-MICHELLE", "asset": assets["N-MICHELLE"], "type": "image/png"}] if k == "N-MICHELLE-AFTER" else []),
           "imageVersions": [{"v": 1, "asset": assets[k], "type": "image/png", "url": urls[k], "model": "nano_banana_pro (logged nano_banana_2)", "connector": "Higgsfield",
                              "credits": 2, "size": size, "at": now, "note": ""}]}
    json.dump(doc, open(out/f"gen_{k}.json", "w"), ensure_ascii=False)
md = pathlib.Path("BUILD_SHEET.md").read_text()
part = md.split("## 1. Absorption Sheet (§42)")[1].split("## 2. Script")[0]
secs = []
for chunk in re.split(r"\n(?=### |## 1b)", part):
    chunk = chunk.strip().strip("-").strip()
    if not chunk: continue
    title, _, body = chunk.partition("\n")
    secs.append({"title": title.lstrip("#").strip(), "md": body.strip().rstrip("-").strip()})
summary = [{"label": "Length", "value": "About 3½–4 minutes — a short 3D animated drama, like a feature film"},
           {"label": "Pace", "value": "Film pace: shots of 3–4 seconds, people talking to each other, a few long held moments"},
           {"label": "Voice", "value": "Michelle, 63, tells her own story over the scenes; Peter, Rosa and the younger woman speak on screen"},
           {"label": "On screen", "value": "A bright big store aisle, her old living room, her bathroom mirror and vanity, her front door, then the same aisle again, the store doors and a sunny patio"},
           {"label": "Opening", "value": "Her shopping cart crashes into her ex-husband's in the first 3 seconds; he stares — “Michelle? Is that you?” — “It is just me.” She glides away"},
           {"label": "Ending", "value": "The younger woman runs after her to ask about her skin; Michelle just smiles and leaves. Peter texts weeks later; she puts the phone down. Then the stick and the offer"},
           {"label": "We do better", "value": "The crash is shown, not told; her sister brings the stick in person; the colour change on her own face in one unbroken shot; Michelle says nothing at the end"},
           {"label": "We leave out", "value": "The store's real name and logo on screen, the Korean claims and numbers, the inspo's pink bottle, the inspo heroine's look"}]
json.dump({"title": "Absorption Sheet & Film Look Sheet", "step": 1, "order": 1, "source": f"builds/{B}/BUILD_SHEET.md", "build": B,
           "updatedAt": now, "sections": secs, "summary": summary}, open(out/"absorption.json", "w"), ensure_ascii=False)
conn = pathlib.Path("connectors.md").read_text().split("\n", 1)[1]
json.dump({"title": "Connector Map", "step": 0, "order": 0, "source": f"builds/{B}/connectors.md", "build": B, "updatedAt": now,
           "sections": [{"title": "Connector map (§5)", "md": conn.strip()}]}, open(out/"connectors.json", "w"), ensure_ascii=False)
bud = pathlib.Path("budget.md").read_text().split("\n", 1)[1]
json.dump({"title": "Credit cap", "step": 2, "order": 2, "source": f"builds/{B}/budget.md", "build": B, "updatedAt": now,
           "sections": [{"title": "Credit cap (§5B, draft)", "md": bud.strip()}]}, open(out/"budget.json", "w"), ensure_ascii=False)
print(len(secs), [s["title"] for s in secs])
