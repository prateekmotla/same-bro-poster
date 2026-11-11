"""BRAVE vs NORMAL — WHO'S RIGHT? #15: phone fell on the metro track (engine: studio/shorts/dilemma.py).
Facts: Lucknow Metro do's & don'ts: "Do not step onto metro track or try to pick the belongings that drop on the track
(contact metro staff for assistance)" - risk of a running train or high-voltage lines. Kochi Metro: third rail is
energised with 750 V DC. Bengaluru (Deccan Herald): a woman jumped down for her phone at Indiranagar - guard tripped the
third-rail power, Purple Line services hit ~15 min; BMRCL usually fines trespassers (min Rs 200). DMRC: entering
restricted areas can lead to prosecution. Voice line timing: silence-gap DP (bounds.json). No injury shown: Brave freezes
at the edge with train lights coming, then the red WRONG freeze."""
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import dilemma as DL  # noqa: E402
import kit as K  # noqa: E402
import body as B  # noqa: E402
from kit import T, S, RED, GRN, WHITE, YEL  # noqa: E402

D = "/home/claude/sid/shorts/c114_metrophone"
CAPS = [
    "Your phone slipped and fell on the METRO TRACK. Brave: 2 seconds, I'll jump and grab it. Normal: wait, call the staff. Whose side are you on?",
    "Brave walks to the platform edge and is about to jump down.",
    "Normal tells the guard right there exactly where the phone fell.",
    "WHO'S RIGHT? Comment B or N.",
    "NORMAL is right. Metros say: never step onto the track, let the staff pick it up. Many lines have a 750 V third rail, and a train can come any second.",
    "Staff will get it out safely. Jump down and you can be fined, and the whole line stops.",
    "You can get a phone back. Not you. What would YOU do?",
]
ROLES = dict(intro=[1], brave=[2], normal=[3], ask=[4], reveal=[5], why=[6], end=[7])
CFG = dict(series="BRAVE vs NORMAL #15", question=("PHONE FELL ON THE TRACK!", "WHAT DO YOU DO?"),
           brave="JUMP DOWN, GRAB IT", normal="TELL METRO STAFF", answer='N', grade='studio',
           why_title="DROPPED SOMETHING?",
           why_rows=[("NEVER step onto the track", RED), ("Third rail can carry 750 V", WHITE),
                     ("A train can come any second", WHITE), ("Tell staff WHERE it fell", WHITE),
                     ("They pick it up safely", GRN)],
           src="SRC: Lucknow & Kochi Metro rules, BMRCL", end=("BRAVE OR SMART?", "COMMENT  B  or  N"))

PLAT = 800     # platform surface
EDGE = 600     # platform edge x
PIT = 955      # track bed


def station(c, t, lights=0.0):
    # back wall
    c.rectangle(-400, 0, 1880, PLAT); c.set_source_rgb(0.84, 0.86, 0.88); c.fill()
    c.rectangle(-400, 300, 1880, 26); c.set_source_rgb(0.2, 0.45, 0.75); c.fill()   # blue line stripe
    for j in range(-3, 13):  # wall tiles
        c.move_to(j * 120, 0); c.rel_line_to(0, PLAT)
    c.set_source_rgba(0.7, 0.72, 0.75, 0.6); c.set_line_width(2); c.stroke()
    # station sign
    # platform slab
    c.rectangle(-400, PLAT, EDGE + 400, 1000 - PLAT); c.set_source_rgb(0.55, 0.55, 0.58); c.fill()
    c.rectangle(EDGE - 70, PLAT, 50, 12); c.set_source_rgb(1, 0.82, 0.1); c.fill()
    c.rectangle(-400, PLAT, EDGE - 70 + 400, 12); c.set_source_rgb(0.62, 0.62, 0.65); c.fill()
    c.rectangle(EDGE - 70, PLAT, 52, 240); c.set_source_rgba(1, 0.82, 0.1, 0.35); c.fill()
    # track pit
    c.rectangle(EDGE, PLAT, 1480 - EDGE, 1000 - PLAT); c.set_source_rgb(0.2, 0.19, 0.2); c.fill()
    c.rectangle(EDGE, PIT, 1480 - EDGE, 70); c.set_source_rgb(0.33, 0.3, 0.28); c.fill()
    for j in range(12):   # sleepers
        c.rectangle(EDGE + 10 + j * 70, PIT - 6, 40, 14); c.set_source_rgb(0.42, 0.38, 0.33); c.fill()
    c.rectangle(EDGE, PIT - 18, 900, 10); c.set_source_rgb(0.7, 0.7, 0.72); c.fill()     # running rail
    c.rectangle(EDGE + 150, PLAT + 70, 900, 16); c.set_source_rgb(0.85, 0.55, 0.15); c.fill()   # third rail
    S.rrect(c, EDGE + 160, PLAT + 92, 110, 40, 8); c.set_source_rgb(1, 0.85, 0.1); c.fill()
    T(c, "750 V", EDGE + 215, PLAT + 122, 26, (0.1, 0.1, 0.1), stroke=None)
    if lights > 0:   # train headlights from the tunnel (right), no train shown hitting anyone
        for dy in (0, 60):
            for r, a in ((140, 0.18), (70, 0.4), (26, 0.95)):
                c.arc(900, PLAT - 60 + dy, r * lights, 0, 2 * math.pi); c.set_source_rgba(1, 0.97, 0.75, a * lights); c.fill()


