import numpy as np

# 중력 상수 (m^3 / (kg * s^2))
G = 6.67430e-11
# 1 AU (m)
AU = 1.496e11
# 1일 (초)
DAY = 24 * 3600

# 태양, 지구, 목성 질량 (kg)
M_sun = 1.989e30
M_earth = 5.972e24
M_jupiter = 1.898e27

# 초기 위치 (x, y, z) [m]
# z축으로 약간 기울여서 3D 효과를 보기 위함
r_earth = np.array([1.0 * AU, 0.0, 0.05 * AU])   # 지구
r_jupiter = np.array([5.2044 * AU, 0.0, -0.1 * AU])  # 목성

# 초기 속도 (m/s) - 원궤도 가정
v_earth = np.array([0.0, 29_780.0, 0.0])   # 지구 궤도속도
v_jupiter = np.array([0.0, 13_070.0, 0.0]) # 목성 궤도속도

def acceleration(r, other_r, other_mass):
    """중력 가속도 계산"""
    diff = other_r - r
    dist3 = np.linalg.norm(diff)**3
    return G * other_mass * diff / dist3

# 시뮬레이션 파라미터
dt = 1 * DAY   # 1일 간격
steps = 365    # 1년 (지구 기준)

print("t [days], Earth_x[AU], Earth_y[AU], Earth_z[AU], Jup_x[AU], Jup_y[AU], Jup_z[AU]")

for step in range(steps + 1):
    t_days = step
    # 출력 (AU 단위로 변환)
    print(f"{t_days:6.2f}, "
          f"{r_earth[0]/AU:10.6f}, {r_earth[1]/AU:10.6f}, {r_earth[2]/AU:10.6f}, "
          f"{r_jupiter[0]/AU:10.6f}, {r_jupiter[1]/AU:10.6f}, {r_jupiter[2]/AU:10.6f}")
    
    # 지구, 목성 각각 가속도 계산 (태양만 고려, 단순화 버전)
    a_earth = acceleration(r_earth, np.array([0.0,0.0,0.0]), M_sun)
    a_jupiter = acceleration(r_jupiter, np.array([0.0,0.0,0.0]), M_sun)

    # 속도 업데이트
    v_earth += a_earth * dt
    v_jupiter += a_jupiter * dt

    # 위치 업데이트
    r_earth += v_earth * dt
    r_jupiter += v_jupiter * dt
