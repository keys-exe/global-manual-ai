"""Wait for HeyGen videos and download them: heygen_wait.py NAME=VIDEO_ID ... -> th/v6/NAME.mp4"""
import json, os, sys, time, urllib.request
K = os.environ["HEYGEN_API_KEY"]
todo = dict(a.split("=") for a in sys.argv[1:])
while todo:
    for name, vid in list(todo.items()):
        req = urllib.request.Request(f"https://api.heygen.com/v1/video_status.get?video_id={vid}", headers={"X-Api-Key": K})
        try:
            d = json.load(urllib.request.urlopen(req, timeout=60))["data"]
        except Exception as e:
            print(name, "poll error", e, flush=True); continue
        if d["status"] == "completed":
            urllib.request.urlretrieve(d["video_url"], f"th/v6/{name}.mp4")
            print(name, "done", d.get("duration"), d["video_url"][:80], flush=True); todo.pop(name)
        elif d["status"] == "failed":
            print(name, "FAILED", d.get("error"), flush=True); todo.pop(name)
    if todo: time.sleep(30)
