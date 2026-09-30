import json,os,urllib.request,time
V="fjMYIJcXAxAnyO48q9x3"; K=os.environ["ELEVENLABS_API_KEY"]
text=open("ALL.enhanced.fitted.txt").read().strip()
sub=json.loads(urllib.request.urlopen(urllib.request.Request("https://api.elevenlabs.io/v1/user/subscription",headers={"xi-api-key":K})).read())
print("credits left",sub["character_limit"]-sub["character_count"],"· text",len(text),flush=True)
log={}
for t in range(1,5):
    body=json.dumps({"text":text,"model_id":"eleven_v4","voice_settings":{"stability":0.5}}).encode()
    r=urllib.request.Request(f"https://api.elevenlabs.io/v1/text-to-speech/{V}?output_format=mp3_44100_192",data=body,headers={"xi-api-key":K,"Content-Type":"application/json"})
    t0=time.time()
    with urllib.request.urlopen(r,timeout=900) as resp:
        open(f"full/T{t}.mp3","wb").write(resp.read()); log[f"T{t}"]={"request_id":resp.headers.get("request-id"),"s":round(time.time()-t0,1)}
    print("T",t,log[f"T{t}"],flush=True)
json.dump(log,open("full/tts_log.json","w"),indent=1)
