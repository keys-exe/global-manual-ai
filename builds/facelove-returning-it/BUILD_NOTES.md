# BUILD_NOTES — facelove-returning-it

**FACELOVE Changing Foundation Stick · "I'm returning it" (fake-out return)** · Mode 1 Photorealistic · UGC Ad (to-lens creator: talking heads + B-roll) · **RUN: MANUAL** · started 2026-10-02 (standards V7.91.3) · GitHub account of the session: `Chicknben` (not the owner — no system changes, no lessons)

Drive task folder `1PvwdhVU13RI6M1GQi9GKy-aEdx_4XZSa`

## Boards
- Current https://claude.ai/artifact/XvBf5D1NNmCN9XAkq4pDfs
- Old https://claude.ai/artifact/TtJDHH94bKokmwcYsVCgqK
- Final https://claude.ai/artifact/Ryuk4diTvt4cmAkjn6kKss
- Plan https://claude.ai/artifact/7HqDH14C4dtjNtJSddmF1C
- Hourly Fix check: `trig_014eDNABLMENQ1wepZFirNg6`, :04 UTC, session_0122FPw9TWDcn1Mf8QgSiudw

## Where it stands (2026-10-02)
- Steps 1–3 delivered: Absorption Sheet, phrase inventory + Visual Instruction Ledger (VN00–VN05, scene labels only), claims pass, Mode & Model Lock → `BUILD_SHEET.md`; board docs `absorption`, `connectors` on Plan + Current.
- 2 cast sheets (N-BEFORE bare skin, N-AFTER foundation on, lines kept) on Sunburst 2k via Higgsfield ODAQ B.V., `avatar.png` attached as Image 1 (F1); ~2.75 credits each (the shared ODAQ balance moved 4,801.34 → 4,548.14 meanwhile — other sessions spend on it too). On the Current board **To check**.
- **Avatar review (user: "confirm and fix", 2026-10-02):** N-AFTER v1 confirmed on the board. N-BEFORE Fix round 1 (owner-marked note "add wrikles"): the wrinkles named deep and counted in `cast/build_sheets.py` (AGE_V2 + a sentence in the sheet: deep crow's feet, three forehead lines, two frown lines, deep nose-to-mouth folds, mouth-corner and upper-lip lines, neck lines); v2 (job 8861a293, ~2.75 cr) on the Current board To check; v1 moved to the Old board (asset 494a8798…) and removed from Current.
- Note for the user: N-AFTER was confirmed with v1's lighter lines; the after keeps "every line", so if v2's deeper wrinkles are confirmed, the after face may read less lined than the before — their call (a Fix on N-AFTER would match it).
- Still waiting: N-BEFORE v2 Confirm/Fix, and the flags F1–F9.

## Steps 4–5 (2026-10-02, user: "confirm and proceed" — N-BEFORE v2 and N-AFTER v1 confirmed)
- 5 plates at 16:9 (P-HOME hall, L-VANITY the talking-head set, L-COUNTER, L-CAFE, L-FRONT) + 2 side-cast sheets (C1-COUNTER, C2-FRIEND), Sunburst 2k, ODAQ B.V., ~2.75 cr each, on the Current board To check.
- `STEP4_5.md`: location pass, property sheet PROP-H (San Antonio ranch house), light plans, act map (24 rows: 16 B-roll, 8 TH; hooks at step 6), wardrobe per story day (D0 counter, D1 café, D2 grocery morning, REC today), Visual Pitch (heroes B02, B06, B12, B13, B16), music register map (no music bed — the inspo has none).
- Checks: angles.py PASS · wardrobe.py PASS · visual_plan.py PASS. Board: 24 planned beat cards; Plan docs locations, actmap, wardrobe, visualplan, music.
- Flags F3/F7/F8/F9 unanswered — held on the defaults (3 hooks, voiced as written, avatar hair).

## Voice stage (§22U) — started 2026-10-02
- Talking-head frames (step 1), propped on the vanity = the L-VANITY plate's viewpoint, refs L-VANITY + her sheet: **N-VOICE-IMG** (finished face, the body; job f93cb289) and **N-VOICE-IMG-B** (bare face, the hooks; job 99d3f3a6). Sunburst 2k. On the board To check.
- Enhance text for Hook 1 + body in one request: `vo/ALL.enhanced.txt` (1,715 chars, `tts_budget.py` verbatim PASS, 30 tags, [slowly] per paragraph, [pause] at sentence ends). ElevenLabs check PASS (1,425 free slots).
- Kling voice takes built (`voice/N_G1.call.json` "I am so mad…" 18 words, `N_G2` "And it is not because it goes on pure white…" 17 words; kling3_0 via Higgsfield, pro, 10 s, sound on): `preflight.py` PASS except **start image approved** — §22X: no paid video call before the user's Confirm of N-VOICE-IMG. Stopped there.
- Higgsfield ODAQ B.V. balance 3,828.24 (shared — other sessions spend on it).

- **Voice run (user: "confim and proceed", all plates, C1/C2 and both talking-head frames confirmed):** Kling voice takes G1 (job 50479076) and G2 (job 28d5e439) on kling3_0 via Higgsfield (pro, 10 s, sound on, 25 cr each; Higgsfield's "IN THE DARK" preset declined, prompts sent as written), both heard back verbatim. `voice_source.py` PASS (210.5 / 197.5 Hz, 6.2%) → 32.3 s → **cloned `Returning` = 9dP3DgqW7TL53p7rTcnP**. `eleven_v4` × 4 at speed 0.9 from `vo/ALL.enhanced.fitted.txt`: T1 90.4 s 190 wpm, T2 189, T3 188, T4 184 — every word present (Whisper writes 60% / 30-day as digits), last word rings out (≤ −84 dB). **T1 = working take.**
- Talking heads: HeyGen photo avatars in one group `90b3886990976ec37c37ddb387fe77a3` — finished face `90b3886990976ec37c37ddb387fe77a3`, bare face `77a6a5e47453baaaab6b6cd4da2a4f4a`. Two looks, so the untrimmed T1 is split once at the hook/body gap (`cut_points.py`, 13.38 s) and rendered as two passes: TH-HK1 on the bare face (video 7ee1d97b), TH-BODY on the finished face (video 7fc276ea). Avatar V rejected `motionPrompt` (no digital twin in the group) → §22U fallback (c): Avatar V without it, never Avatar IV.

## Decisions
- Mode 1 + UGC Ad from the inspo (no MODE/FORMAT in the message) — F2. Hooks 3 by default — F3.
- The inspo file came with no extension (`inspo video`) — renamed `intake/inspo.mp4` and measured as the primary.
- Product sheet byte-identical to `facelove-my-mother`'s.
- Connectors: Kling via Higgsfield (rung 3); images Higgsfield ODAQ B.V.; ElevenLabs API key present; HeyGen connected.

## For the owner (keys-exe) — not made from this account
- Add this build's row to the CLAUDE.md board table (four links above) and the Routine line (`trig_014eDNABLMENQ1wepZFirNg6`, :04 UTC).
- `fetch_drive.py` leaves an extension-less video ("inspo video") unsorted; it could sniff the file type.

## Next (on the user's go)
Steps 4–5: the location plate 16:9 (her room — the talking-head set), product info cards, act map by phrase with the Visual Pitch, angles, wardrobe (one recording day), music register map, placement — then the voice (§22U) and talking heads.
