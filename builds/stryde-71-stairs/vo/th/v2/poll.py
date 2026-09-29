import json,os,urllib.request,time
K=os.environ["HEYGEN_API_KEY"]
ids=json.load(open("th/v2/heygen.json"))["videos"]; res={}
t0=time.time()
while len(res)<len(ids) and time.time()-t0<1500:
    for k,v in ids.items():
        if k in res: continue
        try: d=json.loads(urllib.request.urlopen(urllib.request.Request("https://api.heygen.com/v3/videos/"+v,headers={"X-Api-Key":K}),timeout=30).read())["data"]
        except Exception as e: print(k,e); continue
        if d["status"]=="completed":
            urllib.request.urlretrieve(d["video_url"],f"th/v2/{k}.mp4"); res[k]={"id":v,"duration":d.get("duration"),"url":d["video_url"]}; print(k,"done",flush=True)
        elif d["status"] in ("failed","error"): res[k]={"id":v,"error":d.get("failure_message") or d.get("error")}; print(k,"FAIL",res[k],flush=True)
    time.sleep(15)
json.dump(res,open("th/v2/results.json","w"),indent=1)
print(len(res),"/",len(ids))
