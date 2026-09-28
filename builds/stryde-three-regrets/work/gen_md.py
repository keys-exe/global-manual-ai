#!/usr/bin/env python3
"""Render the act-map tables for STEP4_5.md from actmap.json."""
import json, pathlib
H = pathlib.Path(__file__).resolve().parent
R = json.loads((H / "actmap.json").read_text())
out = []
cur = None
for r in R:
    if r["act"] != cur:
        cur = r["act"]
        out.append(f"\n#### {cur}\n")
        out.append("| Beat | Act | Phrase | Type | Subject | Location | Day · event | Action · pace | Camera · staging · pin | Angle (height · side · scale · fg) — why | Focus | Light key | Key word | Product | Layout · EG | Model | Ledger |")
        out.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    ang = f"{r['height']} · {r['side']} · {r['scale']} · {r['fg']}" + (f" — {r['why']}" if r['why'] else "")
    out.append("| {beat} | {act} | {ph} | {type} | {subject} | {loc} | {day} · {event} | {action} · {pace} | {camera} · {staging} · {pin_end} | {ang} | {plane}, {dof} | {key_side} | {key} | {product} | {layout} | {model} | {ledger} |".format(
        ph=", ".join(r["phrases"]), ang=ang, **r))
print("\n".join(out))
