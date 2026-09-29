import json,os,urllib.request,time,subprocess
K=os.environ["HEYGEN_API_KEY"]; v=json.load(open("th/v4/heygen.json"))["video_id"]; t0=time.time()
while time.time()-t0<3000:
    d=json.loads(urllib.request.urlopen(urllib.request.Request("https://api.heygen.com/v3/videos/"+v,headers={"X-Api-Key":K}),timeout=30).read())["data"]
    if d["status"]=="completed":
        json.dump(d,open("th/v4/result.json","w"),indent=1)
        for i in range(5):
            if subprocess.run(["curl","-sS","--retry","3","-C","-","-o","th/v4/TH_ALL.mp4",d["video_url"]]).returncode==0: break
        print("done",d.get("duration"),os.path.getsize("th/v4/TH_ALL.mp4")); break
    if d["status"] in ("failed","error"): print("FAIL",d); break
    time.sleep(20)
