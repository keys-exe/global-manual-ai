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

## Fix round 1 (2026-09-28, user Fix notes on 19 B-roll videos)
- Diagnosed per §22X; prompts `prompts/frames/<b>.fix1.txt`, `prompts/clips/<b>.v2.kling.json`, calls `calls/<b>.v2.json` (all preflight PASS), scripts `work/fix1*.py`.
- Motion-only fixes (old frame kept): A1-B2 (step-to, both feet on each step), A1-B4, A1-B5 (visible struggle), A4-P1 (band swings with weight). Rendered and on the main board as To check (video v2).
- New frames (Higgsfield nano_banana_pro, 2k) + new clips: A2-B1, A2-B2, A3-B2, A4-B1, A4-B2, A4-M1, A4-P2, A4-P3, A5-B1 (N in work shorts lifting a toolbox), A5-B2, A5-B3, A5-B4, A5-B5, A5-F1. Clips rendered; job ids `work/fix1_jobs.json`, `work/fix1_kie/`.
- All 18 clips on Kie Kling 3.0 (`kling-3.0/video`, pro 1080p) — Kling account at 591 (§5 fallback). Kie spend 1,296 credits (230,736 → 224,010).
- A2-M4 not regenerated: it would be the third video generation (§22X) — waiting for the user's go.
- A4-P1 v2 flagged: the shell reads as lost mid-clip as the band swings; a third try needs the user.
- **Blocker:** the main board's asset store is full (1 GB). Fixes board https://claude.ai/artifact/VxngRxNy7t4faxWgNbGJkt created, 14 new frames uploaded there; uploading the 14 new clips was blocked by the session's permission check — waiting on the user. The 14 main-board cards stay `generating` until then. Orphan assets on the main board (~116 MB, unreferenced by any card) were found but not deleted.
- Local renders are not in git (`renders/fix/`); they are lost when this container ends — upload or re-fetch from the Kie URLs (valid ~24h–3 days) in `work/fix1_kie/`.
