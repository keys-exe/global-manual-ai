"""Scene 5 board docs: ingredient cards (To check) and SC05-T1..T7 (planned)."""
import json, time
from pathlib import Path
H = Path(__file__).parent; B = H.parent.parent
cards = json.load(open(H / "ingredients/cards.json"))
am = [r for r in json.load(open(B / "step5/act_map.json")) if r.get("scene") == "SC05"]
NOW = int(time.time() * 1000)
JOB = {"OUTFIT-N-D4": "586a9154-89db-42db-87e0-bcf867a8969f", "OUTFIT-C3-D4": "99c03052-cd0c-473e-a711-9d21511f49cf",
       "PROD-HAND-CARD": "b2a02fd1-8437-4028-9cdf-243320fc6b7a", "COLOUR-FRONT-CARD": "db72e34c-7892-4e1e-ad8d-b3a88a523f10"}
STAMP = {"OUTFIT-N-D4": "173842", "OUTFIT-C3-D4": "173843", "PROD-HAND-CARD": "173843", "COLOUR-FRONT-CARD": "173845"}
ASSET = {"OUTFIT-N-D4": "97141d9c308da08048ea7d386e1fe41c", "OUTFIT-C3-D4": "eb266c52aced18f280fe6fcf6836cfa1",
         "PROD-HAND-CARD": "04d6267d2f7fed9b0137072d10f3afce", "COLOUR-FRONT-CARD": "39901145cfc1a8c81f1e51feda52ae2a",
         "C3-FACE": "19f758201b4d3adf150e00f3370af5f4", "N-AFTER-FACE": "b8cdfcafe05d5a72cf5ac381e8eee12d",
         "PROD-CLOSED": "02dd0c20ff50bb88c92f6784d3596bfb", "PROD-BALM": "2476aff66629930d145e01174210b925",
         "PROD-BRUSH": "d75262c590d90d1450bafc0238f83ab7"}
REFDOC = {"N-FACE": "facelove-my-mother__N-FACE", "C3-FACE": "facelove-my-mother__C3-FACE",
          "CLOSED": "facelove-my-mother__PROD-CLOSED", "BALM": "facelove-my-mother__PROD-BALM", "BRUSH": "facelove-my-mother__PROD-BRUSH"}
INFO = {
 "OUTFIT-N-D4": ("Susan's outfit, day D4 (Beth's visit) — SC05 all takes", "(outfit) faded sage sweatshirt, grey lounge trousers, grey socks, black elastic (low ponytail) — face from N-FACE through SH06, N-AFTER-FACE from SH07 (HT26)"),
 "OUTFIT-C3-D4": ("Beth's outfit, day D4 (her visit) — SC05 all takes", "(outfit) chambray shirt sleeves rolled, white jeans, tan flats, black garment bag — face from C3-FACE (HT26)"),
 "PROD-HAND-CARD": ("How the stick is held — closed, wordmark to the lens (SC05-T3)", "(product) one closed violet stick in Beth's right hand, the single FACELOVE wordmark facing out"),
 "COLOUR-FRONT-CARD": ("The colour change front — white ahead of the brush, skin behind (SC05-T4/T5)", "(product) the balm goes on white; the brush end works it and it turns to her own skin behind the bristles; her lines stay"),
}
docs = {}
for k, (title, line) in INFO.items():
    c = cards[k]; url = f"https://d8j0ntlcm91z4.cloudfront.net/user_3AViUeU5dIz6pgsjYszQ9iux9YN/hf_20261002_{STAMP[k]}_{JOB[k]}.png"
    refs = [{"label": r[0], "kind": r[1], "role": r[2], "ref": REFDOC.get(r[0], r[0])} for r in c.get("refs", [])]
    size = (H / f"ingredients/{k}_v1.png").stat().st_size
    docs[k] = dict(act="Scene 5", beat=k, build="facelove-my-mother", flow=["image"], scene=5, stage="broll", status="review",
        title=title, line=line, imagePrompt=c["prompt"], imageModel=c["model"], imageRefs=refs, imageAsset=ASSET[k],
        imageType="image/png", imageRes="1520×2688", imageConnector="Higgsfield", imageCredits=2.9, imageJob=JOB[k],
        imageUrl=url, imageAt=NOW, imageStatus="review", imageRegens=0, updatedAt=NOW,
        imageVersions=[dict(v=1, asset=ASSET[k], type="image/png", url=url, model="gpt_image_2_5 sunburst", connector="Higgsfield",
                            credits=2.9, size=size, at=NOW, note="")])
