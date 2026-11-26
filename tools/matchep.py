import json,re,subprocess,html,difflib,sys,os
SC=json.load(open('/home/user/chiqui-channel/episodes/'+os.environ['EP']+'/scenes.json'))
out=sys.argv[1]
for code in sys.argv[2:]:
    t=html.unescape(subprocess.run(["curl","-sSL","-m","40",f"https://higgsfield.ai/s/{code}"],capture_output=True,text=True).stdout)
    m=re.search(r'line-clamp-2">([^<]+)<',t); p=m.group(1).strip() if m else ""
    r=sorted(((difflib.SequenceMatcher(None,p,s['img']).ratio(),s['id']) for s in SC),reverse=True)
    sid=r[0][1]; f=[x for x in os.listdir(out) if code in x][0]
    os.rename(f"{out}/{f}",f"{out}/{sid}_{code}.png")
    print(code,sid,round(r[0][0],3),r[1][1],round(r[1][0],3))
