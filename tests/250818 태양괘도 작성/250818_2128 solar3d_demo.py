import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# 시뮬레이션 시간 설정
t_max = 4 * np.pi   # 애니메이션 길이
n_points = 500
t = np.linspace(0, t_max, n_points)

# 궤도 반지름 (AU)
earth_radius = 1.0
mars_radius = 1.524
jupiter_radius = 5.2

# 공전 주기 (년 단위, 단순 비율)
earth_period = 1.0
mars_period = 1.88
jupiter_period = 11.86

# 시작 각도 (2025년 기준 대략 값, 라디안)
earth_start = np.deg2rad(0.0)      # 기준
mars_start = np.deg2rad(115.0)     # 화성
jup_start  = np.deg2rad(250.0)     # 목성

# 궤도 데이터
earth = np.array([earth_radius * np.cos(2*np.pi*t/earth_period + earth_start),
                  earth_radius * np.sin(2*np.pi*t/earth_period + earth_start),
                  np.zeros_like(t)])

mars = np.array([mars_radius * np.cos(2*np.pi*t/mars_period + mars_start),
                 mars_radius * np.sin(2*np.pi*t/mars_period + mars_start),
                 0.05 * np.sin(2*np.pi*t/mars_period + mars_start)])  # 약간 기울기 반영

jupiter = np.array([jupiter_radius * np.cos(2*np.pi*t/jupiter_period + jup_start),
                    jupiter_radius * np.sin(2*np.pi*t/jupiter_period + jup_start),
                    0.1 * np.sin(2*np.pi*t/jupiter_period + jup_start)])

# 플롯 초기화
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.set_title("3D Orbit of Earth, Mars, and Jupiter around the Sun (2025 approx. start)")
ax.set_xlabel("X [AU]")
ax.set_ylabel("Y [AU]")
ax.set_zlabel("Z [AU]")

# 축 범위 (정육면체)
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_zlim(-1, 1)

# 태양
ax.scatter(0, 0, 0, color="red", s=100, label="Sun")

# 궤도 라인 & 점 초기화
earth_line, = ax.plot([], [], [], "g-", lw=1, label="Earth orbit")
mars_line, = ax.plot([], [], [], "orange", lw=1, label="Mars orbit")
jupiter_line, = ax.plot([], [], [], "b-", lw=1, label="Jupiter orbit")

earth_dot, = ax.plot([], [], [], "go", markersize=6, label="Earth")
mars_dot, = ax.plot([], [], [], "o", color="orange", markersize=6, label="Mars")
jupiter_dot, = ax.plot([], [], [], "bo", markersize=6, label="Jupiter")

ax.legend()

# 업데이트 함수
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

# 애니메이션 실행
ani = FuncAnimation(fig, update, frames=n_points, interval=50, blit=True)

plt.show()
