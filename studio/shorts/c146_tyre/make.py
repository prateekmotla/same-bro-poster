"""BRAVE vs NORMAL — WHO'S RIGHT? #23: tyre bursts at speed on the highway (engine: studio/shorts/dilemma.py).
Facts: Michelin 'Tire blowout' advice: do not brake hard (hard braking can make the car spin or roll), hold the
steering wheel firmly with both hands, ease off the throttle gradually, let speed drop, steer to the shoulder once
stable, hazard lights; main causes: under-inflation, overload, pothole impact -> regular pressure checks.
South Australia Dept for Infrastructure & Transport 'Tyre blowout': keep a firm grip, steer straight, don't brake
suddenly, ease off the accelerator, brake gently to stop, pull off in a safe place. Team-BHP agrees (no slamming).
Brand-safe: no crash; Brave's car only skews with a red 'CAR PULLING' warning, then the red WRONG freeze."""
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import dilemma as DL  # noqa: E402
import kit as K  # noqa: E402
import body as B  # noqa: E402
from kit import T, S, RED, GRN, WHITE, YEL  # noqa: E402

D = "/home/claude/sid/shorts/c146_tyre"
CAPS = [
    "Fast on the highway and suddenly a TYRE BURSTS. Brave: slam the brakes. Normal: hold the steering, slow down gently. You?",
    "Brave stamps the brake all the way. The car starts pulling to one side.",
    "Normal grips the wheel with both hands, eases off the accelerator and keeps the car straight.",
    "WHO'S RIGHT? Comment B or N.",
    "NORMAL is right. Hard braking after a burst can SPIN the car, even roll it.",
    "Keep the wheel straight, let the speed drop on its own, then brake gently, hazard lights, stop on the side.",
    "And check tyre pressure regularly. Real brave = doing it right. What would YOU do?",
]
ROLES = dict(intro=[1], brave=[2], normal=[3], ask=[4], reveal=[5], why=[6], end=[7])
CFG = dict(series="BRAVE vs NORMAL #23", question=("TYRE BURST AT SPEED!", "WHAT DO YOU DO?"),
           brave="SLAM THE BRAKES", normal="HOLD STEERING, EASE OFF", answer='N', grade='warm',
           why_title="TYRE BURST? DO THIS",
           why_rows=[("Grip wheel, both hands", WHITE), ("NO hard braking", RED), ("Ease off accelerator", WHITE),
                     ("Keep it straight, slow down", GRN), ("Then brake gently", WHITE), ("Hazards on, stop on the side", YEL)],
           src="SRC: Michelin + SA Dept of Transport tyre advice", end=("BRAVE OR SMART?", "COMMENT  B  or  N"))

GROUND = 560


def highway(c, t, speed):
    g = __import__('cairo').LinearGradient(0, 0, 0, GROUND)
    g.add_color_stop_rgb(0, 0.5, 0.75, 0.95); g.add_color_stop_rgb(1, 0.88, 0.93, 0.97)
    c.rectangle(-400, 0, 1880, GROUND); c.set_source(g); c.fill()
    # hills + trees scroll at the car's speed
    off = speed
    for j in range(8):
        x = (j * 330 - off * 0.3) % 2400 - 500
        c.arc(x, GROUND - 120, 230, math.pi, 2 * math.pi); c.set_source_rgb(0.55, 0.72, 0.5); c.fill()
    for j in range(10):
        x = (j * 260 - off) % 2600 - 600
        c.rectangle(x - 10, GROUND - 170, 20, 120); c.set_source_rgb(0.42, 0.3, 0.2); c.fill()
        c.arc(x, GROUND - 190, 60, 0, 2 * math.pi); c.set_source_rgb(0.25, 0.52, 0.3); c.fill()
    c.rectangle(-400, GROUND - 50, 1880, 700); c.set_source_rgb(0.32, 0.32, 0.35); c.fill()      # road
    for j in range(12):
        x = (j * 300 - off * 2.2) % 3600 - 800
        c.rectangle(x, GROUND + 130, 160, 16); c.set_source_rgb(0.97, 0.97, 0.95); c.fill()
    c.rectangle(-400, GROUND + 300, 1880, 20); c.set_source_rgb(0.95, 0.8, 0.2); c.fill()
    c.rectangle(-400, GROUND + 320, 1880, 400); c.set_source_rgb(0.5, 0.45, 0.35); c.fill()


