#!/usr/bin/env python3
"""§30H hook variants — one finished video per hook, each hook + the same body.

Usage:
  variants.py VARIANTS.json [--outdir DIR] [--build NAME]

VARIANTS.json:
{
  "body":  {"audio": "voice/body_master.mp3", "script": "work/script.lines.txt",
            "base": "th/body_th.mp4" | null,
            "broll": [ {"beat": "BR-01", "clip": "...", "phrase": "..."}, ... ]},
  "hooks": [
    {"id": "HK1", "audio": "voice/HK1.mp3", "script": "work/HK1.lines.txt",
     "base": "th/HK1_th.mp4" | null, "broll": [ {"beat": "HK1-01", ...} ]},
    {"id": "HK2", ...}, {"id": "HK3", ...}
  ]
}

For each hook, builds one plan — audio [hook, body], script [hook, body], base
[hook, body] (or null), B-roll hook's then body's — runs assemble.py on it, and
writes <BUILD>_<HOOK-ID>.mp4. §30H holds across the hook-to-body seam because the
two are one timeline. Then checks the set:
  - every variant rendered and PASSED on its own
  - the body is the same in every variant: the body segment of each timeline is
    identical once shifted by that hook's length
  - each variant's duration = its hook master + the body master (±2 frames)
Prints one JSON report. Exit 0 = every variant PASS, 2 = any FAIL.
"""
import argparse, json, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
from trim import duration  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("variants")
    ap.add_argument("--outdir")
    ap.add_argument("--build", default="BUILD")
    ap.add_argument("--min-th", type=float, default=1.5)
    a = ap.parse_args()
    root = Path(a.variants).parent
    spec = json.loads(Path(a.variants).read_text())
    body, hooks = spec["body"], spec["hooks"]
    outdir = Path(a.outdir) if a.outdir else root / "variants"
    outdir.mkdir(parents=True, exist_ok=True)
    body_len = duration(root / body["audio"])

    results, body_edls = [], []
    for h in hooks:
        plan = {
            "audio": [h["audio"], body["audio"]],
            "script": [h["script"], body["script"]],
            "base": [h["base"], body["base"]] if body.get("base") and h.get("base") else None,
            "broll": h.get("broll", []) + body["broll"],
        }
        if bool(body.get("base")) != bool(h.get("base")):
            results.append({"hook": h["id"], "status": "FAIL",
                            "detail": "hook and body must both have a talking-head track, or both be voice-only"})
            continue
        pfile = root / f"_plan_{h['id']}.json"
        pfile.write_text(json.dumps(plan, indent=2))
        out = outdir / f"{a.build}_{h['id']}.mp4"
        r = subprocess.run([sys.executable, str(HERE / "assemble.py"), str(pfile), "--out", str(out),
                            "--min-th", str(a.min_th)], capture_output=True, text=True)
        try:
            rep = json.loads(r.stdout)
        except json.JSONDecodeError:
            results.append({"hook": h["id"], "status": "FAIL", "detail": r.stderr[-500:]})
            continue
        hook_len = round(round(duration(root / h["audio"]) * 30) / 30, 4)  # body starts on this frame
        expect = hook_len + body_len
        got = rep.get("render", {}).get("duration_s")
        body_beats = {b["beat"] for b in body["broll"]}
        body_part = [(s["beat"], round(s["start"] - hook_len, 2), round(s["end"] - hook_len, 2))
                     for s in rep["timeline"] if s.get("beat") in body_beats]
        body_edls.append(body_part)
        ok = rep.get("status") == "PASS" and got is not None and abs(got - expect) <= 2 / 30
        results.append({"hook": h["id"], "file": str(out), "status": "PASS" if ok else "FAIL",
                        "hook_s": round(hook_len, 3), "body_s": round(body_len, 3),
                        "duration_s": got, "expected_s": round(expect, 3),
                        "fixes": rep.get("fixes", []), "failures": rep.get("failures", []),
                        "black_frames": rep.get("render", {}).get("black_frames")})

    same_body = len(body_edls) > 1 and all(e == body_edls[0] for e in body_edls[1:])
    status = "PASS" if results and all(r["status"] == "PASS" for r in results) and \
        (same_body or len(body_edls) <= 1) else "FAIL"
    print(json.dumps({"status": status, "variants": results,
                      "body_identical_across_variants": same_body if len(body_edls) > 1 else None},
                     indent=2))
    sys.exit(0 if status == "PASS" else 2)


if __name__ == "__main__":
    main()
