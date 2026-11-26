# 신호등 빨간 등 끄기 (35화 S15~S17, 2026-11-26): python3 -I tools/lampoff.py 원본.mp4 결과.mp4 — 빨갛게 켜진 둥근 등을 찾아 꺼진 갈색으로 바꾼다. scipy 필요.
import sys,subprocess,json,numpy as np
from scipy import ndimage
src,dst=sys.argv[1],sys.argv[2]
p=json.loads(subprocess.run(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=width,height,r_frame_rate','-of','json',src],capture_output=True,text=True).stdout)['streams'][0]
W,H,fr=p['width'],p['height'],p['r_frame_rate']
dec=subprocess.Popen(['ffmpeg','-v','error','-i',src,'-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
enc=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',fr,'-i','-','-c:v','libx264','-crf','14','-preset','medium','-pix_fmt','yuv420p',dst],stdin=subprocess.PIPE)
minA=4000*(W*H)/(2752*1536); n=0; hit=0
while True:
    buf=dec.stdout.read(W*H*3)
    if len(buf)<W*H*3: break
    a=np.frombuffer(buf,np.uint8).reshape(H,W,3).astype(np.float32); r,g,b=a[...,0],a[...,1],a[...,2]
    red=(r>150)&(g<120)&(b<120)&(r-g>70)
    lab,_=ndimage.label(red); keep=np.zeros(red.shape,bool)
    for i,sl in enumerate(ndimage.find_objects(lab),1):
        h=sl[0].stop-sl[0].start; w=sl[1].stop-sl[1].start; area=(lab[sl]==i).sum()
        if area>minA*0.5 and 0.7<h/w<1.4 and area/(h*w)>0.6:
            keep[sl]|=ndimage.binary_dilation(ndimage.binary_fill_holes(lab[sl]==i),iterations=8); hit+=1
    m=keep&(r>g+25)
    a[m,0]=r[m]*0.55+15; a[m,1]=g[m]*0.8+18; a[m,2]=b[m]*0.8+10
    enc.stdin.write(np.clip(a,0,255).astype(np.uint8).tobytes()); n+=1
enc.stdin.close(); enc.wait(); print(src.split('/')[-1],'frames',n,'lamps',hit)
