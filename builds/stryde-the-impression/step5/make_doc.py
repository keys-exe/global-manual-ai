#!/usr/bin/env python3
"""Writes ../STEP4_5.md and the Plan-board docs (board/json/doc_*.json) from act_map.json, wardrobe.md, takes.md, visual_plan.md."""
import json, math, pathlib, time, collections
HERE = pathlib.Path(__file__).parent; B = HERE.parent
rows = json.load(open(HERE / "act_map.json"))["rows"]
now = int(time.time() * 1000)
NAMES = {"N": "Hazel", "C1": "Roy", "C2": "Emma", "C3": "Dan", "C4": "Oscar", "C5": "Wendy", "X1": "Assistant", "X2": "Mum", "X3": "Lollipop lady", "X4": "Grandchildren"}
SHEET_OK = json.load(open(HERE / "wardrobe.json"))
card = {(d["day"], k): (not v.startswith("the cast-sheet outfit")) for d in SHEET_OK["days"] for k, v in d["outfits"].items()}

PROPERTY = """### Property Sheet (§30G) — Hazel and Roy's house

| # | Field | Value |
|---|---|---|
| 1 | Type and era | A Victorian gritstone through-terraced house (c. 1890) on a steep hill in a West Yorkshire mill town; the same couple for forty years |
| 2 | Shell | warm cream emulsion over old lime plaster · tall moulded Victorian skirting, white gone yellow · moulded white architraves · four-panel stripped and waxed pine doors with round brass knobs · high white ceilings with a plain cornice · original red, black and cream geometric tiles in the hall → a sage-green stair carpet with brass rods up the stairs and across the landing → oatmeal carpet in the front room and bedroom → terracotta quarry tiles in the kitchen · white-painted cast-iron column radiators · white plastic switches, slightly yellowed |
| 3 | Floor map | The front door opens straight off the hill pavement into a long, narrow hall running to the kitchen at the back. The stairs rise along the LEFT wall from just inside the door, climbing toward the back (fourteen steps, banister on the open right-hand side). The front room (dining room) is through the first door on the RIGHT. The kitchen is at the far end of the hall, and its doorway looks straight back up the hall to the front door and the foot of the stairs. Upstairs, the front bedroom faces the street |
| 4 | Orientation | The front faces north-east onto the hill: the dining room and front bedroom have cool, soft daylight. The kitchen and back yard face south-west: warm afternoon light. The hall is lit by the front-door glass, and at night by the pendant |
| 5 | Carried elements | the red-black-cream hall tiles · the sage-green stair carpet with brass rods · the row of small framed photographs up the stair wall · the brass coat hooks, oak hall table and round mirror by the door · the oak chest of drawers with the drawer that doesn't shut |
| 6 | Exterior | The house fronts straight onto the steep pavement, with gritstone terraces opposite stepping down the hill. Out of the back window: a stone-flagged yard with pots of geraniums, then the next row up the hill |
| 7 | Standing negatives | NEG-PROP (§30G) — none observed yet |

### Locations and plates (16:9, Sunburst, on the board To check)

| Plate | What | Scenes | Built against |
|---|---|---|---|
| P-HOUSE | the hall from the front door (the property plate) — the frame of both hall films | SC02, SC13, SC14 | nothing (gated first) |
| L-STAIRS | the flight from the hall, looking up | SC07, SC11 | P-HOUSE |
| L-DINING | the front room, the Sunday table | SC01 | P-HOUSE |
| L-KITCHEN | the galley kitchen, the pine table | SC06, SC10 | P-HOUSE |
| L-BEDROOM | the front bedroom, the chest of drawers | SC04, SC11 | P-HOUSE |
| L-CHEMIST | the high-street chemist, the rack of sleeves | SC03 | — |
| L-HILL | the steep street with the red pillar box in the wall halfway up (one place for July, August and September) | SC05, SC12, SC15 | — |
| L-GATE | the school gate at the top of the hill | SC09, SC15, SC16 | — |
| L-CAR | Emma's car at the gate, from the back seat | SC08 | — |
"""
SCENES = collections.OrderedDict()
for r in rows: SCENES.setdefault(r["scene"], []).append(r)
out = ["# Steps 4–5 — stryde-the-impression", "", "Manual run, Mode 4. Built against the confirmed cast. Every plate is on the Current board To check. The plan below is also on the Plan board.", "", PROPERTY]
sl = ["### Scene list (§3B acts · story days · light)", "", "| Scene | Act | Day | Place | Lines | Shots · takes | Est. | Light (K) | Music | Spine |", "|---|---|---|---|---|---|---|---|---|---|"]
for g, rs in SCENES.items():
    ls = [i for r in rs for i in r["lines"].split()]
    rng = f"{ls[0]}–{ls[-1]}" if ls else "—"
    sl.append(f"| {g} | {rs[0]['act']} | {rs[0]['story_day']} | {', '.join(dict.fromkeys(r['location'] for r in rs))} | {rng} | {len(rs)} · {len({r['take'] for r in rs})} | {round(sum(r['duration'] for r in rs))}s | {rs[0]['light']['kelvin']} | {' → '.join(dict.fromkeys(r['music'] for r in rs))} | {rs[0]['spine']} |")
