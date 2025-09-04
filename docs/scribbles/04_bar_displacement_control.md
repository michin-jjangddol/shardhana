# 예제 4 — 변위 제어 (Displacement Control, P–Delta 곡선)

## 문제 설명
길이 2.0 m, 단면 10×10 mm^2 (=0.0001 m^2)인 강재 막대에 변위를 일정 속도(1.0 mm/s)로 증가시킨다.  
재료 특성은 다음과 같다.

- 탄성계수 E = 200 GPa  
- 항복응력 sigma_y = 250 MPa  
- 극한응력 sigma_u = 450 MPa  

거동은 **탄성 → 경화 → 연화 → 파괴** 순으로 진행된다고 가정한다.  
변위 제어 방식을 통해 하중–변위 곡선(P–Delta curve)을 구하고, 파괴 시점을 확인한다.

---

## 입력값 요약
- L = 2.0 m  
- A = 0.0001 m^2 (10×10 mm^2)  
- E = 200 GPa  
- sigma_y = 250 MPa  
- sigma_u = 450 MPa  
- 변위 증가 속도 = 1.0 mm/s

---

## 파이썬 코드 (풀이)

```python
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# 재료 및 기하
E = 200e9
A = 1.0e-4
L = 2.0
sigma_y = 250e6
sigma_u = 450e6

# 개념 경계값
eps_y = sigma_y / E
eps_u = 0.0030
eps_f = 0.0060

# 변위 이력
rate_mm_s = 1.0
dt = 0.1
t_max = 30.0
t = np.arange(0, t_max + dt, dt)
delta_mm = rate_mm_s * t
eps = (delta_mm / 1000.0) / L

def sigma_of_eps(e):
    if e <= eps_y:
        return E * e
    if e <= eps_u:
        H = (sigma_u - sigma_y) / (eps_u - eps_y)
        return sigma_y + H * (e - eps_y)
    if e <= eps_f:
        r = (e - eps_u) / (eps_f - eps_u)
        return sigma_u * max(0.0, 1.0 - r)
    return 0.0

sigma = np.array([sigma_of_eps(e) for e in eps])
P_kN = sigma * A / 1000.0

# 그래프 저장
out_dir = Path("docs/scribbles/img")
out_dir.mkdir(parents=True, exist_ok=True)
fig_path = out_dir / "ex4_p_delta.png"

plt.figure(figsize=(7,5))
plt.plot(delta_mm, P_kN, marker="o", label="P–Delta 곡선")
plt.axvline(eps_y*L*1000, color="gray", linestyle="--", alpha=0.5, label="Delta_y")
plt.axvline(eps_u*L*1000, color="gray", linestyle=":", alpha=0.7, label="Delta_u (피크)")
plt.xlabel("변위 Delta [mm]")
plt.ylabel("하중 P [kN]")
plt.title("예제 4: 변위 제어 P–Delta 곡선")
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig(fig_path, dpi=160)
print(f"saved: {fig_path}")

# 결과 요약 출력
print("Delta_y ≈", round(eps_y*L*1000, 2), "mm")
print("Delta_u ≈", round(eps_u*L*1000, 2), "mm (Pu ≈", round(sigma_u*A/1000.0,1), "kN)")
print("Delta_f ≈", round(eps_f*L*1000, 2), "mm")