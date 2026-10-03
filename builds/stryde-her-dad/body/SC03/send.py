"""Send SC03 takes to Seedance on Kie from their call.json (background, one log per take)."""
import json, subprocess, sys
from pathlib import Path
K = "../../.claude/skills/ai-prompt-engineer/scripts/kie.py"
v = sys.argv[1]
for t in sys.argv[2:]:
    c = json.load(open(f"body/SC03/{t}.call.json"))
    imgs = [f for f in c["files"] if not f.endswith(".mp4")]
    vids = [f for f in c["files"] if f.endswith(".mp4")]
    a = ["python3", K, "seedance", "--prompt-file", f"body/SC03/{t}.prompt.txt", "--ref-image", *imgs]
    if vids:
        a += ["--ref-video", *vids]
    if c["audios"]:
        a += ["--ref-audio", *c["audios"]]
    a += ["--duration", str(c["duration"])]
    if not c["generate_audio"]:
        a += ["--no-audio"]
    a += ["--out", f"body/SC03/{t}_{v}.mp4"]
    subprocess.Popen(a, stdout=open(f"body/SC03/{t}.{v}.kie.log", "w"), stderr=subprocess.STDOUT, start_new_session=True)
    print(t, " ".join(a[3:]))
