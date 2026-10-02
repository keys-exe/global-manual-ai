# Half My Age — takes against the V7.93.0 rule (§24K parts 5–5A)

Report only: nothing was regenerated. Prices use Kie Seedance at **63 credits per second** of take (this build's measured rate).

**How it was measured.** The act map now names each row's take (the confirmed ones), `vo`, `dialogue` and `hold_s`. The narration is the locked line files (`edit/body/vo/L0xx.mp4`, `edit/vo/L004_v2.m4a`, `L016_v2.m4a`). They were transcribed with medium.en, the script words were lined up on the timings, and the lines were joined in script order with 0.5 s between them (`vo_words.json`). The hook VO is in it once per hook. A take's length is its VO plus its holds, rounded up. On-screen dialogue uses the E6 estimate (2.4 words a second plus a breath), so dialogue-only takes are **estimates**. `takes.py`: **35 FAIL** (`takes_check.txt`, table in `takes.md`). The tool's own proposal is in `takes_suggest.txt`: 89 rows in **36 takes**, against **57 takes** today.

## (a) Scenes still split that the new rule makes one take

| Scene | Today (generated s) | New rule | Why |
|---|---|---|---|
| SC02 stairs, night | SH01 + SH02 (7 + 4) | 1 take, 8 s | same stairs, same evening: she calls down, he lifts the bags |
| SC02 stairs, morning | SH03 + SH04 (6 + 4) | 1 one-take, 7 s | one walk down backwards |
| SC02 kitchen | SH05 + SH06 (4 + 4) | 1 take, 4 s | one exchange over the mug |
| SC03 landing | SH01 + SH02 (4 + 4) | 1 one-take, 6 s | the brace slides, then lies at the ankle |
| SC03 bedroom, evening | SH06 + SH07-08 + SH09-10 (5 + 8 + 12) | 1 take, 25 s (conversation) | the drawer, the husband and the phone call are one evening in one room |
| SC04 wedding | T1 + T2 (10 + 14) | 1 take, 23 s (conversation) | one place, one evening, under 30 s |
| SC05 + SC06 kitchen | SC05-T1 + SC0506-T1 (12 + 15) | 1 take (30 s), or 18 + 12 as `takes.py` proposes | the same table, the same morning. SC0506-T1 also fails TAKE+ only because it spans the SC05/SC06 labels |
| SC08 kitchen | T1 + T2 + T3 (12 + 15 + 12) | 2 takes, 21 + 10 s | about 32 s of talk runs over 30 s, so one split is real. T1 and T2 are one take |
| SC12 café | T1 + T2 + T3 (14 + 11 + 12) | 2 takes, 20 + 20 s | about 41 s runs over 30 s, so one split is real. Three takes is one too many |
| Hooks HKA · HKB · HKC · HKE | 20 single shots | HKA 11 + 9 s (station, carriage), HKB 17 s, HKC 20 s, HKE 17 s | each place in a hook was one call per shot |

Also flagged, not a merge:
- **SC07-T** (15 s) needs 19.5 s for L042–L045 and runs past the 15 s action ceiling (VO_LONG). It splits after "Both feet." into 10 + 11 s.
- **SC13-T1** (13 s) needs 16.5 s (VO_LONG). It splits after "…the same week." into 7 + 10 s.
- **SC12-T3** needs 15.5 s (VO_LONG). The SC12 regroup above covers it.
- **SC13-T2** goes from the front door (P-HOUSE) to the stairs (L-STAIRS), so TAKE+ flags a location change. The take is one continuous walk-in and was confirmed. I left it as it is.

## (b) Generated length against measured VO length

**Shorter than its VO plus holds** (the picture leaves before the line ends):

| Take | Generated | Needs | Short by |
|---|---|---|---|
| SC0506-T1 | 15 s | 21.1 s | 6.1 s |
| SC07-T | 15 s | 19.5 s | 4.5 s |
| SC13-T1 | 13 s | 16.5 s | 3.5 s |
| SC12-T3 | 12 s | 15.5 s | 3.5 s |
| SC03-SH06 | 5 s | 7.8 s | 2.8 s |
| SC12-T1 | 14 s | 15.9 s | 1.9 s |
| HKC-SH01 | 4 s | 5.6 s (tannoy estimate) | 1.6 s |
| SC09-T2 | 5 s | 5.7 s | 0.7 s |
| SC02-SH07 | 6 s | 6.7 s | 0.7 s |
| SC10-T2 | 4 s | 4.4 s | 0.4 s |
| SC03-SH09-10 | 12 s | 12.3 s | 0.3 s |
| SC04-T2 | 14 s | 14.3 s | 0.3 s |
| SC09-T1 | 8 s | 8.1 s | 0.1 s |

**Longer than needed.** These are trimmed in the edit and need no redo: SC05-T1 +4 s, SC03-SH07-08 +3, SC08-T1 +3, SC13-T2 +3, SC03-SH04 +2, SC08-T2 +2, SC08-T3 +2, SC12-T2 +2, and +1 on HKA-SH01, SC02-SH01, SC02-SH03, SC04-T1, SC09-T3, SC10-T4, SC10-T5, SC11-T1.

## (c) Cost to redo (63 cr/s, at the new take lengths)

| Redo | Seconds | Credits |
|---|---|---|
| SC02: three merged takes | 8 + 7 + 4 = 19 | 1,197 |
| SC03: landing + bedroom evening | 6 + 25 = 31 | 1,953 |
| SC04: one wedding take | 23 | 1,449 |
| SC05 + SC06: kitchen (fixes SC0506-T1 being 6 s short) | 30 | 1,890 |
| SC07: split for VO_LONG | 10 + 11 = 21 | 1,323 |
| SC08: two takes | 21 + 10 = 31 | 1,953 |
| SC12: two takes (fixes T1 and T3 being short) | 20 + 20 = 40 | 2,520 |
| SC13 kitchen: split for VO_LONG | 7 + 10 = 17 | 1,071 |
| **Body total** | **212 s** | **13,356** |
| Hooks HKA · HKB · HKC · HKE merged | 20 + 17 + 20 + 17 = 74 | 4,662 |
| **Body + hooks** | **286 s** | **18,018** |
| Optional, under 1 s short (the edit can cover these): SC02-SH07 7 s, SC09-T1 9 s, SC09-T2 6 s, SC10-T2 5 s | 27 | 1,701 |

**Limits of these numbers:**
- The VO gaps here are a uniform 0.5 s, not the edit's real gaps.
- Dialogue lengths are E6 estimates, not measured.
- `takes.py` checks a `length` split against the neighbouring take only. So the two real splits (SC08-T3, SC12-T3) still show as SPLIT fails, because the take before each one should have been merged.

Under §24K a running build keeps its takes unless its team asks. Nothing here is redone without the user's go.
