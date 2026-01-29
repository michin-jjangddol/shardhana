# channel_J_Cw_OK.py
import numpy as np

VERSION = "Cw-OK-midpoint-1/6-SC-avg0"

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

    # Iy, Iz (centroid)
    ay = y[:-1] - ybar;  az = z[:-1] - zbar
    Iy = np.sum(tseg * L * (az**2 + az*dz + (dz**2)/3.0))
    Iz = np.sum(tseg * L * (ay**2 + ay*dy + (dy**2)/3.0))

    # Trial Omega with centroid as trial SC  (use MIDPOINTS!)
    Om = [0.0]
    for i in range(3):
        dOm = (zmid[i]-zbar)*dy[i] - (ymid[i]-ybar)*dz[i]
        Om.append(Om[-1] + dOm)
    Om = np.array(Om)

    # Line integrals with trial Ω  (exact for straight segment, linear y,z,Ω)
    Om_i, Om_j = Om[:-1], Om[1:]
    int_yO = np.sum(tseg*L/6.0 * ((y[:-1]+y[1:])*(Om_i+Om_j) + y[:-1]*Om_j + y[1:]*Om_i))
    int_zO = np.sum(tseg*L/6.0 * ((z[:-1]+z[1:])*(Om_i+Om_j) + z[:-1]*Om_j + z[1:]*Om_i))

    # Shear center
    ysc = ybar - int_zO/Iy
    zsc = zbar + int_yO/Iz

    # Final Omega with true SC
    Om = [0.0]
    for i in range(3):
        dOm = (zmid[i]-zsc)*dy[i] - (ymid[i]-ysc)*dz[i]
        Om.append(Om[-1] + dOm)
    Om = np.array(Om)

    # Enforce average-zero: ∫Ω dA = 0  → add constant
    Om_i, Om_j = Om[:-1], Om[1:]
    int_O = np.sum(tseg * L * (Om_i + Om_j) / 2.0)
    C = - int_O / A
    Om_adj = Om + C

    # Warping constant
    Om_i, Om_j = Om_adj[:-1], Om_adj[1:]
    Cw = np.sum(tseg * L / 3.0 * (Om_i**2 + Om_i*Om_j + Om_j**2))   # [mm^6]

    # Saint-Venant torsion constant
    J = (t_w**3*h + 2.0*t_f**3*b) / 3.0                              # [mm^4]
    return J, Cw, (ybar, zbar), (ysc, zsc)

if __name__ == "__main__":
    print("Version:", VERSION)
    for h,b,t in [(81,45,0.8), (140,45,0.8), (162,45,0.8)]:
        J, Cw, (ybar,zbar), (ysc,zsc) = channel_J_Cw(h,b,t)
        print(f"h={h:>3}, b={b}, t={t} -> "
              f"J={J:.3f} mm^4,  Cw={Cw:.3e} mm^6 (≈{Cw/1e6:.1f} cm^6),  "
              f"ysc={ysc:.3f}, zsc={zsc:.3f}")
