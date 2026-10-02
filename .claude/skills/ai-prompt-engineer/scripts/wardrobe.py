#!/usr/bin/env python3
"""§21 / §14A — the wardrobe map is per story day and its events, never per act (V7.89.0).

User, 2026-10-02: "the wardrobe map too — it should not be per act, it should be per day / event."
An act is a section of the edit; a day is time in the story. The clothes follow the day (B-roll, film) and the
recording day (talking heads), never the act.

Usage:
  wardrobe.py ACT_MAP.json WARDROBE.json [--md wardrobe.md] [--json]

ACT_MAP.json: the step-5 act map — a list of rows, or {"rows": [...]}; each row with people in it carries
`story_day` and `cast` (or `subject`). Talking-head rows (`type` TH) are matched to `talking_heads`.

WARDROBE.json:
{
  "days": [ {"day": "B3", "event": "the evening after the physio — the drawer, the phone call",
             "source": "stated: 'that night'" | "event: the wedding" | "contrast: the before" | ...,
             "outfits": {"N": "slate-grey cardigan, cream blouse, navy knee-length skirt", "C3": "..."},
             "events": [ {"id": "B3-E1", "location": "L-BEDROOM", "visibility": "VISIBLE", "beats": ["SC03-SH06", ...]} ]},
            ... ],                                   # in story order
  "talking_heads": [ {"day": "H-D1", "subject": "H", "outfit": "...", "beats": ["TH-01", ...]} ]   # one per recording day
}
The older shape {"<person>": {"<day>": "<outfit>"}} is read too; its days then have no event or source (SOURCE fails).

Checks (any FAIL -> exit 1):
  ACT     no day id is an act or hook section ("Act 2", "Hook 1"); no source is the act ("act boundary", "Act 3")
  SOURCE  every day names its event and its source — the line or fact that makes it a day
  COVER   every act-map row with people has a story_day that is on the map — a day, or an event id of a day (the event
          wears its day's outfit) — with an outfit for each person in it
  BEATS   every beat on a day's event lines is on the act map, and its row's story_day is that day
  TH      talking heads keyed by recording day (never an act); one outfit per subject per recording day; every TH row's
          beat on one of them
"""
import argparse, json, re, sys
from pathlib import Path

ACT_ID = re.compile(r"^\s*(?:act|hook)[\s_-]*\d+\b", re.I)
ACT_SRC = re.compile(r"\bact\s*\d+\b|\bact boundar(?:y|ies)\b|\bper act\b|\bone (?:story )?day per act\b|^\s*act\b", re.I)


def load_days(w):
    if isinstance(w, dict) and "days" in w:
        return w.get("days") or [], w.get("talking_heads") or []
    days = {}
    for person, by_day in (w or {}).items():   # older shape: {person: {day: outfit}}
        if not isinstance(by_day, dict):
            continue
        for d, outfit in by_day.items():
            days.setdefault(d, {"day": d, "outfits": {}})["outfits"][person] = outfit
    return list(days.values()), []


