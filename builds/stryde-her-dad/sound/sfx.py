"""§24M SFX for stryde-her-dad — one sound per generation (SFX-LINE), ElevenLabs text-to-sound (eleven_text_to_sound_v2)."""
import json, os, sys, urllib.request
from pathlib import Path
H = Path(__file__).parent
SFX = {
 "SFX-DRAWER-SHUT": ("a heavy wooden pine chest-of-drawers drawer pushed shut against stuffed contents, a dull wooden thud with a soft scrape, close-mic, small quiet bedroom", 1.5),
 "SFX-BOOT-SLAM": ("a hatchback car boot lid pulled down and slammed shut, a solid muffled thump heard from inside the car, the car body rocking slightly, close inside a parked car", 1.5),
}
for k in sys.argv[1:] or SFX:
    text, dur = SFX[k]
    req = urllib.request.Request("https://api.elevenlabs.io/v1/sound-generation", method="POST",
        data=json.dumps({"text": text, "duration_seconds": dur, "prompt_influence": 0.6, "model_id": "eleven_text_to_sound_v2"}).encode(),
        headers={"xi-api-key": os.environ["ELEVENLABS_API_KEY"], "Content-Type": "application/json", "Accept": "audio/mpeg"})
    (H / f"{k}_v1.mp3").write_bytes(urllib.request.urlopen(req, timeout=120).read())
    print(k, (H / f"{k}_v1.mp3").stat().st_size)
