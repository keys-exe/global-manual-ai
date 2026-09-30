import re,json,pathlib
T=pathlib.Path('/home/user/global-manual-ai/standards/AI_Prompt_Engineer_Global_Standards.md').read_text()
def S(i):
    m=re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```"%re.escape(i),T,re.S); return m.group(1).strip()
j={"shot":"hk3_01",
 "subject":"A consultant's hand, a white woman of about fifty in a navy dress, her forefinger on a lit knee X-ray clipped to the wall light box; her navy shoulder soft in the near foreground; her face not seen.",
 "camera":{"movement":S("RIG-R1"),"framing":"As in the start frame."},
 "motion":"One slow action at a steady explaining pace: her fingertip traces slowly along the narrowed gap between the two bones on the X-ray, from one side of the joint to the other, and stops. The film stays flat and still on the light box. "+S("HOLD-C")+" "+S("PHYS-MOTION-C"),
 "lighting":S("INHERIT-CAP"),
 "style":"As in the start frame.",
 "negatives":", ".join([S("NEG-WARP-C"),"no text appearing on the X-ray, no letters, no numbers, no labels, no arrows, no film moving or bending, no bones changing shape on the film, no second hand, no face turning to camera, no camera travelling with the hand, no zoom, no music, no speech"])}
s=json.dumps(j,ensure_ascii=False,separators=(",",":")); pathlib.Path('HK3-01.kling.json').write_text(s); print(len(s))
url="https://tempfile.aiquickdraw.com/a2/2cf20028675f45eebf56970988cb8855_1790695595846.png"
c={"beat":"HK3-01","connector":"kling","mode":1,"kind":"broll","prompt":s,"duration":6,"resolution":"1080p","aspect_ratio":"9:16","start_image":url,"start_approved":True,
 "pinned":False,"end_image":None,"end_approved":False,"subject_motion":"in_place","prefer_multi_shots":"false","generation":1,"rack":None,
 "risks":[{"risk":"the finger or hand warping as it moves","prevented_by":"one slow trace at a named pace, HOLD-C + PHYS-MOTION-C + NEG-WARP-C"},
          {"risk":"text or numbers appearing on the X-ray","prevented_by":"negatives name text, letters, numbers, labels, arrows"},
          {"risk":"the X-ray bones changing shape (the gap closing or opening)","prevented_by":"motion keeps the film flat and still; 'no bones changing shape on the film'"}],
 "route":"Kie AI kling-3.0 (§5 fallback: Kling connector at 3 credits)"}
json.dump(c,open('HK3-01.call.json','w'),indent=1,ensure_ascii=False)
