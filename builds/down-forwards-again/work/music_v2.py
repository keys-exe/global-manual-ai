#!/usr/bin/env python3
"""Music v2 (user 2026-10-01: "i want a new one investigation and change when the product shows not a sad").
v1 (work/music_map.py: cello drone, felt piano, heartbeat) read as sad. v2 is one investigation family that never mourns:
  up to the product — a modern investigative-documentary groove: tight ticking pulse, punchy low kick, plucky pizzicato, a clean muted synth
  arpeggio; curious, intriguing, driving forward (§40A MUS-OPEN / EDU / EXPOSE, said as intrigue, never as grief);
  from "This does. It is called Stryde." — the same groove lifts into a bright major key: confident, positive, forward (MUS-TURN → AFTER →
  OFFER), steady to the last second.
Composed as short cues (hooks) and two body parts split on the turn word (one long body track left holes in v1). Every section ≥ 3 s, no
silence asked for — fades are made in the mix. Writes edit/music/v2/<cue>.cue.json."""
import json, pathlib, re
B = pathlib.Path(__file__).parents[1]
AW = json.load(open(B / "acts/plan/words.json"))
ACT = {"A1": 31.92, "A2": 25.08, "A3": 33.01, "A4": 39.74, "A5": 18.52}
HOOK = {"HK1": 12.2, "HK2": 8.64, "HK3": 7.64}
start, t = {}, 0.0
for a, d in ACT.items(): start[a] = round(t, 2); t += d
BODY = round(t, 2)
norm = lambda w: re.sub(r"[^a-z0-9]", "", w.lower())
def at(a, phrase):
    p = [norm(x) for x in phrase.split()]; w = AW[a]["words"]; n = [norm(x[0]) for x in w]
    for i in range(len(n) - len(p) + 1):
        if n[i:i + len(p)] == p: return round(start[a] + max(0.0, w[i][1] - 0.15), 2)
    raise SystemExit(phrase)
TURN = at("A3", "this does")
INV = ["modern investigative documentary underscore, like a smart true-crime explainer", "curious and intriguing, NOT sad",
       "driving detective groove at a steady moderate tempo", "tight ticking hi-hat pulse and a punchy low kick",
       "plucky pizzicato strings and a clean muted synth arpeggio", "one consistent groove, instrumentation from start to end",
       "instrumental, sits under a speaking voice"]
LIFT = ["the same groove and instruments as the investigation, now in a bright major key", "confident, positive, hopeful forward momentum",
        "the mystery is solved", "tight hi-hat pulse, punchy low kick, pizzicato and arpeggio now bright and open, a warm pad underneath",
        "instrumental, sits under a speaking voice"]
AVOID = ["sad", "melancholic", "mournful", "slow sad piano", "somber strings", "cello lament", "minor-key ballad", "horror", "dark ambient drone",
         "vocals", "lyrics", "humming", "EDM drop", "big trailer hits", "busy melody", "cute", "ukulele", "whistling", "corporate jingle", "silence", "fade out"]
KEEP = "the groove keeps going to the very last second, never stops, no pause, no fade"
C = {}
for h, L in HOOK.items():
    C[h] = {"scene": f"MUS2-{h}", "length_s": round(L + 4, 2), "theme": INV, "avoid": AVOID, "tempo": "moderate", "bpm": 100,
            "sections": [{"name": "The question", "start": 0, "end": round(L + 4, 2), "energy": "mid",
                          "styles": ["the groove starts immediately at full pulse from the first second", "an intriguing hook", KEEP]}]}
C["BODY_A"] = {"scene": "MUS2-BODY-A", "length_s": round(TURN + 12, 2), "theme": INV, "avoid": AVOID, "tempo": "moderate", "bpm": 100,
    "sections": [{"name": "The case", "start": 0, "end": start["A2"], "energy": "mid",
                  "styles": ["the groove at full pulse from the first second", "curious, the evidence piling up", KEEP]},
                 {"name": "The evidence", "start": start["A2"], "end": round(TURN + 12, 2), "energy": "mid",
                  "styles": ["the same groove, a touch more tension and drive", "still confident, never sad", KEEP]}]}
LB = round(BODY - TURN + 4, 2); AF = round(start["A4"] - TURN, 2)
C["BODY_B"] = {"scene": "MUS2-BODY-B", "length_s": LB, "theme": LIFT, "avoid": AVOID, "tempo": "moderate", "bpm": 100,
    "sections": [{"name": "The reveal", "start": 0, "end": AF, "energy": "high",
                  "styles": ["opens straight into the bright major-key groove on the first beat", "a satisfying confident reveal", KEEP]},
                 {"name": "Proof and the offer", "start": AF, "end": LB, "energy": "high",
                  "styles": ["the same bright groove, steady and confident", "positive momentum to the end", KEEP]}]}
d = B / "edit/music/v2"; d.mkdir(parents=True, exist_ok=True)
for k, c in C.items(): (d / f"{k}.cue.json").write_text(json.dumps(c, ensure_ascii=False, indent=1))
print("TURN", TURN, "BODY", BODY, {k: c["length_s"] for k, c in C.items()})
