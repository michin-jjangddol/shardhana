# From Hand Calculation to HEM

---

# 1. Axial Stress and Shear Stress: Average and Distribution

In structural analysis, the most fundamental stresses are axial stress and shear stress.

Axial stress is expressed as:

σ = N / A

This assumes that stress is uniformly distributed over the entire cross-section.

In contrast, shear stress varies depending on the position within the section.

τ = VQ / Ib

Shear stress inherently involves a distribution concept,
as its value changes across the cross-section.

Thus:

- Axial stress is close to an average concept.
- Shear stress is based on a distribution concept.

This difference is not merely a difference in formulas,
but a difference in how we simplify structural behavior.

---

# 2. Average Stress and Local Stress

In reality, loads are never ideally distributed.

When load is introduced over a small area,
strong local stress concentration occurs near the loading zone.

In this region:

- Multiaxial stress states exist.
- Stress varies rapidly with position.

However, sufficiently far from the load introduction,
stress redistributes and becomes averaged.

σ = N / A

is therefore closer to a representation of the post-redistribution state.

Average stress is not an absolute physical truth,
but a practical simplification to preserve global equilibrium.

---

# 3. Evolution of Analysis Methods

Analysis concerns how structural behavior is calculated.

- Hand Calculation: Average stress–based simplified analysis
- FEM: Stress distribution and local behavior analysis
- AEM: Element separation and collapse tracking
- HEM: State-transition and interaction-based analysis

HEM does not reject previous methods,
but attempts to reduce layers of assumptions in structural modeling.

---

# 4. Evolution of Design Philosophy

Design concerns how uncertainty is handled.

- ASD: Global safety factor
- LSD / LRFD: Load and resistance factors
- PBD: Performance-based design

As analysis becomes more refined,
the structure of conservatism in design also evolves.

---

# 5. The Future of Design Methods

The next design philosophy has yet to be defined.

| Design Philosophy | Core Concept |
|-------------------|--------------|
| ASD | Global safety factor |
| LSD / LRFD | Partial factors, probabilistic basis |
| PBD | Performance-based design |
| ??? | ??? |

HEM analysis awaits a new design philosophy.

---

# 수계산에서 HEM까지

---

# 1. 축응력과 전단응력: 평균과 분포

구조해석에서 가장 기본이 되는 응력은 축응력과 전단응력이다.

축응력은 다음과 같이 표현된다.

σ = N / A

이는 단면 전체에 동일한 응력이 작용한다고 가정한다.

반면 전단응력은 단면 위치에 따라 달라진다.

τ = VQ / Ib

전단응력은 분포 개념을 포함하며,
단면 내 위치에 따라 값이 달라진다.

즉:

- 축응력은 평균 개념에 가깝다.
- 전단응력은 분포 개념을 전제로 한다.

이 차이는 단순한 공식의 차이가 아니라,
우리가 구조를 어떻게 단순화하는가의 차이이다.

---

# 2. 평균응력과 국부응력

현실에서 하중은 이상적으로 분포되지 않는다.

작은 면적으로 하중이 도입되면
하중 도입부에서는 국부 응력 집중이 발생한다.

이 구간에서는:

- 다축 응력이 동시에 존재한다.
- 응력은 위치에 따라 급격히 변화한다.

그러나 하중 도입부에서 충분히 떨어진 위치에서는
응력이 재분배되며 평균화된다.

σ = N / A

는 이러한 평균화 이후의 거동을 표현한 근사식에 가깝다.

평균응력은 절대적 진리가 아니라,
전역 평형을 표현하기 위한 실용적 단순화이다.

---

# 3. 해석 방법의 진화

해석은 거동을 어떻게 계산하는가에 대한 문제이다.

- 수계산: 평균응력 중심의 단순 해석
- FEM: 응력 분포 계산과 국부 거동 분석
- AEM: 요소 분리와 붕괴 과정 추적
- HEM: 상태 변화와 상호작용 기반 해석

HEM은 기존 해석을 부정하는 것이 아니라,
가정의 층을 낮추어 거동을 재구성하려는 시도이다.

---

# 4. 설계 철학의 진화

설계는 불확실성을 어떻게 다루는가에 대한 문제이다.

- ASD: 전역 안전율
- LSD / LRFD: 하중계수와 저항계수 분리
- PBD: 성능 중심 설계

해석이 정밀해질수록
설계의 보수성 구조도 변화해왔다.

---

# 5. 앞으로의 설계법

아직 정의되지 않은 미래의 설계법은
어떤 형태일지 알 수 없다.

| 설계 철학 | 핵심 개념 |
|-----------|-----------|
| ASD | 전역 안전율 |
| LSD / LRFD | 부분계수, 확률 기반 |
| PBD | 성능 중심 설계 |
| ??? | ??? |

HEM 해석법은 새로운 설계법을 기다립니다.

---

> 이 문서는 샤나(GPT)의 도움으로 작성된 문서입니다.