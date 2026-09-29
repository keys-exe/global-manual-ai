# The maker's voice source — §22U steps 1–5 (stryde-thirty-years)

Step 1 image: `C1_step1_v1.png` (job `51f87b4b-2019-4585-9333-b484c691b777`, requested `nano_banana_pro`, logged `nano_banana_2`), confirmed by the user 2026-09-28.
Step 2: Kling `kling-video-v3_0_omni`, 10s, 1080p, 9:16, audio on, `prefer_multi_shots: false`, one render per call, `preflight.py` PASS on each (`C1_G*.call.json`). 360 Kling credits.

| Take | Kling generation | Line | After trim → ×1.2 | Pitch median | Gate | In the source |
|---|---|---|---|---|---|---|
| G1 | `ARzsxriJ_lHbVPOkWb5wa3yLA6LnBTnn4giDZFHkCyfJSy8BTptP6RtyB-56zoT8FYlaygrj` | HK1 "And if you do not believe me, I have spent thirty years making knee braces. Load is my job." | 5.25 → 4.37s | 125.0 Hz | ref | ✓ — Whisper (small and medium.en) hears an extra "job" after "knee braces" at 6.28s |
| G2 | `AWMv7eiQvm2FE_KQ2edZuTRqzLONQn9i4JGiDGz3KjkjWr3OxTzsiIvunad7kvfOTEXxjvpP` | HK2 "I have made knee braces for thirty years. I am about to talk you out of buying one." | 4.43 → 3.71s | 122.1 Hz | +2.3% | ✓ |
| G3 | `AQlZa26IRJiv0qr8byk_CeOslBDYH5tyd8j946rq7ppokkp2F9Mh2iwVcDFaddZ8u8PnmB9k` | P-001 "Seventeen times your bodyweight goes through one spot below your kneecap. Every step." | 5.25 → 4.40s | 137.9 Hz | **+10.3% FAIL** | ✗ never joined (§22U step 2). Not regenerated: G1 + G2 are the two takes §22U needs |

**`Thirty_clone_source.mp3`**: G1 + G2 joined (8.08s), looped ×4 = **32.37s**, no gap over 0.4s. Also on the board as `Thirty_clone_source.mp4` (the same mp3 stream in an mp4 container, because the board takes no .mp3).
Media files are git-ignored; the board holds the clips (15 MB byte parts) and the source.

**Step 6: HUMAN** (the connector has no clone call): ElevenLabs app → Voices → Instant Voice Clone → upload `Thirty_clone_source.mp3` → *Remove background noise* ON → name **Thirty** (if taken: `Thirty-Maker`) → send the voice ID.

**Step 8 ready:** `vo/ALL.tagged.txt`: HK1, HK2, HK3 and the body in one request, 12 tags, 2,354 chars, `tts_budget.py` verbatim lock **PASS**.
