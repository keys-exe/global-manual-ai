# Build notes — stryde-71-stairs (STRYDE · 71 Stairs, Black American Woman · Manual)

Read this first when resuming. Build Sheet: `BUILD_SHEET.md` (steps 1–3).

## Intake
- **Drive task folder:** https://drive.google.com/drive/folders/1B2H-Kx8-NpEKsMoL0IvMqbvy8uAQIL5T
- User message: the Drive link + "RUN MANUAL". MODE blank → Mode 1; HOOKS → 1 in script ("same hook as 71 Stairs"); VOICE from the script note (Black American woman, 71, light Southern accent).
- Script is a native Google Doc: `fetch_drive.py` exported it as .docx → `intake/script.txt`; spoken lines `work/script.lines.txt` (613 words; the direction note is VN01–VN08, not voiced).
- Inspo = the original 71 Stairs ad (155.6s, 82 shots, selfie TH + B-roll, 231 wpm). Transcript kept in the Build Sheet structure map.
- Product Sheet V7.49.32 (same as stryde-lost-moments) → `products/stryde/`.
- **Boards:** Current https://claude.ai/artifact/Ev166tkWbX9QaE1P7VLjti · Old https://claude.ai/artifact/E3hbWw3ea9nS8vTgzGLLmd · Final https://claude.ai/artifact/QVBQW1v5WHJ7cJN4PGxcbY · Plan https://claude.ai/artifact/KZ6FRJSii34aQcCTp6XmNy
- **Hourly Fix check:** `trig_019vEknq3DfbCfaWGSyrTvy5` (:17 UTC, bound to session_01D42imWscMStnxPKqpqZQpb).

## Sessions
- session_01D42imWscMStnxPKqpqZQpb (2026-09-28 18:35–18:55 UTC): steps 1–3. Absorption, ledger, phrase inventory, claims,
  Mode & Model Lock; 3 avatar sheets (N-NARR, C1-LORETTA, C2-DAUGHTER) on Higgsfield (Sunburst, high, 2k, one each) → board
  To check; `docs/absorption` on Plan + Current. Higgsfield 18,072.75 credits before the cast.

- same session, 2026-09-28 19:00–19:15 UTC: user "CONFIRMED ALL" → the 3 avatars and the absorption confirmed on the board;
  flags closed on the recommendations (F1/F2/F4 voiced as written, F5 Amazon voiced never pictured, F9 1 hook, F11 verbatim, F12 natural pace).
  Steps 4–5: 8 plates (Sunburst, one each) → board To check; act map (75 rows: 59 B-roll + 16 TH, `work/actmap.py`, all 613 words
  covered in order, `angles.py` PASS) + wardrobe map + locations → `STEP4_5.md`, docs/actmap, docs/wardrobe, docs/locations on Plan + Current;
  75 planned cards on Current. §22U step 1: N-VOICE-IMG (selfie on the landing, nano_banana_pro requested, Higgsfield logs nano_banana_2)
  → board To check. Voice takes `voice/N_G1.call.json`, `N_G2.call.json` built; preflight PASS except "start image approved".
  Higgsfield 17,998.5 · Kling 3.0 · Kie 215,672.8.

- 19:20 UTC: user "FIX THOSE" → board Fixes: P1-LANDING ("THE PICTURES NOT THE SAME AS THE P0") regenerated with P0-PROP-N attached
  as reference, the photo wall written as P0's (v2, job a53b6e6b); P4-STORE ("FIX THE DISTORTIONS") regenerated as an empty store with
  straight-line geometry, no people, PHYS-FRAME-C body clause dropped (v2, job 751cd1e7). v1s moved to the Old board. N-VOICE-IMG was built
  against P1 v1 — if you want its photo wall to match too, press Fix on it.
