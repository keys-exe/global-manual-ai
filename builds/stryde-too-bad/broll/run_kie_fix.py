#!/usr/bin/env python3
"""Fix round (2026-09-29): regenerate the listed beats on the Kie AI API (§5 — Higgsfield no longer lists nano_banana_pro,
nano_banana_2 or gpt_image_2_5). One render per beat, refs as public URLs, outputs broll/v2/<BEAT>_v<N>.png; results -> broll/kie_fix.json."""
import json, subprocess, sys, pathlib, concurrent.futures as cf
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[2]
KIE = ROOT / ".claude/skills/ai-prompt-engineer/scripts/kie.py"
PR = ROOT / "products/stryde/stryde_refs"
CDN = "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/"
REF = {"front": PR / "front.webp", "back": PR / "back.webp", "worn_front": PR / "worn_front.jpg", "worn_rear": PR / "worn_rear.jpg",
       "worn_bent": PR / "worn_bent.jpg",
       "R1-DENISE": CDN + "hf_20260929_121040_b43b73c7-9c18-4031-a31f-f9b08182e546.png",
       "R4-FIONA": CDN + "hf_20260929_115319_6757bb36-e953-4b36-84c3-23bf20d39d9f.png",
       "P2-D-LOUNGE": CDN + "hf_20260929_121803_d9cc54f9-a111-4553-8a40-77a9550753ef.png",
       "MECH-S1_v1": CDN + "hf_20260929_153901_9296f550-3bf4-40ce-8140-5987882d8745.png",
       "MECH-04_v1": CDN + "hf_20260929_153900_09587ed3-9bdf-42e4-b6b6-7c4091dc1cf3.png",
       "B1-01a_v1": CDN + "hf_20260929_153902_3c9bea78-be72-4495-9591-66846844271f.png"}
REF.update(json.loads((HERE / "extra_refs.json").read_text()) if (HERE / "extra_refs.json").exists() else {})
KIEMODEL = {"nano_banana_pro": "nano-banana-pro", "nano_banana_2": "nano-banana-2", "gpt_image_2_5": "gpt-image-2-5-sunburst-image-to-image"}
B = json.loads((HERE / "broll.json").read_text())
def run(beat, v):
    b = B[beat]
    cmd = [sys.executable, str(KIE), "image", KIEMODEL[b["model"]], "--prompt-file", str(HERE / f"{beat}.t2i.txt"),
           "--out", str(HERE / "v2" / f"{beat}_v{v}.png")]
    if b["refs"]:
        cmd += ["--ref"] + [str(REF[r]) for r in b["refs"]]
    p = subprocess.run(cmd, capture_output=True, text=True)
    try: res = json.loads(p.stdout)
    except Exception: res = {"error": p.stdout[-400:] + p.stderr[-400:]}
    res.update(beat=beat, v=v, kieModel=KIEMODEL[b["model"]], rc=p.returncode)
    return res
if __name__ == "__main__":
    jobs = [a.split(":") for a in sys.argv[1:]]   # BEAT:V
    out = HERE / "kie_fix.json"; done = json.loads(out.read_text()) if out.exists() else {}
    with cf.ThreadPoolExecutor(8) as ex:
        for r in ex.map(lambda j: run(j[0], int(j[1])), jobs):
            done[f'{r["beat"]}_v{r["v"]}'] = r; print(json.dumps({k: r.get(k) for k in ("beat", "v", "rc", "taskId", "file", "url", "error")}))
    out.write_text(json.dumps(done, indent=1))
