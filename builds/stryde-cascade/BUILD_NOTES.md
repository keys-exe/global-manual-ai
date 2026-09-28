# stryde-cascade — build notes

**Build:** STRYDE · The Cascade ("Four Hundred Houses"), picture-in-picture talking head + B-roll, Mode 1, 9:16.
**Run mode:** Automatic (user: "run automation", 2026-09-28). Final videos only; no mid-run messages.
**Drive task folder:** `1nOldjHSuTw6koTHeChJ5BDvZ1MtNBfld` · OUTPUT `1KbCoR11ZmdFzVQSFwqQxGfK5sXqilmaC` (IDs in `drive.json`).
**Board:** https://claude.ai/artifact/QK6FwiCxWuZqoWWVoEx2Yd

## Decisions
- Mode 1 (MODE not given, F5). Three hooks run as written (F4). Caps: E0 default (Higgsfield 600 · Kling 3,000 · Kie 2,000).
- Cast: N (rail fitter, 61, narrator/talking head), C1 (woman, 74; D1 lilac, D2 navy, D3 pink gown), C2 (man, 68, strap on the right knee).
- Voice: clone `Cascade` = `maQgQv00HcQWiW4KwvNq` from three Kling voice takes; TTS flow `PJKuAqmYuN2pReFBUBfa`, master take T4; house cut per variant (`vo/master/*.wav`).
- Talking heads: HeyGen photo avatar `c8d9b4ef04136707e55f0cc8c4447444`, Avatar IV fallback (F9). Videos `th/TH-*.mp4`.
- B-roll: 40 beats (9 hook, 31 body), frames on Higgsfield, clips on Kling `kling-video-v3_0_omni`, audio off (F7). Every frame and clip judged §22V/§22W; rerolls and faults on each board card.
- Assembly: `variants.json` → `variants.py` (hook + identical body). Act 1 "Then…" list cut on each "Then" (F16); A2-B3 `out` 2.1s.
- Finishing: `edit/CAPCUT.md` (captions, banners, 17× / 34% / 200,000 overlays, offer card).

## Delivered (2026-09-28)
- Finals: `edit/STRYDE-CASCADE_HK1/2/3.mp4` (2:03.4 / 2:02.2 / 2:02.4, 1080×1920, 24 fps) — each variant PASS; body identical to the frame (F18).
- Where: full-quality finals page https://claude.ai/artifact/3uDVLnVKanAFsfna7pxvSb (board storage full, Drive connector inline-only — F19). Board FINAL-HK1..3 cards link it.
- Drive 08_EDIT: `OUTPUT.md` (1kiCvVa7wmuPa_H1AHrin3sal2yiV-zBe), `CAPCUT.md` (1X5bJ7U--vksuYpLdORqkccUd5RV3_C89).
- Talking heads for the edit: `th/TH-*.pad.mp4` (held last frame; hooks cut to the VO frame count).

## Spend (start → end balance)
- Higgsfield 20,185.5 → 19,730.25 = **455** of 600.
- Kling 4,087 → 591 = **3,496** of 3,000 — over by 496 (F8: connector under-reports the charge ~2.8×).
- Kie: uploads only (F17).

## Open items
- Flags F1–F3 (claims/disclosure) are the advertiser's call before publishing.
- v2 re-edit (F20, BUILD_SHEET): slower VO (master v2 T2, 199–203 wpm), ~3s B-roll holds, 6/34 split/pip.
- **Resumed 2026-09-28 (session_01XyVmRtQqCbrULWxujVtka1):** the user is checking the B-rolls on the board and will leave Fix notes. Their Fixes are regenerated (no agent verdict), put back as To check; once confirmed, the three finals are re-assembled from the plans. Hourly Fix check `trig_01N8qwCCCFT9S55QL3zasmbh`. Media is not in git — a regenerate/re-assembly pulls clips, VO and heads back from the board assets. A2-M1, A2-M3, A2-M4 already have two video generations: a third waits for the user's go (§22X).

## Files
Prompts `prompts/` · calls `calls/` · act map `actmap.json` / `ACTMAP.md` · job ids `work/jobs.json`, `work/kling_jobs.json` · board cards `work/board/`. Media stays out of git (`renders/`, `th/`, `vo/`, `edit/*.mp4`).
