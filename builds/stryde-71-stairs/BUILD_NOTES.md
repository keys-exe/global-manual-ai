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

- 2026-09-29: user "DELETE THE PREVIOUS HOOKS" → the Kling-era hook cards HK-01a, HK-02a, HK-01b, HK-02b (all their images and the two
  Kling videos) removed from the Current board; every version kept on the Old board (§16A never lose a version). Hooks on Current now:
  HK-A-SD and HK-B-SD only.

- 2026-09-29: user "check the new pr we have something about the seedance" → merged V7.68.x (default branch): **Seedance ingredients
  are information, never frames** — no master/start/scene frame for a Seedance shot. The HK-A-SD / HK-B-SD start images are retired
  (moved to the Old board). `hooks/seedance_hooks.py` rewritten to the V7.68 ING-MANIFEST (characters → @audio → place → product →
  info cards, then the shot in prose). Hook A: @image1 N sheet, @image2 C2 sheet, @audio1 mother voice (VO T2 0–7.3 s, she does not
  speak), @image3 P1 landing, @image4 P0 house, @image5/6 outfit cards A-N / A-C2. Hook B: sheets, @audio1 mother, @audio2 daughter
  line cut from the Hook A clip, @image3 P8 mall, @image4/5 outfit cards B-N / B-C2. **4 outfit info cards** made (Higgsfield jobs
  1b0479d5, 4e0dd1dd, 5ba28b60, ca50d941; caption band added, `hooks/info/`) and on the Current board as their own cards
  (INFO-WARD-A-N, -A-C2, -B-N, -B-C2) To check. HK-A-SD / HK-B-SD cards now carry `ingredients` (no image step); each video unlocks
  once all its ingredients are confirmed. Board template republished to all four 71 Stairs boards (Current, Old, Final, Plan).

- 2026-09-29 ~10:30 UTC: user "the mom voice is just the voice over the one who will only talk is the daughter and the voice clip she will
  use is the one from hook a after generating" → the mother's voice is no longer a Seedance ingredient (it is only the VO, laid over the
  clip in the edit). Hook A: no voice ingredient (the daughter's voice is written in the prompt). Hook B: @audio1 = the daughter's line cut
  from the generated Hook A clip. Also dropped "no American vowel colouring" from the default voice negative for these prompts — it
  contradicts the daughter's Georgia accent. HK-A-SD / HK-B-SD cards updated.

- 2026-09-29 ~10:35 UTC: user "the mall theres no escalator beside the stairs in malls" → P8-MALL plate rewritten with the staircase
  standing on its own (no escalator in view) and regenerated at 16:9 (gpt_image_2_5 high 2k, job e4d9c771) → v2 To check; v1 moved to
  the Old board. Hook B Seedance prompt: escalator removed from the place and the shot, "no escalator" added to its negative.

- 2026-09-29 ~10:40 UTC: user "use https://kie.ai/gpt-image-2 this for the locations" → location plates for this build now go through
  Kie GPT Image 2 (`kie.py image gpt-image-2-text-to-image --plate`, 2K 16:9; `gpt-image-2-image-to-image` when references are needed —
  both models added to kie.py). P8-MALL remade on it: v3 (task 5b55c74e, 2048×1152, 10 credits) To check; v2 (Higgsfield) moved to Old.

- 2026-09-29 ~10:50 UTC: user "re do all the location plates and use the 16:9 settings" → P0–P7 remade on Kie GPT Image 2 at 16:9
  (2K, 2048×1152, 10 credits each): P0 v2, P2 v2, P3 v2, P5 v2, P6 v2, P7 v2 text-to-image from their prompts; P4 v4 from the confirmed
  v3 prompt; P1 v4 image-to-image from the v3 prompt with the new P0 v2 as its reference (same house, same stairs). All To check; every
  replaced version moved to the Old board. P8-MALL was already 16:9 on GPT Image 2 (v3). Task ids in `plates/jobs.json` (`*.16x9`).
  Images already confirmed from the old plates (cast, N-VOICE-IMG) are left as they are.

- 2026-09-29 12:20 UTC (hourly Fix check): three board Fixes on Kie GPT Image 2, 16:9 —
  **P0** "remove the floor mat" → v3, image-to-image edit of v2 with the rug taken out (prompt `P0-PROP-N.v3.prompt.txt`; the rug also
  removed from `build_plates.py`). **P1** "use the p0 as reference" → v5 from P0 v3; the v3 prompt's own photo-wall description
  (black-and-white/sepia only, "no colour graduation portraits") fought P0's wall, so v5 takes the photo wall and every shared finish from
  the reference instead of describing it (`P1-LANDING.v5.prompt.txt`). **P8** "it feels so empty" → v4 with a normal Sunday crowd in the
  middle distance (walkway, concourse, bench, kiosk, open lit shops), the staircase itself clear (`build_plates.py` TAIL now takes a
  people clause). All To check; replaced versions on the Old board.

- 2026-09-29 ~12:40 UTC: user confirmed the location plates, then chose "Confirm all 4, go" for the outfit cards (marked confirmed on
  their word). **HK-A-SD v1** made on Seedance 2.5 via Kie (task fa158cc0, 11 s 720p, 693 credits; ingredients N sheet, C2 sheet,
  P1 v5, P0 v3, INFO-WARD-A-N, INFO-WARD-A-C2; no audio ingredient) → To check. Whisper: the only speech is the daughter's
  "Mama, when did that happen?" 7.62–10.42 s. Cut 7.35–10.95 s → `hooks/sd/daughter_voice_HKA_v1.mp4` = card **VOICE-C2-HKA**
  (To check), the @audio1 ingredient of HK-B-SD. Hook B runs once HK-A-SD and VOICE-C2-HKA are confirmed (call: `hooks/sd/HK-B.call.json`).
  preflight.py on the default branch already checks Seedance calls by `ingredients_approved` (V7.68.0); mine was dropped in favour of it.

- 2026-09-29 ~12:57 UTC: user Fix on Hook A — "Mama, when did that happen?" is the daughter's only line, no laugh, she should be shocked;
  the mother's hands never on the handrail going up. Source of the fault: the prompt's voice note had "half a laugh of disbelief" and the
  mother "her hand only brushing the rail". Fixed in `hooks/seedance_hooks.py` (both hooks): shocked face and gasp, only her one line,
  the mother's arms swinging free and hands never touching the rail or wall, negatives added. **HK-A-SD v2** (gen 2, preflight PASS,
  task 40365bb4, 693 credits) → To check; her line 9.28–10.62 s → **VOICE-C2-HKA v2** (9.00–11.00 s). v1 video + voice on Old.
  A third Hook A generation needs the user's go (§22X).

