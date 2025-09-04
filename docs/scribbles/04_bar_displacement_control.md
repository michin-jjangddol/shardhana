# 예제 4 — 변위 제어 (Displacement Control, P–Delta 곡선)

## 문제
길이 L = 2.0 m, 단면 A = 0.0001 m^2 (10x10 mm^2), 탄성계수 E = 200 GPa인 강재 막대를
변위 제어(속도 1.0 mm/s)로 당긴다. 재료 거동은 개념적으로 탄성 -> 경화 -> 연화 -> 파괴 순서로 진행된다.
하중–변위(P–Delta) 곡선을 그리고, 항복/피크/파괴 변위를 정리하라.

※ 단면 A = 0.0001 m^2 이므로 극한응력 sigma_u = 450 MPa에서
Pu = sigma_u * A = 450e6 * 1e-4 = 45,000 N = 45 kN.

---

## 입력값
- L = 2.0 m
- A = 0.0001 m^2 (10x10 mm^2)
- E = 200 GPa
- sigma_y = 250 MPa
- sigma_u = 450 MPa
- 변위 증가 속도 = 1.0 mm/s (변위 제어)

---

## 결과(숫자 요약)
- 항복 시작 변위 Delta_y ≈ **2.50 mm** (시간 ≈ 2.50 s, 하중 ≈ 25 kN)
- 극한(피크) 변위 Delta_u ≈ **6.00 mm** (시간 ≈ 6.00 s, 하중 ≈ **45 kN**)
- 파괴 변위 Delta_f ≈ **12.00 mm** (시간 ≈ 12.00 s, 하중 → 0)

표로 정리:

| 지점              | Delta [mm] | 시간 t [s] | sigma [MPa] | P [kN] |
|------------------|-----------:|-----------:|------------:|-------:|
| 항복 Delta_y     | 2.50       | 2.50       | 약 250      | 약 25  |
| 피크 Delta_u     | 6.00       | 6.00       | 약 450      | 약 45  |
| 파괴 Delta_f     | 12.00      | 12.00      | 0 근접      | 0 근접 |

---

## 도식(SVG)
예제 4 개념 그림:

![예제4 도식](../img/bar_ex4.svg)

---

## 파이썬 코드(그래프 생성 및 결과 저장)
아래 코드는 P–Delta 곡선을 계산해 `docs/scribbles/img/ex4_p_delta.png` 로 저장한다.
(모바일에서도 보이도록 PNG 사용)

```python
# 파일 경로 예: project_root/docs/scribbles/make_ex4_plot.py
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# 재료 / 기하
E = 200e9
A = 1.0e-4
L = 2.0
sigma_y = 250e6
sigma_u = 450e6

# 개념 경계(탄성-경화-연화 구분용)
eps_y = sigma_y / E          # ~0.00125 -> Delta_y ~ 2.5 mm
eps_u = 0.0030               # Delta_u ~ 6.0 mm (피크)
eps_f = 0.0060               # Delta_f ~ 12.0 mm (파괴)

# 변위 이력 (변위 제어)
rate_mm_s = 1.0
dt = 0.1
t_max = 30.0
t = np.arange(0, t_max + dt, dt)
delta_mm = rate_mm_s * t
eps = (delta_mm / 1000.0) / L

def sigma_of_eps(e):
    if e <= eps_y:
        return E * e                        # 탄성
    if e <= eps_u:
        H = (sigma_u - sigma_y) / (eps_u - eps_y)  # 간단 경화
        return sigma_y + H * (e - eps_y)
    if e <= eps_f:
        r = (e - eps_u) / (eps_f - eps_u)  # 간단 연화
        return sigma_u * max(0.0, 1.0 - r)
    return 0.0

sigma = np.array([sigma_of_eps(e) for e in eps])
P_kN = sigma * A / 1000.0

# 그래프 저장
out_dir = Path("docs/scribbles/img")
out_dir.mkdir(parents=True, exist_ok=True)
fig_path = out_dir / "ex4_p_delta.png"

plt.figure(figsize=(7,5))
plt.plot(delta_mm, P_kN, marker="o", label="P–Delta")
plt.axvline(eps_y*L*1000, color="gray", linestyle="--", alpha=0.5, label="Delta_y")
plt.axvline(eps_u*L*1000, color="gray", linestyle=":", alpha=0.7, label="Delta_u (peak)")
plt.xlabel("Delta [mm]")
plt.ylabel("P [kN]")
plt.title("예제 4: 변위 제어 P–Delta 곡선")
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig(fig_path, dpi=160)
print(f"saved: {fig_path}")

# 결과 숫자 재확인 출력
print("Delta_y ~", round(eps_y*L*1000, 2), "mm")
print("Delta_u ~", round(eps_u*L*1000, 2), "mm (Pu ~", round(sigma_u*A/1000.0,1), "kN)")
print("Delta_f ~", round(eps_f*L*1000, 2), "mm")