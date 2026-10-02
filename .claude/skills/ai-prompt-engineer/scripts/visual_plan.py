#!/usr/bin/env python3
"""§30M — the Visual Pitch: check that every hook, act and scene shows its strongest picture (V7.85.0).

Usage:
  visual_plan.py PLAN.json [--md visual_plan.md] [--json]

PLAN.json:
{
  "build": "stryde-x",
  "hooks": [ {"hook": 1, "line": "the hook's opening line",
              "concepts": [ {"id": "A", "frame1": "what is seen in the first half-second",
                             "stakes": "what is at risk / the question it opens", "where": "out in the world: a station platform",
                             "turn": "how it lands on the next line",
                             "score": {"stop": 2, "line": 2, "feel": 2, "specific": 2, "fresh": 1, "makeable": 2}}, ... ],
              "pick": "A"} ],
  "groups": [ {"group": "Act 1" | "SC-02", "role": "problem" | "agitate" | "mechanism" | "solution" | "proof" | "after" | "offer" | "scene",
               "idea": "one sentence: what this act / scene is about in pictures",
               "rows": [ {"beat": "B-04", "line": "the phrase (§27)",
                          "candidates": [ {"route": "STAKES", "picture": "one concrete picture",
                                           "score": {"stop": 2, "line": 2, "feel": 2, "specific": 2, "fresh": 2, "makeable": 1}}, ... ],
                          "pick": 0, "hero": false}, ... ]} ]
}

Routes: LITERAL (the noun itself) · STAKES (what it costs, the moment it fails) · PROOF (seen to be true in 3 s) ·
CONTRAST (two states, one subject) · DETAIL (an extreme close detail that tells it) · REACTION (a face taking the news) ·
WORLD (out in the world, people around, public stakes) · MECHANISM (§12A) · SYMBOL (a real object that carries the idea:
the unused walking shoes by the door) · POV (in the viewer's place, sparingly) · PRODUCT (the product doing its job, §30B).

Score: six criteria, 0–2 each, /12 — STOP (reads in half a second at phone size and makes you look), LINE (shows what
the line says, its key word visible), FEEL (carries the line's emotion and stakes), SPECIFIC (particular, concrete
details — never stock), FRESH (new against the rows before it), MAKEABLE (the model can make it right first time:
§27G motion, House Taste). MAKEABLE 0 is never picked.

Checks (any FAIL -> exit 1):
  ROW      every row: >= 3 candidates on >= 3 different routes; every criterion scored 0-2; the pick is the top total
           (ties allowed); the pick scores >= 9 and MAKEABLE >= 1; no generic stock wording in the pick
  ACT      a group of 4+ rows uses >= 3 routes; LITERAL on <= 30% of its picks; no route three picks in a row;
           exactly one hero shot (the act's or scene's strongest picture, total >= 10); problem / agitate groups
           pick STAKES at least once; proof / after groups pick PROOF or PRODUCT at least once
  HOOK     every hook: >= 5 concepts, each with frame1, stakes and where; the pick is the top total, >= 10,
           STOP = 2; the hooks' picked concepts are all different (where and frame1)
"""
import argparse, json, re, sys
from collections import Counter
from pathlib import Path

ROUTES = {"LITERAL", "STAKES", "PROOF", "CONTRAST", "DETAIL", "REACTION", "WORLD", "MECHANISM", "SYMBOL", "POV", "PRODUCT"}
CRIT = ("stop", "line", "feel", "specific", "fresh", "makeable")
GENERIC = re.compile(r"\b(smil(?:e|es|ing)|happy (?:woman|man|person|couple)|stock|beautiful|generic|lifestyle shot|"
                     r"looks? (?:at|into) the camera happily|thumbs? up|a person|someone|people (?:walking|talking)|"
                     r"nice|great|amazing|feels good)\b", re.I)
ROW_MIN, HERO_MIN, HOOK_MIN = 9, 10, 10