def car(c, t, who, x, y, rot=0.0, flat=True, hazard=False, mouth='flat', arms=((100, 20), (100, 20))):
    c.save(); c.translate(x, y); c.rotate(rot)
    # cabin + driver
    c.move_to(-200, -60); c.line_to(-140, -190); c.line_to(150, -190); c.line_to(230, -60); c.close_path()
    c.set_source_rgb(0.15, 0.4, 0.75); c.fill()
    c.save(); c.rectangle(-120, -175, 250, 110); c.clip()
    c.rectangle(-120, -175, 250, 110); c.set_source_rgb(0.75, 0.88, 0.98); c.fill()
    if who == 'B':
        K.sid(c, t, 20, -150, 0.24, mouth=mouth, look=(0.8, 0), arms=arms, eyes=1.15)
    else:
        B.figure(c, 20, -150, 0.24, t, who='friend', mouth=mouth, look=(0.8, 0), arms=arms)
    c.restore()
    c.move_to(5, -175); c.line_to(5, -65); c.set_source_rgb(0.12, 0.3, 0.6); c.set_line_width(10); c.stroke()
    S.rrect(c, -330, -70, 660, 150, 40); c.set_source_rgb(0.2, 0.48, 0.85); c.fill()
    S.rrect(c, 290, -40, 40, 30, 8); c.set_source_rgb(1, 0.95, 0.7); c.fill()          # headlight
    on = hazard and int(t * 3) % 2 == 0
    S.rrect(c, -330, -40, 30, 30, 8); c.set_source_rgb(*((1, 0.65, 0.1) if on else (0.75, 0.15, 0.1))); c.fill()
    if on:
        c.arc(-315, -25, 40, 0, 2 * math.pi); c.set_source_rgba(1, 0.65, 0.1, 0.35); c.fill()
    for wx, fl in ((-200, flat), (210, False)):          # rear wheel = the burst one
        if fl:
            c.save(); c.translate(wx, 95); c.scale(1.25, 0.72); c.arc(0, 0, 58, 0, 2 * math.pi); c.restore()
            c.set_source_rgb(0.08, 0.08, 0.1); c.fill()
            c.arc(wx, 92, 24, 0, 2 * math.pi); c.set_source_rgb(0.7, 0.7, 0.72); c.fill()
        else:
            c.arc(wx, 80, 58, 0, 2 * math.pi); c.set_source_rgb(0.08, 0.08, 0.1); c.fill()
            c.arc(wx, 80, 24, 0, 2 * math.pi); c.set_source_rgb(0.7, 0.7, 0.72); c.fill()
    c.restore()


def badge(c, txt, col, y=150):
    w = len(txt) * 20 + 60
    S.rrect(c, 540 - w / 2, y, w, 60, 24); c.set_source_rgba(*col, 0.92); c.fill()
    T(c, txt, 540, y + 42, 32, WHITE, stroke=None)


def gauge(c, kmh, x=740, y=340):
    c.arc(x, y, 95, math.pi, 2 * math.pi); c.set_source_rgba(0.05, 0.06, 0.1, 0.85); c.fill()
    a = math.pi + math.pi * min(1, kmh / 140)
    c.move_to(x, y); c.line_to(x + 80 * math.cos(a), y + 80 * math.sin(a))
    c.set_source_rgb(1, 0.3, 0.2); c.set_line_width(8); c.stroke()
    T(c, f"{int(kmh)} km/h", x, y + 45, 32, WHITE, stroke=None)


def scene(c, side, t, p):
    if side == 'B':
        stop = S.ease(min(1, p / 0.5))
        speed = 1000 * (t * (1 - 0.6 * stop)) if p > 0 else 1000 * t
        highway(c, t, speed)
        rot = -0.13 * S.ease(min(1, max(0, (p - 0.2) / 0.5)))
        car(c, t, 'B', 540, GROUND + 90, rot, mouth='o' if p > 0.3 else 'flat', arms=((100, -20), (100, 30)))
        if p > 0.25:   # skid marks
            for j in range(3):
                c.move_to(140 - j * 120, GROUND + 150 + j * 6); c.line_to(220 - j * 120, GROUND + 150 + j * 6)
                c.set_source_rgba(0.08, 0.08, 0.08, 0.7); c.set_line_width(10); c.stroke()
        gauge(c, 100 - 40 * stop)
        badge(c, "FULL BRAKE!", (0.75, 0.35, 0.1))
        if p > 0.4:
            badge(c, "CAR PULLING TO ONE SIDE!", RED, 230)
    else:
        sl = S.ease(min(1, p / 0.9))
        speed = 1000 * t - 500 * sl * t
        highway(c, t, speed)
        car(c, t, 'N', 540, GROUND + 90, 0.0, hazard=p > 0.7, mouth='flat', arms=((100, 10), (100, 10)))
        gauge(c, 100 - 55 * sl)
        msg = "GRIP THE WHEEL" if p < 0.33 else ("EASE OFF THE GAS" if p < 0.66 else "STRAIGHT + SLOW DOWN")
        badge(c, msg, (0.05, 0.4, 0.15))
    if p < 0.12 and side in ('B', 'N'):
        pass
    # 'BANG' burst marker at the start of each side's action / intro
    if p == 0:
        S.rrect(c, 160, GROUND - 10, 210, 70, 30); c.set_source_rgba(1, 0.85, 0.2, 0.95); c.fill()
        T(c, "BANG!", 265, GROUND + 40, 44, (0.6, 0.1, 0.05), stroke=None)


def build():
    return DL.Dilemma(D, CAPS, ROLES, scene, CFG, mood='tense')


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        sh.preview(sh.preview_times(), f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in sh.L])
    else:
        sh.render(f"{D}/short.mp4")