def people(r):
    c = r.get("cast")
    if isinstance(c, list) and c:
        return [x for x in c if x]
    s = str(r.get("subject") or "")
    if not s or s.upper().startswith(("ANAT", "MECH", "PRODUCT", "-", "—")):
        return []
    # "S2 + S1", "S1 hands", "G-01 hands" -> the cast ids
    ids = [re.match(r"\s*([A-Z]+-?\d+[a-z]?)\b", part) for part in re.split(r"[+,&/]", s)]
    return [m.group(1) for m in ids if m]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("actmap")
    ap.add_argument("wardrobe")
    ap.add_argument("--md")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    am = json.loads(Path(a.actmap).read_text())
    rows = am if isinstance(am, list) else am.get("rows", [])
    days, ths = load_days(json.loads(Path(a.wardrobe).read_text()))
    out = []

    def fail(kind, where, detail):
        out.append({"check": kind, "where": where, "detail": detail})

    by_day = {}
    for d in days:
        did = str(d.get("day", "")).strip()
        if not did:
            fail("SOURCE", "?", "a day with no id"); continue
        by_day[did] = d
        if ACT_ID.search(did):
            fail("ACT", did, "a day named after an act or hook — name the day by the story (the wedding, last Sunday), never the edit section")
        if not str(d.get("event") or "").strip():
            fail("SOURCE", did, "no event — say what this day is in the story (\"the wedding, June evening\")")
        src = str(d.get("source") or "").strip()
        if not src:
            fail("SOURCE", did, "no source — the line or fact that makes it a day (stated · event · contrast · timeframe · ownership)")
        elif ACT_SRC.search(src):
            fail("ACT", did, f"source {src!r} is the act — a day comes from the script's events, never from an act boundary")

    # a row's story_day may name a day or one of its events (B3d = the drawer, on day B3): the event wears its day's outfit
    alias = {str(ev.get("id")): did for did, d in by_day.items() for ev in d.get("events") or [] if ev.get("id")}
    beat_row = {r.get("beat"): r for r in rows if r.get("beat")}
    for r in rows:
        if str(r.get("type", "")).upper() == "TH":
            continue
        ps = people(r)
        if not ps:
            continue
        b = r.get("beat", "?")
        sd = r.get("story_day")
        if not sd:
            fail("COVER", b, "row with people and no story_day"); continue
        d = by_day.get(str(sd)) or by_day.get(alias.get(str(sd), ""))
        if not d:
            fail("COVER", b, f"story day {sd} is not on the wardrobe map — add the day, or list it as an event of its day"); continue
        miss = [p for p in ps if p not in (d.get("outfits") or {})]
        if miss:
            fail("COVER", b, f"no outfit on day {sd} for {', '.join(miss)}")

    for did, d in by_day.items():
        for ev in d.get("events") or []:
            for b in ev.get("beats") or []:
                r = beat_row.get(b)
                if not r:
                    fail("BEATS", f"{did} · {ev.get('id', '?')}", f"{b} is not on the act map")
                elif r.get("story_day") and str(r.get("story_day")) != did and alias.get(str(r.get("story_day"))) != did:
                    fail("BEATS", f"{did} · {ev.get('id', '?')}", f"{b} is on day {r.get('story_day')} in the act map")

    seen, th_beats = {}, set()
    for t in ths:
        td, sj = str(t.get("day", "")).strip(), t.get("subject", "?")
        if not td or ACT_ID.search(td) or ACT_SRC.search(td):
            fail("TH", f"{sj} · {td or '?'}", "talking heads are keyed by recording day (one sitting), never by act")
        if (sj, td) in seen:
            fail("TH", f"{sj} · {td}", "two outfits for one recording day — one sitting, one outfit")
        seen[(sj, td)] = t
        th_beats |= set(t.get("beats") or [])
    for r in rows:
        if str(r.get("type", "")).upper() == "TH" and ths and r.get("beat") not in th_beats:
            fail("TH", r.get("beat", "?"), "talking-head row on no recording day")

    if a.md:
        md = ["### Wardrobe map — per story day and event", "",
              "One outfit per person per story day, in story order; each day's event and what makes it a day. Never grouped by act (§21, V7.89.0).", "",
              "| Day | Event | Source | " + " | ".join(sorted({p for d in days for p in (d.get('outfits') or {})})) + " | Events · beats |"]
        persons = sorted({p for d in days for p in (d.get("outfits") or {})})
        md.append("|" + "---|" * (len(persons) + 4))
        for d in days:
            evs = " · ".join(f"{e.get('id', '')} {e.get('location', '')} {e.get('visibility', '')}: {', '.join(e.get('beats') or [])}".strip()
                             for e in d.get("events") or [])
            md.append(f"| {d.get('day')} | {d.get('event', '')} | {d.get('source', '')} | "
                      + " | ".join((d.get("outfits") or {}).get(p, "—") for p in persons) + f" | {evs} |")
        if ths:
            md += ["", "### Talking heads — per recording day", "", "| Recording day | Subject | Outfit | Beats |", "|---|---|---|---|"]
            md += [f"| {t.get('day')} | {t.get('subject')} | {t.get('outfit', '')} | {', '.join(t.get('beats') or [])} |" for t in ths]
        Path(a.md).write_text("\n".join(md) + "\n", encoding="utf-8")

    if a.json:
        print(json.dumps({"pass": not out, "days": len(days), "fails": out}, indent=1))
    else:
        for f in out:
            print(f"FAIL  {f['check']:6} {f['where']}  — {f['detail']}")
        print(f"WARDROBE PASS ({len(days)} story days)" if not out else f"WARDROBE FAIL ({len(out)})")
    sys.exit(1 if out else 0)


if __name__ == "__main__":
    main()