def total(c):
    s = c.get("score") or {}
    return sum(int(s.get(k, 0)) for k in CRIT)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("plan")
    ap.add_argument("--md")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    plan = json.loads(Path(a.plan).read_text())
    out = []

    def fail(kind, where, detail):
        out.append({"check": kind, "where": where, "detail": detail})

    def scored(c, where):
        s = c.get("score") or {}
        bad = [k for k in CRIT if not isinstance(s.get(k), int) or not 0 <= s[k] <= 2]
        if bad:
            fail("ROW", where, f"score missing or not 0-2 on {', '.join(bad)}")

    for g in plan.get("groups", []):
        gid, rows, picks = g.get("group", "?"), g.get("rows", []), []
        for r in rows:
            where = f"{gid} · {r.get('beat', '?')}"
            cs = r.get("candidates", [])
            for c in cs:
                scored(c, where)
            routes = {c.get("route") for c in cs}
            if len(cs) < 3 or len(routes) < 3:
                fail("ROW", where, f"{len(cs)} candidates on {len(routes)} routes — write three pictures on three different routes")
            unknown = routes - ROUTES
            if unknown:
                fail("ROW", where, f"unknown route(s) {sorted(x for x in unknown if x)}")
            p = r.get("pick")
            if not isinstance(p, int) or not 0 <= p < len(cs):
                fail("ROW", where, "no pick"); continue
            c = cs[p]; picks.append((r, c))
            best = max(total(x) for x in cs)
            if total(c) < best:
                fail("ROW", where, f"pick scores {total(c)}/12 but a candidate scores {best}/12 — pick the strongest or say why in the score")
            if total(c) < ROW_MIN:
                fail("ROW", where, f"the best picture scores {total(c)}/12 (< {ROW_MIN}) — write stronger candidates")
            if int((c.get("score") or {}).get("makeable", 0)) < 1:
                fail("ROW", where, "the pick is not makeable (MAKEABLE 0)")
            m = GENERIC.search(c.get("picture", ""))
            if m:
                fail("ROW", where, f"generic stock wording in the pick: {m.group(0)!r} — say the particular thing")
        if not picks:
            continue
        pr = [c.get("route") for _, c in picks]
        if len(picks) >= 4:
            if len(set(pr)) < 3:
                fail("ACT", gid, f"{len(set(pr))} route(s) across {len(picks)} pictures — use at least three")
            lit = pr.count("LITERAL")
            if lit * 10 > len(pr) * 3:
                fail("ACT", gid, f"LITERAL on {lit}/{len(pr)} pictures — at most 30%: the noun itself is the weakest picture")
        for i in range(2, len(pr)):
            if pr[i] == pr[i - 1] == pr[i - 2]:
                fail("ACT", gid, f"{pr[i]} three pictures in a row ({', '.join(r.get('beat', '?') for r, _ in picks[i - 2:i + 1])})")
        heroes = [(r, c) for r, c in picks if r.get("hero")]
        if len(heroes) != 1:
            fail("ACT", gid, f"{len(heroes)} hero shots — mark exactly one: the picture this act or scene is remembered for")
        elif total(heroes[0][1]) < HERO_MIN:
            fail("ACT", gid, f"hero shot {heroes[0][0].get('beat')} scores {total(heroes[0][1])}/12 (< {HERO_MIN})")
        role = g.get("role", "")
        if role in ("problem", "agitate") and "STAKES" not in pr:
            fail("ACT", gid, "a problem act with no STAKES picture — show what it costs, the moment it fails")
        if role in ("proof", "after") and not ({"PROOF", "PRODUCT"} & set(pr)):
            fail("ACT", gid, "an after / proof act with no PROOF or PRODUCT picture — show it working, seen to be true")

    seen = Counter()
    for h in plan.get("hooks", []):
        where = f"Hook {h.get('hook', '?')}"
        cs = h.get("concepts", [])
        for c in cs:
            scored(c, where)
            for k in ("frame1", "stakes", "where"):
                if not c.get(k):
                    fail("HOOK", where, f"concept {c.get('id')} has no {k}")
        if len(cs) < 5:
            fail("HOOK", where, f"{len(cs)} concepts — write five cold opens and pick the strongest")
        pick = next((c for c in cs if c.get("id") == h.get("pick")), None)
        if not pick:
            fail("HOOK", where, "no pick"); continue
        best = max(total(c) for c in cs)
        if total(pick) < best:
            fail("HOOK", where, f"pick scores {total(pick)}/12 but a concept scores {best}/12")
        if total(pick) < HOOK_MIN or int(pick["score"].get("stop", 0)) < 2:
            fail("HOOK", where, f"the pick scores {total(pick)}/12 with STOP {pick['score'].get('stop')} — a hook needs >= {HOOK_MIN} and STOP 2")
        m = GENERIC.search(pick.get("frame1", ""))
        if m:
            fail("HOOK", where, f"generic stock wording in the first frame: {m.group(0)!r}")
        seen[(pick.get("where", "").lower(), pick.get("frame1", "").lower())] += 1
    if any(n > 1 for n in seen.values()):
        fail("HOOK", "hooks", "two hooks open on the same place and first frame — each hook is its own way in")

    if a.md:
        md = ["### Visual plan", "", "The strongest picture for every line, picked from three (hooks from five). "
              "Scores out of 12: stop · line · feel · specific · fresh · makeable.", ""]
        for h in plan.get("hooks", []):
            md += [f"### Hook {h.get('hook')} — {h.get('line', '')}", "", "| | First frame | Stakes | Where | Score |", "|---|---|---|---|---|"]
            for c in sorted(h.get("concepts", []), key=lambda c: -total(c)):
                mark = "**▶ picked**" if c.get("id") == h.get("pick") else c.get("id", "")
                md.append(f"| {mark} | {c.get('frame1', '')} | {c.get('stakes', '')} | {c.get('where', '')} | {total(c)}/12 |")
            md.append("")
        for g in plan.get("groups", []):
            md += [f"### {g.get('group')} — {g.get('idea', '')}", "", "| Beat | Line | Picked | Route | Score | Also considered |", "|---|---|---|---|---|---|"]
            for r in g.get("rows", []):
                cs = r.get("candidates", []); p = r.get("pick", 0)
                if not cs or not isinstance(p, int) or p >= len(cs):
                    continue
                c = cs[p]
                alts = " · ".join(f"{x.get('route')}: {x.get('picture', '')} ({total(x)})" for i, x in enumerate(cs) if i != p)
                hero = " ★ hero" if r.get("hero") else ""
                md.append(f"| {r.get('beat')}{hero} | {r.get('line', '')} | {c.get('picture', '')} | {c.get('route')} | {total(c)}/12 | {alts} |".replace("\n", " "))
            md.append("")
        Path(a.md).write_text("\n".join(md), encoding="utf-8")

    if a.json:
        print(json.dumps({"pass": not out, "fails": out}, indent=1))
    else:
        for f in out:
            print(f"FAIL  {f['check']:5} {f['where']}  — {f['detail']}")
        print("VISUAL PLAN PASS" if not out else f"VISUAL PLAN FAIL ({len(out)})")
    sys.exit(1 if out else 0)


if __name__ == "__main__":
    main()
