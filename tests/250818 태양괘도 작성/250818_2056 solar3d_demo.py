# tests/solar3d_demo.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

# --- 시간 설정 ---
t_max = 20 * 365  # 20년 (일 단위)
n_points = 1000
t = np.linspace(0, t_max, n_points)

# --- 행성 궤도 파라미터 ---
# [AU] 단위
R_earth = 1.0
R_jupiter = 5.2

# [일] 단위
T_earth = 365
T_jupiter = 4333

# --- 각도 계산 ---
theta_earth = 2 * np.pi * t / T_earth
theta_jupiter = 2 * np.pi * t / T_jupiter

# --- 궤도 좌표 (간단히 기울기 반영) ---
earth = np.array([
    R_earth * np.cos(theta_earth),
    R_earth * np.sin(theta_earth),
    0.05 * np.sin(theta_earth)   # z 방향 작은 기울기
])

jupiter = np.array([
    R_jupiter * np.cos(theta_jupiter),
    R_jupiter * np.sin(theta_jupiter),
    0.1 * np.sin(theta_jupiter)  # z 방향 작은 기울기
])

# --- 플롯 설정 ---
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.set_title("Animated 3D Orbit of Earth and Jupiter around the Sun")

ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_zlim(-1, 1)
ax.set_xlabel("X [AU]")
ax.set_ylabel("Y [AU]")
ax.set_zlabel("Z [AU]")

# --- 초기 궤도선 ---
earth_line, = ax.plot([], [], [], "b-", lw=1, label="Earth")
jupiter_line, = ax.plot([], [], [], "orange", lw=1, label="Jupiter")
earth_dot, = ax.plot([], [], [], "bo")
jupiter_dot, = ax.plot([], [], [], "ro")
ax.scatter(0, 0, 0, color="yellow", s=200, label="Sun")

ax.legend()

# --- 업데이트 함수 ---
def update(frame):
    earth_line.set_data(earth[0, :frame], earth[1, :frame])
    earth_line.set_3d_properties(earth[2, :frame])

    jupiter_line.set_data(jupiter[0, :frame], jupiter[1, :frame])
    jupiter_line.set_3d_properties(jupiter[2, :frame])

    earth_dot.set_data([earth[0, frame]], [earth[1, frame]])
    earth_dot.set_3d_properties([earth[2, frame]])

    jupiter_dot.set_data([jupiter[0, frame]], [jupiter[1, frame]])
    jupiter_dot.set_3d_properties([jupiter[2, frame]])

    return earth_line, jupiter_line, earth_dot, jupiter_dot

# --- 애니메이션 생성 ---
ani = FuncAnimation(fig, update, frames=n_points, interval=30, blit=True)

# --- MP4 저장 ---
writer = FFMpegWriter(fps=30, metadata=dict(artist="Shardhana Project"), bitrate=1800)
ani.save("tests/solar3d_orbit.mp4", writer=writer)
print("✅ 애니메이션이 'tests/solar3d_orbit.mp4' 로 저장되었습니다.")
