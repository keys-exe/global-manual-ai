"""Send SC01 takes to Seedance on Kie from their call.json (background, one log per take)."""
import json, subprocess, sys
from pathlib import Path
K = "../../.claude/skills/ai-prompt-engineer/scripts/kie.py"
v = sys.argv[1]
for t in sys.argv[2:]:
    c = json.load(open(f"hooks/SC01/{t}.call.json"))
    a = ["python3", K, "seedance", "--prompt-file", f"hooks/SC01/{t}.prompt.txt", "--ref-image", *c["files"]]
    if c["audios"]:
        a += ["--ref-audio", *c["audios"]]
    a += ["--duration", str(c["duration"])]
    if not c["generate_audio"]:
        a += ["--no-audio"]
    a += ["--out", f"hooks/SC01/{t}_{v}.mp4"]
    subprocess.Popen(a, stdout=open(f"hooks/SC01/{t}.{v}.kie.log", "w"), stderr=subprocess.STDOUT, start_new_session=True)
    print(t, " ".join(a[3:]))
