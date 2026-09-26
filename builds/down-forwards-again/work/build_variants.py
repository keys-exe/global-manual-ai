import json
d=json.load(open('../act_map.json'))
INP={"BR27":1.2}
def br(r): return {"beat":r['beat_id'],"clip":f"renders/{r['beat_id']}.mp4","phrase":r['phrase'],"in":INP.get(r['beat_id'],0.0),"layout":r['layout']}
body={"audio":"voice/Forwards_master.wav","script":"work/body.lines.txt","base":"th/TH-BODY.mp4",
      "broll":[br(r) for r in d if r['part']=='body'],"punch_in":[],"th_focus_y":0.33,"th_face":[0.33,0.24,0.69,0.47]}
hooks=[{"id":h,"audio":f"voice/Forwards_{h}_master.wav","script":f"work/{h}.lines.txt","base":f"th/TH-{h}.mp4",
        "broll":[br(r) for r in d if r['part']==h]} for h in ("HK1","HK2","HK3")]
json.dump({"body":body,"hooks":hooks},open('../variants.json','w'),indent=1)
json.dump(dict(audio=body['audio'],script=body['script'],base=body['base'],broll=body['broll'],punch_in=[],th_focus_y=0.33,th_face=[0.33,0.24,0.69,0.47]),open('../plan.json','w'),indent=1)
print(len(body['broll']),[len(h['broll']) for h in hooks])
