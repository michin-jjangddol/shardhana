import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- 행성 궤도 데이터 생성 ---
def orbital_elements(a, e, i, omega, Omega, M0, T, n_points=500):
    M = np.linspace(0, 2*np.pi, n_points) + M0
    E = M + e*np.sin(M)  # 근사 해 (저편심도 가정)
    x = a * (np.cos(E) - e)
    y = a * np.sqrt(1 - e**2) * np.sin(E)
    z = np.zeros_like(x)

    # 3D 궤도 회전 변환
    cosO, sinO = np.cos(Omega), np.sin(Omega)
    cosi, sini = np.cos(i), np.sin(i)
    cosw, sinw = np.cos(omega), np.sin(omega)

    X = (cosO*cosw - sinO*sinw*cosi) * x + (-cosO*sinw - sinO*cosw*cosi) * y
    Y = (sinO*cosw + cosO*sinw*cosi) * x + (-sinO*sinw + cosO*cosw*cosi) * y
    Z = (sini*sinw) * x + (sini*cosw) * y

    return X, Y, Z

# 태양, 지구, 목성 궤도 요소 (단순화)
earth = orbital_elements(a=1.0, e=0.0167, i=np.radians(0.00005), omega=0, Omega=0, M0=0, T=365)
jupiter = orbital_elements(a=5.2, e=0.0489, i=np.radians(1.3), omega=0, Omega=0, M0=0, T=4332)

# --- 그림/애니메이션 설정 ---
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.set_title("Animated 3D Orbit of Earth and Jupiter around the Sun")

# 축 라벨
ax.set_xlabel("X [AU]")
ax.set_ylabel("Y [AU]")
ax.set_zlabel("Z [AU]")

# 초기 데이터
line_earth, = ax.plot([], [], [], "b-", lw=1)
point_earth, = ax.plot([], [], [], "bo", label="Earth")

line_jupiter, = ax.plot([], [], [], "orange", lw=1)
point_jupiter, = ax.plot([], [], [], "o", color="orange", label="Jupiter")

ax.scatter(0, 0, 0, color="yellow", s=200, label="Sun")  # 태양
ax.legend()

# 좌표 범위
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_zlim(-0.5, 0.5)

# --- 애니메이션 업데이트 함수 ---
def update(frame):
    # Earth
    line_earth.set_data(earth[0][:frame], earth[1][:frame])
    line_earth.set_3d_properties(earth[2][:frame])
    point_earth.set_data(earth[0][frame-1:frame], earth[1][frame-1:frame])
    point_earth.set_3d_properties(earth[2][frame-1:frame])

    # Jupiter
    line_jupiter.set_data(jupiter[0][:frame], jupiter[1][:frame])
    line_jupiter.set_3d_properties(jupiter[2][:frame])
    point_jupiter.set_data(jupiter[0][frame-1:frame], jupiter[1][frame-1:frame])
    point_jupiter.set_3d_properties(jupiter[2][frame-1:frame])

    return line_earth, point_earth, line_jupiter, point_jupiter

# --- 실행 ---
ani = FuncAnimation(fig, update, frames=len(earth[0]), interval=30, blit=True)
plt.show()
