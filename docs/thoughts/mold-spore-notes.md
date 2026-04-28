# Mold Spore Dispersion — HEM Concept Memo
*(Shardhana / HEM Concept Memo — Draft)*

---

## 1. Observed Phenomenon

When water is dropped onto food with mold on its surface,
the following occurs:

- The mold does not move along with the water
- At the moment water makes contact:
  → mold powder (spores) burst outward
- Not in a specific direction —
  → spherical (omnidirectional) dispersion into the air

> "The mold spores spread as if becoming one with the air."

---

## 2. Difference from Common Intuition

Common expectation:

- Water → dispersion medium
- Mold → carried by water

Actual observation:

- Water does not "carry" the spores
- Water acts as a trigger

---

## 3. Physical Interpretation

This phenomenon can be understood in three stages:

### (1) Attached State
- Spores are weakly attached to the surface in powder form

### (2) Trigger Event (Moisture Impact)
- Upon water contact:
  - Surface tension changes
  - Adhesion decreases
  - Structure collapses

### (3) Release & Dispersion
- Spores detach simultaneously
- Via air flow and micro-turbulence:
  → transition to aerosol state
  → dispersion into the air

> Not "movement" —
> but a transition from attached state to air-dominated state.

---

## 4. Behavior in Air

Spores are very small particles (approx. 1–10 μm):

- Air influence dominates over gravity
- Movement is probabilistic due to turbulence

Characteristics:

- Omnidirectional dispersion (spherical distribution)
- Prolonged suspension in air
- Gradual settling over time

> Spores do not fall —
> they are incorporated into the air system and drift.

---

## 5. Modeling Perspective

This phenomenon can be simplified into the following elements:

### Core Physics
- Particle detachment
- Aerosolization
- Turbulent dispersion
- Viscous drag + gravity

### Level of Analysis
- Microscopic (molecular) analysis not required
- Continuum air + particle model is sufficient

---

## 6. HEM Interpretation

Element composition:

- **Seed**: mold spore
- **Space**: air

### State (Internal)
- phase: attached / released / airborne
- adhesion: attachment strength (0.0 ~ 1.0)
- velocity: velocity vector

### Trigger (External Condition)
- moisture: phase transition occurs when threshold is reached

### Relation
- State transition occurs at threshold condition
- Probabilistic movement coupled with air flow

---

### State Transition

```
attached
→ (moisture trigger)
→ released
→ airborne
→ dispersion
```

---

## 7. Conceptual Definition

> "Mold spore dispersion is an event in which
> fixed particles are released under threshold conditions
> and incorporated into the air system."

---

## 8. Simulation Feasibility

This phenomenon can be modeled with the following structure:

### Model Composition
- Particle: spore (Seed)
- Field: air flow + turbulent noise (Space)
- State:
  - phase (attached / released / airborne)
  - adhesion
  - velocity

### Event
- moisture trigger → phase transition occurs

### Algorithm Flow
1. Initialization:
   - All spores in attached state
2. Trigger applied:
   - Spores → released when moisture threshold is reached
3. Burst (release):
   - released → airborne transition
   - Initial velocity assigned (random, no directional bias)
4. Dispersion:
   - Air flow + random noise applied
   - Probabilistic movement
5. Settling:
   - Viscous drag + gravity applied
   - Re-attachment possible under certain conditions

---

## 9. CFD Assessment

- CFD: analyzes the fluid itself → excessive for this case
- This problem: "particle behavior within fluid"

> Fully reproducible without CFD.

---

## 10. Core Summary

- Mold does not fly on its own
- Water does not create the movement

> "attached → released → incorporated into air → dispersion"

---

> This document was written with the help of Shana (GPT) and Laude (Claude).

---
<br>
<br>

# 곰팡이 포자 확산에 대한 메모
*(Shardhana / HEM Concept Memo — 초안)*

---

## 1. 관찰된 현상

음식 표면에 곰팡이가 생긴 상태에서
물을 떨어뜨리면 다음과 같은 현상이 발생한다:

- 곰팡이가 물을 따라 이동하는 것이 아님
- 물이 닿는 순간
  → 곰팡이 가루(포자)가 화악 퍼짐
