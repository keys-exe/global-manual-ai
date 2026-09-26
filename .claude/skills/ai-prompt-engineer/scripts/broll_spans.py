#!/usr/bin/env python3
"""E6 + §30H — time every B-roll beat on the voice master BEFORE any B-roll call.

Usage:
  broll_spans.py SPANS.json [--min-th 1.5]

SPANS.json:
{
  "audio": "voice/body_master.mp3",          # the master (a list for hook + body)
  "script": "work/script.lines.txt",          # verbatim spoken lines (script_lines.py)
  "words": "work/body.words.json",            # optional: [[start, end, word], ...]
  "talking_heads": true,                      # false = voice-only build
  "beats": [ {"beat": "BR-01", "phrase": "seventeen times your bodyweight",
              "read": "the load arriving on one small spot below the kneecap",
              "read_kind": "state"}, ... ]    # state | event | contrast (§30B Part 4)
}

For every beat, from the master's script-aligned word timestamps:
  span_s       first word start -> last word end of the phrase (E6)
  on_screen_s  how long the B-roll will be on screen: until the next B-roll starts
               (voice-only), or until its line ends, bridged to the next B-roll when
               the talking-head window left would be a flicker (< --min-th) — the
               pause after the phrase counts, as it does in assembly (§30H)
  call_s       the generation length: span + 0.5s, rounded up, Kling 3-15s (E6)
Flags (the agent acts on every one before writing the prompt):
  FLASH        on screen under the read floor for its kind (state 0.8s, event 1.2s,
               contrast 1.8s). Event/contrast: re-plan the shot as a STATE (the READ
               visible in every frame). State under 0.8s: §30H FLASH — fold into the
               neighbour's slot, flagged to the user (the script's split is theirs)
  SHORT        on screen under 1.5s: the READ must be visible from the first frame
               (a state, or the event already under way — §27A short-beat rule)
  LONG         span over 3s: one continuous action that lasts the whole span, or
               the window picker has only dead footage to choose from
  SPLIT        span over 14.5s: split at a word boundary into two clips (E6)
  NEGATION     the phrase says what does NOT happen (no, not, never, without,
               unlike, isn't...). The shot shows the opposite state, never the
               named failure (§22W Q1)
  NO_READ      the beat has no READ yet (§30B Part 4) — write it first
Prints JSON. Exit 0 = no FLASH and every phrase found, 2 otherwise.
"""
import argparse, json, math, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from assemble import timed_words, find_phrase, line_end, snap, MIN_READ, MIN_FLASH  # noqa: E402
from trim import duration  # noqa: E402

NEG = re.compile(r"\b(no|not|never|without|none|nothing|nobody|unlike|isn't|aren't|doesn't|don't|"
                 r"won't|can't|cannot|didn't|wasn't|hasn't|haven't|stop|stops|stopped)\b", re.I)
KLING_MIN, KLING_MAX, HANDLE = 3, 15, 0.5


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spans")
    ap.add_argument("--min-th", type=float, default=1.5)
    ap.add_argument("--model", default="base.en")
    a = ap.parse_args()
    root = Path(a.spans).parent
    plan = json.loads(Path(a.spans).read_text())
    parts = plan["audio"] if isinstance(plan["audio"], list) else [plan["audio"]]
    total = sum(snap(duration(root / p)) for p in parts)
    ws = timed_words(root, plan, a.model)
    th = bool(plan.get("talking_heads"))

    rows, fails, cursor = [], [], 0
    for b in plan["beats"]:
        hit = find_phrase(ws, b["phrase"], cursor)
        if not hit:
            fails.append({"beat": b["beat"], "fail": "PHRASE_NOT_FOUND", "phrase": b["phrase"]})
            continue
        i, j = hit
        cursor = i + 1
        rows.append({"beat": b["beat"], "phrase": b["phrase"], "read": b.get("read"),
                     "read_kind": b.get("read_kind"), "start": snap(ws[i][0]),
                     "span_s": round(ws[j][1] - ws[i][0], 2), "line_end": snap(line_end(ws, j))})
    rows.sort(key=lambda r: r["start"])
    for n, r in enumerate(rows):
        nxt = rows[n + 1]["start"] if n + 1 < len(rows) else total
        if th:
            end = min(nxt, max(r["line_end"], r["start"] + r["span_s"]))
            if n + 1 < len(rows) and nxt - end < a.min_th:
                end = nxt  # a flicker is closed onto the next B-roll (§30H FLICKER)
        else:
            end = nxt  # voice-only: every frame is B-roll (§30H HOLE)
        r["on_screen_s"] = round(end - r["start"], 2)
        r["call_s"] = min(KLING_MAX, max(KLING_MIN, math.ceil(r["span_s"] + HANDLE)))
        flags = []
        floor = MIN_READ.get(r["read_kind"], MIN_FLASH)
        if r["on_screen_s"] < floor - 1e-3:
            flags.append("FLASH")
            fails.append({"beat": r["beat"], "fail": "FLASH",
                          "detail": f"on screen ~{r['on_screen_s']:.2f}s < {floor}s ({r['read_kind'] or 'no read_kind'})"})
        if r["on_screen_s"] < 1.5:
            flags.append("SHORT")
        if r["span_s"] > 3.0:
            flags.append("LONG")
        if r["span_s"] + HANDLE > KLING_MAX:
            flags.append("SPLIT")
        if NEG.search(r["phrase"]):
            flags.append("NEGATION")
        if not r["read"]:
            flags.append("NO_READ")
        r["flags"] = flags
        del r["line_end"]
    print(json.dumps({"master_s": round(total, 3), "talking_heads": th, "beats": rows,
                      "failures": fails, "status": "FAIL" if fails else "PASS"}, indent=2))
    sys.exit(2 if fails else 0)


if __name__ == "__main__":
    main()
