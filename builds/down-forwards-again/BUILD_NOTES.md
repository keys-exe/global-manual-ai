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

- 2026-09-29 ~08:40 UTC: user "CONFIRM PROCEEDS" → TH-HK1/2/3 + TH-A1…A5 set `use`. Step 6 hooks: `hooks/build_hooks.py` writes the four hook
  frames (§22T order + ANGLE-LINE / FOCUS-LINE / LIGHT-SHOT, start frame caught in the action, HK1-01a CONCEALED + NEG-CONCEAL, HK3-01a SKIN-T + CAP-SHARP),
  refs by Higgsfield job id → nano_banana_2 9:16 2k, one each (jobs 11d544d2, e46ab752, 82a43e53, b38467ec; Higgsfield reports `nano_banana_flash`)
  → board HK1-01a, HK1-02a, HK2-02a, HK3-01a images To check. Higgsfield 17,584 credits.
  Note: the act map's hook layouts (HK1-01a pip then HK1-02a cutout) predate the V7.65.0 layout limit (≤1 boxed in 5, never two in a row) —
  settle at assembly (`assemble.py` LAYOUT_MIX); frames are composed full-frame so either layout crops.

- 2026-09-29 ~09:15 UTC: user "I WANT A HOOK THAT WILL SELL I DONT WANT THIS NORMAL LOOKING HOOKS" → §34 correction on all four hook pictures
  (spoken lines unchanged, verbatim): HK1-01a → home-camera footage (§22E CCTV-FULL, hall corner), P-D1, coming down BACKWARDS with both hands on the
  banister, layout full; HK1-02a → the overfull drawer spilling onto the tiles; HK2-02a → tears the blank top sheet off the prescription pad (F12);
  HK3-01a → overhead, desk buried under knee scans, one more dropped on the heap, layout full. `work/actmap.py` rows + STEP4_5 + docs/actmap (Plan + Current)
  updated; angles.py PASS. `hooks/build_hooks_v2.py` → nano_banana_2 v2 renders (jobs 49b86e44, fd67eaff, 00f46dd9, f282b14c) → board To check;
  v1 frames moved to the Old board (copies confirmed, then deleted from Current). CapCut: HK1-01a gets a home-camera timestamp overlay in post (§22E, §17).

- 2026-09-29 ~10:15 UTC: user "FIX THOSE" → the board Fix notes (§34): HK1-01a "…RUNNING DOWN THE STAIRS AT THE SUBWAY STATION, NOT JUST AT HOME" →
  v3: she runs down Underground entrance stairs, forwards, P-D2, CONCEALED (new INCIDENTAL location L-TUBE); HK1-02a "SHOW ALL OF THOSE" → split into
  HK1-02a the operation (pre-op marker arrow on her left knee, L-HOSP) · HK1-02b the physio (resistance band, front-room floor, overhead) · HK1-02c the
  drawer (the v2 spill render carried over, no new call); HK2-02a "TEN SECONDS TO PUT ON THE STRYDE STRAP" → seating beat (§9B, SEAT_LOCK start frame:
  closed strap at mid-shin, both hands on the shell; NEG_SEAT kept for the clip, pin_end yes) — the product now first appears in Hook 2 (was PR-12).
  HK3-01a confirmed by the user. `hooks/build_hooks_v3.py`; jobs dc061b02, 21b325d8, caaf587d, dd2add6c (HK2-02a: nano_banana_pro requested,
  Higgsfield reports nano_banana_2). Replaced v2s (HK1-01a, HK2-02a) moved to the Old board. Act map rows + STEP4_5 + docs/actmap updated; angles.py PASS.
  Note: three B-rolls on the HK1-02 line (~6 s) sit near the 2.0 s minimum hold (§30H) — checked at assembly. Higgsfield 17,548.

