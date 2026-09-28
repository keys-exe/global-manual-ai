import sys, subprocess, json
from faster_whisper import WhisperModel
m=WhisperModel("small.en",compute_type="int8")
B="https://d8j0ntlcm91z4.cloudfront.net/user_3E7WMFD8fj8yU5aCHYXh86ZLzxV/"
for arg in sys.argv[1:]:
    beat,url=arg.split("=",1)
    subprocess.run(["curl","-sSL","-o",f"renders/{beat}.mp4",url if url.startswith("http") else B+url],check=True)
    subprocess.run(["python3","../../.claude/skills/ai-prompt-engineer/scripts/contact_sheet.py",f"renders/{beat}.mp4","--frames","8","--out",f"qa/{beat}.sheet.jpg"],capture_output=True)
    segs,_=m.transcribe(f"renders/{beat}.mp4",word_timestamps=True)
    ws=[(w.word.strip(),round(float(w.start),2),round(float(w.end),2)) for s in segs for w in s.words]
    print(beat, ws)
