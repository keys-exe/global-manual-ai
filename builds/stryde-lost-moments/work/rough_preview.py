# Rough-cut preview only: lets the short lines through (the FLASH decision is still the user's).
import sys
sys.path.insert(0, "/home/user/global-manual-ai/.claude/skills/ai-prompt-engineer/scripts")
import assemble
assemble.MIN_FLASH = 0.7
sys.argv[0] = "assemble.py"
assemble.main()
