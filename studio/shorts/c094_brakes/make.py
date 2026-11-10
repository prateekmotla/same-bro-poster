"""BRAVE vs NORMAL — WHO'S RIGHT? #10: brakes fail on the highway (engine: studio/shorts/dilemma.py).
Fact: RACV 'What to do if your brakes fail' and Michelin 'Brake problems' advice: stay calm, hazard lights + horn,
pump the brake pedal, shift down gradually through the gears (engine braking), apply the handbrake/parking brake
GRADUALLY (yanking it at speed can lock the rear wheels and make the car skid or spin), steer to a safe place off the
road. Voice take sped 1.1x (44.7 s > 40.7 s)."""
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import dilemma as DL  # noqa: E402
from kit import T, S, RED, GRN, WHITE, YEL  # noqa: E402

D = "/home/claude/sid/shorts/c094_brakes"
CAPS = [
    "Highway, you press the brake, and the pedal goes straight to the floor. BRAKES FAILED. Brave: yank the handbrake. Normal: gear down, stop slowly. Whose side are you on?",
    "Brave pulls the handbrake in ONE jerk at speed. Rear wheels lock, and the car starts to skid.",
    "Normal turns on hazard lights, pumps the brake pedal, drops one gear at a time, and pulls the handbrake slowly.",
    "WHO'S RIGHT? Comment B or N.",
    "NORMAL is right. Road safety experts say: jerk the handbrake at speed and the wheels can lock and the car can spin.",
    "Pump the pedal, shift down slowly, handbrake gently, and stop at a safe spot on the side.",
    "Brakes fail? No jerks, go slow. What would YOU do?",
]
ROLES = dict(intro=[1], brave=[2], normal=[3], ask=[4], reveal=[5], why=[6], end=[7])
CFG = dict(series="BRAVE vs NORMAL #10", question=("BRAKES FAILED!", "WHAT DO YOU DO?"),
           brave="YANK THE HANDBRAKE", normal="GEAR DOWN, STOP SLOWLY", answer='N', grade='studio',
           why_title="BRAKES FAILED? DO THIS",
           why_rows=[("Hazard lights + horn", WHITE), ("Pump the brake pedal", WHITE), ("Shift down one gear at a time", WHITE),
                     ("Handbrake GENTLY, never a jerk", RED), ("Steer to a safe spot, stop", GRN)],
           src="SRC: RACV & Michelin brake-failure advice", end=("BRAVE OR SMART?", "COMMENT  B  or  N"))

ROAD_T, ROAD_B = 560, 770
ORANGE_CAR = (0.95, 0.5, 0.15)
BLUE_CAR = (0.25, 0.5, 0.9)


def bg(c, t, speed, shoulder=0.0):
    g = __import__('cairo').LinearGradient(0, 0, 0, ROAD_T)
    g.add_color_stop_rgb(0, 0.45, 0.62, 0.85); g.add_color_stop_rgb(1, 0.85, 0.85, 0.8)
    c.rectangle(-400, 0, 1880, ROAD_T); c.set_source(g); c.fill()
    off = (t * speed * 60) % 400
    for j in range(7):   # hills
        x = -400 + j * 360 - (off * 0.2) % 360
        c.arc(x, ROAD_T + 40, 260, math.pi, 2 * math.pi); c.set_source_rgb(0.42, 0.58, 0.38); c.fill()
    for j in range(8):   # poles / trees
        x = -400 + j * 300 - off * 0.75 % 300
        c.rectangle(x, ROAD_T - 200, 14, 200); c.set_source_rgb(0.35, 0.28, 0.2); c.fill()
        c.arc(x + 7, ROAD_T - 210, 50, 0, 2 * math.pi); c.set_source_rgb(0.2, 0.45, 0.25); c.fill()
    c.rectangle(-400, ROAD_T, 1880, ROAD_B - ROAD_T); c.set_source_rgb(0.25, 0.25, 0.27); c.fill()
    c.rectangle(-400, ROAD_B, 1880, 200); c.set_source_rgb(0.55, 0.48, 0.35); c.fill()   # gravel shoulder
    for j in range(10):
        x = -400 + j * 220 - off % 220
        c.rectangle(x, (ROAD_T + ROAD_B) / 2 - 6, 110, 12); c.set_source_rgb(0.95, 0.95, 0.9); c.fill()
    c.rectangle(-400, ROAD_B - 6, 1880, 6); c.set_source_rgb(0.95, 0.85, 0.2); c.fill()


