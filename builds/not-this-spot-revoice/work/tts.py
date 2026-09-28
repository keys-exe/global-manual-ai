import json,os,sys,urllib.request
def tts(text,out,speed=1.0,model="eleven_v4",voice="T8ewLtYUVAFApwsMjq9U",stab=None,prev=None,nxt=None):
    vs={"speed":speed}
    if stab is not None: vs["stability"]=stab
    body={"text":text,"model_id":model,"voice_settings":vs}
    if prev: body["previous_text"]=prev
    if nxt: body["next_text"]=nxt
    req=urllib.request.Request(f"https://api.elevenlabs.io/v1/text-to-speech/{voice}?output_format=mp3_44100_192",method="POST",data=json.dumps(body).encode(),headers={"xi-api-key":os.environ["ELEVENLABS_API_KEY"],"Content-Type":"application/json"})
    try:
        with urllib.request.urlopen(req,timeout=600) as r: open(out,"wb").write(r.read())
    except urllib.error.HTTPError as e: sys.exit(e.read().decode())
if __name__=="__main__":
    tts(open(sys.argv[1]).read(),sys.argv[2],float(sys.argv[3]),sys.argv[4] if len(sys.argv)>4 else "eleven_v4")
