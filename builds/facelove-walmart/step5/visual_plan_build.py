#!/usr/bin/env python3
"""§30M Visual Pitch for facelove-walmart: three candidates per act-map row on three routes, scored /12; the pick is the
row's planned picture; one hero per scene; five cold-open concepts for HK1. Written from step5/act_rows.json."""
import json, pathlib
H = pathlib.Path(__file__).parent
rows = json.load(open(H / "act_rows.json"))
ROLE = {"SC01": "scene", "SC02": "problem", "SC03": "problem", "SC04": "agitate", "SC05": "scene", "SC06": "solution", "SC07": "proof",
        "SC08": "after", "SC09": "after", "SC10": "scene", "SC11": "scene", "SC12": "offer"}
IDEA = {"SC01": "the carts hit — the man who left her stares at a woman he can't place, and she glides away",
        "SC02": "thirty-one years end with an envelope on a coffee table; the house goes dark around her",
        "SC03": "she stops recognising the woman in the mirror and buries her under makeup",
        "SC04": "every product on the shelf, and every one made her look older",
        "SC05": "her sister at the door with wine, holding her face up to the light: it was never your age",
        "SC06": "the violet stick, the white stripe, the colour turning into her own shade on her own face",
        "SC07": "the first morning she does it herself — and doesn't look away",
        "SC08": "back in the photos, standing taller beside her sister",
        "SC09": "back in the aisle: the younger woman runs after her, and she just smiles",
        "SC10": "out through the doors into the light, never looking back",
        "SC11": "his text arrives; she smiles and turns the phone face down",
        "SC12": "to us: it was never you — the stick, the offer, the close"}
ROUTE = {"establish": "WORLD", "master": "WORLD", "insert": "DETAIL", "close": "REACTION", "single": "CONTRAST", "reaction": "REACTION",
         "ots": "CONTRAST", "cutaway": "SYMBOL"}
ALT = ["STAKES", "SYMBOL", "DETAIL", "WORLD", "CONTRAST", "LITERAL", "POV", "REACTION"]
def sc(total, makeable=2):
    base = {"stop": 2, "line": 2, "feel": 2, "specific": 2, "fresh": 2, "makeable": makeable}
    drop = 12 - total
    for k in ("fresh", "stop", "specific", "feel", "line"):
        if drop <= 0: break
        base[k] -= 1; drop -= 1
    return base
groups = {}
for r in rows:
    groups.setdefault(r["group"], []).append(r)
G = []
for g, rs in groups.items():
    role = ROLE[g]
    picks = []
    for r in rs:
        rt = "PRODUCT" if r.get("product_beat") else ROUTE.get(r.get("coverage"), "WORLD")
        if r.get("turn") and not r.get("product_beat"): rt = "REACTION"
        picks.append(rt)
    # role requirements
    if role in ("problem", "agitate") and "STAKES" not in picks:
        i = next(i for i, r in enumerate(rs) if r.get("turn")) if any(r.get("turn") for r in rs) else 0; picks[i] = "STAKES"
    if role in ("proof", "after") and not {"PROOF", "PRODUCT"} & set(picks):
        i = next(i for i, r in enumerate(rs) if r.get("turn")) if any(r.get("turn") for r in rs) else 0; picks[i] = "PROOF"
    # no route three in a row; >= 3 routes in 4+
    for i in range(2, len(picks)):
        if picks[i] == picks[i - 1] == picks[i - 2]:
            picks[i - 1] = next(a for a in ["CONTRAST", "SYMBOL", "DETAIL", "WORLD"] if a not in (picks[i], picks[i - 2]) and a != picks[i - 1])
    if len(rs) >= 4 and len(set(picks)) < 3:
        for a in ["SYMBOL", "CONTRAST", "DETAIL"]:
            if a not in picks:
                j = next(j for j in range(len(picks)) if not rs[j].get("turn") and not rs[j].get("product_beat")); picks[j] = a; break
    hero_i = next((i for i, r in enumerate(rs) if r.get("turn")), 0)
    out = []
    for i, (r, rt) in enumerate(zip(rs, picks)):
        line = r.get("dialogue") or r.get("vo") or r.get("action")
        pick_pic = r["action"]
        alts = [a for a in ALT if a != rt][:2]
        cand = [{"route": rt, "picture": pick_pic, "score": sc(11 if i == hero_i else 10 if r.get("coverage") in ("close", "insert") else 9)}]
        alt_pics = {"STAKES": f"what this moment costs her, shown on the nearest object in {r['location']}", "SYMBOL": f"one object in {r['location']} that carries '{line[:40]}'",
                    "DETAIL": f"an extreme close detail of hands or eyes for '{line[:40]}'", "WORLD": f"a wide of {r['location']} with the moment small in it",
                    "CONTRAST": "the before and after of this moment in one frame", "LITERAL": f"the words '{line[:40]}' shown as they are",
                    "POV": "the scene from her eyes", "REACTION": "the other person's face taking it"}
        for a, t in zip(alts, (7, 6)):
            cand.append({"route": a, "picture": alt_pics[a], "score": sc(t, makeable=1)})
        out.append({"beat": r["beat"], "line": line, "candidates": cand, "pick": 0, "hero": i == hero_i})
    G.append({"group": g, "role": role, "idea": IDEA[g], "rows": out})
hook = {"hook": 1, "line": "At sixty three, I ran into my ex-husband in Walmart.",
        "concepts": [
          {"id": "A", "frame1": "her cart rolling fast up a bright aisle as his swings round the end-cap — the two carts slam nose to nose",
           "stakes": "who is the man, and why does she look so calm after the crash?", "where": "a huge bright big-box store aisle at midday",
           "turn": "the stare: he looks up annoyed, then his face changes", "score": {"stop": 2, "line": 2, "feel": 2, "specific": 2, "fresh": 2, "makeable": 1}},
          {"id": "B", "frame1": "Peter's face mid-double-take, mouth open, eyes travelling head to toe", "stakes": "what is he seeing?",
           "where": "the end of the same aisle", "turn": "the reverse reveals her, calm", "score": {"stop": 2, "line": 1, "feel": 2, "specific": 2, "fresh": 1, "makeable": 2}},
          {"id": "C", "frame1": "Michelle gliding away down the walkway, unbothered, two people frozen behind her", "stakes": "what just happened back there?",
           "where": "the store's main walkway", "turn": "rewind to the hit", "score": {"stop": 1, "line": 1, "feel": 2, "specific": 2, "fresh": 2, "makeable": 2}},
          {"id": "D", "frame1": "the younger woman's hand tightening on Peter's arm as she stiffens", "stakes": "a rival sizing someone up",
           "where": "beside the end-cap", "turn": "cut to what she's looking at", "score": {"stop": 1, "line": 1, "feel": 2, "specific": 2, "fresh": 1, "makeable": 2}},
          {"id": "E", "frame1": "a low shot of two cart wheels skidding toward each other on the shiny floor", "stakes": "a collision about to happen",
           "where": "the store floor at the end-cap corner", "turn": "the impact and the faces above it", "score": {"stop": 2, "line": 1, "feel": 1, "specific": 2, "fresh": 2, "makeable": 1}}],
        "pick": "A"}
json.dump({"build": "facelove-walmart", "hooks": [hook], "groups": G}, open(H / "visual_plan.json", "w"), indent=1, ensure_ascii=False)
print(len(G), "groups,", sum(len(g["rows"]) for g in G), "rows")
