# 예제 4 — 변위 제어(Displacement Control) : 하중–변위 곡선

이 예제는 1차원 막대(길이 L=2.0 m, 단면 A=10×10 mm²=0.0001 m², 강재 E=200 GPa)에
**변위를 점진적으로 증가**시키며 하중–변위(P–Δ) 거동을 그려 봅니다.
개념 모델은 **탄성 → 경화(hardening) → 연화(softening) → 파괴** 순서입니다.

> ⚠️ 단위 확인  
> 단면 \(A=0.0001\,\text{m}^2\) 이므로 극한응력 \(\sigma_u=450\,\text{MPa}\)에서  
> \(P_u=\sigma_u A = 450\times 10^6 \times 10^{-4} = 45\,\text{kN}\) 입니다. (450 kN 아님)

---

## 입력 요약

- 탄성계수: \(E=200\,\text{GPa}\)
- 단면적: \(A=0.0001\,\text{m}^2\) (10×10 mm²)
- 길이: \(L=2.0\,\text{m}\)
- 항복응력: \(\sigma_y=250\,\text{MPa}\)
- 극한응력: \(\sigma_u=450\,\text{MPa}\)
- 변위 이력: 속도 \( \dot{\Delta}=1.0\,\text{mm/s} \) (변위 제어)

경화/연화 구간의 변형률 경계(개념값):
- 항복 변형률 \( \varepsilon_y = \sigma_y/E \approx 0.00125 \Rightarrow \Delta_y \approx 2.5\,\text{mm}\)
- 극한 변형률 \( \varepsilon_u \approx 0.003 \Rightarrow \Delta_u \approx 6.0\,\text{mm}\)
- 파괴 변형률 \( \varepsilon_f \approx 0.006 \Rightarrow \Delta_f \approx 12.0\,\text{mm}\)

---

## 핵심 결과

| 구간/지점 | 변위 Δ [mm] | 시간 t [s] (Δ=1.0 mm/s 가정) | 응력 σ [MPa] | 하중 P [kN] |
|---|---:|---:|---:|---:|
| 항복 시작 \( \Delta_y \) | **≈ 2.50** | **≈ 2.50** | ≈ 250 | ≈ 25 |
| 극한 하중 \( \Delta_u \) | **≈ 6.00** | **≈ 6.00** | **≈ 450** | **≈ 45** |
| 파괴(거동 소실) \( \Delta_f \) | **≈ 12.00** | **≈ 12.00** | → 0 | → 0 |

- **P–Δ 곡선**: 처음엔 직선(탄성), 이후 완만한 증가(경화),  
  피크(≈45 kN) 뒤로 **하중 감소(연화/파괴)** 구간이 나타난다.  
- 변위 제어라서 **피크 이후 거동도 안정적으로 관찰**된다(하중 제어와 대비되는 장점).

---

## 그래프

> 저장한 그림을 참조 이미지로 링크합니다. (아래 코드로 생성)

![P–Δ 곡선](../img/ex4_p_delta.png)

---

## 파이썬 코드 (그래프/데이터 생성 및 저장)

```python
# docs/scribbles/make_ex4_plot.py  같은 위치에서 실행 예
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

# ----- 재료/기하 -----
E = 200e9       # Pa
A = 1.0e-4      # m^2
L = 2.0         # m
sigma_y = 250e6 # Pa
sigma_u = 450e6 # Pa

# 개념용 변형률 경계(경화/연화)
eps_y = sigma_y / E      # ≈0.00125 => Δy≈2.5 mm
eps_u = 0.0030           # Δu≈6.0 mm (피크)
eps_f = 0.0060           # Δf≈12.0 mm (파괴)

# ----- 변위 이력(변위 제어) -----
rate_mm_s = 1.0
dt = 0.1
t_max = 30.0
t = np.arange(0, t_max + dt, dt)
delta_mm = rate_mm_s * t
eps = (delta_mm / 1000.0) / L

def sigma_of_eps(e):
    if e <= eps_y:                           # 탄성
        return E * e
    if e <= eps_u:                           # 경화 (선형 가정)
        H = (sigma_u - sigma_y) / (eps_u - eps_y)
        return sigma_y + H * (e - eps_y)
    if e <= eps_f:                           # 연화 (선형 가정)
        return sigma_u * max(0.0, 1.0 - (e - eps_u)/(eps_f - eps_u))
    return 0.0

sigma = np.array([sigma_of_eps(e) for e in eps])
P_kN = sigma * A / 1000.0

# ----- 그래프 저장 -----
out_dir = Path(__file__).resolve().parents[0] / "img"
out_dir.mkdir(parents=True, exist_ok=True)
fig_path = out_dir / "ex4_p_delta.png"

plt.figure(figsize=(7,5))
plt.plot(delta_mm, P_kN, marker="o", label="P–Δ (displacement control)")
plt.axvline(eps_y*L*1000, color="gray", linestyle="--", alpha=0.5, label="yield δ_y")
plt.axvline(eps_u*L*1000, color="gray", linestyle=":",  alpha=0.7, label="ultimate δ_u")
plt.xlabel("Displacement Δ [mm]")
plt.ylabel("Load P [kN]")
plt.title("Bar: Elastic → Hardening → Softening → Failure")
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig(fig_path, dpi=160)
print(f"saved: {fig_path}")

# ----- 결과 요약 -----
print(f"Δ_y ≈ {eps_y*L*1000:.2f} mm,  Δ_u ≈ {eps_u*L*1000:.2f} mm (P_u ≈ {sigma_u*A/1000.0:.1f} kN),  Δ_f ≈ {eps_f*L*1000:.2f} mm")