def car(c, x, yb, col, yaw=0.0, tilt=0.0, face=(0.86, 0.63, 0.47), mouth='flat', hazard=False, t=0.0, s=1.25):
    c.save(); c.translate(x, yb); c.scale(s, s); c.rotate(tilt); c.scale(max(0.35, math.cos(yaw)), 1)
    c.move_to(-140, -30); c.line_to(-140, -75); c.line_to(-95, -82); c.line_to(-55, -140); c.line_to(55, -140)
    c.line_to(95, -85); c.line_to(140, -75); c.line_to(140, -30); c.close_path(); c.set_source_rgb(*col); c.fill()
    c.move_to(-45, -130); c.line_to(45, -130); c.line_to(80, -88); c.line_to(-80, -88); c.close_path()
    c.set_source_rgb(0.7, 0.85, 0.95); c.fill()
    c.arc(18, -102, 17, 0, 2 * math.pi); c.set_source_rgb(*face); c.fill()
    c.arc(18, -106, 18, math.pi, 2 * math.pi); c.set_source_rgb(0.12, 0.09, 0.08); c.fill()
    c.arc(27, -103, 3.5, 0, 2 * math.pi); c.set_source_rgb(0.1, 0.1, 0.1); c.fill()
    if mouth == 'o':
        c.arc(30, -92, 4.5, 0, 2 * math.pi); c.set_source_rgb(0.3, 0.1, 0.1); c.fill()
    c.rectangle(128, -68, 12, 14); c.set_source_rgb(1, 0.95, 0.6); c.fill()
    on = hazard and int(t * 3) % 2 == 0
    for hx in (-140, 128):
        c.rectangle(hx, -56, 12, 12); c.set_source_rgb(1, 0.65, 0.05) if on else c.set_source_rgb(0.5, 0.3, 0.1); c.fill()
    for wx in (-85, 85):
        c.arc(wx, -28, 28, 0, 2 * math.pi); c.set_source_rgb(0.1, 0.1, 0.1); c.fill()
        c.arc(wx, -28, 12, 0, 2 * math.pi); c.set_source_rgb(0.6, 0.6, 0.62); c.fill()
    c.restore()


def bubble(c, x, y, txt, col=(1, 1, 1)):
    w = len(txt) * 24 + 60
    S.rrect(c, x - w / 2, y, w, 74, 30); c.set_source_rgba(*col, 0.95); c.fill()
    T(c, txt, x, y + 50, 36, (0.1, 0.1, 0.15), stroke=None)


def hud(c, speed, gear, hb, hb_col, hazard, t):
    S.rrect(c, 220, 360, 640, 150, 30); c.set_source_rgba(0.05, 0.05, 0.08, 0.85); c.fill()
    T(c, f"{int(speed)}", 320, 455, 70, WHITE, stroke=None)
    T(c, "km/h", 320, 495, 24, (0.7, 0.7, 0.75), stroke=None, bold=False)
    T(c, f"GEAR {gear}", 520, 450, 44, YEL, stroke=None)
    T(c, hb, 520, 495, 26, hb_col, stroke=None)
    on = hazard and int(t * 3) % 2 == 0
    c.move_to(760, 390); c.line_to(820, 490); c.line_to(700, 490); c.close_path()
    c.set_source_rgb(1, 0.3, 0.2) if on else c.set_source_rgb(0.35, 0.3, 0.3); c.fill()


def scene(c, side, t, p):
    if side == 'B':
        q = max(0.0, (p - 0.25) / 0.75)
        bg(c, t, 14 * (1 - 0.6 * q))
        yaw = 1.1 * min(1, q * 1.3)
        x = 540 + 60 * math.sin(q * 2.0)
        if q > 0:   # skid marks + smoke
            c.move_to(x - 260, ROAD_B - 40); c.line_to(x - 100, ROAD_B - 40 - 10 * q)
            c.set_source_rgba(0.05, 0.05, 0.05, 0.8); c.set_line_width(14); c.stroke()
            for j in range(6):
                r = 30 + 18 * j * q + 8 * math.sin(t * 5 + j)
                c.arc(x - 140 - j * 45, ROAD_B - 80 - j * 12, r, 0, 2 * math.pi)
                c.set_source_rgba(0.85, 0.85, 0.85, 0.5 * q); c.fill()
        car(c, x, ROAD_B - 30, ORANGE_CAR, yaw=yaw, tilt=0.04 * q * math.sin(t * 9), mouth='o' if q > 0 else 'flat')
        hud(c, 80 - 15 * q, 5, "HANDBRAKE: JERKED!" if p > 0.2 else "HANDBRAKE: OFF", RED if p > 0.2 else WHITE, False, t)
        if p < 0.25:
            bubble(c, 540, 262, "YANK THE HANDBRAKE!", (1, 0.85, 0.8))
        else:
            bubble(c, 540, 262, "WHEELS LOCKED! SKIDDING!", (1, 0.8, 0.78))
    else:
        q = S.ease(min(1, p / 0.95))
        bg(c, t, 14 * (1 - q))
        x = 540 - 80 * q
        car(c, x, ROAD_B - 30 + 45 * q, BLUE_CAR, mouth='flat', hazard=p > 0.05, t=t)
        gear = max(2, 5 - int(p * 4))
        hud(c, 80 * (1 - q), gear, "HANDBRAKE: SLOWLY" if p > 0.7 else ("PUMPING BRAKE" if p > 0.2 else "HAZARDS ON"),
            GRN, p > 0.05, t)
        if p > 0.9:
            bubble(c, 540, 262, "STOPPED. SAFE SIDE.")
        else:
            bubble(c, 540, 262, "GEAR DOWN, STOP SLOWLY")


def build():
    return DL.Dilemma(D, CAPS, ROLES, scene, CFG, mood='tense')


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        sh.preview(sh.preview_times(), f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in sh.L])
    else:
        sh.render(f"{D}/short.mp4")
