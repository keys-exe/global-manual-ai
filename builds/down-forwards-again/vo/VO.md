# Doctor VO — §22U steps 2–12 (down-forwards-again)

**Voice takes (step 2):** G1–G3 via **Kie AI** `kling-3.0-omni/image-to-video` (user override for the Kling connector), start = D-VOICE-IMG v2
(approved by the user in chat), 10s, 1080p, audio on, `aspect_ratio: auto` (Kie requires it for single-frame i2v; the start frame is 9:16).
Kie tasks `1d02f25b…` / `0e057107…` / `07f5a960…`, 230 credits each (690). Output 1072×1928.

**Steps 3–5:** `voice_source.py D_G1.mp4 D_G2.mp4 D_G3.mp4 --name Down` → PASS: transcripts verbatim; pitch 135.6 / 129.0 / 141.6 Hz (max 4.9%);
speech 3.92 + 4.53 + 2.20s after ×1.2 = 10.65s, looped ×3 → **`Down_clone_source.mp3`, 32.0s**, no gap over 0.4s.

**Clone (steps 6–7):** `elevenlabs_clone.py clone` → **Down**, voice ID **`lLQRuUpi2CbzE9mw4WRD`**, noise removal on.

**Text (step 8):** `tts_enhanced.fitted.txt` (Enhance, verbatim lock PASS, 3,180 chars, rung 1, 15 tags).

**TTS (step 9):** ElevenLabs API, `eleven_v4`, one request per take (HK1+HK2+HK3+body), 4 takes:

| Take | Request | Raw | Transcript vs script (criterion 1, instrument only) | Split HK1 / HK2 / HK3 at |
|---|---|---|---|---|
| **T1** (working) | `z2yg7iSUZthidnljclxL` | 172.24s | "stretched"→"stretch" (possibly the transcriber: the d before "strap") | 12.29 / 21.13 / 28.32 |
| T2 | `vRYrVNbXhKVATUxGTNzb` | 169.12s | same as T1 | 12.17 / 20.71 / 27.64 |
| T3 | `fn8GkF7JJ6sq3t4nbLZK` | 173.04s | "do not"→"don't" | 12.35 / 21.06 / 28.54 |
| T4 | `5DVONDDOjFOKwxgVbRVh` | 167.76s | 5 changes ("I am"→"I'm", "round"→"around", "worn"→"warm", "do not"→"don't", "it is"→"it's") | 12.01 / 20.66 / 27.68 |

**House cut (step 10a):** `vo_trim.py` on all 16 parts (on the board as VO-T<n>-<PART>) and, per the one-go correction, **the whole T1 take in one pass**:
172.24 → **135.83s**, 30 breaths cut at phrase boundaries, no gap over 0.4s, tail −41.8 dB → PASS (`cut/T1.ALL.mp3`).
Cut points (`cut_points.py`): HK1 0–9.78 · HK2 9.78–16.87 · HK3 16.87–22.76 · BODY 22.76–135.83.
Pace: body ≈ 113s for 480 words ≈ **255 wpm** after the house cut (the cut removes air, not tempo) — faster than `VOICE-DOC`'s ~155 wpm target (F9).

**Step 10 — the master listen is yours.** T1 is the working take (no stop); confirm a different take on the board and I re-cut and redo the talking heads.

**Talking heads (steps 11–13, one go — user corrections 2026-09-28 on the stryde-thirty-years branch, applied here):** HeyGen photo avatar
`bd3f0bac586f197776acbda930af3599` from D-VOICE-IMG v2; **Avatar V**, audio = `T1.ALL.mp3` (asset `76f2445946d546f3ac67bd5cf6450a7b`), 9:16, 1080p.
`motionPrompt` rejected by Avatar V (no digital twin in the group — a generated doctor can never have one) → **Avatar V without it**, never Avatar IV.
Video `c48a6bc28ca8d4f342d089c62f9b04d1`. Then cut at the points above into TH-HK1+BODY, TH-HK2+BODY, TH-HK3+BODY; trim (step 14) after.
