# six-weeks-ago — STRYDE · "Six Weeks Ago" (AI Drama) — BGM replacement

**Drive (intake):** `13RSuqtkClewZFp9YzV_kSLj6e7l_kdgd` — "C - VID | AI Drama | TOF | Refusing Help | Iteration | Six Weeks Ago": three finished videos (HOOK 1/2/3, 1080×1920, 30 fps, ~9:28–9:30).
**Board:** https://claude.ai/artifact/QD4ZSJz5eWVGnRAqDQDesA
**Ask (user, 2026-09-28):** remove the BGM and replace it with music that fits every scene. Run mode: Manual (default).

## Structure (measured)
- Every variant = its own hook + one identical body. The body's first frame (stairlift brochure) is at HK1 17.533 s, HK2 15.467 s, HK3 14.900 s (frame diff = 0 after it).
- Body scenes (HK1 time, cut-aligned): SC01 kitchen w/ Sarah 17.53 · SC02 night/Frank 84.43 · SC03 wedding 106.20 · SC04 Barbara's kitchen 138.03 · SC05 stairs w/ Barbara (turn) 321.50 · SC06 doctor 369.70 · SC07 hallway w/ Frank 405.93 · SC08 stairs w/ Sarah (mirror) 455.13 · SC09 the dance 505.33 · SC10 call to Joan (close) 529.67 → 570.52.

## What was done
1. Dialogue isolated with the ElevenLabs Voice Isolator: HK1 full, HK2/HK3 hooks only (body reused from HK1). Sync vs original ±5 ms. This also removes Seedance room tone/SFX — gaps between lines are clean silence under the new music.
2. One music cue per scene + one per hook (`sound/*.cue.json`, §24M sections on cut cues; theme: intimate British family-drama score, felt piano + string quartet, no drums/synths/vocals). 13 tracks, `music.py compose`, one generation each.
3. `music.py check`: every flag was a lead-in silence, the natural tail or a piano-note attack — except energy order (SC03, SC05, SC06, SC09, SC10) and SC05's silent turn not silent. Fixed in the mix with section gain automation (`mix_gain_db`), not recomposed. Turn silence measured −85 dB for 3.8 s.
4. `sound/mix_film.py HK1|HK2|HK3`: every cue levelled, music −18 dB under dialogue, ducked 8 dB under speech, cues start on scene cuts (outgoing faded 0.8 s), −14 LUFS / −1 dBTP, picture stream copied untouched. Results: −14.2 / −14.1 / −14.1 LUFS; body audio identical across variants (corr 1.0).

## Delivery
- Main board (music cards + FINAL-HK1): https://claude.ai/artifact/QD4ZSJz5eWVGnRAqDQDesA
- A board's file store holds 1 GB. User chose overflow boards (2026-09-28): FINAL-HK2 → https://claude.ai/artifact/R56ud78WXoJJ5KqsUNWf3W · FINAL-HK3 → https://claude.ai/artifact/3NhxkJc513PzEWBmu11sK1 (same template; the main board's HK2/HK3 cards link there via `videoUrl`).
- HK3 part40 began with a `<` byte and was refused as markup; that byte was moved to the end of part39 (15,000,001 / 14,999,999 bytes). The joined file's MD5 matches the render.
- All three finals: status `review`, waiting on the user's check.

## v2 — room tone and sound effects back (user, 2026-09-28: "add the room tone and sound effects back")
- The isolator had removed Seedance's room sound and effects with the music; they cannot be split back out of the old mix, so they were rebuilt per §24M: `sound/sound_plan.json` (7 location room tones, 9 SFX objects, 22 placed events), made by `sound/fx.py` (ElevenLabs `eleven_text_to_sound_v2`, one call each, tones looped), mixed by `sound/mix_film.py` (`ambience()`: tone per scene/hook location, changed only at cuts; room tone ~30 dB under dialogue, wedding hall and station +8/+9 dB; SFX on their frames).
- Actions pinned from a 1 fps contact sheet of the whole film plus 10 fps strips at the key moments (HK3 plate smash 1.3s, fall on the 5.6s cut; HK2 sneaker steps 9.45/10.05; slipper step 336.45; strap 285.5…).
- Checks: tones steady (p95−p50 ≤ 5 dB), no words; SFX-CHAIR-SIT flagged 2 words by whisper on a 1s noise file (likely false; noted on its card). Levels per scene: tone −30 dB vs dialogue (wedding −22). Finals −14.1/−14.2 LUFS, peak ≤ −0.4 dBFS; body identical across variants (corr ≥ 0.9998).
- Board: 16 sound cards on the main board (TONE-*, SFX-*), status review. v2 finals on three new overflow boards (Hook 1 RL8KTniZLFyLxFPtfoFBgN · Hook 2 RkjU4VbYoV5nnkoJaKhms5 · Hook 3 BzZEiQFZYtVYKWQXFomiif), each card keeping v1 as version 1 (link) and v2 as version 2; main-board FINAL cards link v2 via `videoUrl`. v1 kept on its boards.
- With the user's OK, the 24 unreferenced HK2 pieces (360 MB) on the main board were deleted to make room (checked against every live card first).