def phone(c, x, y):
    c.save(); c.translate(x, y); c.rotate(0.3)
    S.rrect(c, -24, -42, 48, 84, 8); c.set_source_rgb(0.1, 0.1, 0.12); c.fill()
    S.rrect(c, -19, -35, 38, 66, 5); c.set_source_rgb(0.3, 0.6, 0.95); c.fill()
    c.restore()


def bubble(c, x, y, txt, col=(1, 1, 1)):
    w = len(txt) * 23 + 60
    S.rrect(c, x - w / 2, y, w, 74, 30); c.set_source_rgba(*col, 0.95); c.fill()
    T(c, txt, x, y + 50, 34, (0.1, 0.1, 0.15), stroke=None)


def scene(c, side, t, p):
    if side == 'B':
        lights = S.ease(max(0, min(1, (p - 0.45) / 0.4)))
        station(c, t, lights)
        phone(c, 740, PIT - 45)
        q = S.ease(min(1, p / 0.5))
        x = 300 + 200 * q
        K.sid(c, t, x, PLAT - 445, 0.42, mouth='o' if p > 0.55 else 'smirk', look=(0.8, 0.5),
              arms=((14, -10), (90, 40)), eyes=1.2 if p > 0.55 else 1.0)
        if p > 0.55:
            S.rrect(c, 270, 640, 330, 56, 20); c.set_source_rgba(*RED, 0.92); c.fill()
            T(c, "TRAIN COMING!", 435, 678, 30, WHITE, stroke=None)
            bubble(c, 540, 205, "WAIT... LIGHTS?!", (1, 0.82, 0.8))
        else:
            bubble(c, 540, 205, "2 SECONDS, I'LL JUMP", (1, 0.85, 0.8))
    else:
        station(c, t)
        phone(c, 740, PIT - 45)
        B.figure(c, 245, PLAT - 445, 0.42, t, who='friend', mouth='flat', arms=((14, -10), (120, -30)), look=(0.6, 0))
        # metro staff (guard) with vest + badge
        B.figure(c, 445, PLAT - 445, 0.42, t, who='bhai', mouth='flat', look=(-0.5, 0.1),
                 arms=((14, -10), (14, -10)) if p < 0.45 else ((14, -10), (110, 10)))
        S.rrect(c, 395, PLAT - 300, 100, 40, 10); c.set_source_rgb(1, 0.55, 0.1); c.fill()
        T(c, "STAFF", 445, PLAT - 270, 24, WHITE, stroke=None)
        if p > 0.45:   # long grabber from the platform, staff stays up
            c.move_to(535, PLAT - 220); c.line_to(730, PIT - 65)
            c.set_source_rgb(0.25, 0.25, 0.28); c.set_line_width(10); c.stroke()
            S.rrect(c, 330, 690, 300, 50, 18); c.set_source_rgba(0.05, 0.4, 0.15, 0.9); c.fill()
            T(c, "STAFF ON IT", 480, 724, 26, WHITE, stroke=None)
        msg = "BHAIYA, PHONE ON TRACK" if p < 0.25 else ("THERE, NEAR PILLAR 3" if p < 0.45 else "STAFF GETS IT SAFELY")
        bubble(c, 540, 205, msg)


def build():
    return DL.Dilemma(D, CAPS, ROLES, scene, CFG, mood='tense')


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        sh.preview(sh.preview_times(), f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in sh.L])
    else:
        sh.render(f"{D}/short.mp4")
