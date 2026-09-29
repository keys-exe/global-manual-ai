import json,os,urllib.request,time
K=os.environ["HEYGEN_API_KEY"]; v=json.load(open("th/v3/heygen.json"))["video_id"]; t0=time.time()
while time.time()-t0<3000:
    d=json.loads(urllib.request.urlopen(urllib.request.Request("https://api.heygen.com/v3/videos/"+v,headers={"X-Api-Key":K}),timeout=30).read())["data"]
    if d["status"]=="completed":
        urllib.request.urlretrieve(d["video_url"],"th/v3/TH_ALL_T1.mp4"); json.dump(d,open("th/v3/result.json","w"),indent=1); print("done",d.get("duration")); break
    if d["status"] in ("failed","error"): print("FAIL",d); json.dump(d,open("th/v3/result.json","w"),indent=1); break
    time.sleep(20)
