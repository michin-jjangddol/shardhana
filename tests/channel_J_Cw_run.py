# channel_J_Cw_OK_run.py
import numpy as np

VERSION = "Cw-OK-midpoint-1/6-SC-avg0 + selftest"

def channel_J_Cw(h, b, t_w, t_f=None):
    if t_f is None:
        t_f = t_w

    # Nodes along midlines: (b,0)->(0,0)->(0,h)->(b,h)
    y = np.array([b, 0.0, 0.0, b], dtype=float)
    z = np.array([0.0, 0.0, h,   h], dtype=float)

    # Segments: bottom flange, web, top flange
    dy = np.diff(y);  dz = np.diff(z)
    L  = np.hypot(dy, dz)
    tseg = np.array([t_f, t_w, t_f], dtype=float)
    ymid = 0.5*(y[:-1] + y[1:])
    zmid = 0.5*(z[:-1] + z[1:])

    # Thin-wall area & centroid
    A    = np.sum(tseg * L)
    ybar = np.sum(tseg * L * ymid) / A
    zbar = np.sum(tseg * L * zmid) / A

    # Iy, Iz about centroid (exact for straight segments)
    ay = y[:-1] - ybar;  az = z[:-1] - zbar
    Iy = np.sum(tseg * L * (az**2 + az*dz + (dz**2)/3.0))
    Iz = np.sum(tseg * L * (ay**2 + ay*dy + (dy**2)/3.0))

    # Trial Ω (centroid as trial SC) — USE MIDPOINTS!
    Om = [0.0]
    for i in range(3):
        dOm = (zmid[i] - zbar) * dy[i] - (ymid[i] - ybar) * dz[i]
        Om.append(Om[-1] + dOm)
    Om = np.array(Om)

    # ∫yΩ, ∫zΩ — the 1/6 factor is crucial
    Om_i, Om_j = Om[:-1], Om[1:]
    int_yO = np.sum(tseg*L/6.0 * ((y[:-1]+y[1:])*(Om_i+Om_j) + y[:-1]*Om_j + y[1:]*Om_i))
    int_zO = np.sum(tseg*L/6.0 * ((z[:-1]+z[1:])*(Om_i+Om_j) + z[:-1]*Om_j + z[1:]*Om_i))

    # Shear center
    ysc = ybar - int_zO / Iy
    zsc = zbar + int_yO / Iz

    # Final Ω (true SC)
    Om = [0.0]
    for i in range(3):
        dOm = (zmid[i] - zsc) * dy[i] - (ymid[i] - ysc) * dz[i]
        Om.append(Om[-1] + dOm)
    Om = np.array(Om)

    # Enforce average-zero: ∫Ω dA = Σ tL * avgΩ = 0
    Om_i, Om_j = Om[:-1], Om[1:]
    int_O = np.sum(tseg * L * (Om_i + Om_j) / 2.0)
    C = - int_O / A
    Om_adj = Om + C

    # Warping constant
    Om_i, Om_j = Om_adj[:-1], Om_adj[1:]
    Cw = np.sum(tseg * L / 3.0 * (Om_i**2 + Om_i*Om_j + Om_j**2))  # [mm^6]

    # Saint-Venant J
    J = (t_w**3 * h + 2.0 * t_f**3 * b) / 3.0                      # [mm^4]
    return J, Cw, (ybar, zbar), (ysc, zsc)

def _selftest():
    # 기대값 (엑셀과 일치)
    cases = [
        (81, 45, 0.8, 29.184, 5.54196711e8, 27.833, 19.215),
        (140, 45, 0.8, 39.25333333, 1.236995e9, 30.022, 36.129),
        (162, 45, 0.8, 43.008, 1.548418e9, 27.833, 42.632),
    ]
    for h,b,t, Jexp, Cwexp, ysc_exp, zsc_exp in cases:
        J, Cw, (_, _), (ysc, zsc) = channel_J_Cw(h,b,t)
        assert abs(J-Jexp) < 1e-6, (h,b,t,J,Jexp)
        assert abs((Cw-Cwexp)/Cwexp) < 5e-6, (h,b,t,Cw,Cwexp)
        assert abs(ysc-ysc_exp) < 1e-3 and abs(zsc-zsc_exp) < 1e-3, (ysc,zsc,ysc_exp,zsc_exp)
    print("SELFTEST OK")

if __name__ == "__main__":
    print("Version:", VERSION)
    _selftest()
    for h,b,t in [(81,45,0.8), (140,45,0.8), (162,45,0.8)]:
        J, Cw, (ybar,zbar), (ysc,zsc) = channel_J_Cw(h,b,t)
        print(f"h={h:>3}, b={b}, t={t} -> "
              f"J={J:.3f} mm^4,  Cw={Cw:.3e} mm^6 (≈{Cw/1e6:.1f} cm^6),  "
              f"ysc={ysc:.3f}, zsc={zsc:.3f}")