tot = sum(r["duration"] for r in rows)
sl += ["", f"**{len(rows)} shots in {len({r['take'] for r in rows})} Seedance takes · about {int(tot // 60)}:{int(tot % 60):02d} estimated at the inspo's 165 wpm plus the silent beats** (the inspo runs 6:29). That's longer because our script has 911 words and many held, silent walks. Film pace, no trimming (§24L). The edit cuts between whole shots."]
am = ["### Act map (E4 rows — full fields in `step5/act_map.json`)", "", "| Beat | Take | Setup | Shot | Who | Line | What happens | s |", "|---|---|---|---|---|---|---|---|"]
for r in rows:
    am.append(f"| {r['beat']} | {r['take'].split('-')[1]} | {r['height']} {r['side']} {r['scale']} | {' '.join(r['shot'])} | {', '.join(NAMES.get(c, c) for c in r['cast'])} | {r['line_text'].replace('|', '/')} | {r['action'].replace('|', '/')} | {r['duration']} |")
# ingredients per take
TK = collections.OrderedDict()
for r in rows: TK.setdefault(r["take"], []).append(r)
ing = ["### Ingredients per take (§24H — Seedance, information only, no frames)", "", "| Take | Shots | s | Cast sheets / outfit cards | Places | Voices | Product / info |", "|---|---|---|---|---|---|---|"]
secs = 0; cards = set()
for t, rs in TK.items():
    d = rs[0]["story_day"]; cast = list(dict.fromkeys(c for r in rs for c in r["cast"]))
    who = []
    for c in cast:
        if card.get((d, c)): who.append(f"{c} + OUT-{c}-{d}"); cards.add(f"OUT-{c}-{d}")
        else: who.append(c)
    places = list(dict.fromkeys([r["location"] for r in rs] + (["P-HOUSE"] if any(r["location"] in ("L-DINING", "L-STAIRS", "L-KITCHEN", "L-BEDROOM") for r in rs) else [])))
    voices = list(dict.fromkeys(f"VOICE-{c}" for r in rs if r["speaking"] for c in r["cast"][:1]))
    prod = list(dict.fromkeys(x for r in rs for x in r["ingredients"] if x.startswith(("PRODUCT", "INFO"))))
    s = math.ceil(sum(r["duration"] for r in rs)); secs += max(4, s)
    ing.append(f"| {t} | {len(rs)} | {s} | {', '.join(who)} | {', '.join(places)} | {', '.join(voices) or '— (silent)'} | {', '.join(prod) or '—'} |")
ing += ["", f"**Before any clip:** {len(cards)} outfit cards (one per person per story day where the outfit isn't the cast sheet's, plus a face-and-hair crop, HT26), the product and info cards (PRODUCT = the photo set; INFO-WORN-WENDY, INFO-SEAT), and the §24I voice masters (one per speaking character, 9). These are made scene by scene, as each scene starts.",
        f"**Seedance spend (estimate):** {secs}s of takes × ~63 Kie cr/s ≈ **{secs * 63:,} Kie credits** for one pass (Kie balance 99,229.6). Plus the voice masters (9 × ~10 s ≈ 5,700) and the outfit and info cards (Sunburst, 2.75 Higgsfield cr each)."]
