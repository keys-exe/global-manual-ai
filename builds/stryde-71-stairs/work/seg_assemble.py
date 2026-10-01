"""Run assemble.py (segments padded to their full frame count), but render its one big ffmpeg graph segment by segment (memory) and join them losslessly."""
import sys, subprocess, re, os, runpy, tempfile
A="/home/user/global-manual-ai/.claude/skills/ai-prompt-engineer/scripts/assemble.py"
_run=subprocess.run
def run(cmd,*a,**k):
    if isinstance(cmd,list) and "-filter_complex" in cmd and "[s0]" in cmd[cmd.index("-filter_complex")+1]:
        FF=cmd[0]; g=cmd[cmd.index("-filter_complex")+1]
        ins=[cmd[i+1] for i,x in enumerate(cmd) if x=="-i"]
        out=cmd[-1]; audio_idx=int(re.search(r"'?(\d+):a",' '.join(cmd[cmd.index('-map'):])).group(1))
        chains=g.split(";")[:-1]
        td=tempfile.mkdtemp(dir=os.path.dirname(os.path.abspath(out)))
        lst=[]
        for ch in chains:
            m=re.match(r"\[(\d+):v\](.*)\[(s\d+)\]$",ch); i,body,name=m.groups()
            f=f"{td}/{name}.mp4"
            _run([FF,"-hide_banner","-loglevel","error","-y","-i",ins[int(i)],"-filter_complex",f"[0:v]{body}[v]","-map","[v]","-an","-c:v","libx264","-crf","18","-r","24",f],check=True)
            lst.append(f)
        open(f"{td}/list.txt","w").write("".join(f"file '{x}'\n" for x in lst))
        r=_run([FF,"-hide_banner","-loglevel","error","-y","-f","concat","-safe","0","-i",f"{td}/list.txt","-i",ins[audio_idx],"-map","0:v","-map","1:a","-c:v","copy","-c:a","aac","-b:a","192k","-shortest",out],check=True)
        for x in lst: os.remove(x)
        os.remove(f"{td}/list.txt"); os.rmdir(td)
        return r
    if isinstance(cmd,list) and "-frames:v" in cmd and "-filter_complex" in cmd and "_segs" in str(cmd[-1]):
        # a clip exactly as long as its slot can end a frame short: hold its last frame so every
        # segment has its full frame count (-frames:v still cuts it to the slot) — cut 7, 2026-10-01
        i=cmd.index("-filter_complex")+1; g=cmd[i]; j=g.rfind("[v]")
        cmd=cmd[:i]+[g[:j]+",tpad=stop_mode=clone:stop=24[v]"+g[j+3:]]+cmd[i+1:]
    return _run(cmd,*a,**k)
subprocess.run=run
sys.argv=[A]+sys.argv[1:]
runpy.run_path(A,run_name="__main__")
