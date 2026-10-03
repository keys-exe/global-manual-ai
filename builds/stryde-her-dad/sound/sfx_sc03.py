"""§24M SC03 re-score (2026-10-03 Fix: "change the sound make it like suit on these video", "add a sound based of these video").
One sound per generation (SFX-LINE / ROOM-TONE), ElevenLabs text-to-sound eleven_text_to_sound_v2. Placed by mix_sc03.py on the frames."""
import json, os, sys, urllib.request
from pathlib import Path
H = Path(__file__).parent / "sc03"
SFX = {
 "TONE-BEDROOM": ("quiet suburban British bedroom room tone, closed window, very faint distant traffic and birds outside, soft air, no music, no voices", 6.0),
 "SFX-SLEEVES-RUMMAGE": ("an old man's hands rummaging through a wooden drawer full of soft knitted fabric knee sleeves and supports, cloth rustling and shifting, close-mic, no voice", 3.0),
 "SFX-DRAWER-SHUT": ("a pine chest-of-drawers drawer slid slowly shut on wooden runners, a dry wooden slide ending in a dull heavy wooden thud, close-mic, quiet bedroom", 1.6),
 "SFX-EXHALE-TONY": ("a tired old man's long slow heavy exhale through the nose, resigned, close-mic, quiet room, no words", 1.6),
 "TONE-HALL": ("quiet carpeted house hallway and staircase room tone, soft indoor air, a faint distant clock, no music, no voices", 8.0),
 "SFX-STAIR-STEP": ("one single heavy footstep of a work boot landing slowly on a carpeted wooden stair, a soft muffled thud with a faint wooden creak", 0.8),
 "SFX-HANDRAIL-GRIP": ("a hand gripping and sliding slowly along a varnished wooden staircase handrail, skin squeaking on the wood, the rail creaking under weight, close-mic", 3.0),
 "SFX-BREATH-STRAIN": ("an old man's strained, careful breathing going slowly down stairs on painful knees, short held breaths and pained exhales, quiet, no words", 8.0),
 "TONE-CAR-INT": ("inside a parked car with the engine off and the windows closed, muffled supermarket car park outside, distant trolleys and cars, quiet cabin air, no music, no voices", 9.5),
 "SFX-BAGS-BOOT": ("paper and plastic shopping bags rustled and set down one by one into an open hatchback car boot, heard from inside the car, muffled, the car body dipping slightly", 4.5),
 "SFX-STEP-NAT-A": ("one single slow, careful footstep: a heavy man in worn leather work boots lowering his foot down onto a carpeted stair, a soft, natural, muffled thud of the sole on carpet, no creak, no echo, close and dry", 0.7),
 "SFX-STEP-NAT-B": ("one single heavy footstep: a man's work boot set down slowly onto thick stair carpet, a dull soft natural thump with a faint brush of the sole, no creak, no echo, close and dry", 0.7),
 "SFX-STEP-NAT-C": ("one single cautious footstep: a stiff leg in a leather work boot placed down onto a carpeted step, a quiet natural muffled tap and settle of weight, no creak, no echo, close and dry", 0.7),
 "SFX-STRAIN-TONY": ("an old man's short closed-mouth grunt of effort and pain through the nose while pushing hard, a tight strained 'mmh', lips sealed, close-mic, quiet room, no words", 1.0),
 "SFX-SHUFFLE-STAIR": ("a work boot shifting its weight on a carpeted stair without lifting, a faint soft scuff of sole on carpet, close and dry, no creak", 0.6),
 "TONE-CAR-QUIET": ("inside a parked car with the engine off and the windows closed, a still quiet cabin, a faint low wind outside, no traffic, no cars, no voices, no music", 9.5),
 "SFX-SEAT-SETTLE": ("a heavy man shifting slightly in a cloth car seat, a soft fabric rustle and a faint seat creak, close inside a quiet car", 0.6),
 "SFX-SIGH-NOSE-TONY": ("an old man's single slow, quiet, resigned breath out through the nose, mouth closed, close-mic in a quiet car, no words, no groan", 1.6),
 "SFX-BREATH-IN-DEEP": ("an old man's single slow deep breath in through the nose, mouth closed, the chest filling, close-mic in a quiet parked car, no words, no voice", 1.6),
 "SFX-BREATH-OUT-LONG": ("an old man's single long, slow, heavy breath out through the nose, mouth closed, tired and resigned, steady to the end, close-mic in a quiet parked car, no words, no groan", 3.4),
 "SFX-BREATH-SOFT": ("an old man's soft, shallow, quiet breath in and then out through the nose, mouth closed, close-mic in a quiet parked car, no words", 2.0),
 "SFX-BOOT-SLAM": ("a hatchback car boot lid pulled down and slammed shut, a solid muffled thump heard from inside the car, the cabin rocking slightly", 1.5),
}
for k in sys.argv[1:] or SFX:
    text, dur = SFX[k]
    out = H / f"{k}_v1.mp3"
    if out.exists(): print(k, "exists"); continue
    req = urllib.request.Request("https://api.elevenlabs.io/v1/sound-generation", method="POST",
        data=json.dumps({"text": text, "duration_seconds": dur, "prompt_influence": 0.6, "model_id": "eleven_text_to_sound_v2"}).encode(),
        headers={"xi-api-key": os.environ["ELEVENLABS_API_KEY"], "Content-Type": "application/json", "Accept": "audio/mpeg"})
    out.write_bytes(urllib.request.urlopen(req, timeout=120).read())
    print(k, out.stat().st_size)
