#!/usr/bin/env python3
"""Build-local wrapper (down-forwards-again only): runs the shared assemble.py with MIN_FLASH 1.5 s instead of 2.0 s.
ADJUST 2026-09-29, user: "the broll are late" — with three 'Without…' cut-ins on one line (the user's own ask, 'SHOW ALL OF THOSE')
the 2.0 s minimum pushes each cut after its word. The shared script is not changed (CLAUDE.md: a system change never touches other builds)."""
import sys, runpy, pathlib, os
S = pathlib.Path(__file__).resolve().parents[4] / ".claude/skills/ai-prompt-engineer/scripts"
sys.path.insert(0, str(S))
g = runpy.run_path(str(S / "assemble.py"), run_name="assemble_lib")
import os
G = g["main"].__globals__
G["MIN_FLASH"] = float(os.environ.get("DFA_MIN_FLASH", 1.5))
# ADJUST 2026-10-01, user: "SOME OF THE BROLLS ARE MISSING, BROLL PLACEMENT ARE NOT TIMED TO THE SCRIPT LINE" — the body keeps every
# B-roll on its own line, so a 1.0 s line ("The garden.") shows its clip for its line: DFA_MIN_FLASH=1.0 on the body cut.
# ADJUST 2026-09-29, user: "the broll ends even though the script line hasnt finish yet": B-roll holds past its line's last word
# (DFA_HOLD seconds on screen when the footage and the next cut allow); cuts land on the next line's first word (--lead 0).
if os.environ.get("DFA_HOLD"): G["HOLD"] = float(os.environ["DFA_HOLD"])
g["main"]()
