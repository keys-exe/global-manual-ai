# Build notes: not-this-spot-revoice (STRYDE · Not This Spot, voice-over fix · Manual)

Read this first when resuming.

## Task
- **Drive folder (finished videos):** https://drive.google.com/drive/folders/1JyFFJVGv5gKIOvBxYpp2YZI5U_Qf7Fl0
  holds `Hook A.mp4`, `Hook B.mp4` and `Hook C.mp4`. Each is ~3:27, 1080×1920, 30 fps, with word-by-word captions burned in.
- **Script:** `NOT_THIS_SPOT.script.txt`, from the user's `NOT_THIS_SPOT.docx` ("C - VID | Doctor Demo | TOF | Doctor Authority | New | Not This Spot").
- **User's ask:** replace the voice-over in all three videos so it doesn't sound robotic.
- **User's choices (2026-09-28):**
  - Re-voice on the same timings, so the captions, B-roll cuts and doctor lip-sync all stay.
  - Keep the doctor's own cloned voice.
  - Keep "my knee" in the second review. The script's "me knee" is a typo (user, 2026-09-28).
- The build was made outside this repo; no earlier build folder matches it.

## Diagnosis of the old voice-over
- It ran at ~205 wpm with ~0.24s between sentences.
- Median pitch was 135 Hz, against the clone's natural 120 Hz, so it was sped up without pitch correction.
- Pitch spread was 4.71 semitones (flat).
- The videos have no music bed: the non-voice stem sits at −61 dB, so they are voice only.

## Method (`work/`)
1. **Split the voice from the track:** demucs htdemucs `--two-stems=vocals`.
2. **Transcribe the original:** whisper medium.en with word timestamps. Script units (`script.txt`) are aligned to the original, and each sentence's span is tightened to where the voice is audible (`revoice.py X plan`).
3. **Voice:** ElevenLabs **Doctor-NTS** `T8ewLtYUVAFApwsMjq9U`. It is the doctor's clone, with a speaker match of 0.895 (next-closest 0.78).
   - Model `eleven_multilingual_v2`, speed 1.1, read in ~250-character chunks with previous_text/next_text context. Chunks too slow for their slot were re-read at 1.2.
   - **Deviation from §4 / §22U (eleven_v4):** v4 ignores `speed`. Measured 152 wpm at speed 1.0 and at 1.15, and it can't reach the locked 205-wpm picture timing without a 35% squeeze, which is what made the old voice robotic. Multilingual v2 honours speed (219 wpm at 1.2).
4. **Build (`revoice.py X build`):** each sentence is cut from its chunk and placed on its original start.
   - For each sentence, the build uses whichever read (1.1 or 1.2) needs the least stretch.
   - Stretch is rubberband with pitch and formant kept, clamped at 0.87–1.15, except where the next sentence's start forces more.
   - Median tempo: A 0.968, B 0.966, C 0.986. The highest is 1.37, on short phrases in tight slots, e.g. "Let me show you where it goes."
   - `FORCE=18:s110` is used for B, because its 1.2 read said "warm part".
   - B chunk 10 was re-read because the old read said "The sleeve".
5. **Loudness:** matched to the original's integrated −19.4 LUFS (`mix.sh`).
6. **Verify (`verify.py`):** all three match the script word for word; the only differences are spellings (Stryde/stride, centimetres, orthopaedic). Sentence start drift has a median of 0.03s.
7. **Lip-sync:**
   - The doctor's on-camera shots (`th.json`: 9 per video) were cut frame-exact and joined with the new audio (`thclip.py`).
   - HeyGen `create_lipsync`, precision mode, one job per video:
     - A: `23e0c2de67cf4258aabe31628fb4c04c`
     - B: `a762d6d36ccd49f3817379732fd8a0d5`
     - C: `573416da45ed4a9f8fa5685f4d1173a3`
   - `splice.py` puts the lip-synced frames back over the original frames and re-encodes with x265 at CRF 17.

## Files not in git (scratchpad; regenerate with the scripts above)
- The drive videos, demucs stems, TTS chunks (`gen/`) and mixes.
- The old "me knee" reads are kept as `gen/*_cNN.me.mp3`.
