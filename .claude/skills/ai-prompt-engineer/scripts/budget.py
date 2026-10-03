#!/usr/bin/env python3
"""§5B — the build's credit cap: estimate everything first, then never spend past it (V7.95.0;
user 2026-10-03 — "make a cap of points for every task, estimate everything so we will not use so much credits").

Every build, both run modes, gets a cap per connector before its first paid call. The cap is the estimate
of everything the plan needs plus a Fix allowance; a `CAP` line in the intake wins over it.

Usage:
  budget.py draft --build ID --mode 1-5 --words N [--hooks 3] [--talking-heads] [--cast 3] [--locations 4]
                  [--voices 1] [--anatomy 0] [--music-video] [--routes image=Higgsfield,kling=Kie AI,...]
                  --out plan.json
      Step 2: a first plan from the script's spoken word count (script_lines.py) — rough, said as such.
  budget.py estimate plan.json [--cap "Kie AI=3000, Higgsfield=500"] [--out budget.json] [--md budget.md]
      Step 2 and again at step 5 from the act map's real counts and `assemble.py --lengths` seconds:
      the cost of every job, per connector, + the Fix allowance = the cap.
  budget.py check budget.json --spend spend.json --batch "Kie AI=270[, Higgsfield=6.2]"
      Before every paid batch: this build's spend so far (build_spend.py --out spend.json, or 0 with no
      spend file yet) + the batch <= the cap. OVER -> exit 1: the batch is not sent.

Plan jobs (one entry each; `route` / `model` optional overrides):
  cast · plates · info_cards              image, one render each
  beat_images · end_frames · anatomy_images   image, an A/B pair each in Modes 1-3 (two renders)
  broll_video · hook_video                Kling seconds in total (`seconds`), silent
  voice_source                            Kling seconds with sound (§22U source takes)
  seedance                                Seedance seconds in total
  talking_heads                           HeyGen renders
  tts                                     characters (`chars`) x `takes`
  music · sfx                             tracks / sounds
Prices: references/credit_prices.json (measured or unverified, per connector, in that connector's credits).
Credits are never added across connectors — each connector has its own cap.
"""
import argparse, json, math, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
PRICES = json.loads((HERE.parent / "references" / "credit_prices.json").read_text())

JOBS = {  # job -> (price kind, allowance class, unit field)
    "cast": ("image", "image", "n"), "plates": ("image", "image", "n"), "info_cards": ("image", "image", "n"),
    "beat_images": ("image", "image", "n"), "end_frames": ("image", "image", "n"),
    "anatomy_images": ("image", "image", "n"),
    "broll_video": ("kling", "video", "seconds"), "hook_video": ("kling", "video", "seconds"),
    "voice_source": ("kling", "audio", "seconds"),
    "seedance": ("seedance", "video", "seconds"),
    "talking_heads": ("talking", "video", "n"),
    "tts": ("tts", "audio", "chars"), "music": ("music", "audio", "n"), "sfx": ("sfx", "audio", "n"),
}
PAIRED = {"beat_images", "end_frames", "anatomy_images"}
DEFAULT_ROUTES = {"image": "Higgsfield", "kling": "Kling", "seedance": "Kie AI", "talking": "HeyGen",
                  "tts": "ElevenLabs", "music": "ElevenLabs", "sfx": "ElevenLabs"}


def norm(conn):
    c = (conn or "").lower().replace("api", "").replace("connector", "").strip()
    for name in ("Higgsfield", "Kling", "Kie AI", "HeyGen", "ElevenLabs", "Higgsless"):
        if c.startswith(name.lower().split()[0]):
            return name
    return (conn or "").strip()


def price(kind, route, model=None, sound=False):
    table = PRICES["prices"][kind]
    key = route + ("+sound" if sound and (route + "+sound") in table else "")
    p = table.get(key, table["_default"])
    if isinstance(p, dict):
        p = p.get(model) or next(iter(p.values()))
    return p  # [credits, unit, source]


def image_model(job, mode, override=None):
    if override:
        return override
    if job == "anatomy_images" or mode in (2, 3, 5):
        return "nano_banana_pro"
    return "gpt_image_2_5"  # realistic, §18A (V7.72.0)


def parse_pairs(s):
    out = {}
    for part in (s or "").split(","):
        if "=" in part:
            k, v = part.split("=", 1)
            out[k.strip()] = v.strip()
    return out