for k, src, label, line, mid in [
  ("C3-FACE", "C3-BETH", "C3-BETH sheet", "(face) C3-BETH sheet, close-up panel cropped to face and hair — her D4 clothes are not her sheet's party outfit", "16a0127c-0945-4187-ae78-eabf7c732819"),
  ("N-AFTER-FACE", "N-SUSAN-AFTER", "N-SUSAN-AFTER sheet", "(face) N-SUSAN-AFTER sheet, close-up panel cropped to face and hair — Susan from SH07 on, once the stick is on", "860d3197-f292-42d0-9357-6d8b2427389a")]:
    size = (H / f"ingredients/{k}.png").stat().st_size
    docs[k] = dict(act="Scene 5", beat=k, build="facelove-my-mother", flow=["image"], scene=5, stage="broll", status="review",
        title=f"{label.split()[0]}'s face-and-hair crop — from the confirmed cast sheet's close-up (no new render, HT26)", line=line,
        imageModel=f"crop of {src}_v1 (no render)", imageRefs=[{"kind": "character", "label": label, "ref": f"facelove-my-mother__{src}", "role": "cropped from"}],
        imageAsset=ASSET[k], imageType="image/png", imageRes="860×910", imageConnector="crop", imageCredits=0, imageAt=NOW,
        imageStatus="review", updatedAt=NOW,
        imageVersions=[dict(v=1, asset=ASSET[k], type="image/png", model="crop", connector="crop", credits=0, size=size, at=NOW, note=f"Higgsfield media {mid}")])
for k, f, t, mid in [("PROD-CLOSED", "CLOSED.jpg", "the stick closed — both ends capped", "7278afd1-9898-41bb-a85f-e23b1e645a73"),
                     ("PROD-BALM", "BALM_END_DEPLOYED.jpg", "the balm end uncapped", "e85268b0-5816-4e38-bf31-5f7f829ae31e"),
                     ("PROD-BRUSH", "BRUSH_END_DEPLOYED.jpg", "the brush end uncapped", "10c8c91d-dff7-4675-b394-d414a19f9ec8")]:
    size = (B / "product" / f).stat().st_size
    docs[k] = dict(act="Scene 5", beat=k, build="facelove-my-mother", flow=["image"], scene=5, stage="broll", status="review",
        title=f"Client product photo — {t}", line=f"(product) the client's own photo ({f}), attached as-is to every product take",
        imageModel="client product photo (no render)", imageRefs=[], imageAsset=ASSET[k], imageType="image/jpeg", imageRes="1143×2048",
        imageConnector="client photo", imageCredits=0, imageAt=NOW, imageStatus="review", updatedAt=NOW,
        imageVersions=[dict(v=1, asset=ASSET[k], type="image/jpeg", model="client photo", connector="client photo", credits=0, size=size, at=NOW, note=f"Higgsfield media {mid}")])
# planned takes
LINES = {}
for l in (B / "BUILD_SHEET.md").read_text().splitlines():
    p = [x.strip() for x in l.split("|")]
    if len(p) > 5 and p[1].startswith("L0") and "SC05" in p[2]: LINES[p[1]] = (p[3], p[4])
TITLES = {"SC05-T1": "Beth arrives: 'There's a thing Saturday' / Susan on the bed (SH01–SH02)",
          "SC05-T2": "Beth on Paula's Botox, then pulls out the stool: 'Come sit. Watch this.' (SH03–SH04)",
          "SC05-T3": "Beth tilts Susan's chin, takes out the closed stick, uncaps the balm end (SH05)",
          "SC05-T4": "Insert — the balm draws a white stripe up her cheekbone (SH06, silent)",
          "SC05-T5": "Insert — the brush works the stripe; white turns to her skin behind it (SH07)",
          "SC05-T6": "Beth steps back; Susan in the mirror: '…and this is all you did?' (SH08–SH10)",
          "SC05-T7": "Beth, plain: 'This is all I did.' (SH11)"}
LEN = {"SC05-T1": 13, "SC05-T2": 15, "SC05-T3": 12, "SC05-T4": 4, "SC05-T5": 10, "SC05-T6": 15, "SC05-T7": 4}
for t, title in TITLES.items():
    rows = [r for r in am if r["take"] == t]
    ids = []
    for r in rows:
        for x in str(r.get("lines") or "").replace("+", ",").split(","):
            x = x.strip()
            if x.startswith("L0") and x not in ids: ids.append(x)
    line = " / ".join(LINES[i][1] for i in ids if i in LINES) or "(no dialogue)"
    if t == "SC05-T4": line = "(silent insert — L014's 'Goes on white, don't panic.' plays over it in the edit)"
    docs[t] = dict(act="Scene 5", beat=t, build="facelove-my-mother", scene=5, stage="broll", status="planned", flow=["video"],
        covers=[r["beat"] for r in rows], title=f"Scene 5 · {t[-2:]} — {title}", line=line, duration=LEN[t],
        model="seedance_2_5 · omni_reference · 720p · 9:16", videoConnector="Higgsfield",
        motionPlan=" ; ".join(r.get("action", "") for r in rows if r.get("action")),
        note="Waits for the Scene 5 ingredient cards' Confirm, then one Seedance call.", updatedAt=NOW)
writes = [{"op": "set", "collection": "generations", "doc_id": f"facelove-my-mother__{k}", "data": d} for k, d in docs.items()]
json.dump(writes, open(H / "board/writes.json", "w"), ensure_ascii=False, indent=1)
print(len(writes)); [print(w["doc_id"], w["data"]["line"][:90]) for w in writes]
