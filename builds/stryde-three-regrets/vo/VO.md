# Narrator VO — §22U steps 6–10 (stryde-three-regrets)

**Clone (steps 6–7):** by API on the user's instruction (2026-09-28: "you will be the one to clone and create the talking heads").
`Regrets` · voice ID **`OxNH6H9HajjAxTXIVONJ`** · source `voice/Regrets_clone_source.mp3` v2 (G1+G2+G4, 38.09s) · noise removal on.

**Text (step 8):** `tts_tagged.txt` = HK1, HK2, HK3, body in script order, one request (one voice across hooks and body).
Lock against `work/script.lines.txt`: **PASS** · 3,663 chars · rung 1 · 15 tags from `TAG-PALETTE`.

**TTS (step 9):** ElevenLabs connector, `eleven_v3`, 4 takes, flow `O1rxzq3NBuTTEQlgN7gg` (~3,663 credits each, ~14,651 total).

**Split** (`split_vo.py`, medium.en): word diff against the whole script (transcriber spelling/homophone noise normalised:
25,000/200,000, body weight, post bag, stride, US spellings, draw/drawer, bear/bare), cut in the middle of the silence after each hook.

| Take | Generation | Raw | Words (criterion 1) | Ending (criterion 4) | HK1 / HK2 / HK3 / Body after house cut |
|---|---|---|---|---|---|
| **T1** | `vFHSBvN0Nx0VnjYeM4sK` | 216.4s | verbatim | complete, −85.5 dB | 6.13 / 7.14 / 7.92 / 151.61s |
| **T2** | `uJ7gJb0q3e9uTepRCJVK` | 206.4s | verbatim | complete, −65.6 dB | 6.22 / 7.53 / 8.39 / 153.49s |
| T3 | `nid7HoOO0s3x7biVZS4q` | 197.4s | **2 changes:** "round" → "around", "stretched" → "stretch" | −47.8 dB (borderline) | 6.14 / 6.99 / 7.97 / 147.47s |
| T4 | `uzOAGceZFT1tJLSieKp9` | 208.2s | verbatim | **cut off**, −39.8 dB (final "stairs") | 6.12 / 7.12 / 8.31 / 153.10s |

**House cut (step 10a):** `vo_trim.py` on all 16 parts — every one PASS (no breaths left, no gap over 0.4s).
Pace: the body is ~151s for 580 words ≈ **230 wpm**, faster than `VOICE-NARR`'s ~185 wpm; each variant ≈ 2:37–2:41.

**Step 10 — the master listen is the user's.** Instruments pass T1 and T2 on both criteria; T3 fails (1), T4 fails (4).
The master, once picked, is built per variant as raw HKn + raw BODY of the same take, trimmed in one pass.
