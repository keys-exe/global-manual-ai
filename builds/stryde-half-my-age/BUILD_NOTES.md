# stryde-half-my-age — build notes

- **Task:** "A - VID | AI Drama VSL | TOF | Discovery Story | Iteration | HalfMyAge Drama" — Drive `1R1jJrUhMjPzbIsbM3fmXdJUpxnu48iOT`
- **Run:** **Manual**, **Mode 4 — Realistic Film**, AI Drama VSL (§3B), 9:16, Seedance 2.5 on Kie at 720p. Standards V7.74.2 (default branch; the user asked for "the updated branches" — no branch carries newer standards).
- **Boards:** Current https://claude.ai/artifact/RrQR9jKnsbqT6v8uJMbqR2 · Old https://claude.ai/artifact/SXWuEkNiYcdetxvhetCFaZ · Final https://claude.ai/artifact/FH22SWdaLRACaGTyS92KpH · Plan https://claude.ai/artifact/UK75G7UMCa1sSmvwJQFWJo
- **Hourly Fix check:** `trig_018sxCBh92CESZPjxJZLiUJr`, :42 UTC, bound to session_01ATkDYk1GiEuqTMW9L5VV4H.

## State (2026-09-30)
- Steps 1–3 delivered (`BUILD_SHEET.md`): Absorption Sheet, Film Look Sheet (`LOOK-HALFMYAGE`, `edit/LUT-HALFMYAGE.cube` PASS), Visual Instruction Ledger VN01–VN26, phrase inventory L001–L074, claims, Mode & Model Lock.
- **Seven cast sheets** on the Current board as To check (Sunburst, 2.75 cr each): N-HER, C1-BARBARA, C2-DAUGHTER, C3-HUSBAND, C4-SISTER, C5-FRIEND1, C6-FRIEND2. **Waiting on the user's avatar decision** (§18B).
- Absorption on the Plan board (`docs/absorption`, not yet confirmed).
- Product: repo sheet V7.49.38 kept (the Drive's V7.49.32 is older); new ref `back_ref_v2.png` added to `products/stryde/stryde_refs/`.

- 2026-09-30 Fix round 1: C5-FRIEND1 "I WANT A NEW ONE HERE" → new casting v2 (white Irish woman, 69, copper-red crop, navy pea coat; Sunburst 2.75 cr); v1 moved to Old. Other six sheets still To check.

- 2026-09-30 **Cast confirmed** (user: "CONFIRMED ALL PROCEED"); absorption confirmed. Steps 4–5 delivered (`STEP4_5.md`): Property Sheet, 12 plates (16:9, Sunburst 2.75 cr each) To check, act map 89 shots (`angles.py` PASS), Scene Bibles, wardrobe map, ingredient ledger. Flags F6/F8/F9/F10 run on my recommendations.
- 2026-09-30 **Voice stage:** 7 §24I voice masters on Kie Seedance (10s, **630 Kie credits each**, 4,410 total); narrator clone `HalfMyAge` (voice_id m8paURpcIo2oNWLiWDYk, from HER's tightened master); 29 narration takes (eleven_v4, verbatim PASS, no pause tags, speed 1.0) on the board as `VO-T1-Lxxx`.
- 2026-09-30 **Fix round 2 (user):** "FIX THE LOCATION" → L-STAIRS "FIX THIS ITS DISTORTED": v2 prompt (35mm, level camera, straight verticals, distortion negatives) — **Higgsfield timed out on submit and on every call after; outcome unknown** → card back on `regenerate` with a `fixPlan`; the hourly check checks Higgsfield for a finished stairs plate before resubmitting. "THE VOICE HAS A LOT OF DEAD SPACE" → the masters spoke 1–7s of each 10s clip: idle silence cut from all 7 (raw kept as `voice/*_raw.m4a`, v2 on the cards), narration re-voiced without pause tags; §24I amendment in Pending Amendments + `preflight.py` voice_master duration-fit check.

## Open (Flags in BUILD_SHEET.md)
F1, F2, F4 claims to confirm · F8 Hook E's action (proposed: HER gets up off the living-room floor unaided as the daughter reaches to help) · F9 "Three weeks ago" vs six weeks · F10 trouser-leg reveal vs FP13 · F6 right knee default · F11 mechanism insert optional · F12 no to-lens close · F16 no Drive connector.

## Next
On the user's go: steps 4–5 (property sheet + 16:9 plates, scene list + Scene Bibles, act map + wardrobe map, ingredient lists, `angles.py`), then §24I voice masters, then hooks one by one on Seedance.
