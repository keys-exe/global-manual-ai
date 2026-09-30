import json,os,urllib.request,time,subprocess,sys
K=os.environ["HEYGEN_API_KEY"]; v=sys.argv[1]; out=sys.argv[2]; t0=time.time()
while time.time()-t0<3500:
    d=json.loads(urllib.request.urlopen(urllib.request.Request("https://api.heygen.com/v3/videos/"+v,headers={"X-Api-Key":K}),timeout=30).read())["data"]
    if d["status"]=="completed":
        json.dump(d,open(out+".result.json","w"),indent=1)
        for i in range(5):
            if subprocess.run(["curl","-sS","--retry","3","-C","-","-o",out,d["video_url"]]).returncode==0: break
        print("done",d.get("duration"),os.path.getsize(out)); break
    if d["status"] in ("failed","error"): print("FAIL",d); break
    time.sleep(20)
