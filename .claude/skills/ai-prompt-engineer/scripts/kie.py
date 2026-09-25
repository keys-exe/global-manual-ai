#!/usr/bin/env python3
"""Kie AI API client (§5) — the route for Seedance 2.5 and the image fallback.

Needs KIE_API_KEY in the environment (an environment secret; never pasted in chat).

  kie.py credit
  kie.py upload FILE [--path DIR]                       -> public URL (temporary: 24h-3 days)
  kie.py image  MODEL --prompt-file P [--ref URL ...] [--out FILE]
        MODEL: nano-banana-pro | nano-banana-2 |
               gpt-image-2-5-sunburst-text-to-image | gpt-image-2-5-sunburst-image-to-image
  kie.py seedance --prompt-file P --ref-image URL ... [--ref-audio URL ...]
        [--duration 10] [--no-audio] [--out FILE]
  kie.py wait TASK_ID [--out FILE]

Fixed by the standard, never overridden here: aspect 9:16; images 2K; Seedance
720p, ingredients mode (reference_image_urls, never first_frame_url), duration
stated (never -1). A local path passed as --ref is uploaded first.
Every command prints JSON. Exit 0 = success, 2 = task failed, 1 = error.
"""
import argparse, json, os, sys, time, urllib.request
from pathlib import Path

API = "https://api.kie.ai/api/v1"
UPLOAD = "https://kieai.redpandaai.co/api/file-stream-upload"
IMAGE_MODELS = {
    "nano-banana-pro": ("image_input", 8),
    "nano-banana-2": ("image_input", 14),
    "gpt-image-2-5-sunburst-text-to-image": (None, 0),
    "gpt-image-2-5-sunburst-image-to-image": ("input_urls", 16),
}


def key():
    k = os.environ.get("KIE_API_KEY")
    if not k:
        sys.exit(json.dumps({"error": "KIE_API_KEY is not set in the environment"}))
    return k


def call(method, url, body=None):
    req = urllib.request.Request(url, method=method,
                                 data=json.dumps(body).encode() if body is not None else None,
                                 headers={"Authorization": f"Bearer {key()}",
                                          "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


def upload(path, folder="pipeline"):
    import subprocess
    out = subprocess.run(["curl", "-sS", "-m", "300", "-X", "POST", UPLOAD,
                          "-H", f"Authorization: Bearer {key()}",
                          "-F", f"file=@{path}", "-F", f"uploadPath={folder}",
                          "-F", f"fileName={Path(path).name}"],
                         capture_output=True, text=True)
    d = json.loads(out.stdout)
    if not d.get("success"):
        sys.exit(json.dumps({"error": "upload failed", "response": d}))
    return d["data"]["downloadUrl"]


def as_url(ref):
    return upload(ref) if Path(ref).exists() else ref


def create(model, inp):
    d = call("POST", f"{API}/jobs/createTask", {"model": model, "input": inp})
    if d.get("code") != 200:
        sys.exit(json.dumps({"error": "createTask failed", "response": d}))
    return d["data"]["taskId"]


def wait(task_id, out=None, timeout=900):
    t0 = time.time()
    while True:
        d = call("GET", f"{API}/jobs/recordInfo?taskId={task_id}")
        if d.get("code") != 200:
            return {"taskId": task_id, "error": d.get("msg"), "code": d.get("code")}, 1
        data = d.get("data") or {}
        state = data.get("state")
        if state in ("success", "fail"):
            break
        if time.time() - t0 > timeout:
            return {"taskId": task_id, "state": state, "timed_out": True}, 1
        time.sleep(8)
    res = {"taskId": task_id, "state": state, "credits": data.get("creditsConsumed"),
           "failMsg": data.get("failMsg")}
    if state == "success":
        rj = json.loads(data.get("resultJson") or "{}")
        res["urls"] = rj.get("resultUrls", [])
        if out and res["urls"]:
            Path(out).parent.mkdir(parents=True, exist_ok=True)
            urllib.request.urlretrieve(res["urls"][0], out)
            res["saved"] = out
    return res, 0 if state == "success" else 2


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("credit")
    u = sub.add_parser("upload"); u.add_argument("file"); u.add_argument("--path", default="pipeline")
    i = sub.add_parser("image"); i.add_argument("model", choices=IMAGE_MODELS)
    i.add_argument("--prompt-file", required=True); i.add_argument("--ref", nargs="*", default=[])
    i.add_argument("--out")
    s = sub.add_parser("seedance"); s.add_argument("--prompt-file", required=True)
    s.add_argument("--ref-image", nargs="+", required=True); s.add_argument("--ref-audio", nargs="*", default=[])
    s.add_argument("--duration", type=int, default=5); s.add_argument("--no-audio", action="store_true")
    s.add_argument("--out")
    w = sub.add_parser("wait"); w.add_argument("task_id"); w.add_argument("--out")
    a = ap.parse_args()

    if a.cmd == "credit":
        print(json.dumps({"credits": call("GET", f"{API}/chat/credit").get("data")})); return
    if a.cmd == "upload":
        print(json.dumps({"url": upload(a.file, a.path)})); return
    if a.cmd == "wait":
        res, rc = wait(a.task_id, a.out); print(json.dumps(res, indent=2)); sys.exit(rc)

    prompt = Path(a.prompt_file).read_text(encoding="utf-8")
    if a.cmd == "image":
        field, cap = IMAGE_MODELS[a.model]
        refs = [as_url(r) for r in a.ref]
        if len(refs) > cap:
            sys.exit(json.dumps({"error": f"{a.model} takes at most {cap} references, got {len(refs)}"}))
        inp = {"prompt": prompt, "aspect_ratio": "9:16", "resolution": "2K"}
        if a.model.startswith("nano"):
            inp["output_format"] = "png"
        if field:
            inp[field] = refs
        task = create(a.model, inp)
    else:
        if not 4 <= a.duration <= 30:
            sys.exit(json.dumps({"error": "Seedance duration must be 4-30s, stated (E6)"}))
        imgs = [as_url(r) for r in a.ref_image]
        auds = [as_url(r) for r in a.ref_audio]
        if len(imgs) > 30 or len(auds) > 10:
            sys.exit(json.dumps({"error": "Seedance takes at most 30 images and 10 audio references"}))
        inp = {"prompt": prompt, "reference_image_urls": imgs, "resolution": "720p",
               "aspect_ratio": "9:16", "duration": a.duration,
               "generate_audio": not a.no_audio, "output_format": "mp4"}
        if auds:
            inp["reference_audio_urls"] = auds
        task = create("bytedance/seedance-2-5", inp)
    res, rc = wait(task, a.out)
    print(json.dumps(res, indent=2)); sys.exit(rc)


if __name__ == "__main__":
    main()
