#!/usr/bin/env python3
"""§16A — the whole build's credits, per connector, for the Final output board (V7.83.0).

Usage:
  build_spend.py DIR [DIR ...] [--build BUILD_ID] [--out spend.json]

Each DIR is an ArtifactData `list` dump of one board's `generations` collection
(out_dir=<DIR>; files at <DIR>/generations/<doc_id>.json) — every board of the build:
Current (and Current 2…), Old (and Old 2…), Final, Plan.

Counts every render once, the way the board's own Credits spent card does (spendRows):
each version entry's own credits, connector and model; a step with no version records
falls back to its own fields. A version that a Fix moved to Old sits on both boards
(archived on Current, kept on Old) — it is counted once, by doc id + step + version.

Writes {"buildSpend": {...}} for `ArtifactData update` on the build doc `builds/<id>`
of every board (the Final output page shows it):
  {"connectors": [{"conn", "credits", "renders", "models": [{"model", "credits", "renders"}]}],
   "credits": total, "renders": n, "boards": number of dumps read, "at": ms}
Credits are never added across connectors on the page — each connector is its own row.
"""
import argparse, glob, json, sys, time
from pathlib import Path

STEPS = {  # mirrors STEP in dashboard/generation_board.html
    "image": {"vers": "imageVersions", "conn": "imageConnector", "model": "imageModel", "credits": "imageCredits",
              "asset": "imageAsset", "defConn": "Higgsfield", "defModel": "nano_banana_pro"},
    "video": {"vers": "videoVersions", "conn": "videoConnector", "model": "model", "credits": "credits",
              "asset": "videoAsset", "defConn": "Kling", "defModel": "kling-video-v3_0_omni"},
}


def num(x):
    try:
        return float(x or 0)
    except (TypeError, ValueError):
        return 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dirs", nargs="+")
    ap.add_argument("--build")
    ap.add_argument("--out")
    a = ap.parse_args()
    seen, acc = set(), {}

    def add(key, conn, model, credits):
        if not credits or key in seen:
            return
        seen.add(key)
        c = acc.setdefault(conn, {"conn": conn, "credits": 0.0, "renders": 0, "models": {}})
        c["credits"] += credits
        c["renders"] += 1
        m = c["models"].setdefault(model, {"model": model, "credits": 0.0, "renders": 0})
        m["credits"] += credits
        m["renders"] += 1

    docs = 0
    for d in a.dirs:
        for f in sorted(glob.glob(str(Path(d) / "**" / "*.json"), recursive=True)):
            try:
                g = json.load(open(f))
            except (OSError, json.JSONDecodeError):
                continue
            g = g.get("data", g) if isinstance(g, dict) else None
            if not isinstance(g, dict) or not (g.get("beat") or g.get("build")):
                continue
            if a.build and g.get("build") not in (None, a.build):
                continue
            docs += 1
            gid = g.get("id") or Path(f).stem
            for step, s in STEPS.items():
                conn = g.get(s["conn"]) or s["defConn"]
                model = g.get(s["model"]) or s["defModel"]
                got = 0.0
                for v in g.get(s["vers"]) or []:
                    if not isinstance(v, dict):
                        continue
                    c = num(v.get("credits"))
                    if c:
                        key = (gid, step, v.get("v") if v.get("v") is not None else v.get("asset"))
                        add(key, v.get("connector") or conn, v.get("model") or model, c)
                        got += c
                if not got:
                    add((gid, step, "fields", g.get(s["asset"])), conn, model, num(g.get(s["credits"])))

    rows = []
    for c in sorted(acc.values(), key=lambda x: -x["credits"]):
        c["credits"] = round(c["credits"], 2)
        c["models"] = sorted(({**m, "credits": round(m["credits"], 2)} for m in c["models"].values()),
                             key=lambda m: -m["credits"])
        rows.append(c)
    spend = {"connectors": rows, "credits": round(sum(r["credits"] for r in rows), 2),
             "renders": sum(r["renders"] for r in rows), "boards": len(a.dirs), "docs": docs,
             "at": int(time.time() * 1000)}
    out = {"buildSpend": spend}
    if a.out:
        Path(a.out).write_text(json.dumps(out, indent=1))
    print(json.dumps(out, indent=1))
    if not docs:
        print("build_spend: no generation docs found in the dumps", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
