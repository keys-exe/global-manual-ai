import re,json,pathlib
T=pathlib.Path('/home/user/global-manual-ai/standards/AI_Prompt_Engineer_Global_Standards.md').read_text()
def S(i):
    m=re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```"%re.escape(i),T,re.S); return m.group(1).strip()
j={"shot":"hk2_01",
 "subject":"Folake, a Black British woman of sixty-six with long grey-and-black box braids tied back, in a burnt-orange cardigan over a black top, sitting in her burgundy armchair by the window with a mug of tea in her left hand. No strap on her knee.",
 "camera":{"movement":S("RIG-R1"),"framing":"As in the start frame."},
 "motion":"One slow action at a tired pace: her right hand rubs her right knee once, a slow press-and-circle, then comes to rest on it, and she lets out a small breath and looks out of the window. The mug stays still on the chair arm. "+S("HOLD-C")+" "+S("PHYS-MOTION-C"),
 "lighting":S("INHERIT-CAP"),
 "style":"As in the start frame.",
 "negatives":", ".join([S("NEG-WARP-C"),"no knee strap, no brace, no support appearing on her leg, no tea spilling, no mug moving to her mouth, no standing up, no smile, no looking at the camera, no camera travelling with the subject, no zoom, no second person, no music, no speech"])}
s=json.dumps(j,ensure_ascii=False,separators=(",",":")); pathlib.Path('HK2-01.kling.json').write_text(s); print(len(s))
url="https://tempfile.aiquickdraw.com/a2/757179987f1271c3c0a215f818f2cbe0_1790694992529.png"
c={"beat":"HK2-01","connector":"kling","mode":1,"kind":"broll","prompt":s,"duration":5,"resolution":"1080p","aspect_ratio":"9:16","start_image":url,"start_approved":True,
 "pinned":False,"end_image":None,"end_approved":False,"subject_motion":"in_place","prefer_multi_shots":"false","generation":1,"rack":None,
 "risks":[{"risk":"her hand or fingers warping during the rub","prevented_by":"one slow action at a named pace, HOLD-C + PHYS-MOTION-C + NEG-WARP-C"},
          {"risk":"the mug spilling or moving to her mouth (a second action)","prevented_by":"motion says the mug stays still; negatives name spilling and drinking"},
          {"risk":"a strap appearing on her knee before its time","prevented_by":"subject and negatives say no strap, no brace"}],
 "route":"Kie AI kling-3.0 (§5 fallback: Kling connector at 3 credits)"}
json.dump(c,open('HK2-01.call.json','w'),indent=1,ensure_ascii=False)
