#!/usr/bin/env python3
"""Build-local wrapper (down-forwards-again only): runs the shared assemble.py with MIN_FLASH 1.5 s instead of 2.0 s.
ADJUST 2026-09-29, user: "the broll are late" — with three 'Without…' cut-ins on one line (the user's own ask, 'SHOW ALL OF THOSE')
the 2.0 s minimum pushes each cut after its word. The shared script is not changed (CLAUDE.md: a system change never touches other builds)."""
import sys, runpy, pathlib
S = pathlib.Path(__file__).resolve().parents[4] / ".claude/skills/ai-prompt-engineer/scripts"
sys.path.insert(0, str(S))
g = runpy.run_path(str(S / "assemble.py"), run_name="assemble_lib")
g["MIN_FLASH"] = 1.5
g["main"].__globals__["MIN_FLASH"] = 1.5
g["main"]()
