#!/usr/bin/env python3
"""Step 6 — the three hooks (§30H): Hook 1 = the script's Scene 1 (L1), verbatim; Hooks 2–3 written here for the user's approval
(voiced only after approval, as separate files — §22U). Five cold-open concepts per hook (§30M), the strongest picked."""
import json, pathlib
HERE = pathlib.Path(__file__).parent
def s(st, li, fe, sp, fr, mk): return dict(stop=st, line=li, feel=fe, specific=sp, fresh=fr, makeable=mk)
def C(i, f1, stakes, where, turn, sc): return dict(id=i, frame1=f1, stakes=stakes, where=where, turn=turn, score=sc)
HOOKS = [
 dict(hook=1, source="script (Scene 1), verbatim",
  line='You could throw out every expensive foundation on your shelf right now, and you would not lose a thing. Because not one of them was ever going to work on your skin. And I can show you exactly why in about thirty seconds.',
  concepts=[
   C("A", "she stands square to the lens holding a plain beige foundation bottle in one hand and the closed violet FACELOVE stick in the other, two shelves of forty unlabelled bottles behind her", "every bottle behind her was a waste", "her dressing room, at the shelves", "'…not one of them was ever going to work' — her eyes flick to the shelf", s(2, 2, 2, 2, 2, 2)),
   C("B", "she pulls one bottle off the crowded shelf and drops it into a wastebasket at her feet without looking", "throwing money away", "her dressing room, at the shelves", "she turns to the lens: 'You could throw out every…'", s(2, 2, 2, 2, 2, 1)),
   C("C", "a slow slide along the row of forty bottles, each a slightly different wrong beige", "years of failed matches", "the shelf, close", "it ends on her face", s(2, 2, 1, 2, 1, 2)),
   C("D", "close on her bare tired face, then she lifts the stick into frame", "her face is the problem", "her dressing room", "the stick in frame on 'thirty seconds'", s(2, 1, 2, 1, 1, 2)),
   C("E", "a department-store beauty counter, her bag full of bottles", "another expensive purchase", "a mall beauty hall", "cut to the shelf at home", s(1, 1, 1, 1, 2, 1))],
  pick="A"),
 dict(hook=2, source="written for this build — needs your approval",
  line="I spent years blaming my skin for every foundation on this shelf. It turns out it was never my skin at all.",
  concepts=[
   C("A", "close on her fingertip running along the crowded shelf, tapping bottle after bottle, every one a slightly different wrong beige, until it stops on the last and she looks up at the lens", "years and money on the wrong shades", "along the shelf, close", "'…never my skin at all' — straight into 'I am fifty seven'", s(2, 2, 2, 2, 2, 2)),
   C("B", "her bare tired face in the hand mirror, the shelf behind her reflected", "she has blamed herself", "the hand mirror", "she lowers the mirror to the lens", s(2, 2, 2, 2, 1, 2)),
   C("C", "an armful of bottles tipped onto the white dresser", "the pile of failures", "the dresser", "she picks the stick out of the pile", s(2, 1, 1, 2, 2, 1)),
   C("D", "she shakes her head at the shelf, arms folded", "fed up", "her dressing room", "she turns to the lens", s(1, 2, 2, 1, 1, 2)),
   C("E", "a receipt pinned to the shelf edge", "what it cost", "the shelf", "the stick set beside it", s(1, 1, 1, 2, 2, 1))],
  pick="A"),
 dict(hook=3, source="written for this build — needs your approval",
  line="Watch what happens when I paint this wall with one factory color. Because this is exactly what your foundation is doing to your face.",
  concepts=[
   C("A", "low and wide: the roller drags one long stripe of flat pinkish beige up the bare warm plaster wall, plainly the wrong colour, and she turns to the lens with the roller in hand", "the wrong colour, plain as day", "the plaster wall", "'…what your foundation is doing to your face' — cut to the caked macro", s(2, 2, 2, 2, 2, 2)),
   C("B", "macro: beige paint sinking into the wall's hairline cracks", "it makes the lines worse", "the wall, macro", "the same pattern on her cheek", s(2, 2, 2, 2, 2, 1)),
   C("C", "she pops the lid off the plain paint can and holds it up beside her face", "the colour is wrong for her", "the drop cloth", "she dips the roller", s(2, 2, 1, 2, 2, 1)),
   C("D", "the paint can and the foundation bottle side by side on the drop cloth", "the same thing", "the drop cloth from above", "she picks up the bottle", s(1, 2, 1, 2, 1, 2)),
   C("E", "she stands beside the wall, arms folded, unimpressed", "a demonstration is coming", "the plaster wall", "she picks up the roller", s(1, 1, 1, 1, 1, 2))],
  pick="A"),
]
plan = json.load(open(HERE.parent / "step5/visual_plan.json"))
plan["hooks"] = [dict(hook=h["hook"], line=h["line"], concepts=h["concepts"], pick=h["pick"]) for h in HOOKS]
json.dump(plan, open(HERE / "visual_plan_hooks.json", "w"), indent=1, ensure_ascii=False)
json.dump(HOOKS, open(HERE / "hooks.json", "w"), indent=1, ensure_ascii=False)
md = ["### The three hooks (one finished video per hook: hook + the same body)", "", "| Hook | Line (voiced) | Source | Cold open (pick) |", "|---|---|---|---|"]
for h in HOOKS:
    pk = next(c for c in h["concepts"] if c["id"] == h["pick"])
    md.append(f"| HK{h['hook']} | {h['line']} | {h['source']} | **{h['pick']}** — {pk['frame1']} ({pk['where']}) |")
md += ["", "### Cold-open concepts (five per hook, scored /12)", "", "| Hook | ID | First frame | Stakes | Where | Turn | Score |", "|---|---|---|---|---|---|---|"]
for h in HOOKS:
    for c in h["concepts"]:
        md.append(f"| HK{h['hook']} | {c['id']}{' ✓' if c['id']==h['pick'] else ''} | {c['frame1']} | {c['stakes']} | {c['where']} | {c['turn']} | {sum(c['score'].values())}/12 |")
(HERE / "hooks.md").write_text("\n".join(md) + "\n")
print("ok")
