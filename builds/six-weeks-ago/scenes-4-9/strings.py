import re
SRC="/home/user/global-manual-ai/standards/AI_Prompt_Engineer_Global_Standards.md"
txt=open(SRC).read()
S={}
for m in re.finditer(r"^\*\*`([A-Z0-9][A-Z0-9\-]+)`\*\*[^\n]*\n+```\n(.*?)\n```", txt, re.M|re.S):
    S.setdefault(m.group(1), m.group(2).strip())
if __name__=="__main__":
    print(len(S))
    for k in ["ING-MANIFEST","MULTI-FILM","SCENE-MASTER","SCENE-KEY","DRAMA-DELIVERY","LISTEN-LINE","HERO-FILM","MECH-SCREEN","ANAT-BASE","ANAT-LIGHT","ANAT-FIELD","ANAT-A","ANAT-B","ANAT-LOAD","ANAT-HOT","ANAT-PHYS-C","NEG-ANAT-PHYS","ANAT-PROD","ANAT-NEG","ANAT-MOD3","SURF-PATTERN","SURF-SWEEP","NEG-TEX","NEG-SUPPORT","NEG-CONT","SIGHT-LINE","VIEW-OUT","SCENE-BRIDGE","HOLD-PC","NEG-ORIENT","AUD-FILM","PLATE-PROP"]:
        print(k, len(S.get(k,'')) or 'MISSING')
