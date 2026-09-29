# VO — §22U steps 8–10a (stryde-too-bad)

One request per take: HK1 + BODY1 + HK2 + BODY2, voice `TooBad` (5Iu9piJEpm2ewCIAa3Wm), `eleven_v4`, `tts_api.py`. Every text passes `tts_budget.py --script-lines` (verbatim PASS).

| Text | Tags | Chars | Takes | Raw | After the house cut (per video) |
|---|---|---|---|---|---|
| `ALL.enhanced.txt` (v1) | Enhance tags + `[slowly]` per paragraph + `[pause]` per sentence | 2,434 | T1–T4 (speed 0.8) | ~120s, 157 wpm | 58–61s, **154–161 wpm** |
| `ALL.enhanced.v3.txt` | Enhance tags only (no pace tags) | 2,038 | T5–T8 (speed 1.0) | 110–113s, 167–172 wpm | 55–57s, **166–172 wpm** |

**Measured, 2026-09-29:** `voice_settings.speed` has no effect on `eleven_v4` (a v1 probe at 0.92 ran 121.4s vs 120.8s at 0.8) — the standard marked it unverified. Pace here is set by the tags. With every sentence ending on `[pause]` this short-sentence script finishes near 155 wpm; without the pace tags, 167–172, closest to the inspo's ~180 (the house cut's 0.45s sentence pause is the rest of the gap). Probe files: `full/probe092_T1.mp3` (v1 text at 0.92, not a board take). Two further probes were mis-built (my file moves overwrote their texts with v1) and were deleted.

**Split and cut:** `split_vo.py` (the build-local `cut_points.py` for HK1|BODY1|HK2|BODY2) finds the boundaries by word timestamps; each video (hook + its body, contiguous in the take) is cut from the take and house-cut in one pass (`vo_trim.py --script V<n>.lines.txt`): `cut/T<n>_V1.mp3`, `cut/T<n>_V2.mp3` — every one PASS (no breaths left, no gaps over the limit, every word finished). Then each is split mid-gap into `parts/T<n>_HK<v>.mp3` + `parts/T<n>_BODY<v>.mp3` for the board.

**Working take (§22U step 10): T5** — T1 passes the take check, but the v1 takes miss the inspo's pace; T5 is the first take at the right pace. Every take is on the board; a different confirmed take re-cuts that part.