- 19:30 UTC: user "FIX THE LOCATIONS FIRST" → second board Fixes: P1-LANDING v3 ("WRONG STAIRS": now P0's own straight open flight
  seen from the top — photo wall left, balusters + dark rail right, hall and front door at the bottom, P0 attached; job 2cc80516);
  P4-STORE v3 ("WRONG COUNTERS NOT REAL": a standard US checkout stand — belt, divider, register screen, scanner, card terminal on a post,
  bag carousel, impulse rack, lane light; job 87a0c23e). v2s moved to Old. Other 6 plates confirmed by the user. Voice waits on the
  locations (user's order) and on Kling credits.
- 19:45 UTC: user "LOCKED LOCATIONS FOR TH IMAGE DONT USE SELFIE STYLE" → all 8 plates confirmed (locked). §34 correction for this build:
  talking heads are **propped, never selfie** — TH-01…TH-16, C-06a and N-VOICE-IMG (act map, STEP4_5, Build Sheet EG02/§20, Kling
  voice calls: camera "Propped", hands at the waist). N-VOICE-IMG v2: standing at the top of her stairs, phone propped at chest height,
  waist-up; refs N sheet + P1 v3 + P0 (nano_banana_pro requested, logged nano_banana_2; job 6ceca5c9). v1 moved to Old.
  `angles.py` PASS.

- 19:50–20:05 UTC: user "USE KIE FOR KLING" (Kling connector 3.0 credits) → Kling voice takes run on Kie `kling-3.0/video`
  (pro 1080p, 10s, sound; `kie.py kling` brought in from claude/amazing-bohr-tsowwg). User "USE GPT IMAGE FOR THIS TH IMAGE" →
  N-VOICE-IMG v3 on gpt_image_2_5 Sunburst (§18A rule 7 overridden on the user's word), then "USE NANO BANANA PRO MUCH BETTER"
  → **v2 (nano_banana_pro) chosen and confirmed**; v1 + v3 on the Old board. Enhance pass written (`vo/ALL.enhanced.txt`,
  `tts_budget.py` verbatim PASS, 3,525 chars, 1 request). ElevenLabs check PASS (519 free slots).
  G1 (Kie ae8336fc, 190.5 Hz) ✓. G2 (Kie 773d0b83) 210.5 Hz = +10.5% → same-voice gate FAIL; cause in my prompt (quote "lighter,
  a little higher") → G2 v2 (Kie 4ea2119b, quote in her own voice) 222.2 Hz = +16.6% → FAIL again. Kie spend 810 credits.

- 20:10–20:50 UTC: user "USE THE NEXT LINE" → G3 "Six weeks ago… One step at a time." (Kie 58f49e8d) 205.1 Hz, +7.7% → gate PASS.
  `voice_source.py G1 G3` → 31.5s → **cloned `Stairs` = fjMYIJcXAxAnyO48q9x3**. `eleven_v4` ×4 (one request each, Enhance text)
  → house cut: T1 168.4s PASS (**working take**), T2 FAIL (breath 91.6s), T3 170.6s PASS, T4 172.5s PASS.
  `vo/th_split.py` cut TH-01…16 from T1 between words (595/613 words aligned) → Kie public URLs → HeyGen photo avatar
  `f9ceab51c06ef232a9d1ebc53c5d40f2` (N-VOICE-IMG v2). **Avatar V rejected motionPrompt (no animation reference in the group)**
  → §22U fallback (c): Avatar IV + expressiveness high + motionPrompt, 16/16 rendered (`vo/th/heygen.json`), `trim.py` PASS ×16.
  Board: N-VOICE-G3, VOICE-SOURCE-N, VO-T1-FULL (4 takes), TH-01…16 (untrimmed v1 + trimmed v2). Audio as mp3-in-mp4 (board refuses .mp3).

- 20:55–21:10 UTC: user "CONFIRMED PROCEED TO HOOK VIDEOS but do 2 versions same script different visual" → HK-01a/HK-02a images
  confirmed = **Hook 1 (version A)**. Kling on Kie (pro 1080p, multi_shots off, §22X preflight PASS, start frame = confirmed image):
  HK-01a 5s (Kie fbb62285, 90 cr), HK-02a 4s (Kie 6b771158, 72 cr) → board `review`.
  **Hook 2 (version B)** = same VO lines, new visuals: rows HK-01b (N on the church steps, L-CHURCH, low/three-quarter/MEDIUM; refs N + P5;
  job ae039237) and HK-02b (N + C2 on the home stairs in profile, eye/profile/MEDIUM; refs N + C2 + P0; job 86af8fdd) added to
  `work/actmap.py` (77 rows, `angles.py` PASS). Images on the board as `review` — their videos wait on the user's Confirm (§22X).
  Note: `vo/th_split.py` dedupes only consecutive duplicate lines — skip HK-0xb rows (they reuse HK-0xa times) if it's rerun.

- 21:15–21:30 UTC: user "fix those and hook 2 should be not at home it should be at the mall". Board Fix on HK-01a video: "re do this make
  the woman in gray at the back of the woman in green". §22X diagnosis: **frame fault**. The start image had the daughter on the hall floor
  beside the newel, so Kling walked her up the outside of the banister. Fix at the source: HK-01a image v2 has the daughter already on the
  flight, two steps directly behind her mother, inside the rail (job a9b2dd72). The video waits for the frame's Confirm. The next video is
  gen 2, and it needs a fix_note.
  Hook 2 moved to the mall. New location L-MALL, plate **P8-MALL** (Sunburst, job 8b47c878): an open terrazzo staircase beside the up
  escalator. HK-01b v2: she climbs the mall stairs, passing two younger women riding the escalator (refs N + P8, job 0a335321).
  HK-02b v2: side-on, the daughter one step behind with shopping bags (refs N + C2 + P8, job 0d4a602a). `actmap.py` rows updated,
  `angles.py` PASS. The v1 images went to the Old board, and their files were deleted from Current. All new renders are on `review`.

- 2026-09-28 21:35 → 2026-09-29 06:10 UTC: user "the th is too quick the trim" → "the vo is what i mean" → "its trimmed even though she is
  not done talking" → "ill make a pr wait for it" → (V7.66.0 merged into the default branch) "Ive added the new trim. Proceed with the vo again".
  Merged the default branch (V7.66.0) into this branch (CLAUDE.md board table conflict resolved, both sides kept).
  **VO re-cut, V7.66.0 house cut** (`vo_trim.py`: every word to −50 dB + 80 ms release, pauses 0.45/0.20 s, ≤210 wpm) → `vo/cut/v2/`:
  T1 212.95 s 173 wpm PASS (**working take**), T2 208.1 s FAIL (breath 156.45 s), T3 211.2 s FAIL (breath 141.8 s), T4 211.7 s PASS.
  **Talking heads per §22U step 13 (V7.66.0): one HeyGen Avatar V render of the whole T1 cut** (video 4f39b935…, 212.9 s, no
  motionPrompt — Avatar V refuses it for this photo avatar; never Avatar IV) → `vo/th_split_v3.py` cut points on the new cut
  (`vo/cut/v2/VO_T1.beats.json`) → 16 segments → `trim.py` (V7.66.0 defaults) PASS ×16 → board v3. The Avatar IV THs (v1/v2) and the
  168 s house-cut takes moved to the Old board. The intermediate Avatar IV re-renders from 21:40 (`vo/th/v2/`, natural-pace audio) are
  superseded by the V7.66.0 Avatar-V-only rule and were not put on the board. TH-01 begins on the tail of "up" (connected speech,
  no gap in the take). New beat times: HK-01a/b 0–~4.1 s, HK-02a/b ~4.1–7.98 s, TH-01 7.98–10.68 s (see beats.json).

- 2026-09-29 ~07:30 UTC: user "REMOVE THE LAUGH AND SIGH" → `[laughs]`, `[chuckles]` ×2, `[sighs]` removed from the Enhance text
  (`vo/ALL.enhanced.v2.fitted.txt`, tts_budget verbatim PASS, 3,486 chars, 15 tags left) → 4 new eleven_v4 takes (`tts_api.py`,
  `vo/full/v2/`) → V7.66.0 house cut (`vo/cut/v3/`): T1 205.9 s FAIL (breath 166.75 s), **T2 209.95 s 175 wpm PASS = working take**,
  T3 208.5 s FAIL (breath 168.8 s), T4 211.6 s FAIL (breath 156.4 s). One Avatar V render of T2 (HeyGen 8978513a…, 209.9 s, no
  motionPrompt) → TH cut points `vo/cut/v3/VO_T2.beats.json` → 16 THs `trim.py` PASS → board. The T1-based THs + VO cuts + one-go
  render moved to the Old board.

- 2026-09-29: user "CONFIRM THE TH LETS MOVE TO THE HOOKS" → TH-01…16 + TH-ALL-T1 `use`, VO T2 locked (`voLocked`). Asked about the
  unconfirmed hook frames (HK-01a v2, P8-MALL, HK-01b/HK-02b v2): user will check them on the board first — no hook video until then.

- 2026-09-29 ~08:55 UTC: user "THE HOOK 2 CONCEPT SHOULD BE GOING DOWN THE STAIRS" → HK-01b / HK-02b rewritten to going DOWN the mall
  stairs facing forwards (pays off "six weeks ago I was going down my stairs backwards"): HK-01b passes two younger women on the down
  escalator (job 2120c4f8), HK-02b side-on with the daughter one step behind and above (job b2bc7304). `actmap.py` + `beats.py` updated,
  `angles.py` PASS; v2 (climbing) moved to the Old board. Note: the HK-02 line says "walked behind me the whole way up" — the picture
  now goes down, on the user's call.

- 2026-09-29 ~09:15 UTC: user "THE HOOKB THE MAIN CHARACTER SHOULD BE RUSHING DOWN OVER TAKING THE DAUGHTER AND THE DAUGHTER JUST SAID WHEN DID
  THAT HAPPENDED, USE SEEDANCE FOR BOTH HOOK A AND HOOK B SO RE DO THEM, BE SURE THAT THE CLOTHES ARE NOT THE SAME …" + answers: the daughter
  says "Mama, when did that happen?" on camera in BOTH hooks; VO over the clip (mother doesn't speak); new outfits for both hooks.
  → One continuous Seedance 2.5 clip per hook (11 s) replaces HK-01x + HK-02x + TH-01 in that hook. New start images (nano_banana_2):
  **HK-A-SD** (from the landing: mother in a royal-blue skirt suit climbs fast toward the lens, daughter in a burgundy sweater behind; job 4fa1da0d)
  and **HK-B-SD** (mall, from the foot of the stairs: daughter in a denim jacket coming down with bags, mother in a mustard cardigan about to
  overtake her; job 652b9992). Prompts: `work/beats.py` (HK-A-SD/HK-B-SD), clips `hooks/seedance_hooks.py` → `hooks/sd/HK-A|B.seedance.txt`.
  Voices: @audio1 = mother, `hooks/sd/mother_voice_T2_0-7.3.mp3` (VO T2 hook lines); Hook A first — its daughter line is cut out and becomes
  @audio2 for Hook B. Edit: the daughter's on-camera line replaces the mother reading it in the VO. The old Kling hook cards (HK-01a/02a/01b/02b)
  stay on Current until the Seedance hooks are confirmed, then move to Old.

## Where it stands
- **Voice stage redone to V7.66.0, no laugh/sigh** (2026-09-29): VO takes (text v2) + TH-ALL-T1 (now T2) + TH-01…16 on the board To check. Working take **T2** (`vo/cut/v3/VO_T2.mp3`, beats `vo/cut/v3/VO_T2.beats.json`); a confirmed different take → one new Avatar V render + re-cut.
- **Step 6 — hooks (the hook gate):** Hook 1: HK-02a video confirmed (use); HK-01a new frame v2 To check (then its video, gen 2).
  Hook 2 (mall): P8-MALL plate + HK-01b/HK-02b v2 images To check → then their videos on Kie.
  Beat times from `vo/cut/VO_T1.beats.json`: HK-01a 0.00–3.84s, HK-02a 4.04–7.00s, TH-01 7.00–8.94s (Hook 2 uses the same times).
- **Next on the user's Confirm:** HK-01a video gen 2 + Hook 2 videos (add to `hooks/build_calls.py`, preflight, Kie) → both hooks approved → Acts 1–7 B-roll.
  Finals: FINAL-HK1 (Hook 1 + body), FINAL-HK2 (Hook 2 + body) on the Final board.
