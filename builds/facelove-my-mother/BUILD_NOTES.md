# BUILD_NOTES — facelove-my-mother

**FACELOVE Changing Foundation Stick · "YOU LOOK LIKE MY MOTHER"** · Mode 4 Realistic Film · AI Drama VSL · **RUN: MANUAL** · started 2026-10-02 (standards V7.90.7) · GitHub account of the session: `Chicknben` (not the owner — no system changes, no lessons)

Drive task folder `1M1DbzCv_DwDnXnhwkztLtgEB69yjBUiZ` · cast pictures `1__Tfn0-oRlpOnPL9ev8zfii2Q9vAcqT0`

## Boards
- Current https://claude.ai/artifact/Gyh667QAbW2fA3GYgjgM23
- Old https://claude.ai/artifact/KZ2UKhTA7GAysVcfgj7K41
- Final https://claude.ai/artifact/1NUkwd9icgtPGXenBTr5Ah
- Plan https://claude.ai/artifact/VmUne7ypBrBQa52jVqXRrs
- Hourly Fix check: `trig_01XaBTxvhuhW64zeHnySBmKR`, :52 UTC, session_01J4zbJqsKjmgPFMHmw3ibaJ

## Where it stands (2026-10-02, Hook 1 To check — user: "PROCEED")
- **Voices (§24I):** six neutral film voice masters on Seedance 2.5 via Higgsfield (omni_reference, 720p; duration fitted to the words; 459.4 credits): Susan 17.8 s, Greg 18.1 s, Beth 14.0 s, Paula 8.6 s, Friend A 5.0 s, Friend B 6.8 s of speech — audio stream-copied, only the outer idle silence cut (0.4 s / 0.5 s). All words heard back; Greg's "Paula's" transcribed as "Paul is" — flagged on the card. `voice/build_masters.py`, `voice/process_masters.py`, `voice/masters.json`. All To check (stage Voice).
- **Narrator clone** `Mother` (ElevenLabs IVC, voice_id `Keqdw9ZWsMjWZgsJl2h0`) from Susan's master looped whole to 35.8 s. Five narration takes VO-T1-L008/L009/L021/L026/L027 (eleven_v4, speed 1.0, Enhance tags from the library, `tts_budget.py` verbatim PASS, every word heard back, 141–188 wpm, used as generated — §24L). To check (stage VO).
- **L015 (F6)** voiced as written by default — the user's "proceed" did not answer it; still open before SC05's takes.
- **Hook 1 = SC01 (user: "PROCEED", 2026-10-02):** VOICE-N, VOICE-C1 and CAKE-CARD confirmed. Four Seedance takes (`body/SC01/`, preflight PASS on V7.91.1, ODAQ B.V. workspace) rendered and on the board To check: T1 the toast 12 s (job cac3a2c5), T2 "You look like my mother" 13 s one-take push-in (162a3bf9), T3 "Greg. Sit down." + Greg on Paula 15 s (b3c50789), T4 the silent table + untouched cake 7 s, no audio (a5178dcd). 386.76 credits (ODAQ 7,384.85 → 6,998.09), split per second on the cards. Every spoken word heard back verbatim (medium.en). Voice refs: Greg's own words cut from his master (`voice/C1_ref_L001.mp3`, `C1_ref_L005.mp3`), Susan's "Greg. Sit down." from the clone (`voice/N_ref_L004.mp3`). Hook 1 runs ~47 s against the script's ~36 s — the edit trims it.
- **SC01 Fix round 1 (user's board Fix on T3 and T4, 2026-10-02: "fix the seat position of susan use the 2nd video as reference"):** T1 confirmed, T2 To check. v1 of T3 (last shot) and T4 (the wide) seated Susan at the END of the table with the house and deck behind her — the prompts' "straight on Susan from across the table" / "behind her shoulder looking down the length of the table" let the model put her at its head. Fixed at the source in `body/SC01/build_clips.py`: T2 attached as `@video1` (video_references, job 162a3bf9) for her seat, a SEAT clause (long side, garden and low sun behind her, never the house), T3 SHOT 3 framed from Paula's side, T4 SHOT 1 looking ACROSS the table, NEG_SEAT; preflight PASS (gen 2 with fix_note). v2 To check (T3 c1794aff, T4 937d48ab, ≈181 cr at the build's 8.23 cr/s); v1 of both on the Old board. Seen on T4 v2: Susan is on the long side now, but the wide still looks along the table and Greg sits at its end with his back to camera — told the user, their call.
- **SC01-T1 Fix (user's board Fix, 2026-10-02: "change the seating location of susan use the 2nd video as reference where susan located"; T2 and T1 v1 had been confirmed, T1 reopened):** v1 put Paula in Susan's chair beside Greg (shot 2) and Susan beside Friend B (shot 3) — shot 2 never named who sits beside Greg. Fixed in `build_clips.py`: T2 as `@video1`, SEAT clause, shot 2 names Susan beside him (frame left) and Paula across the table, shot 3 framed as @video1 with Greg's sleeve at her side, seat negatives; preflight PASS. v2 (job 96666395, ≈98.75 cr) To check; v1 on Old. Seen on v2: Susan beside Greg and shot 3 matches T2; a woman in plum still sits on Greg's other side in shot 2. The user's earlier "this line are missing" (L002/L003) went unanswered: T2 v1 carries both lines verbatim (0–4.6 s, 6.8–11.6 s).

## Board review (2026-10-02)
- **Confirmed by the user:** all 8 cast sheets; plates P-HOUSE, L-YARD, L-YARD-REV, L-GATHERING, L-VANITY, L-PORCH-IN (v1, as is), L-HOSTS-FRONT.
- **L-VANITY-REV retired** on the user's Fix "dont use this": copied to the Old board, removed from Current; SC05-SH01/SH02 restaged on L-VANITY (Beth enters from the doorway behind the camera). Checks rerun: angles / wardrobe / visual plan PASS; takes.py now 6 false SPLIT lines (pairs 17–25 s).
- An L-PORCH-IN v2 was generated (5.67 credits) before the board was read — v1 had already been confirmed, so v2 is kept off the board (`plates/unused.txt`). Lesson for this build: read the board before acting on a chat reply.
- Open: F6 (L015 wording: niacinamide, "settles into the lines", "reads your skin") before the voice stage; F3 hooks; F16 yard reading (kept).

## Steps 4–5 (2026-10-02)
- Steps 4–5 delivered on the user's "go" (cast sheets not yet confirmed/fixed — still To check): 8 plates (Sunburst 16:9, 24.92 credits) on the Current board To check; `STEP4_5.md` with Property/Location Sheets, act map (48 shots, 26 Seedance takes, ~3:51), wardrobe per story day (6 days), Visual Pitch, music register map, ingredient ledger; Plan board docs: locations, actmap, takes, wardrobe, visualplan, music.
- Checks: angles.py PASS · wardrobe.py PASS · visual_plan.py PASS · takes.py 5 SPLIT lines that are false (shots-only count; each pair is 17–24 s > 15 s) — F19.
- New flags: F16 (yard = the hosts' house), F17 (L-PORCH-IN shows a house through the glass, not the yard), F18 (~3:51 runtime), F19.
- Next: the voices (§24I), straight through in Manual — needs the F6 ruling first.

## Earlier (steps 1–3)
- Steps 1–3 delivered: Absorption Sheet + Film Look Sheet, Visual Instruction Ledger (VN01–VN27), phrase inventory (L001–L027), claims, Mode & Model Lock → `BUILD_SHEET.md`.
- 8 cast sheets generated (Sunburst, 22 Higgsfield credits, ODAQ B.V.), all on the Current board as **To check**. Five copy the client's cast pictures (Susan old → N-SUSAN, Susan new → N-SUSAN-AFTER, Greg, Paula, Beth); three are new (daughter, Friend A, Friend B).
- **Stopped at the avatar gate** — waiting for the user's Confirm/Fix on the sheets and answers to the flags.

## Decisions
- Mode 4 + AI Drama VSL from the script's own "REAL MOVIE (not animation)" instruction (no MODE in the message) — F2.
- One hook in the script (the toast); 2 more to be written at step 6 unless the user says one — F3.
- The stick stays violet on screen; "plain white stick" read as unlabelled (Beth's hand covers the wordmark) — F10.
- Connectors: no Kie key → Seedance via Higgsfield (rung 2); Higgsfield on ODAQ B.V. (this account's private workspace id matches the rule).

## Open items (user)
F3 hooks count · F4 Botox lines for paid Meta · F6 "reads your skin" / niacinamide / "settles into the lines" · F7 "No downtime. Thirty seconds." · F8 50,000 figure · F9 free primer bundle · F12 wardrobe colours.

## For the owner (keys-exe) — system changes asked/needed, not made from this account
- Add this build's row to the CLAUDE.md board table (four links above) and the Routine line (`trig_01XaBTxvhuhW64zeHnySBmKR`, :52 UTC).
- Add the FACELOVE Product Sheet to `products/facelove/` (the client's `facelove_product_sheet.py` V7.49.5 + its `--md` prose and the product photos are in `builds/facelove-my-mother/product/`).
- `takes.py` SPLIT "length" counts shots only (≤ 4) and ignores seconds, while its TAKE+ check holds a take to 15 s — so a split of two takes that together run over 15 s but hold ≤ 4 shots fails falsely. Suggest: a length split holds when the joined take would exceed --max-shots OR --max-seconds.
- §19 has no rule for client-supplied cast pictures: this build attached each picture as Image 1 and copied the face onto the five-panel sheet (F1). Consider writing that into §19.

## Next (on the user's go)
Steps 4–5: location plates 16:9 (party yard, porch door from inside, bathroom mirror + kitchen counter, family gathering, bedroom vanity), product info cards, act map with takes (`takes.py`), visual pitch, angles, wardrobe per story day, music register map — then voices (§24I).