- 2026-09-29 ~13:35 UTC: user "thats an OA be realistic here no one would believe that" → chose "Tone down the daughter only", then
  "the daughter reaction looks like staged". Source: v2 prompt had her stop, look up past the lens with a frozen shocked face and a
  whisper-gasp. Now (both hooks): she is in frame from the start two steps behind, keeps moving, never looks at the camera, says the line
  to her mother with a small natural reaction; negatives against posing/overacting. **HK-A-SD v3** (3rd generation on the user's go,
  preflight PASS, task 71da4e8d, 693 credits) → To check; her line 8.10–10.56 s → **VOICE-C2-HKA v3** (7.85–10.95 s). v2 on Old.

- 2026-09-29 ~13:50 UTC: user confirmed Hook 1 (HK-A-SD v3), chose "Go up the mall stairs" for Hook B (matches the VO "the whole way up",
  no re-voice) and "Yes, use it" for the voice clip (VOICE-C2-HKA v3 confirmed on their word). Hook B rewritten: phone on the upper walkway
  looking down the flight, the daughter climbing with bags, the mother overtaking her on the open side going up, hands never on the rail,
  the daughter candid, never to camera. **HK-B-SD v1** (task 416c4189, 693 credits; ingredients N, C2, P8 v4, INFO-WARD-B-N/B-C2,
  @audio1 `hooks/sd/daughter_voice_HKA_v3.mp3`) → To check. Whisper: only her line, 7.98–10.58 s.

- 2026-09-29 ~14:06 UTC: user "the main character should be carrying bags too same as her daughter" → Hook B prompt: the mother carries
  two big shopping bags, one in each hand, like her daughter's (was one small bag + free arm); negative "no empty-handed mother".
  **HK-B-SD v2** (gen 2, preflight PASS, task 036eb3e4, 693 credits) → To check; only speech her line 8.10–10.56 s. v1 on Old.
  The confirmed Hook A prompt is kept as `hooks/sd/HK-A_v3.prompt.txt` (the shared negative now also has "no empty-handed mother").

- 2026-09-29 ~14:15 UTC: user confirmed both hooks → step 7, B-roll. `work/broll.py` writes the Mode 1 candid seeds (§22T) with the
  §30I–§30K angle / focus / light lines from the act map; Act 1's ten prompts (P-01a…P-05a) on the board as Prompt ready.
  Plates imported to Higgsfield (`plates/higgsfield_media.json`). First batch came back 768×1376 (no `resolution` param) — kept in
  `broll/images/*_v1.png`, not put on the board; re-sent at `resolution: 2k` (jobs in `broll/images/jobs_act1.json`). Higgsfield then
  asked to be signed in again before the 2K jobs could be collected — collect them once it is reconnected.

- 2026-09-29 ~14:55 UTC: Higgsfield reconnected (user). Act 1's ten B-roll images collected at 2K (1536×2752) and on the board To check;
  P-01b's first 2K job failed on Higgsfield and was re-sent once (job 551fef92). Next: the user's Confirm / Fix on Act 1, then
  `assemble.py --lengths` on the T2 beats (E6) and the Act 1 videos on Kling (§27G, preflight).

## Where it stands
- Voice done: VO T2 locked, TH-01…16 confirmed. Locations P0–P8 confirmed (16:9, Kie GPT Image 2). Outfit cards confirmed.
- **Hooks:** Hook 1 = HK-A-SD v3 confirmed. Hook 2 = HK-B-SD v2 To check (the mother with bags). In the edit the daughter's on-camera line replaces the
  mother reading "Mama, when did that happen?" in VO T2 (TH-01, 7.36–9.93 s).
