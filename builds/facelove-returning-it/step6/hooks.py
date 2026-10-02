#!/usr/bin/env python3
"""Step 6 — the three hooks (§30H): Hook 1 = the script's Scene 1, verbatim; Hooks 2–3 written here for the user's approval
(voiced only after approval, as separate files — §22U). Five cold-open concepts per hook (§30M), the strongest picked."""
import json, pathlib
HERE = pathlib.Path(__file__).parent
def s(st, li, fe, sp, fr, mk): return dict(stop=st, line=li, feel=fe, specific=sp, fresh=fr, makeable=mk)
def C(i, f1, stakes, where, turn, sc): return dict(id=i, frame1=f1, stakes=stakes, where=where, turn=turn, score=sc)
HOOKS = [
 dict(hook=1, source="script (Scene 1 · Cold-Open Hook), verbatim",
  line="I am so mad, and this is exactly why you read the reviews before you buy another foundation. Because I bought this FACELOVE stick that everyone would not stop raving about, and I am going to be returning it.",
  concepts=[
   C("A", "her bare, red-cheeked face close to the lens, the FACELOVE carton held up beside it and tapped twice, sticker 'I'm so mad 😡'", "she is furious at a product everyone loves", "her vanity, late afternoon", "'…and I am going to be returning it' — the carton drops into a return mailer", s(2, 2, 2, 2, 1, 2)),
   C("B", "the return mailer slapped down on the white vanity, the carton dropped into it from above", "the product is already going back", "her vanity top from above", "cut up to her cross face for the first line", s(2, 2, 1, 2, 2, 2)),
   C("C", "close on her red cheek, one finger pointing at the redness", "the problem she has lived with", "her vanity mirror", "the stick enters frame", s(2, 1, 2, 2, 1, 2)),
   C("D", "she walks out of a department store beauty hall, shopping bag swinging, jaw set", "another wasted purchase", "a mall beauty hall", "cut to her at home, still mad", s(1, 1, 1, 1, 2, 1)),
   C("E", "a pile of half-used foundation bottles swept off the vanity into a bin", "years of money on the wrong shades", "her vanity", "she holds up the one stick she is 'returning'", s(2, 1, 2, 2, 2, 1))],
  pick="A"),
 dict(hook=2, source="written for this build — needs your approval",
  line="Okay, I need to vent. I finally found a foundation that actually matches my redness, and I am sending it back. Here is why.",
  concepts=[
   C("A", "screech of tape: her hands tape shut a grey return mailer with the FACELOVE carton inside, then she looks straight up at the lens", "she's sending back the one that worked", "her vanity, hands and face", "'Here is why.' — straight into the body", s(2, 2, 2, 2, 2, 2)),
   C("B", "half her face: one cheek even, the other still red, she points at both", "it worked — so why return it?", "her vanity", "'and I am sending it back'", s(2, 2, 2, 2, 1, 2)),
   C("C", "she rolls her eyes and drops into the vanity chair, bare-faced", "she has had enough", "her bedroom", "she lifts the stick to the lens", s(1, 1, 2, 1, 1, 2)),
   C("D", "a post-office counter, the parcel slid across", "it is really going back", "a post office", "flash back to her vanity", s(1, 2, 1, 1, 2, 1)),
   C("E", "close on the stick in her fist, knuckles tight", "the anger is real", "her vanity", "she opens her hand", s(1, 1, 2, 1, 1, 2))],
  pick="A"),
 dict(hook=3, source="written for this build — needs your approval",
  line="Every makeup counter told me nothing would ever match my redness. So why am I returning the one stick that finally did?",
  concepts=[
   C("A", "over the saleswoman's shoulder at the makeup counter: a bottle held to her red jaw, three wrong swatches, a slow head shake", "the experts gave up on her skin", "the department-store makeup counter", "cut to her at home holding the stick: 'So why am I returning…'", s(2, 2, 2, 2, 2, 2)),
   C("B", "macro: the white balm laid across her red cheek, the brush turning it to her exact shade", "proof it did what the counter said was impossible", "her vanity", "her face, puzzled at her own question", s(2, 2, 1, 2, 1, 2)),
   C("C", "a row of wrong-shade bottles on the counter, each one too pink or too orange against her jaw", "every match failed", "the makeup counter", "the stick against her jaw — perfect", s(2, 2, 1, 2, 2, 1)),
   C("D", "she shrugs at the lens holding the stick, eyebrows up", "the puzzle", "her vanity", "the body explains", s(1, 2, 1, 1, 1, 2)),
   C("E", "a shopping bag of returned foundations on the bed", "years of failed matches", "her bedroom", "the one she's returning now", s(1, 1, 1, 1, 2, 1))],
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
