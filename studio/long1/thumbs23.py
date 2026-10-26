import sys
sys.path.insert(0,'/home/claude/sid/long1'); sys.path.insert(0,'/home/claude/sid/v3'); sys.path.insert(0,'/home/claude/sid/v2')
import thumbs2 as T2, thumbsL as TL, env as V, chars as CH, props as P, sid2 as S
from thumbs import words, tag, YEL, RED, GRN
WH=(1,1,1); W,H=1280,720
def sid_face(c, mouth, extra, x=960, y=330, s=1.35, phone=True):
    CH.sid_body(c,x,y,s,0.2,arms=((14,-10),(30,150)) if phone else ((14,-10),(14,-10)),phone_hand=1 if phone else None,glow=1.0 if phone else 0)
    CH.sid_head(c,x,y,s,0.2,tilt=-4,mouth=mouth,**extra)
    if phone: T2.phone_glow_face(c,x,y,s)
def mk(path, scene, lines, face):
    base=TL.base_scene(scene); s,c=T2.surf(W,H); c.set_source_rgba(0,0,0,0.3); c.paint(); face(c)
    base.alpha_composite(T2.to_pil(s)); s,c=T2.surf(W,H)
    for (parts,y,size) in lines: words(c,parts,46,y,size)
    tag(c,50,630); base.alpha_composite(T2.to_pil(s)); T2.finish(base,path)
night=lambda c:V.room(c,1,'night'); day=lambda c:V.room(c,1,'day')
def clock(c,txt,col):
    S.rrect(c,770,40,300,110,18); c.set_source_rgb(0.03,0.03,0.04); c.fill()
    P.text(c,txt,920,120,76,fill=col,stroke=None)
mk('/home/claude/sid/long2/thumb_A.jpg',night,[([("WHY YOU",WH)],190,110),([("CAN'T STOP",YEL)],330,110),([("SCROLLING",RED)],470,110)],
   lambda c:(sid_face(c,'o',dict(eyes=0.8,bags=1,look=(0.6,0.5))),clock(c,"3:10 AM",RED)))
mk('/home/claude/sid/long2/thumb_B.jpg',night,[([("2 AM",RED),("REELS?",WH)],200,110),([("NOT YOUR",WH)],340,110),([("FAULT",YEL)],490,140)],
   lambda c:sid_face(c,'flat',dict(eyes=0.6,bags=1,look=(0.6,0.5))))
mk('/home/claude/sid/long3/thumb_A.jpg',day,[([("SALARY",GRN)],190,120),([("GONE BY",WH)],330,110),([("20TH?",RED)],490,150)],
   lambda c:sid_face(c,'frown',dict(sad=1,sweat=1,eyes=1.0,look=(0.6,0.5))))
mk('/home/claude/sid/long3/thumb_B.jpg',day,[([("WHERE YOUR",WH)],200,100),([("SALARY",GRN)],330,120),([("REALLY GOES",YEL)],470,100)],
   lambda c:sid_face(c,'o',dict(eyes=1.2,look=(0.6,0.5),**{'raise':0.9})))
print('ok')
