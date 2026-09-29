import json,sys,time
now=int(time.time()*1000)
A=json.loads(sys.argv[1])   # {"TH-01": ["asset", "url", duration], ...}
W=[]
for k,(a,url,dur) in A.items():
    d=json.load(open(f'work/board/{k}.json'))
    d.update({"status":"review","videoAsset":a,"videoType":"video/mp4","videoUrl":url,"videoAt":now,"videoRes":"1080×1920","duration":round(dur,2),"updatedAt":now,
      "videoVersions":[{"v":1,"asset":a,"type":"video/mp4","url":url,"model":"HeyGen Avatar IV, expressiveness high, motionPrompt","connector":"HeyGen","size":f"{dur:.2f}s","at":now,"note":"first render"}]})
    json.dump(d,open(f'work/board/{k}.json','w'),ensure_ascii=False)
    W.append({"op":"set","collection":"generations","doc_id":f"stryde-thirty-years__{k}","if_version":1,"file_path":f"/home/user/global-manual-ai/builds/stryde-thirty-years/work/board/{k}.json"})
print(json.dumps(W))
