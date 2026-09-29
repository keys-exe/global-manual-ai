# TH-A — narrator talking head, Hook 1 (Variant A)

- Asked by the user 2026-09-29 ("GIVE ME THE HOOK A TALKING HEADS") — the Build Sheet was voice-only / 0 talking heads ("say 'talking heads' to change").
- §22U talking-head task: raw take 1 (ElevenLabs history AGEjLCNEsKA4hCC0ADOI, untrimmed), Variant A = 0–66.8s (hook + body), one HeyGen pass.
- HeyGen: photo avatar `efbb46e8744762728bf0d65d16031742` from N-VOICE-IMG (hf_20260928_154353_f96a440e…), engine **avatar_v**, 9:16, 1080p; audio asset `3e5510de2cbb46268a8c287ab82fa9fc`; video `e500b4986685a2c736aa09a1d4475515`.
- Motion prompt rejected by Avatar V (photo avatar with no digital twin in its group) → rendered without it (§22U step 13 allows this).
- Hook cut at 5.73s (word "longer." ends 5.64s, "Built" starts 5.83s), trimmed `trim.py --style natural` → 5.32s, PASS (hook alone 225 wpm; the pace gate applies to hook + body).
- Board: `generations/stryde-lost-moments__TH-A` — videoAsset = trimmed hook; rawParts = the untrimmed full render (3 × 15 MB parts).
