#!/usr/bin/env python3
"""§22U steps 6-7 — ElevenLabs Instant Voice Clone over the API (E7).

Needs ELEVENLABS_API_KEY in the environment (an environment secret; never pasted in chat).
The ElevenLabs connector has no clone call, so this is the clone route.

  elevenlabs_clone.py check                               -> plan, IVC allowed, free voice slots
  elevenlabs_clone.py clone FILE --name KEYWORD [--min 30] [--no-denoise]
  elevenlabs_clone.py get VOICE_ID
  elevenlabs_clone.py delete VOICE_ID

clone runs `check` first, refuses a source under --min seconds (E1: a source under
30s is never uploaded), uploads with remove_background_noise on, then reads the
voice back to confirm it exists. FILE is the step-5 <Keyword>_clone_source.mp3.
Every command prints JSON. Exit 0 = success, 2 = refused / check failed, 1 = error.

Setup (per session): pip install imageio-ffmpeg
"""
import argparse, json, os, subprocess, sys, urllib.error, urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from trim import duration  # noqa: E402

API = "https://api.elevenlabs.io/v1"


def key():
    k = os.environ.get("ELEVENLABS_API_KEY")
    if not k:
        sys.exit(json.dumps({"error": "ELEVENLABS_API_KEY is not set in the environment"}))
    return k


def call(method, path):
    req = urllib.request.Request(f"{API}{path}", method=method, headers={"xi-api-key": key()})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        sys.exit(json.dumps({"error": f"HTTP {e.code} on {method} {path}",
                             "response": e.read().decode(errors="replace")[:1000]}))


def subscription():
    s = call("GET", "/user/subscription")
    return {
        "key_set": True,
        "tier": s.get("tier"),
        "status": s.get("status"),
        "can_use_instant_voice_cloning": s.get("can_use_instant_voice_cloning"),
        "voice_slots_used": s.get("voice_slots_used"),
        "voice_limit": s.get("voice_limit"),
        "free_voice_slots": (s.get("voice_limit") or 0) - (s.get("voice_slots_used") or 0),
        "voice_add_edits_left": (s.get("max_voice_add_edits") or 0) - (s.get("voice_add_edit_counter") or 0),
    }


def check_ok(c):
    return bool(c["can_use_instant_voice_cloning"]) and c["free_voice_slots"] > 0 \
        and c["voice_add_edits_left"] > 0


def cmd_check(a):
    c = subscription()
    c["status_check"] = "PASS" if check_ok(c) else "FAIL"
    print(json.dumps(c, indent=2, ensure_ascii=False))
    sys.exit(0 if check_ok(c) else 2)


def cmd_clone(a):
    src = Path(a.file)
    if not src.is_file():
        sys.exit(json.dumps({"error": f"no such file: {src}"}))
    c = subscription()
    if not check_ok(c):
        print(json.dumps({"status": "REFUSED", "reason": "account cannot clone", "check": c}, indent=2, ensure_ascii=False))
        sys.exit(2)
    secs = duration(src)
    if secs < a.min:
        print(json.dumps({"status": "REFUSED", "reason": f"source {secs:.2f}s < {a.min}s (§22U step 5)",
                          "file": str(src)}, indent=2, ensure_ascii=False))
        sys.exit(2)

    # multipart upload through curl (same route as kie.py upload)
    out = subprocess.run(["curl", "-sS", "-m", "300", "-X", "POST", f"{API}/voices/add",
                          "-H", f"xi-api-key: {key()}",
                          "-F", f"name={a.name}",
                          "-F", f"files=@{src}",
                          "-F", f"remove_background_noise={'false' if a.no_denoise else 'true'}",
                          "-F", f"description={a.description}"],
                         capture_output=True, text=True)
    try:
        d = json.loads(out.stdout)
    except json.JSONDecodeError:
        sys.exit(json.dumps({"error": "clone failed", "stdout": out.stdout[:1000], "stderr": out.stderr[:500]}))
    if "voice_id" not in d:
        sys.exit(json.dumps({"error": "clone failed", "response": d}))

    v = call("GET", f"/voices/{d['voice_id']}")
    print(json.dumps({
        "status": "PASS",
        "voice_name": v.get("name"),
        "voice_id": d["voice_id"],
        "category": v.get("category"),
        "requires_verification": d.get("requires_verification"),
        "source": str(src),
        "source_s": round(secs, 3),
        "remove_background_noise": not a.no_denoise,
    }, indent=2, ensure_ascii=False))


def cmd_get(a):
    v = call("GET", f"/voices/{a.voice_id}")
    print(json.dumps({k: v.get(k) for k in ("voice_id", "name", "category", "description")}, indent=2, ensure_ascii=False))


def cmd_delete(a):
    d = call("DELETE", f"/voices/{a.voice_id}")
    print(json.dumps({"status": "DELETED", "voice_id": a.voice_id, "response": d}, indent=2, ensure_ascii=False))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check").set_defaults(fn=cmd_check)
    p = sub.add_parser("clone")
    p.add_argument("file")
    p.add_argument("--name", required=True, help="voice name: one keyword from the script title (§22U step 7)")
    p.add_argument("--min", type=float, default=30.0)
    p.add_argument("--no-denoise", action="store_true")
    p.add_argument("--description", default="§22U clone")
    p.set_defaults(fn=cmd_clone)
    for name, fn in (("get", cmd_get), ("delete", cmd_delete)):
        p = sub.add_parser(name)
        p.add_argument("voice_id")
        p.set_defaults(fn=fn)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
