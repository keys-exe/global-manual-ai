#!/usr/bin/env python3
"""Board docs for steps 4–5: plate / worn-ref cards (stage locations) and one planned card per act-map beat."""
import json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent; B = HERE.parent
AM = json.load(open(HERE / "actmap.json")); PL = json.load(open(B / "plates/plates.json"))
REN = json.load(open(B / "plates/renders.json"))
NOW = 1790626800000
TITLE = {"P0-PROP-P": "P0 · her house — hall and stairs (property plate)", "P1-P-FRONTROOM": "P1 · her front room (armchair)",
 "P2-P-KITCHEN": "P2 · her kitchen (the drawer, the garden)", "P3-D-CONSULT": "P3 · the doctor's consulting room (TH set)",
 "W-L-FRONT": "W-L-FRONT · strap worn, LEFT knee, front", "W-L-REAR": "W-L-REAR · strap worn, LEFT knee, rear", "W-L-BENT": "W-L-BENT · strap worn, LEFT knee, bent"}
docs = {}
for k, p in PL.items():
    r = REN.get(k); d = dict(build="down-forwards-again", stage="locations", beat=k, title=TITLE[k], line="",
        imagePrompt=f"see builds/down-forwards-again/plates/{k}.prompt.txt ({p['chars']} chars) · attach: {p['attach']}",
        imageModel=("gpt_image_2_5 · sunburst · high · 2k · 9:16" if "sunburst" in p["model"] else "nano_banana_pro · 2k · 9:16"),
        imageConnector="Higgsfield", flow=["image"], updatedAt=NOW)
    if r:
        d.update(status="review", imageStatus="review", imageAsset=r["asset"], imageType="image/png", imageUrl=r["url"], imageRes=r["res"],
                 imageAt=r["at"], imageCredits="×1", imageVersions=[dict(v=1, asset=r["asset"], type="image/png", url=r["url"], model=r["model"],
                 connector="Higgsfield", size=r["size"], at=r["at"], note="first render — job " + r["job"])], notes=r.get("note", "To check — your Confirm or Fix."))
    else:
        d.update(status="generating", notes="Generating — attaches P0")
    docs[k] = d
for r in AM:
    if r["type"] == "TH":
        stage, flow = "talking", ["video"]
    else:
        stage, flow = ("hooks" if r["act"].startswith("Hook") else "broll"), ["image", "video"]
    notes = (f'{r["action"]} · {r["pace"]} · {r["loc"]} · {r["day"]} · {r["height"]}/{r["side"]}/{r["scale"]}'
             + (f' — {r["why"]}' if r["why"] else "") + f' · {r["layout"]} · product: {r["product"]}' + (f' · {r["ledger"]}' if r["ledger"] != "—" else ""))
    docs[r["beat"]] = dict(build="down-forwards-again", act=r["act"], stage=stage, beat=r["beat"], title=f'{r["beat"]} · {r["subject"]}',
        line=r["line"], imageModel=({"NB2": "nano_banana_2", "NBP": "nano_banana_pro", "GPT Sunburst": "gpt_image_2_5 sunburst"}.get(r["model"], r["model"])),
        model=("HeyGen Avatar V" if r["type"] == "TH" else "kling-video-v3_0_omni"), duration="pending-master", status="planned",
        flow=flow, notes=notes, updatedAt=NOW)
w = [dict(op="set", collection="generations", doc_id=f"down-forwards-again__{k}", data=v) for k, v in docs.items()]
for i in range(0, len(w), 50):
    json.dump(w[i:i+50], open(B / f"board/batch{i//50+1}.json", "w"), ensure_ascii=False)
print(len(w), "docs")
