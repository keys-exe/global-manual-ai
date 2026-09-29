# Build notes — down-forwards-again (STRYDE · Down Forwards Again, Doctor VSL · Manual)

Read this first when resuming. Build Sheet: `BUILD_SHEET.md` (steps 1–3).

## Intake
- **Drive task folder:** https://drive.google.com/drive/folders/1m1H8YO6MEVQBnoD2gkWPfn-y__PW0Bbk
- User message: the Drive link + "RUN MANUAL". MODE blank → Mode 1; HOOKS → 3 in script (A/B/C) → 3 finished videos; VOICE derived (the script's "his" → male doctor, British).
- Script is a native Google Doc: `fetch_drive.py` exported it as .docx → `intake/script.txt`; spoken lines `work/script.lines.txt`, split into `work/HK1–HK3.lines.txt` and `work/BODY.lines.txt` (576 words). Hook labels / "(the reference's construction, exactly)" are authoring notes (VN01–VN03), not voiced.
- Inspo = a doctor-authority menopause supplement ad (the script's "Reference" link), 142.1s, 40 shots, 360×640 download, renamed `intake/inspo.mp4`; transcript `intake/inspo_transcript.txt`; measurements `intake/inspo_report.json`.
- Product Sheet V7.49.32 → `products/stryde/` (was V7.49.31 on this branch).
- **Boards:** Current https://claude.ai/artifact/UqVKJB21YyfBZTjxh5dNNT · Old https://claude.ai/artifact/8eXUW9NwJq49zRfPHtgC5Y · Final https://claude.ai/artifact/W11NPXayafpTXoY4FqMccb · Plan https://claude.ai/artifact/5Wzyk63o5viz5t4wLVZUu7
- **Hourly Fix check:** `trig_01XNVEi8936asCGsYpstFCaw` (:41 UTC, bound to session_01YaVWUyhH3VYNdrBjxmx6TC).

## Sessions
- session_01YaVWUyhH3VYNdrBjxmx6TC (2026-09-28 19:05–19:25 UTC): steps 1–3. Absorption, ledger, phrase inventory, claims,
  Mode & Model Lock; 2 avatar sheets (D-DOC, P-PATIENT) on Higgsfield (Sunburst, high, 2k, one each) → board To check;
  `docs/absorption` on Plan + Current. Higgsfield 17,998.5 credits before the cast.

- Same session 19:48 UTC: user "USE BRITISH ETNICITY" → D-DOC recast white British (v2 `71b20c5a`), v1 moved to Old; VOICE-DOC → light Yorkshire. Hourly check 19:41 found no Fixes.

- Same session ~20:00 UTC: user "go ahead with steps 4–5" → STEP4_5.md: PROP-P (Victorian terrace, stairs on the left wall),
  plates P0 hall/stairs, P1 front room, P2 kitchen (both with P0 attached), P3 consulting room; LEFT-knee worn refs W-L-FRONT/REAR/BENT
  (sent as nano_banana_pro, Higgsfield job record says nano_banana_2 — flagged on the cards); act map 44 rows (8 TH, 4 MECH),
  angles.py PASS; wardrobe map; 51 cards on Current; docs locations/actmap/wardrobe on Plan + Current. Higgsfield 17,894 after.
- Same session ~20:10 UTC: user "THE HOUSE LOOKS SMALL AND COMPRESSED" → cause: v1 prompts asked for a narrow Victorian terrace hall + galley
  kitchen, framed through doorways. Rebuilt as a large Edwardian semi (wide hall/stairs, ~3 m ceilings, shot from inside each room, no-cramped
  negative): P0 v2 `176c5c39`, P1 v2 `d0eeaf2a`, P2 v2 `abc2c220` (both against P0 v2); v1s on the Old board. Layout unchanged, angles PASS. Higgsfield 17,879.75.

- Same session ~20:20 UTC: user "go ahead with the voice stage" (every avatar/plate/ref was Confirmed on the board). Step 1 frame D-VOICE-IMG
  (job edd8434b, reported nano_banana_2) → board To check. G1–G3 Kling calls written + preflighted (PASS but 'start image approved'). Enhanced VO text
  locked (verbatim PASS, 3,180 chars). **STOP: Kling 3.0 credits** (§5 CREDIT_CAP, no reroute). See voice/VOICE_SOURCE.md.

- ~20:30 UTC: user "USE KEI AI AS SUBSTITUTE FOR NOW" → ADJUST recorded in BUILD_SHEET (Mode & Model Lock): every Kling call routes through
  Kie `kling-3.0-omni/image-to-video` (same Kling 3.0 Omni, prompt ≤3,072) via `voice/kie_kling.py` (refuses without preflight PASS), until Kling
  is topped up. Kie 186,607.8 credits. G1–G3 preflight: only 'start image approved' left (D-VOICE-IMG still To check).

- ~20:52 UTC: user "USE A DOCTOR CLOTHES" → D-VOICE-IMG v2 (job b17f293d): white coat + stethoscope locked in the prompt; v1 to Old; G1–G3 point at v2.

- ~21:00–21:40 UTC: user "go ahead with the voice stage" (taken as approval of D-VOICE-IMG v2). G1–G3 via Kie (690 credits; first send
  rejected free: Kie needs aspect_ratio auto). voice_source PASS → clone **Down** `lLQRuUpi2CbzE9mw4WRD` → eleven_v4 ×4 → split → house cut (16 parts +
  whole T1 one pass 135.83s PASS) → HeyGen photo avatar `bd3f0bac…` → Avatar V one-go render `c48a6bc2…` (motionPrompt rejected: no digital twin).
  Applied the user's 2026-09-28 corrections from the stryde-thirty-years branch (Avatar V only, one go) — that branch's §22U is not merged here yet.
  See vo/VO.md.

- ~22:00 UTC: user "the vo feels so fast the trims i dont like that" + "its trimmed even though she is not done talking".
  Measured: raw takes speak ~235 wpm speech-only (clone learned from the §22U ×1.2 source); the house cut left parts ending at −29…−38 dB
  (last word clipped); the HK3/body split clipped HK3 too. eleven_v4 ignores voice_settings.speed (0.85 and 0.7 both 12.32s on HK1).
  Fix in progress: re-cloned from the SAME takes at ×1.0 → **Down-Doctor** `a0lv6tcMVlFOFYq3VUob` (HK1 167 wpm vs 181); 4 new takes `vo/full2/`
  (T1, T4 verbatim by transcript; T2, T3 contractions); split with cuts snapped to the quietest point in each gap (`split_vo2.py`, `split2.json`).
  Planned cut: `trim.py` natural pace (0.35s sentence / 0.2s comma kept) with `--post 0.4` so every part ends in silence (test: −87 dB), not the house cut.
  **PAUSED on the user's word: "ill make a pr wait for it".** The HeyGen render `c48a6bc2…` (fast T1.ALL audio) is superseded once the new VO is cut.

- 2026-09-29 ~05:30 UTC: user "Ive added the new trim. Proceed with the vo again". Merged the default branch (V7.66.0, PR #36: no tight cuts —
  vo_trim −50 dB + 80 ms release, 60 ms fade, natural pauses 0.45/0.20s kept, pace gate ≤210 wpm). §22U step 4 still says ×1.2, so the ×1.0
  re-clone is NOT standard → the user picks. Re-cut all 8 whole takes (vo/cut766/): Down T1–T4 = 201/204/200/206 wpm (T4 FAIL: a breath left),
  Down-Doctor T1–T4 = 190/192/192/192 wpm, all others PASS, every tail −54…−59 dB. Board: VO-T1…T4-ALL (Down), VO-T5…T8-ALL (Down-Doctor), To check;
  the 16 old house-cut part cards + old T1.ALL moved to the Old board.

- 2026-09-29 ~08:05 UTC: user "CONFIRMED VO" — confirmed **VO-T7 (Down-Doctor take 3, ×1.0 clone, V7.66.0 cut, 192 wpm)** on the board → VO locked
  (the ×1.0 source is the user's call, off §22U step 4). Audio → HeyGen asset `bace0e73…` → Avatar V one go (photo avatar `bd3f0bac…`, 9:16 1080p, no
  motionPrompt) → video `f3fed9116b971e93d10e105279df52ae` (179.5 s). `vo/cut_points.py` now cuts at every hook AND act (A1–A5 lines from the act map;
  A1..A5 = BODY verified) → `th/TH-<k>.cut.mp4` → trim.py V7.66.0 → all 8 PASS (0.11–0.65 s removed each) → board TH-HK1/2/3 + TH-A1…A5 To check.
  Flag: at 69.2 s (TH-A2 ~7.8 s) both transcribers hear "the good **me**" for "the good knee" — told the user.

## Where it stands
- **Waiting on the user:** check the 8 talking-head clips (TH-HK1/2/3, TH-A1…A5) on the board — Confirm or Fix. Listen to TH-A2 "the good knee".
- **Then:** hooks one by one (step 6), B-roll (step 7), CapCut block; finished videos = TH-HKn + TH-A1…A5 (+ B-roll).
- Old HeyGen render `c48a6bc2…` (old fast cut) is superseded, not used.
