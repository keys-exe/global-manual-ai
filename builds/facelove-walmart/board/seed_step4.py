"""Step-4 cards on the Current board: 7 plates (stage locations) + 2 product info cards + the 3 product photos (ingredients)."""
import json, time, pathlib, os
os.chdir(pathlib.Path(__file__).resolve().parents[1])
B = "facelove-walmart"; now = int(time.time()*1000); R = json.load(open("plates/renders.json"))
A = {"P-HOUSE": "ed03b3f201fadd1d5c03bbcc32173be1", "L-LIVING": "7067c5e226ccbd02e0405a3a7946a579", "L-VANITY": "69794936cba0a1e3b7b72e21b440cf57",
     "L-PATIO": "9f431017ccc05ddc772f746ae560b1aa", "L-AISLE": "7a447d47877fde73f8c2a7c94bf29d30", "L-AISLE-REV": "540831542b5ddd7e7ffd543b0dc72b3b",
     "L-STORE-DOORS": "175a8107e1ac93997d11c9e2280e4568", "PROD-HAND-CARD": "4ced2ec649c6717301a7d14ba075f9dd", "COLOUR-FRONT-CARD": "1f00de80684bf6818e6e4a3e198500fa"}
PH = {"PROD-CLOSED": ("9de410b9e5a631acf42f610060a16234", "CLOSED.jpg", "The stick, closed — your product photo (canonical, attachable)"),
      "PROD-BALM": ("5e1de0c7805f8c2c0d37aac0b0690f2d", "BALM_END_DEPLOYED.jpg", "The balm end open — your product photo (canonical, attachable)"),
      "PROD-BRUSH": ("d9938847ff4944a03efcfd2146c4a9d1", "BRUSH_END_DEPLOYED.jpg", "The brush end open — your product photo (canonical, attachable)")}
T = {"P-HOUSE": "Michelle's house — the entry hall and front door (property plate; The Sister, The Reveal)",
     "L-LIVING": "The living room — the armchair, the coffee table, the archway to the front door (The Divorce)",
     "L-VANITY": "Her bedroom vanity and mirror (The Undoing, Nothing Worked, The Change)",
     "L-PATIO": "Her back patio, morning sun (The Epilogue, CTA)",
     "L-AISLE": "The store aisle — looking to the corner where the carts hit (Hook, The Payoff)",
     "L-AISLE-REV": "The same aisle from the walkway — the reverse (Hook, The Payoff)",
     "L-STORE-DOORS": "The store's sliding doors into golden light (The Epilogue)",
     "PROD-HAND-CARD": "Info card — the closed violet stick in Rosa's hand, true size (Rosa draws it from her bag)",
     "COLOUR-FRONT-CARD": "Info card — the colour front: white ahead of the brush, her own shade behind, every line kept (The Reveal)"}
LINE = {"PROD-HAND-CARD": "(info) the stick is a little longer than her hand is wide; held low, the wordmark clear; photoreal in the animated world (PIX-SPLIT)",
        "COLOUR-FRONT-CARD": "(info) white ahead of the brush, matched behind; the lines stay exactly as deep (TERRAIN_LOCK)"}
REFS = {"L-LIVING": ["P-HOUSE"], "L-VANITY": ["P-HOUSE"], "L-PATIO": ["P-HOUSE"], "L-AISLE-REV": ["L-AISLE"], "L-STORE-DOORS": ["L-AISLE"]}
CREFS = {"PROD-HAND-CARD": [("PROD-CLOSED", "Image 1 · the closed stick", "product"), ("C3-ROSA", "Image 2 · Rosa — hand and skin tone", "character")],
         "COLOUR-FRONT-CARD": [("N-MICHELLE-AFTER", "Image 1 · Michelle — face and skin tone", "character"), ("PROD-BRUSH", "Image 2 · the brush end", "product")]}
docs = {}
for k, a in A.items():
    card = k.endswith("CARD"); d = "cards" if card else "plates"
    p = pathlib.Path(f"{d}/{k}.prompt.txt").read_text(); size = pathlib.Path(f"{d}/{k}_v1.png").stat().st_size
    refs = ([{"label": f"{r} plate", "role": "Image 1 · the same place", "kind": "location", "ref": f"{B}__{r}"} for r in REFS.get(k, [])] if not card else
            [{"label": r, "role": role, "kind": kind, "ref": f"{B}__{r}"} for r, role, kind in CREFS[k]])
    docs[k] = {"build": B, "act": "Product" if card else "Locations", "stage": "broll" if card else "locations", "beat": k, "title": T[k], "line": LINE.get(k, ""),
               "imagePrompt": p, "imageModel": "nano_banana_pro (logged nano_banana_2) · 2k · " + ("9:16" if card else "16:9"),
               "imageStatus": "review", "status": "review", "imageRegens": 0, "imageAsset": a, "imageType": "image/png", "imageConnector": "Higgsfield",
               "imageUrl": R["urls"][k], "imageJob": R["jobs"][k], "imageRes": "1536×2752" if card else "2752×1536", "imageCredits": 2, "imageAt": now, "updatedAt": now,
               "flow": ["image"], "imageRefs": refs,
               "imageVersions": [{"v": 1, "asset": a, "type": "image/png", "url": R["urls"][k], "model": "nano_banana_pro (logged nano_banana_2)", "connector": "Higgsfield",
                                  "credits": 2, "size": size, "at": now, "note": ""}]}
for k, (a, f, t) in PH.items():
    docs[k] = {"build": B, "act": "Product", "stage": "broll", "beat": k, "title": t, "line": "(info) the advertiser's own photo — layer 1 (§7)", "imageStatus": "confirmed", "status": "use",
               "imageAsset": a, "imageType": "image/jpeg", "imageConnector": "client", "imageCredits": 0, "imageAt": now, "updatedAt": now, "flow": ["image"],
               "imageVersions": [{"v": 1, "asset": a, "type": "image/jpeg", "model": "client photo", "connector": "client", "credits": 0, "at": now, "note": "supplied"}]}
out = pathlib.Path("board/json"); json.dump(docs, open(out / "step4_docs.json", "w"), ensure_ascii=False)
json.dump([{"op": "set", "collection": "generations", "doc_id": f"{B}__{k}", "file_path": str((out / f"gen_{k}.json").resolve())} for k in docs], open(out / "step4_batch.json", "w"))
for k, d in docs.items(): json.dump(d, open(out / f"gen_{k}.json", "w"), ensure_ascii=False)
print(len(docs))