- 특정 방향이 아니라
  → 공기 중으로 구형(전방향) 확산

> "곰팡이 포자가 공기와 하나가 된 것처럼 퍼진다"

---

## 2. 기존 직관과의 차이

일반적인 예상:

- 물 → 확산 매개체
- 곰팡이 → 물 따라 이동

실제 관찰:

- 물이 "운반"하는 것이 아니라
- 물이 트리거(trigger) 역할을 함

---

## 3. 현상의 물리적 해석

이 현상은 다음 3단계로 이해할 수 있다:

### (1) 고정 상태 (Attached State)
- 포자는 표면에 가루 형태로 약하게 부착됨

### (2) 트리거 발생 (Moisture Impact)
- 물이 닿으면서:
  - 표면 장력 변화
  - 접착력 감소
  - 구조 붕괴

### (3) 방출 및 확산 (Release & Dispersion)
- 포자가 동시에 떨어짐
- 공기 흐름 및 미세 난류에 의해
  → 에어로졸 상태로 전환
  → 공기 중 확산

> "이동"이 아니라
> 고정 상태 → 공기 지배 상태로의 전이

---

## 4. 공기 중 거동

포자는 매우 작은 입자 (약 1~10 μm)이므로:

- 중력보다 공기 영향이 큼
- 난류에 의해 확률적으로 이동

특징:

- 전방향 확산 (구형 분포)
- 장시간 공기 중 부유
- 이후 서서히 침강

> 포자는 떨어지는 것이 아니라
> 공기 시스템에 편입되어 떠다닌다

---

## 5. 모델링 관점

이 현상은 다음 요소로 단순화 가능:

### 핵심 물리
- 입자 탈착 (detachment)
- 에어로졸화 (aerosolization)
- 난류 확산 (turbulent dispersion)
- 점성 저항 + 중력

### 해석 수준
- 미시(분자) 해석 불필요
- 연속체 공기 + 입자 모델로 충분

---

## 6. HEM 관점 해석

Element 구성:

- **Seed**: 곰팡이 포자
- **Space**: 공기

### State (내부 상태)
- phase: attached / released / airborne
- adhesion: 부착 강도 (0.0 ~ 1.0)
- velocity: 속도 벡터

### Trigger (외부 조건)
- moisture: 임계값 도달 시 phase 전이 발생

### Relation
- 임계 조건에서 상태 전이 발생
- 공기 흐름과 결합된 확률적 이동

---

### State Transition

```
attached
→ (moisture trigger)
→ released
→ airborne
→ dispersion
```

---

## 7. 개념적 정의

> "곰팡이 포자 확산은
> 고정된 입자가 임계 조건에서 해제되어
> 공기 시스템으로 편입되는 사건이다."

---

## 8. 시뮬레이션 가능성

이 현상은 다음과 같은 구조로 모델링할 수 있다:

### 모델 구성
- Particle: 포자 (Seed)
- Field: 공기 흐름 + 난류 노이즈 (Space)
- State:
  - phase (attached / released / airborne)
  - adhesion
  - velocity

### 이벤트
- moisture trigger → phase 전이 발생

### 알고리즘 흐름
1. 초기화:
   - 모든 포자는 attached 상태
2. 트리거 적용:
   - moisture 임계값 도달 시 일부 포자 → released
3. 방출 (burst):
   - released → airborne 전이
   - 초기 속도 부여 (랜덤 + 방향성 없음)
4. 확산:
   - 공기 흐름 + 랜덤 노이즈 적용
   - 확률적 이동
5. 침강:
   - 점성 저항 + 중력 적용
   - 일정 조건에서 재부착 가능

---

## 9. CFD 필요성 판단

- CFD: 유체 자체 해석 → 과도함
- 본 문제: "유체 속 입자 거동"

> CFD 없이도 충분히 재현 가능

---

## 10. 핵심 정리

- 곰팡이는 스스로 날아가는 것이 아님
- 물이 "이동"을 만드는 것이 아님

> "고정 → 해제 → 공기 편입 → 확산"

---

> 이 문서는 샤나(GPT)와 로드 Laude(Claude)의 도움으로 작성되었습니다.
