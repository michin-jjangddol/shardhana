# tests/solar_demo.py
# 뉴턴 N-body (태양-지구-목성) 초간단 데모 — velocity-Verlet 적분

from math import sqrt

G = 6.67430e-11            # 만유인력상수 [m^3 kg^-1 s^-2]
M_SUN = 1.9885e30          # 태양 질량 [kg]
M_EARTH = 5.972e24         # 지구 질량 [kg]
M_JUPITER = 1.898e27       # 목성 질량 [kg]
AU = 1.495978707e11        # 1 AU [m]

class Body:
    def __init__(self, name, m, x, y, vx, vy):
        self.name = name
        self.m = m
        self.x = x; self.y = y
        self.vx = vx; self.vy = vy
        self.ax = 0.0; self.ay = 0.0

def accel(bodies):
    # 각 천체의 가속도 초기화
    for b in bodies:
        b.ax = b.ay = 0.0
    # 짝(pair)별 중력 계산 (O(N^2))
    n = len(bodies)
    for i in range(n):
        bi = bodies[i]
        for j in range(i+1, n):
            bj = bodies[j]
            dx = bj.x - bi.x
            dy = bj.y - bi.y
            r2 = dx*dx + dy*dy
            r = sqrt(r2)
            if r == 0: 
                continue
            f_over_r = G / (r2 * r)  # = G / r^3
            ax = f_over_r * dx
            ay = f_over_r * dy
            # 뉴턴 제3법칙: 서로 반대 방향
            bi.ax += ax * bj.m
            bi.ay += ay * bj.m
            bj.ax -= ax * bi.m
            bj.ay -= ay * bi.m

def step_verlet(bodies, dt):
    # 1) x_half = x + v*dt + 0.5*a*dt^2 (여기서는 v_half를 쓰는 전형적 형태)
    for b in bodies:
        b.vx += 0.5 * b.ax * dt
        b.vy += 0.5 * b.ay * dt
        b.x  += b.vx * dt
        b.y  += b.vy * dt
    # 2) 새 위치에서 가속도 갱신
    accel(bodies)
    # 3) v_{t+dt} = v_half + 0.5*a_new*dt
    for b in bodies:
        b.vx += 0.5 * b.ax * dt
        b.vy += 0.5 * b.ay * dt

def circular_speed(mu, r):
    # 원궤도 근사 속도: v = sqrt(mu / r),  mu = G * M_sun
    return sqrt(mu / r)

def main():
    mu = G * M_SUN

    # 초기 조건 (태양을 원점, 지구/목성은 +x축에 두고 +y방향으로 공전 시작)
    r_e = 1.0 * AU
    r_j = 5.2044 * AU
    v_e = circular_speed(mu, r_e)
    v_j = circular_speed(mu, r_j)

    sun = Body("Sun",     M_SUN,     0.0, 0.0, 0.0, 0.0)
    earth = Body("Earth", M_EARTH,   r_e, 0.0, 0.0,  v_e)
    jup = Body("Jupiter", M_JUPITER, r_j, 0.0, 0.0,  v_j)

    bodies = [sun, earth, jup]

    # 첫 가속도 계산
    accel(bodies)

    # 시뮬레이션 설정: 1년 정도 (dt = 6시간)
    hours = 6
    dt = hours * 3600.0
    days = 365
    steps = int((days*24)/hours)

    print("t [days],  Earth_x[AU], Earth_y[AU],  Jup_x[AU], Jup_y[AU]")
    t = 0.0
    for k in range(steps):
        if k % 10 == 0:  # 너무 많이 찍히지 않게 간격 출력
            ex = earth.x / AU; ey = earth.y / AU
            jx = jup.x / AU;   jy = jup.y / AU
            print(f"{t/86400:8.2f}, {ex:10.6f}, {ey:10.6f}, {jx:10.6f}, {jy:10.6f}")
        step_verlet(bodies, dt)
        t += dt

if __name__ == "__main__":
    main()
