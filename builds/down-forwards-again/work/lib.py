"""Prompt builder for down-forwards-again. Strings are imported, never retyped."""
import re, sys, json, os
ROOT = os.path.dirname(os.path.abspath(__file__))
MASTER = os.path.join(ROOT, '../../../standards/AI_Prompt_Engineer_Global_Standards.md')
sys.path.insert(0, ROOT)
import stryde_sheet as P  # noqa

_txt = open(MASTER).read()
def S(i):
    m = re.search(r"^\*\*`%s`\*\* —[^\n]*\n+```\n(.*?)\n```" % re.escape(i), _txt, re.S | re.M)
    if not m: raise KeyError(i)
    return m.group(1).strip()
