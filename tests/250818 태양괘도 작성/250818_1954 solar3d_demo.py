import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- 시간 설정 ---
t_max = 12 * 365  # 12년 동안 시뮬레이션
n_points = 1000
t = np.linspace(0, t_max, n_points)

# --- 공전 주기 (단위: 일) ---
T_earth = 365
T_jupiter = 4332

# --- 궤도 함수 (단순 원궤도) ---
def orbit(a, T, t):
    theta = 2 * np.pi * t / T
    x = a * np.cos(theta)
    y = a * np.sin(theta)
    z = np.zeros_like(theta)
    return x, y, z

earth = orbit(1.0, T_earth, t)
jupiter = orbit(5.2, T_jupiter, t)

# --- 3D 그림 ---
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(earth[0], earth[1], earth[2], 'b', label='Earth')
ax.plot(jupiter[0], jupiter[1], jupiter[2], 'orange', label='Jupiter')
ax.scatter(0, 0, 0, color='yellow', s=200, label='Sun')

ax.set_xlabel("X [AU]")
ax.set_ylabel("Y [AU]")
ax.set_zlabel("Z [AU]")
ax.set_title("3D Orbit of Earth and Jupiter (with period difference)")
ax.legend()
plt.show()
