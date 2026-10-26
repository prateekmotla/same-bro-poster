import sys, cairo
sys.path.insert(0,'/home/claude/sid/long1'); sys.path.insert(0,'/home/claude/sid/v3'); sys.path.insert(0,'/home/claude/sid/v2')
from PIL import ImageFilter
import thumbs2 as T2, env as V, body as B, props as P
from thumbs import words, tag, YEL, RED, GRN
W,H=1280,720; WH=(1,1,1)
def base_scene(fn):
    s,c=T2.surf(W,H); c.scale(W/1920,H/1080); fn(c); return T2.to_pil(s).filter(ImageFilter.GaussianBlur(7))
def A(path):
    base=base_scene(lambda c:V.studio(c,1))
    s,c=T2.surf(W,H)
    c.set_source_rgba(0,0,0,0.35); c.paint()
    B.figure(c,940,250,0.62,0.3,who='bhai',pose='stand',mouth='smirk',arms=((70,120),(70,120)))
    for x,y,r in ((760,560,30),(1180,520,26),(820,660,24),(1220,660,28),(700,420,20)): P.coin(c,x,y,r)
    base.alpha_composite(T2.to_pil(s))
    s,c=T2.surf(W,H)
    words(c,[("LIVE TRADERS'",WH)],46,190,92)
    words(c,[("SECRET",YEL)],46,330,140)
    words(c,[("INCOME",GRN)],46,470,140)
    tag(c,50,620); base.alpha_composite(T2.to_pil(s)); T2.finish(base,path)
def Bv(path):
    base=base_scene(lambda c:V.room(c,1,'night'))
    s,c=T2.surf(W,H)
    c.set_source_rgba(0,0,0,0.3); c.paint()
    import chars as CH
    CH.sid_body(c,960,330,1.35,0.2,arms=((14,-10),(30,150)),phone_hand=1,glow=1.0)
    CH.sid_head(c,960,330,1.35,0.2,tilt=-4,mouth='o',eyes=1.2,sweat=1.0,look=(0.6,0.5),**{'raise':0.9})
    T2.phone_glow_face(c,960,330,1.35)
    base.alpha_composite(T2.to_pil(s))
    s,c=T2.surf(W,H)
    words(c,[("LIVE TRADERS",YEL)],46,180,96)
    words(c,[("EARN FROM",WH)],46,310,110)
    words(c,[("YOU",RED)],46,490,180)
    words(c,[("not from trading",(0.85,0.87,0.95))],52,575,46,lw=7)
    tag(c,50,630); base.alpha_composite(T2.to_pil(s)); T2.finish(base,path)
A('thumbL_A.jpg'); Bv('thumbL_B.jpg'); print('ok')
