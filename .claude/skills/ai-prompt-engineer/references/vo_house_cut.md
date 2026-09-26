# VO house cut — measured from the user's reference edit (2026-09-26)

The user supplied their own trim of a §22U VO (`builds/stryde-identity/vo/ref/A_MUST_FOR_vtrim.mp3`: HK1 + body of
take T4, 57.55s, 191 words) with "this is how I would cut it, make this as an example". It is the spec for every
audio-only VO trim (hooks, bodies, variant masters). `scripts/vo_trim.py` defaults reproduce it.

| Measure (reference) | Value | `vo_trim.py` |
|---|---|---|
| Silence at phrase breaks (, . ? !), 24 breaks | 0.02s median, max 0.08s — butt joins | `PAUSE_SENT` 0.015s |
| Silence between other words | removed to ~0.01s | `PAUSE_WORD` 0.01s |
| Short gaps inside words (stop closures) | kept, 20–60ms, max 0.14s | `MERGE` 0.12s: shorter silences untouched |
| Silence left in total | 1.61s in 57.55s (40 runs ≥ 20ms) | 1.1–1.3s in ~58s |
| Where a word is cut | once it falls to about −38 dBFS (median of 24 breaks) — the audible word is whole, the quiet decay goes | `FLOOR` −38 dBFS, 20ms fade |
| Breaths | none left | breaths cut at phrase boundaries |
| Hook → body | butt-joined like any phrase break | raw hook + raw body trimmed in one pass |
| Speed / pitch | unchanged (F0 126 vs 127 Hz source; no tempo change) | no speed change |
| Start / end | starts on the first word's onset; ends ~−41…−46 dB with a fade | `HEAD` 10ms; `TAIL` 20ms + 20ms fade |

Check against the reference (stryde-identity, HK1 master): 57.85s vs 57.55s; 40 silences, 1.34s total vs 1.61s;
no breaths; every word present.
