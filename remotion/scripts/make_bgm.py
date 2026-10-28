import numpy as np, wave, sys
sr=44100; bpm=104; beat=60/bpm; total=float(sys.argv[2]) if len(sys.argv)>2 else 31.0
t_all=int(sr*total); out=np.zeros(t_all)
def note(f,start,dur,amp,decay):
    n=int(sr*dur); t=np.arange(n)/sr
    env=np.exp(-t*decay)*np.minimum(1,t/0.008)
    w=(np.sin(2*np.pi*f*t)+0.3*np.sin(2*np.pi*2*f*t)+0.1*np.sin(2*np.pi*3*f*t))*env*amp
    s=int(start*sr)
    if s>=t_all: return
    e=min(s+n,t_all); out[s:e]+=w[:e-s]
hz=lambda m:440*2**((m-69)/12)
prog=[[60,64,67],[55,59,62],[57,60,64],[53,57,60]]  # C G Am F
pattern=[0,1,2,1,0+12,2,1,2]
mel=[76,74,72,74,76,76,76,None, 74,74,74,None,76,79,79,None]
t=0; bar=0
while t<total:
    ch=prog[bar%4]
    note(hz(ch[0]-12),t,beat*4,0.18,0.9)
    for i,p in enumerate(pattern):
        m=ch[p%3]+(12 if p>=12 else 0)+12
        note(hz(m),t+i*beat/2,beat*1.2,0.07,4.0)
    t+=beat*4; bar+=1
# simple melody every other phrase
t=0; i=0
while t<total:
    m=mel[i%len(mel)]
    if m and (i//16)%2==0: note(hz(m),t,beat*0.9,0.06,3.0)
    t+=beat/2*2; i+=1
# fade out
fo=int(sr*2.5); out[-fo:]*=np.linspace(1,0,fo)
out/=np.max(np.abs(out))*1.1
pcm=(out*32767).astype(np.int16)
with wave.open(sys.argv[1],'w') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes(pcm.tobytes())