- **Hooks:** both confirmed ("confirmed hookjs").
- **B-roll images (2026-09-29):** all 57 on the board To check, on Kie AI (nano-banana-2 / nano-banana-pro, 2K 1536×2752).
  The user flagged that the wardrobe was the same on every day. Fix: the wardrobe map in STEP4_5.md now gives every day and event its own outfit.
  - The problem days are split: D1 stairs + brace (house dress), D1b physical therapy (burgundy tracksuit), D1c pills (mustard sweater), D1d cortisone (striped blouse + navy skirt), D1e braces evening (olive knit top).
  - N-D7 box/card is a lilac top.
  - Every prompt names the day's clothes and takes only face, hair and build from the cast sheet ("not the clothes she wears on the sheet").
  - Act 1 fixes applied: P-01a (facing up the stairs, both hands on the rails, struggling backwards), P-01b (mid-flight, both feet onto the same step), P-02a (camera at her back, she looks down the stairs and turns away), P-03b (same brace as P-03a, ref = P-03a v1), P-03a ("fix the p03a too": grey cardigan + pink slippers, same brace).
  - Act 1 v1s were moved to the Old board.
  - **Fix round 2 (2026-09-29):** P-01a v3 and P-01b v3 were remade on nano-banana-pro. P-01a is filmed from the hall, side-behind: she faces up the stairs, both hands on the handrail, and reaches one foot down behind her. P-01b has both feet together on the same step, toes up the stairs.
  - P1-LANDING v6 (Kie GPT Image 2 i2i from P0) was rebuilt to match P0: full-width carpet with brass stair rods, small dark frames with black-and-white/sepia portraits, the console table, the coat stand and the front door below.
  - House wording everywhere is now "full-width oatmeal-beige stair carpet with brass stair rods", not "runner".
  - P1 v7 (Fix: "still not the same as the p0 stairs"): P0 layout mirrored for the view from the top (photo wall left, balusters right, coat stand in the hall beyond the balusters, front door and console bottom right, no corridor ahead); the P0 photo-wall crop (plates/P0-photowall_crop.png) is a 2nd reference.
  - **Fix round 3 (2026-09-29), 27 images on nano-banana-pro (Kie).** Root causes found:
    - (a) broll.py used only her face markers and never "a Black American woman … deep brown skin". Now NID/C1ID carry the skin line; the seed adds a skin line and "no white woman" on every N beat.
    - (b) The product size was never stated on worn shots. PS.SIZE_WORN is now added; the held shots state the size against the hand; the box shot states it against the forearm.
    - (c) The montage showed people putting the strap on. PR-01a/b/c are now productive: mulch up the porch steps, a wheelbarrow in the garden, a stepladder in the garage. C-07a is her heading out the door.
    - (d) M-01a's overhead camera is replaced by a companion's-chair eye-level view.
    - (e) M-05a now points at the patellar tendon, not the kneecap.
  - **Fix round 4 (2026-09-29), 12 images.** The model kept inventing its own knee gear. The seed now:
    - puts the product photos first in the refs;
    - opens with PROD_COPY ("copy it EXACTLY … NOT a brace/sleeve/pad/shield … on bare skin below the kneecap");
    - adds PROD_NEG.

    The beats changed:
    - PR-01b: the strap is hidden under long trousers.
    - PR-05a: her hands are off the strap.
    - PR-05b: no strap shown.
    - C-06a: made from a TH-09 frame (broll/images/TH-frame_ref.png), so her face and the landing match the talking heads.
    - L-02a: the tote comes from the L-01a render.
    - R-07a: starts from the very top step.
    - R-04a: the knee is bare under the rolled trouser.
  - **Fix round 5 (2026-09-29), 8 images.**
    - The worn photo now leads the refs, and PROD_COPY names the two peaks and the high placement right under the kneecap.
    - C-06a: the straps are held horizontally, each no longer than her hand.
    - L-02a: the tote is copied from a crop of L-01a (broll/images/L-01a_tote_crop.png).
    - M-06a: a new concept, her first step down facing the camera, hands free.
    - PR-03a: one strap, right knee, high.
    - PR-05a: made productive — she waters the flower bed.
    - R-07a: shot from the landing beside her, the very top step, a mug in her hand so she never touches the rail.
    - R-04a hit Kie's false "unsafe" flag once (no charge); the retry went through.
  - **Fix round 6 (2026-09-29), 4 images.**
    - PROD_COPY now states the strap's size against the kneecap: about as wide as the kneecap plus a thumb on each side, about as tall as the kneecap.
    - It also requires no bare skin between the kneecap and the strap.
    - R-07a uses the P0 viewpoint, with her face taken from the TH-09 frame.
  - **Fix round 7 (2026-09-29): M-06a v6, R-07a v6.**
    - The N_BUILD line (full-figured, heavy-set, wide round face) and a face crop from the cast sheet (broll/images/N-face_crop.png) went in, because she kept rendering slim.
    - N_HANDS gives her a mug and a dish towel, so her hands never touch the rail.
    - R-07a: she's upstairs on the landing (the TH frame spot), before the first step.
  - **Redo from scratch (2026-09-29), M-06a v7 and R-07a v7.**
    - M-06a: a close side view at step height, no face. Her slipper lands on the first step, the strap shows, and her free hand swings clear of the rail.
    - R-07a: the P0 view from the foot of the stairs. She stands upstairs on the landing before the first step, hands empty at her sides.
  - R-07a v8: "the strap is too big". This was an edit of v7 (prompt work/prompts/R-07a.edit.txt, refs v7 + worn_front + front): only the strap was shrunk, everything else kept.
  - R-07a v9: "wrong product and too low". This was an edit of v8 (work/prompts/R-07a.edit2.txt): the exact product, placed higher under the kneecap. nano-banana-pro failed twice on Kie ("create task failed", no charge), so it was sent on nano-banana-2.
  - **Act 1 videos v1 (2026-09-29)**, all 10 on the board To check.
    - Lengths: E6 from VO T2 (work/plan_T2.json → work/lengths_T2.json; P-01a…P-05a 3–5 s). PR-01b/c/d share one phrase and are PHRASE_NOT_FOUND — to be split before Act 5.
    - Calls: work/video_act1.py → broll/video/<beat>.call.json + prompt.txt, preflight PASS ×10.
    - Route: Kling 3.0 on Kie (`kling-3.0/video`, pro, 1072×1928, sound off), because the Kling connector has 3 credits (§5 fallback). 666 Kie credits.
  - **R-07a/b/c merged into ONE B-roll going down the stairs** (user). R-07a carries all three lines; R-07b and R-07c were moved to the Old board and removed from Current and the act map.
  - P-03b uses the new P-03a v3 as its brace reference. T-02a uses T-01b as its reference for Loretta's dress.
  - **P1-LANDING removed from the build (user 2026-09-29: "lets just remove it the p1").** All 7 versions are on the Old board, and the card and file are gone from Current. P-02a and C-06a now use P0 only (their current renders were made with P1 v5; regenerate only if the user asks). The confirmed hooks, TH and voice cards are untouched.
  - Asset ids are in broll/images/board_assets_2026-09-29.txt; Kie logs are in the scratchpad (URLs on the cards).
  - **Act 1 video Fixes + Act 2 videos (2026-09-29).**
    - P-01b video v2 (user: "same step on the stair both feet"): generation 2 of that shot. Locked camera, one step-to only, both feet end together on the same step and hold; alternating feet are banned (work/video_act2.py, preflight PASS). v1 is on the Old board. A third generation needs the user's go (§22X).
    - P-01a (user: "we should be looking at her back… walking down backwards same step both feet"): a new image first (v5, 12 Kie credits; v4 and the old video v1 moved to the Old board). Shot from the hall floor at the foot of the stairs looking up at her back; she comes down backwards facing up the flight, both hands on the rail, both feet on one step. nano-banana-pro gave Kie "Internal Error" (no charge), so it went on nano-banana-2. The P-01a video waits for the user to confirm this image. It will be video generation 2 and needs a fix_note.
    - Act 2 videos v1: T-01a 3 s, T-01b 5 s, T-02a 3 s, T-02b 5 s, T-03a 4 s. All are on the board To check. They used a locked camera and anatomy shots held still. 360 Kie credits, plus 72 for P-01b v2.
  - **Round 2026-09-30.**
    - P-01a image v6. User: "she should be way more up like half way of the stairs". Now about seven empty steps sit between the hall floor and her heels. v5 is on the Old board.
    - T-03a image v2. User: "should be the ghost limb anatomy here". Switched to ANAT-B (no muscle layer). anat() in work/broll.py now takes `dens`. Image v1 and the old video v1 are on the Old board.
    - Act 3 videos v1: R-01a, R-02a, R-02b, R-03a, R-04a, R-05a, R-06a, R-07a.
      - Built with work/video_act3.py; all pass preflight.
      - Locked camera. A RIGID strap clause goes on every beat that shows the strap.
      - R-07a is 6 s of her walking down forwards, hands free.
      - The R-02b download from Kie's file host crawled at about 1 KB/s, so it is being resumed with curl.
    - After the user's check:
      - R-03a video Fix: "make her just showing the stryde strap". Generation 2: hands stay on her thighs and she turns the knee a little toward the camera.
      - R-05a video Fix: "dont make her turn it over". Generation 2: hands still, the strap flat, the same side up.
      - P-01a and T-03a videos: generation 2 from the new confirmed images, each with a fix_note.
    - Act 4 videos v1: M-01a through M-06a (work/video_act4.py), all pass preflight. Anatomy shots use a completely still camera.
    - The Old board is full (1 GB), so the R-03a and R-05a v1 videos stay on Current as earlier versions until the user decides (a second Old board?).
    - M-03a runs 8 s as one clip, not split: E6 needs 7.6 s, and the §27G 6 s cap applies to human motion, not an anatomy pulse.
  - **Act 5 (2026-09-30).**
    - The PR-01a–d plan phrases are split into "Over 200,000" / "people" / "wear one" / "now", so each montage clip gets its own cut. `--lengths` now has no failures (3 s each), and work/lengths_T2.json is refreshed.
    - Act 5 videos v1 (work/video_act5.py), all pass preflight.
      - PR-01b and PR-05b keep the strap hidden under the trousers.
      - PR-04a jogs toward a locked camera and stays in frame.
    - M-04a and M-04b are on the board.
    - Kie's file host serves some finished renders at about 1 KB/s and drops the connection. A resumed curl join of R-02b came out corrupt, so it was deleted; P-01a v2 and R-02b now download clean from zero with getclean.py (scratchpad), which verifies the file decodes before it goes in.
  - **Act 6 + Act 5 Fixes (2026-09-30).**
    - PR-01b video Fix: "just normal pushing the wagon she should not be struggling". Generation 2: she straightens out of the lean and pushes lightly, one easy step; straining is banned.
    - PR-06a: "the stap is too big". The size is fixed in the start image, so this is an image edit of v1 (work/prompts/PR-06a.edit.txt).
      - Only the strap is shrunk: the shell is about as wide as the mug is tall, with the band looped behind it.
      - The PR-06a video waits for the user to confirm the new image.
    - Plan: C-01a's cut key moved from "strap" to "That", so L-03a no longer runs over the next line. L-03a now needs 6 s and C-01a 6 s; lengths refreshed.
    - Act 6 videos v1 (work/video_act6.py): L-01a, L-01b, L-02a, L-02b, L-03a. All pass preflight, locked camera, the strap hidden under the jeans.
    - PR-05a v1 arrived truncated from Kie's file host and is being re-downloaded clean.
  - **Act 7 (2026-09-30).**
    - Act 7 videos v1 (work/video_act7.py): C-01a, C-02a, C-03a, C-04a, C-05a, C-06a, C-07a, C-09a. All pass preflight.
    - Motion is written from the confirmed images. C-07a's image is her stepping down the porch steps, not the box from the old act-map note.
    - Downloads: Kie's `common/download-url` gives a direct storage link that is fast where tempfile.aiquickdraw.com stalls.
      - scratchpad fetch.py uses it and checks size and decode before a file goes in.
      - kie.py's own slow download is stopped once the task id is logged, so it can't overwrite a good file.
  - **2026-10-01: Current board storage full (1 GB).**
    - On the board: PR-06a image v2 (strap shrunk), PR-01b v2, L-01a, L-01b (2 parts), L-02a.
    - Rendered and kept locally, not on the board yet: L-02b, L-03a, C-02a–C-09a. The Old board is full too.
    - Waiting for the user to decide how to free space (e.g. a second Old board for replaced versions).
    - C-01a failed on Kie ("Image fetch failed") and was resent.
    - fetch.py fix: the signed direct link refuses HEAD requests, so the size is read from the GET's headers. That is why the first background fetches saved nothing.
  - **2026-10-01: second Current board (user's choice).**
    - Acts 6–7 + the edit now live on https://claude.ai/artifact/HSmTXmZTygXQAoyxk5Kqhc (same template, `BOARD_ROLE` "current", title "STRYDE · 71 Stairs · Acts 6–7"). Its `builds` doc has `boards.current` = this board and `boards.currentFirst` = the first Current board.
    - Nothing on the existing boards was moved or deleted. Images and the uploaded L videos were copied server-side; cast and plate references are written as `imageRefs` with `asset` so no extra cards show. Older archived image versions keep their Old-board `archiveAsset`.
    - Uploaded: L-02b (2 parts), L-03a, C-01a–C-09a, all To check. The first Current board's docs carry a note linking here.
    - PR-01b and PR-06a moved to this board too, because the first Current board can't take new files.
    - PR-01b video Fix: "use a different image cause he video gets distorted". The frame was the cause: a lunge with the back leg raised, the barrow seen nose-on with crossing, bent handles. New start image v4 (work/prompts/PR-01b.v4.t2i.txt, nano-banana-pro, ref = v3 for the same woman and garden): she walks upright behind the barrow in a clean side view, both feet down, straight handles, single wheel ahead. The light line had said "bedroom window" and now reads afternoon sun. Video generation 3 waits for the user to confirm image v4 (§22X go).
    - PR-06a video generation 2 from the confirmed image v2 (work/video_act6.py G2, preflight PASS).
  - **2026-10-01: Fixes + the edit.**
    - The user's Fixes pressed on the first Current board (PR-01b "new image", PR-06a "wrong image") are the same as the ones done on the Acts 6–7 board: PR-01b image v4 and PR-06a video v2 (from image v2) are To check there. The first board's cards point there.
    - Body rough cut v1: `assemble.py` with every beat's latest clip (`work/plan_rough_v1.json`), PASS (209.95 s, matches the master, no black frames). One ffmpeg graph with 70 inputs ran out of memory, so `work/seg_assemble.py` renders the same cut list segment by segment and joins them losslessly.
    - **FINAL-HK1 v1 / FINAL-HK2 v1** (`work/final_join.sh`): hook clip with the mother's VO 0–8.0 s laid over it (clip audio at 0.4 until 7.9 s, then her daughter's own line from the clip), then the body from 10.0 s ("Six weeks ago"). 210.9 s, 1080×1920, 24 fps. On the Final board as `review`, 11 parts each.
    - These finals use clips still To check. A Fix on any of them is re-cut locally for free: run `seg_assemble.py`, then `final_join.sh`.
    - Not done yet: the CapCut finish (captions, colour).
  - **2026-10-01 Fixes (Acts 6–7 board).** The user confirmed C-01a–C-09a (except C-05a), L-02b, L-03a and PR-06a v2.
    - **C-05a** video Fix "THIS SHOULD BE THE LOOK A LIKES": the image was at fault (v2 was a generic nylon strap with buckles). Image v3 (`work/prompts/C-05a.v3.t2i.txt`, nano-banana-pro, refs N sheet, P2, STRYDE front/back) shows two cheap look-alike copies of the real strap. Same shell, peaks, notch, band and slides, but glossy warped plastic, grey plastic slides, thin curling elastic and no brand. To check; video generation 2 follows the confirm.
    - **PR-01b** image Fix "NEW TYPE OF IMAGE" (v4 the wheelbarrow walk rejected): image v5 (`work/prompts/PR-01b.v5.t2i.txt`) has her hanging a white sheet on the garden washing line. She stands upright with both feet planted and a laundry basket at her feet, the strap hidden. To check; video generation 3 follows the confirm.
    - Round 2: the user confirmed PR-01b image v5. PR-01b video generation 3 (the user's go recorded as `user_go` in the call; `work/video_act6.py --g3`; she presses the peg onto the sheet and lowers her hands, feet planted) is To check.
      - C-05a Fix "SHOULD BE THE SAME AS COPIES": v3 came out as loose black loops. Image v4 (`work/prompts/C-05a.v4.t2i.txt`, product photos as the first refs) shows two copies with the exact shape of the real strap, blank (no wordmark) with a cheaper shine, lying flat on the torn mailer. To check; its video follows the confirm.
      - The finals are re-cut once C-05a's video exists.
      - C-05a Fix "SHOULD BE LOOKING CHEAP COPIES" (v4 looked like the real premium strap and showed only one). Image v5 is an edit of v4 (`work/prompts/C-05a.v5.edit.txt`): same shape and kitchen; thin glossy scuffed shell with a seam and a crack, dull grey plastic slides, curling elastic; a second identical copy added. To check.
      - The user said "CONFIRM": C-05a image v5 confirmed on their word. C-05a video generation 2 (`work/video_act7.py --g2`; she pushes the two copies away with the back of her fingers) is To check.
      - **FINAL-HK1 v2 / FINAL-HK2 v2** re-cut with PR-01b v3, PR-06a v2 and C-05a v2 (`work/plan_rough_v2.json`, rough cut PASS); on the Final board as `review`. v1 stays there as the earlier version (the Old board is full).
      - C-05a Fix "IT SHOULD JUST BE ONE PAD NOT 2 IN ONE STRAP" + "give me a new c05a cause its stuck": v5 and its video had two shells on one band. Image v6 is an edit of v4 with ONE cheap copy (`work/prompts/C-05a.v6.edit.txt`). To check; video generation 3 follows the confirm (user asked for a new C-05a).
  - **2026-10-01: the music (V7.77 §40A, user "use the new bgm update").** The default branch (V7.77.1) was merged into the session branch.
    - The Music Register Map is BUILD_SHEET 5c (`work/music_register_map.md`), mirrored to `docs/music` on the Plan and Acts 6–7 boards. Hook MUS-OPEN → Act 1 EXPOSE → Act 2 OPEN → Act 3 EDU → "I did." TURN → Act 4 EDU → Acts 5–6 AFTER → Act 7 OFFER, as one family: felt piano, low cello and strings, a soft pulse.
    - Composed with ElevenLabs Music, one track (`edit/music/MUS-FINAL.cue.json`).
    - music.py check on the raw track failed: it ended early (faded by 208.5 s, the video runs 210.9 s) and the sections were barely louder or softer than each other. Both were fixed in the mix: the final chord was extended with a crossfade, and section levels were set (low −4, mid 0, high +2.5 dB). The bed re-check passes LENGTH, ENERGY, DROPOUT, VOCALS and TEMPO. The CLICK flags left are musical onsets.
    - Mixed by `work/music_mix.sh`: voice about −14.5 LUFS, music about 18 dB under it in pauses and about 26 dB under while she speaks.
    - The first mix was 39 dB under, inaudible, and was corrected. The reference had no music bed (EG07); this deviation is noted.
    - FINAL-HK1 / FINAL-HK2 board v3 (local files `_v4`) have the music and C-05a v3 (one cheap copy, the user's go after "give me a new c05a"). They are on the Final board as `review`. The MUS-FINAL audio card is on the Acts 6–7 board.
    - The Final board holds 3 versions × 2 finals (~0.9 GB), so a later re-cut needs room (a second Final board).
  - **2026-10-01: music v2 (user: "i want a ne one investigation and change whe nthe produt shows not a sad").** The default branch (V7.77.2) was merged.
    - New cue (`edit/music/MUS-FINAL.v3.cue.json`): before the strap, an investigation register (ticking, low synth pulse, plucked strings; sad piano and cello banned). From the product reveal (R-03a "She pulled up her pant leg", 72.3 s in the finished video) it turns warm and major to the end.
    - Three compositions: the first went silent for 19 s near the end and the second stopped dead for 7 s at the strap reveal, so both were discarded. The third asked for continuous music and plays through.
    - The bed is shaped by `work/music_bed.py`: levels −17 dB before the strap, −13.7 from it, −9.7 in the proof. Mixed at about 18 dB under the voice in pauses and 26 dB while she speaks, −14.4 LUFS.
    - The register map is rewritten (BUILD_SHEET 5c, `docs/music` on Plan and Acts 6–7). The MUS-FINAL card has v3 (raw) and v4 (bed).
    - The first Final board was full (0.92 GB), so **Final 2** https://claude.ai/artifact/Hcw2AWLhQAmz1pVMs2TY1u was published from the template (`BOARD_ROLE` "final"). FINAL-HK1/HK2 cut 4 (local `_v5`) are on it as `review`. The first Final board's cards link there.
  - **2026-10-01: music v3 (user: "the music chnage wehn the product shows"; V7.78.0 merged).** The product's first frame is R-03a at 72.28 s (act map: the first `worn · REVEAL` row; the hooks and T-02a keep it hidden).
    - The single-track bed never changed character there: its brightness was the same either side, and only my level step marked it.
    - Now two compositions of one family: MUS-A investigation (`edit/music/MUS-A.cue.json`) and MUS-B warm major (`MUS-B.cue.json`). They are joined on the frame by `work/music_splice.py`: A's last bars repeat to 71.3 s, then a one-second breath, then B's full chord at 72.30 s. B's offer section repeats to cover the last line, and the levels come from the cue.
    - Combined cue `MUS-FINAL.v5.cue.json` with `product_at` 72.28: plan PASS. Bed check passes except the CLICK flags, all located on musical onsets.
    - Mixed at −8.0 dB music gain: 18.1 dB under the voice in pauses, 26.2 under speech, −14.4 LUFS.
    - FINAL-HK1/HK2 **cut 5** (local `_v6`) are on Final 2 as `review`. The MUS-FINAL card has v5 (A), v6 (B) and v7 (bed).
  - **2026-10-01: the finish (user: "confirm proceed").** Confirmed on the user's word: MUS-FINAL and FINAL-HK1/HK2 cut 5 (C-05a v3 and PR-01b v3 were already confirmed on the board).
    - **Cut 6** (local `_v7`): EG01 boxed captions burned in by `work/captions.py`. Black text on white boxes, centred at 72%, phrase by phrase; long clauses split evenly; no caption ends on a small word; no word stands alone unless it is a one-word phrase.
    - The captions are the script verbatim, all 613 words in order (checked). They are timed to each video's own audio: Whisper aligned to the script, 581/584 words matched and the rest spread between neighbours.
    - On Final 2 as `review`.
    - **Shot match (§40 step 1, Mode 1: no LUT, no creative grade):** `light_check.py colour` per scene (location + story day, anatomy excluded). 15 clips are off their scene's first shot; the largest are T-01b and T-02b at the reception, about 30% darker.
    - Left for the team in CapCut desktop as `edit/CAPCUT_MATCH.md`, also `docs/match` on the Plan board. The clips were not changed.
  - **2026-10-01: B-roll on the script lines (user: "BROLL PLACEMENT ARE NOT TIMED ON THE SCRIPT LINE FIX THAT").** The default branch (V7.78.1) was merged.
    - Cause: every plan row carried `key`, the word the picture shows, so assemble.py cut on that word, not the line's start. 44 of 55 B-rolls came in more than 0.3 s late: most by 2–3 s, PR-02a by 5.0 s, R-07a by 9.1 s (it waited for "Forwards").
    - `work/plan_rough_v4.json` has no keys: each B-roll cuts 6 frames before its line's first word. Measured on the render (`edit/ROUGH_BODY_v4.timing.json`): all 50 cuts land 0.08–0.27 s before their line's first word.
    - Lines too short for a 2.0 s picture:
      - P-02a starts on "going down them at all. I'd just stay upstairs." (she looks down the flight).
      - R-03a starts on "something? She pulled up her pant leg."
      - The list "I done tried everything. Physical therapy. Pain pills. Cortisone shots." is one composite clip, `P-04abc_list` (`work/composite.py`). P-04a, P-04b and P-04c each cut on their own words: 3.5, 0.84 and 1.4 s.
      - The montage "Over 200,000 people wear one now." is `PR-01abcd_montage`: four pictures of 0.69 s each.
      - These two lists are faster than 2 s per picture. That was a choice for placing each picture on its item; the user is told.
    - `work/seg_assemble.py` now holds each segment's last frame to its full frame count. The first render was 0.12 s short because clips exactly as long as their slot dropped a frame. Re-render PASS, 209.95 s.
    - The strap's first frame (R-03a) moved from 72.28 to 70.41 s. Music re-spliced from the same two pieces (`MUS-FINAL.v6.cue.json`, bed v6): plan PASS. The bed check's CLICK flags are musical onsets as before. Its TEMPO reads 199 BPM on the same composition (66 BPM on v5), a detector octave error.
    - The MUS-FINAL card has v8 (bed v6), `review`. `docs/music` on Plan and Current 2 is updated.
    - Final 2 is near 1 GB, so **Final 3** https://claude.ai/artifact/P5J5XwVeLRrFR1nbSPaLj4 (template, `BOARD_ROLE` "final") was published. The `builds` doc's `boards.final` on every board points to it.
    - FINAL-HK1/HK2 **cut 7** (local `_v10`; `_v8` no music, `_v9` music) are on Final 3 as `review`: 210.9 s, −14.4 LUFS, captions verbatim (613 words).
  - **2026-10-01: cut 8 (user: "REMOVE THE CAPTION BACKGROUND, THEN SOME BROLLS STILL LATE OR EARLY TO SHOW AND END FIX THE BROLL PLACEMENTS").** The default branch (V7.79.1, §30H rules 0/1/5/6: cut on the line, a hold never runs into the next line, no word under another line's picture) was merged.
    - Captions (`work/captions.py`): white text with a black outline and a light shadow, no box. Same phrasing and timing; all 613 words verbatim.
    - `work/script.lines.txt` held one paragraph per line, so the new line check saw no line ends. `work/script.sentences.txt` has one sentence per line (93, the same 613 words), and `work/plan_rough_v5.json` uses it.
    - The check found six B-rolls running into the next sentence (P-01b, P-02a, P-04d, PR-02a, L-03a) or cutting in mid-sentence (T-02a on "and").
    - Fixes:
      - The P-02a and R-03a phrases are back on their own sentences.
      - T-01b and T-02a: T-01b runs "My cousin Loretta was there. She's 74," then T-02a cuts in on "and she was out on that dance floor".
      - P-04d ends at 33.08 s (`in` 0.4, `out` 2.5), before "Nothing worked."
      - L-03a holds over "I said, 'I know.'" on purpose (`span: hold`). It is the same moment, and the face gap would be under 1.5 s.
    - Lines too short for a 2.0 s picture share one clip with their neighbour (`work/composite.py`), each picture changing on its own line: `P-01ab_pair`, `P-0203_pair`, `R-0304_pair`, `T-01b-02a_pair`, and `PR-01-02_montage` (the 4-person montage then PR-02a). The P-04abc list stays.
    - Rough cut v5 PASS: 45 cuts, each 0.08–0.27 s before its sentence's first word, at least 2.0 s on screen, and none over another sentence's words except the L-03a hold (`edit/ROUGH_BODY_v5.timing.json`).
    - The strap shot is back on "She pulled up her pant leg", so its first frame is 71.33 s. Music re-spliced from the same two pieces (`MUS-FINAL.v7.cue.json`, bed v7): plan OK; the check flags only CLICK onsets. The MUS-FINAL card has v9 (`review`). `docs/music` on Plan and Current 2 and BUILD_SHEET 5c are updated.
    - FINAL-HK1/HK2 **cut 8** (local `_v13`; `_v11` no music, `_v12` music) are on Final 3 as v8, `review`: 210.9 s, −14.4 LUFS. Final 3 now holds about 580 MB.
    - The hourly Fix check prompt points at plan v5, bed v7 and 71.33 s.
- **Next:** Acts 1–7 B-roll on the T2 beats → edit → FINAL-HK1 / FINAL-HK2 on the Final board.
  - **2026-10-02: Hook 3 (user: "one more hook — going down stairs holding shopping bags at a metro station, running to catch the metro, then inside the train her daughter says something like that"; "same concept as the other 2 hooks"; kept "down" after the VO's "the whole way up" was flagged).**
    - Same concept as Hooks 1 and 2: **HK-C-SD**, one continuous Seedance 2.5 clip (12 s, 720p), the phone propped inside the stopped train looking out through the open doors at the platform stairs; the mother hurries down with two shopping bags past two women in their thirties, crosses the platform and steps in; the daughter follows and, inside, says "Mama, when did that happen?" (@audio1 = VOICE-C2-HKA v3). Mother's VO laid over it in the edit. "Running" written as a brisk hurry (§35A); the speed is made in the edit.
    - §30M five concepts in `hooks/hk3/hk3_visual_plan.json` (PASS) — superseded by the user's own brief.
    - New references on **Current 2** as To check: **P9-METRO** plate (Kie gpt-image-2, 16:9, 10 cr), **INFO-WARD-C-N** (teal quilted jacket, cream knit top, charcoal trousers, white trainers) and **INFO-WARD-C-C2** (olive utility jacket, grey hoodie, black jeans, black trainers) (Higgsfield nano_banana_2 + caption band). N and C2 sheets and the voice clip copied to Current 2 as ingredient files.
    - `hooks/hk3/seedance_hk3.py` → `HK-C.seedance.txt`; `HK-C.call.json` preflight PASS except "every ingredient approved" — the video is sent once the user confirms P9 and both outfit cards.
    - Same day, user: "Cause the last sunday is a different scene" → Hook 3 is **two shots**, cut together: **HK-C1-SD** (5 s, silent, `generate_audio: false`) under "I'm 71… half my age." (VO 0.00–3.94 s) — she hurries down the metro stairs past two women in their thirties and into the waiting train, seen from inside the carriage (P9); **HK-C2-SD** (7 s) under "Last Sunday… the whole way up and said," + the daughter's line — inside the moving train, same door wall as P9 (doors closed, no reverse plate needed), the daughter says "Mama, when did that happen?" (@audio1). One SCENE SO FAR block in both (HT23). HK-C-SD card replaced by the two cards on Current 2; both calls preflight PASS except ingredient approval. About 63 Kie credits a second → ~315 + ~440.
