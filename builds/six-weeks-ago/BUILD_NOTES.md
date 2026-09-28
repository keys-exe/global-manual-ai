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

## Open
- Board file store is capped at 1 GB: FINAL-HK1 (703 MB, 47 parts) + music are on the board. HK2 and HK3 (~700 MB each) rendered but not on the board — 21 HK2 parts (315 MB) uploaded before the cap hit are orphans. Delivery route for HK2/HK3 is the user's call.
- Old SFX/room tone went with the old music (isolator keeps voice only). Add room tone/SFX per §24M if the user wants them back.