def cmd_draft(a):
    words, hooks, mode = a.words, a.hooks, a.mode
    film = mode in (4, 5)
    sec = words / 2.8                       # ~168 wpm, under the 210 wpm gate (§22U)
    hook_sec = 6.0 * hooks
    routes = {**DEFAULT_ROUTES, **parse_pairs(a.routes)}
    jobs = [{"job": "cast", "n": a.cast}, {"job": "plates", "n": a.locations}]
    if film:
        scenes = max(1, math.ceil(sec / 20))
        jobs += [{"job": "info_cards", "n": scenes * 2},
                 {"job": "seedance", "seconds": math.ceil(sec + hook_sec), "note": "one take per scene (§24K part 5)"},
                 {"job": "seedance", "seconds": 15 * a.voices, "note": "voice masters (§24I)"},
                 {"job": "music", "n": scenes}, {"job": "sfx", "n": 8}]
    else:
        cover = 0.6 if a.talking_heads else 1.0
        rows = math.ceil(sec * cover / 2.5)     # one picture per phrase, ~2.5 s (§27)
        hook_shots = 2 * hooks
        anat = min(a.anatomy, rows)
        jobs += [{"job": "beat_images", "n": rows - anat + hook_shots},
                 {"job": "end_frames", "n": math.ceil(0.15 * rows)},
                 {"job": "broll_video", "seconds": math.ceil(rows * 3.4), "note": "time on screen + 0.9 s (E6)"},
                 {"job": "hook_video", "seconds": math.ceil(hook_shots * 4)}]
        if anat:
            jobs.append({"job": "anatomy_images", "n": anat})
        if a.music_video:
            jobs.append({"job": "music", "n": 1 + hooks})
        else:
            jobs += [{"job": "voice_source", "seconds": 20 * a.voices},
                     {"job": "tts", "chars": math.ceil((words + 15 * hooks) * 6.2), "takes": 2},
                     {"job": "music", "n": 2}]
            if a.talking_heads:
                jobs.append({"job": "talking_heads", "n": a.voices})
    plan = {"build": a.build, "mode": mode, "draft": True, "words": words, "hooks": hooks,
            "routes": routes, "jobs": jobs}
    Path(a.out).write_text(json.dumps(plan, indent=1))
    print(json.dumps(plan, indent=1))


def estimate(plan, cap_line=None):
    mode = int(plan.get("mode", 1))
    routes = {**DEFAULT_ROUTES, **(plan.get("routes") or {})}
    conns, lines = {}, []
    for j in plan.get("jobs", []):
        job = j["job"]
        if job not in JOBS:
            sys.exit(f"budget: unknown job {job!r} (known: {', '.join(JOBS)})")
        kind, cls, unit = JOBS[job]
        route = norm(j.get("route") or routes[kind])
        model = image_model(job, mode, j.get("model")) if kind == "image" else j.get("model")
        sound = job == "voice_source" or bool(j.get("sound"))
        cr, per, src = price(kind, route, model, sound)
        qty = float(j.get(unit) or 0) * (float(j.get("takes") or 1) if job == "tts" else 1)
        renders = 2 if (job in PAIRED and mode in (1, 2, 3)) else 1
        base = cr * qty * renders
        allow = base * PRICES["fix_allowance"][cls]
        c = conns.setdefault(route, {"conn": route, "base": 0.0, "allowance": 0.0})
        c["base"] += base
        c["allowance"] += allow
        lines.append({"job": job, "conn": route, "model": model, "qty": qty, "unit": per,
                      "renders_each": renders, "credits": round(base, 2), "price": cr, "source": src,
                      "note": j.get("note", "")})
    caps = {norm(k): float(v.replace(",", "")) for k, v in parse_pairs(cap_line).items()} if cap_line else {}
    if cap_line and not caps:
        sys.exit("budget: a CAP line names each connector (e.g. \"Kie AI=3000, Higgsfield=500\") — "
                 "credits differ by connector and are never added across them")
    rows = []
    for c in sorted(conns.values(), key=lambda x: -x["base"]):
        est = c["base"] + c["allowance"]
        step = 10 if est < 500 else 50
        c["estimate"] = math.ceil(est / step) * step
        c["cap"] = caps.get(c["conn"], c["estimate"])
        c["cap_source"] = "CAP line" if c["conn"] in caps else "estimate"
        c["base"], c["allowance"] = round(c["base"], 2), round(c["allowance"], 2)
        rows.append(c)
    for k, v in caps.items():
        if k not in conns:
            rows.append({"conn": k, "base": 0, "allowance": 0, "estimate": 0, "cap": v, "cap_source": "CAP line"})
    lines.sort(key=lambda x: -x["credits"])
    return {"budget": {"build": plan.get("build"), "draft": bool(plan.get("draft")), "mode": mode,
                       "connectors": rows, "lines": lines, "warn_at": PRICES["warn_at"],
                       "at": int(time.time() * 1000)}}