music = """### Music Register Map (§40A, Build Sheet 5c) — one family: sparse piano and low strings, a soft pulse

| Register | Scenes | Feel | Rule |
|---|---|---|---|
| MUS-OPEN | SC01–SC02 (the hook and the first ~90 s) | investigative-documentary curiosity: a low drone, a slow pulse, a few unresolved piano notes | never sad, never cute |
| MUS-EXPOSE | SC03–SC08 | darker, sparse: the failed fixes, the hill, the car | never mournful (`NEG-SAD`) |
| MUS-EDU | SC09 to SH12 (Wendy explains) | inquisitive, a ticking pulse | — |
| MUS-TURN | **from SC09-SH13, the product's first frame (Wendy's hem)** through SC11 | the release: the theme's first full statement | `product_at` = SC09-SH13 ±0.25 s |
| MUS-AFTER | SC12–SC15 | warm, hopeful, the theme in full; never cute | — |
| MUS-OFFER | SC16 (the close) | confident, resolved, under her voice | — |

Composed at the edit with `music.py plan --register` → `compose` → `check` (I listen first), then put on the board To check.
"""
flags = """### Flags carried from steps 1–3 (applied as recommended — you said "CONFIRMED ALL PROCEED")

- **F11:** the strap goes on in the bedroom in her nightdress (bare knee, front-on insert SC11-SH01). Trousers go on over it off screen. On the stairs she's dressed and the strap is never seen. The A/B test (SC11-SH04/SH05) takes the strap off and puts it back on off screen in the bedroom: never shown sliding down, never with trousers pushed up round it (FP10, FP13).
- **F10:** on the stairs, the banister is held on the first two steps only (the script). Every other stairs shot has her hands free.
- **F13:** right knee throughout. **F15:** the close is to camera without the product in hand. **F12:** one hook → one film.
- F1, F2, F3, F6, F7 stay voiced as written. Tell me if the advertiser wants any line changed.

### Checks

`takes.py` PASS (148 shots, 52 takes) · `angles.py` PASS (angles, shot library, focus, light) · `wardrobe.py` PASS (11 story days) · `visual_plan.py` PASS (hook 5 concepts, pick A 12/12; 16 picture rows, one hero per scene).
"""
doc = "\n".join(out + sl + [""] + [music] + ing + [""] + [flags] + am) + "\n\n" + (HERE / "takes.md").read_text() + "\n" + (HERE / "wardrobe.md").read_text() + "\n" + (HERE / "visual_plan.md").read_text()
(B / "STEP4_5.md").write_text(doc)
def D(name, title, order, md_secs, source):
    return {"title": title, "step": 5 if order > 2 else 4, "order": order, "source": source, "build": "stryde-the-impression", "updatedAt": now, "sections": md_secs}
def split_md(md):
    secs = []
    for ch in md.split("\n### "):
        ch = ch.strip().lstrip("#").strip()
        if not ch: continue
        t, _, body = ch.partition("\n"); secs.append({"title": t.strip(), "md": body.strip()})
    return secs
bj = B / "board/json"
docs = {"property": D("property", "Property & locations", 2, split_md(PROPERTY), "builds/stryde-the-impression/STEP4_5.md"),
        "actmap": D("actmap", "Scene list & act map", 3, [{"title": "Scene list", "md": "\n".join(sl[2:])}, {"title": "Act map", "md": "\n".join(am[2:])}], "builds/stryde-the-impression/step5/act_map.json"),
        "takes": D("takes", "Takes (one Seedance call each)", 4, split_md((HERE / "takes.md").read_text()), "builds/stryde-the-impression/step5/takes.md"),
        "wardrobe": D("wardrobe", "Wardrobe map — by story day", 5, split_md((HERE / "wardrobe.md").read_text()), "builds/stryde-the-impression/step5/wardrobe.md"),
        "visualplan": D("visualplan", "Visual pitch", 6, split_md((HERE / "visual_plan.md").read_text()), "builds/stryde-the-impression/step5/visual_plan.md"),
        "music": D("music", "Music register map", 7, split_md(music), "builds/stryde-the-impression/STEP4_5.md"),
        "ingredients": D("ingredients", "Ingredients per take", 8, [{"title": "Ingredients per take", "md": "\n".join(ing[2:])}], "builds/stryde-the-impression/STEP4_5.md")}
for k, v in docs.items(): json.dump(v, open(bj / f"doc_{k}.json", "w"), ensure_ascii=False)
print("STEP4_5.md", len(doc), "chars ·", len(cards), "outfit cards ·", secs, "s ·", {k: len(json.dumps(v)) for k, v in docs.items()})
