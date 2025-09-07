import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

# 시뮬레이션 시간 설정
t_max = 4 * np.pi
n_points = 500
t = np.linspace(0, t_max, n_points)

# 궤도 반지름 (AU)
earth_radius = 1.0
mars_radius = 1.524
jupiter_radius = 5.2

# 공전 주기 (년 단위)
earth_period = 1.0
mars_period = 1.88
jupiter_period = 11.86

# 시작 각도 (2025년 개략 위치)
earth_start = np.deg2rad(0.0)
mars_start  = np.deg2rad(115.0)
jup_start   = np.deg2rad(250.0)

# 궤도 좌표
earth = np.array([earth_radius * np.cos(2*np.pi*t/earth_period + earth_start),
                  earth_radius * np.sin(2*np.pi*t/earth_period + earth_start),
                  np.zeros_like(t)])

mars = np.array([mars_radius * np.cos(2*np.pi*t/mars_period + mars_start),
                 mars_radius * np.sin(2*np.pi*t/mars_period + mars_start),
                 0.05 * np.sin(2*np.pi*t/mars_period + mars_start)])

jupiter = np.array([jupiter_radius * np.cos(2*np.pi*t/jupiter_period + jup_start),
                    jupiter_radius * np.sin(2*np.pi*t/jupiter_period + jup_start),
                    0.1 * np.sin(2*np.pi*t/jupiter_period + jup_start)])

# 플롯 초기화
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_zlim(-1, 1)

# 태양
ax.scatter(0, 0, 0, color="red", s=100, label="Sun")

# 라인 & 점
earth_line, = ax.plot([], [], [], "g-", lw=1)
mars_line, = ax.plot([], [], [], color="orange", lw=1)
jupiter_line, = ax.plot([], [], [], "b-", lw=1)
earth_dot, = ax.plot([], [], [], "go", markersize=6)
mars_dot, = ax.plot([], [], [], "o", color="orange", markersize=6)
jupiter_dot, = ax.plot([], [], [], "bo", markersize=6)

def update(frame):
    earth_line.set_data(earth[0, :frame], earth[1, :frame])
    earth_line.set_3d_properties(earth[2, :frame])
    mars_line.set_data(mars[0, :frame], mars[1, :frame])
    mars_line.set_3d_properties(mars[2, :frame])
    jupiter_line.set_data(jupiter[0, :frame], jupiter[1, :frame])
    jupiter_line.set_3d_properties(jupiter[2, :frame])

    earth_dot.set_data([earth[0, frame]], [earth[1, frame]])
    earth_dot.set_3d_properties([earth[2, frame]])
    mars_dot.set_data([mars[0, frame]], [mars[1, frame]])
    mars_dot.set_3d_properties([mars[2, frame]])
    jupiter_dot.set_data([jupiter[0, frame]], [jupiter[1, frame]])
    jupiter_dot.set_3d_properties([jupiter[2, frame]])

    return earth_line, mars_line, jupiter_line, earth_dot, mars_dot, jupiter_dot

ani = FuncAnimation(fig, update, frames=n_points, interval=50, blit=True)

# 동영상 저장
writer = FFMpegWriter(fps=30, bitrate=1800)
output_file = "tests/solar3d_earth_mars_jupiter.mp4"
ani.save(output_file, writer=writer)

plt.close(fig)  # ✅ figure 닫아서 파이썬 종료 안 걸리게 함
print(f"✅ 동영상 저장 완료: {output_file}")
