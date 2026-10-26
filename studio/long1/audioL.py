import sys, wave
import numpy as np
sys.path.insert(0,'/home/claude/sid/v3'); sys.path.insert(0,'/home/claude/sid/long1')
import importlib.util
spec=importlib.util.spec_from_file_location('a3','/home/claude/sid/v3/audio3.py')
# reuse synth helpers without running audio3's main body: copy minimal helpers
from scipy.signal import lfilter
SR=44100; DUR=235.0; N=int(SR*DUR); rng=np.random.default_rng(3); t=np.arange(N)/SR
def lp(x,k): return lfilter([k],[1,-(1-k)],x)
def env(n,a=0.01,d=0.3):
    tt=np.arange(n)/SR; return np.minimum(1,tt/max(a,1e-4))*np.exp(-tt/d)
def add(buf,sig,at,g=1.0):
    i=int(at*SR); j=min(len(buf),i+len(sig))
    if 0<=i<len(buf): buf[i:j]+=sig[:j-i]*g
def tone(f,dur,a=0.005,d=0.4):
    n=int(dur*SR); tt=np.arange(n)/SR; return np.sin(2*np.pi*f*tt)*env(n,a,d)
def noise(dur): return rng.standard_normal(int(dur*SR))
import render_long as R
cuts=[sh[0] for sh in R.SHOTS[1:]]
bed=np.zeros(N)
for f,g in ((49.0,.5),(73.4,.3),(98.0,.15)):
    bed+=np.sin(2*np.pi*f*t+np.sin(2*np.pi*0.05*t)*1.5)*g
bed*=0.06
pulse=np.zeros(N); step=60/96/2
for i in range(int(DUR/step)):
    at=i*step
    f=[98.0,87.3,110.0,82.4][(i//16)%4]
    if 94<at<137: f*=1.5
    add(pulse,lp(tone(f,.3,.003,.09)+.3*tone(f*2,.3,.003,.05),.3),at,.1)
inten=np.interp(t,[0,13,22,40,49,53.7,57,79,91,109,148,153,161,185,207,212,225,231,235],
                  [.4,.6,.7,.8,1,.2,.7,.8,.9,1,.9,.6,.8,.7,.5,.3,.3,.4,0])
bed=bed+pulse*inten
# warm pad for ending
for f in (220,277.2,329.6,440):
    add(bed,lp(tone(f,28,3,30),.2),207.8,.05)
sfx=np.zeros(N)
def whoosh(dur=.32):
    n=int(dur*SR); w=lp(noise(dur),.15)
    return w*np.sin(np.linspace(0,np.pi,n))**2
for c in cuts: add(sfx,whoosh(),c-.16,.3)
def impact(): return lp(tone(55,.6,.002,.25)+.4*noise(.6)*env(int(.6*SR),.001,.05),.15)
for at in (17.3,21.1,45.0,50.2,61.2,73.6,88.1,102.6,106.2,115.0,151.5,168.3,174.0,181.4,224.6):
    add(sfx,impact(),at,.7)
def coin(f=2400): return tone(f,.25,.001,.06)+.6*tone(f*1.52,.25,.001,.04)
for a0,a1 in ((13.5,17.0),(104.4,109.0),(113.2,116.3),(127.5,129.5)):
    n=int((a1-a0)/.22)
    for i in range(n): add(sfx,coin(2200+rng.uniform(-300,500)),a0+i*.22+rng.uniform(0,.06),.1)
def stamp(): return lp(noise(.25)*env(int(.25*SR),.001,.04),.3)+tone(80,.25,.001,.08)
for at in (33.8,45.0,54.6,117.7,142.6,229.0): add(sfx,stamp(),at,.8)
def heart(): return lp(tone(48,.25,.004,.07),.08)*3
for i in range(9):
    add(sfx,heart(),49.0+i*.5,.8); add(sfx,heart(),49.0+i*.5+.15,.55)
for i in range(60):
    add(sfx,noise(.012)*.5,64.3+i*.022,.12); add(sfx,noise(.012)*.5,94.6+i*.05,.1)
add(sfx,tone(880,.6,.002,.2)+tone(1320,.6,.002,.15),24.1,.22)
add(sfx,tone(880,.6,.002,.2)+tone(1320,.6,.002,.15),36.3,.2)
nn=int(.4*SR)
for at in (40.6,42.4,46.3):
    add(sfx,np.sign(np.sin(2*np.pi*110*np.arange(nn)/SR))*env(nn,.005,.15)*.4,at,.22)
def save(name,x):
    x=np.clip(x,-1,1)
    with wave.open(name,'w') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((x*32767).astype(np.int16).tobytes())
save('bedL.wav',bed/np.abs(bed).max()*.8); save('sfxL.wav',sfx/np.abs(sfx).max()*.9); print('ok')
