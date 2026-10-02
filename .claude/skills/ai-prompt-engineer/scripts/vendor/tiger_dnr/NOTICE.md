# TIGER-DnR (vendored)

Dialogue / effects / music separation used by `scripts/unmusic.py` (§24M, V7.92.0).

- Source: https://github.com/JusperLee/TIGER — commit `9f18d4a10a7137e1ce8052cfb62215179f1287b6` (2026-04-20)
- Paper: Xu, Li, Chen, Hu — "TIGER: Time-frequency Interleaved Gain Extraction and Reconstruction for Efficient Speech Separation", ICLR 2025 (Tsinghua University)
- Weights: Hugging Face `JusperLee/TIGER-DnR` (downloaded on first use into the Hugging Face cache, not stored in this repo)
- Licence: Apache License 2.0 (`LICENSE` in this folder)

Copied files: `look2hear/models/tiger_dnr.py` → `model.py`, `look2hear/models/base_model.py`, `look2hear/layers/activations.py`, `look2hear/layers/normalizations.py`.
One change: `model.py` imports `activations` and `normalizations` from this folder (`from . import …`) instead of `..layers`, so the rest of the upstream package (training code and its dependencies) is not needed.