- 2026-09-29 ~12:25 UTC: user "fix those" → board Fix notes (§34): HK1-01a "her hands should never hold the hand rail" → v4 both hands free, rail far off;
  HK1-02a "the operation is a knee replacement" → v4 a surgeon holds a total knee replacement implant above her bare left knee; HK1-02b "should be a COURSE
  not at home" → v2 NHS physio class (new INCIDENTAL L-PHYSIO), step-down with the physio watching; HK1-02c "holding the stryde strap … braces at the back,
  focus only on the stryde" → v2 held beat (§9A, HELD_GRIPS fingertips behind, nano_banana_pro requested / Higgsfield reports nano_banana_2), the overflowing
  drawer soft behind. HK2-02a (strap put on) and HK3-01a confirmed by the user. `hooks/build_hooks_v4.py`; jobs 76034f69, b03e5124, 96983a1e, 183c767a.
  Replaced versions moved to the Old board. Act map + STEP4_5 + docs/actmap updated; angles.py PASS. Higgsfield 17,445.25.

- 2026-09-29 ~12:35 UTC: user "fiix those" → board Fix notes (§34); HK1-01a v4 confirmed. HK1-02a "not an operation immediately — the doctor proposing a knee
  replacement" → v5 consultation (L-ORTHO): over the surgeon's shoulder, implant held out across the desk, her worried face (SKIN-T); HK1-02b "too simple,
  camera angle" → v3 busy NHS physio class, ground level through the parallel bars, straining step-up, physio spotting; HK1-02c "create a new one" → v3 from
  inside the drawer past the old braces, her hand lifts the STRYDE strap out (HELD_GRIPS bottom-edge pinch, focus on the strap). `hooks/build_hooks_v5.py`;
  jobs b6817ac4, cac8d27e, 11e82707. Replaced versions to the Old board. Act map + STEP4_5 + docs/actmap updated; angles.py PASS. Higgsfield 17,398.25.

- 2026-09-29 ~12:50 UTC: user "fix those" → HK1-02a v5 and HK1-02b v3 confirmed; HK1-02c "she should never put that strap on that drawer" → v4: the strap lies
  apart on the kitchen table, sharp in the foreground (§15A object beat); behind, soft, she tips the whole drawer of old braces into a black bin bag
  (`hooks/build_hooks_v6.py`, job 31dd56c8, nano_banana_pro requested / Higgsfield reports nano_banana_2). v3 to the Old board. Act map updated, angles.py PASS.

- 2026-09-29 ~13:20 UTC: user "that is good but dont make the braces magically going to the trash bag she should be putting them there" → HK1-02c v5:
  same frame as v4, she puts one brace into the bin bag by hand (bag held open with the other hand), the rest still in the drawer, nothing in mid-air
  (`hooks/build_hooks_v7.py`, job 08be9db1). v4 to the Old board.

- 2026-09-29 ~13:25 UTC: user "confirmed all" → all hook images confirmed. Lengths from `assemble.py --lengths` (hooks/plan/*.plan.json, on the trimmed
  TH-HKn audio): HK1-01a/02a/02b 3 s, HK1-02c 4 s, HK2-02a 4 s, HK3-01a 5 s. `hooks/build_hook_videos.py` → §35 JSON (RIG-R1C, one action + pace, HOLD-C,
  PHYS-MOTION-C, NEG-WARP-C + NEG-LIGHT-C, audio off), preflight PASS ×5 → Kie kling-3.0-omni (tasks 4c31f723, 0580e273, 9805c9fe, e3c78916, 885279cc;
  324 Kie credits) → board To check (generation 1 each). HK2-02a is pinned (§27G rule 5): its END frame (strap seated, hands lifting off,
  `hooks/build_hk2_end.py`, job 74bff83d) is on the board as card HK2-02a-END for the user's Confirm before its video. Kie 168,280.8.

- 2026-09-29 ~13:40 UTC: user "hk2 02a should not need an end frame remove it" → ADJUST: HK2-02a not pinned (act map pin_end no). END frame card removed from
  Current (image kept on the Old board as HK2-02a-END, unchosen). `hooks/build_hk2_video.py` → start frame only, SEAT_LOCK slide compressed, preflight PASS
  → Kie task c54cdc14 (72 credits) → board To check.

## Where it stands
- **Waiting on the user:** all six hook videos (HK1-01a, HK1-02a, HK1-02b, HK1-02c, HK2-02a, HK3-01a — generation 1) — Confirm or Fix.
- **Then:** hook variants assembled (assemble.py + variants.py with the TH hooks); then B-roll acts (step 7), CapCut block.
  A second generation of any shot follows §22X (diagnose, fix at source); a third waits for the user.