def to_md(b):
    b = b["budget"]
    out = [f"### Credit cap — {b['build']}" + (" (draft from the script word count)" if b["draft"] else ""), "",
           "| Connector | Planned | Fix allowance | Cap | From |", "|---|---|---|---|---|"]
    for c in b["connectors"]:
        out.append(f"| {c['conn']} | {c['base']:,.0f} | {c['allowance']:,.0f} | **{c['cap']:,.0f}** | {c['cap_source']} |")
    out += ["", "Credits are each connector's own — never added across connectors.", "",
            "| Job | Connector | Model | Qty | Each | Credits | Price source |", "|---|---|---|---|---|---|---|"]
    for l in b["lines"]:
        each = f"{l['price']} {l['unit']}" + (" ×2 (A/B)" if l["renders_each"] == 2 else "")
        out.append(f"| {l['job']} | {l['conn']} | {l['model'] or ''} | {l['qty']:g} | {each} | {l['credits']:,.0f} | {l['source']} |")
    return "\n".join(out) + "\n"


def cmd_estimate(a):
    b = estimate(json.loads(Path(a.plan).read_text()), a.cap)
    if a.out:
        Path(a.out).write_text(json.dumps(b, indent=1))
    if a.md:
        Path(a.md).write_text(to_md(b))
    print(to_md(b))


def cmd_check(a):
    b = json.loads(Path(a.budget).read_text())["budget"]
    caps = {norm(c["conn"]): float(c["cap"]) for c in b["connectors"]}
    spent = {}
    if a.spend and Path(a.spend).exists():
        s = json.loads(Path(a.spend).read_text())
        for c in (s.get("buildSpend", s).get("connectors") or []):
            spent[norm(c["conn"])] = spent.get(norm(c["conn"]), 0) + float(c.get("credits") or 0)
    batch = {norm(k): float(v.replace(",", "")) for k, v in parse_pairs(a.batch).items()}
    if not batch:
        sys.exit("budget: --batch names the connector and cost, e.g. \"Kie AI=270\"")
    worst = 0
    for conn, cost in batch.items():
        cap, done = caps.get(conn), spent.get(conn, 0.0)
        if cap is None:
            print(f"OVER  {conn}: no cap for this connector — re-run `estimate` with the job on it before spending")
            worst = 2
            continue
        after = done + cost
        if after > cap:
            print(f"OVER  {conn}: spent {done:,.1f} + batch {cost:,.1f} = {after:,.1f} > cap {cap:,.0f} "
                  f"(left {cap - done:,.1f}) — not sent; ask the user to raise the cap (Automatic: stop)")
            worst = 2
        elif after >= cap * float(b.get("warn_at", 0.8)):
            print(f"WARN  {conn}: {after:,.1f} of {cap:,.0f} after this batch ({after / cap:.0%}) — tell the user once")
            worst = max(worst, 1)
        else:
            print(f"OK    {conn}: {after:,.1f} of {cap:,.0f} after this batch ({after / cap:.0%})")
    sys.exit(1 if worst == 2 else 0)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("draft")
    d.add_argument("--build", required=True)
    d.add_argument("--mode", type=int, required=True)
    d.add_argument("--words", type=int, required=True, help="spoken words in the script (script_lines.py)")
    d.add_argument("--hooks", type=int, default=3)
    d.add_argument("--talking-heads", action="store_true")
    d.add_argument("--cast", type=int, default=3)
    d.add_argument("--locations", type=int, default=4)
    d.add_argument("--voices", type=int, default=1)
    d.add_argument("--anatomy", type=int, default=0, help="anatomy / mechanism beats")
    d.add_argument("--music-video", action="store_true")
    d.add_argument("--routes", help="kind=connector pairs from the Connector Map, e.g. \"kling=Kie AI\"")
    d.add_argument("--out", required=True)
    e = sub.add_parser("estimate")
    e.add_argument("plan")
    e.add_argument("--cap", help="the intake's CAP line, per connector")
    e.add_argument("--out")
    e.add_argument("--md")
    c = sub.add_parser("check")
    c.add_argument("budget")
    c.add_argument("--spend")
    c.add_argument("--batch", required=True)
    a = ap.parse_args()
    {"draft": cmd_draft, "estimate": cmd_estimate, "check": cmd_check}[a.cmd](a)


if __name__ == "__main__":
    main()
