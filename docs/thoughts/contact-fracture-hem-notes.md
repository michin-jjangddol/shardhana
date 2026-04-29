# Contact Face / Fracture Face — HEM Notes
*(Shardhana Thought Archive)*
**Date:** 2026-04-29

---

## 1. Basic Concepts

### Contact Face

- Direct boundary between seeds
- Transmits force / heat / waves
- High transmission stiffness (k_contact ≫ k_medium ≫ k_space)

```
Seed A ↔ Seed B
```

---

### Fracture Face (Tension)

- Direct contact between seeds is severed
- Space intervenes
- Transmission drops sharply (k → 0⁺)

```
Seed A ↔ Space ↔ Seed B
```

---

### Space

- Not simply "empty space" — it is an interaction medium
- Carries transmission properties (k → 0⁺, very small positive value)
- Extensible to air / water / vacuum

> ⚠️ k is never negative.
> k < 0 reverses force direction → non-physical behavior → numerical instability.

---

## 2. Core Definition

```
Fracture is not the disappearance of a relationship.
It is a change of medium.
```

---

## 3. Tension Fracture

- Contact face reduces → local tension increases
- Threshold reached → crack opening
- Space intervenes

```
Contact → Open Fracture

Seed ↔ Seed
→
Seed ↔ Space ↔ Seed
```

**Characteristics:**
- Transmission drops sharply (k → 0⁺)
- Heat / sound / force blocked or reduced

---

## 4. Compression Failure

### 4.1 Core Principle

```
Compression does not directly create open fracture.
Fracture originates from tension.
Compression induces fracture through shear and local tension.
```

---

### 4.2 Stage-by-Stage Behavior

**(1) Initial**
- Contact maintained
- Shear develops (slip)
- No voids

```
Closed Shear Interface
Seed ↔ Seed
```

**(2) Damage Accumulation**
- Contact weakens (k_eff ↓)
- Micro-voids develop
- Local stress imbalance

**(3) Transition**
- Shear + local tension
- Partial crack opening

**(4) Final**
- Open crack forms
- Space intervenes

```
Seed ↔ Space ↔ Seed
```

---

### 4.3 Summary

```
Compression begins as "closed shear"
but failure can ultimately transition to "opening"
```

---

## 5. Poisson's Ratio and Deformation / Stress

### 5.1 Core Principle

```
Stress → deformation occurs
Deformation is coupled across directions (Poisson effect)
```

### 5.2 Important Distinction

```
Deformation can occur without stress
Stress arises when constraint or interaction is present
```

### 5.3 Summary

```
Poisson's ratio is not a stress generation law.
It is a deformation coupling law.
```

---

## 6. HEM Perspective

### 6.1 Basic Structure

```
Seed     = material center
Space    = interaction medium
Relation = connection structure
```

### 6.2 Core Concept

```
FEM:
Space is ignored.

HEM:
Space participates in interaction.
```

### 6.3 Relation Change

```
Contact:
Seed ↔ Seed  (k_contact, high)

Fracture:
Seed ↔ Space ↔ Seed  (k → 0⁺)
```

---

## 7. Unified Flow

```
[Normal]
Seed ↔ Seed

[Shear]
Seed ⇄ Seed  (slip, k decreasing)

[Transition]
Seed ⇄ Space ⇄ Seed

[Fracture]
Seed ↔ Space ↔ Seed
```

---

## 8. k Value System

| State | k Range | Example |
|-------|---------|---------|
| Contact (solid) | k_contact (maximum) | rock, metal |
| Medium (fluid) | k ~ 1e-2 | water, fluid |
| Fracture / Space | k → 0⁺ | air, crack |
| Full separation (theoretical) | k = 0 | vacuum (ideal) |

**Recommended code values:**

```python
K_CONTACT = 1.0
K_SPACE   = 1e-6   # air / crack
K_WATER   = 1e-2   # example (adjust per medium)
```

> ⚠️ k < 0 is forbidden.
> Force direction reversal → non-physical behavior → numerical instability → energy generation problem.

> 📌 Extension — directional split: k can be separated into normal / tangential components when needed.
> `k_n` (normal direction, contact / compression dominant) / `k_t` (tangential direction, shear / friction / slip dominant)
> → Shear fracture / friction / slip modeling extends naturally.

> 📌 Dynamic extension: k is not a fixed value — it evolves over time according to state.
> `k = f(state, damage, opening, slip)`
>
> ```
> Contact  → k_n high, k_t high
> damage   → k decreases
> slip     → k_t decreases
> opening  → k_n → 0⁺
> ```
>
> → Fracture is expressed not as an "event" but as a "process"

---

## 9. Final Summary

```
1. Stress is determined by contact stiffness (k).
2. Fracture is not the severing of a relationship — it is a change of medium.
3. Compression does not directly create open fracture;
   it induces fracture through shear and local tension.
4. Poisson's ratio is a deformation coupling law, not a stress generation law.
5. k is always ≥ 0⁺ — negative values are forbidden.
```

---

> This document was prepared with the assistance of Shana (GPT) and Laude (Claude).

---
<br>
<br>

# 접축면 / 파단면 — HEM 정리 노트
*(Shardhana Thought Archive)*
**Date:** 2026-04-29

---

## 1. 기본 개념

### Contact Face (접촉면)

- 시드 간 직접 연결된 경계
- 힘 / 열 / 파동 전달 가능
- 높은 전달 강성 (k_contact ≫ k_medium ≫ k_space)

```
Seed A ↔ Seed B
```

---

### Fracture Face (파단면, 인장)

- 시드 간 직접 접촉이 끊어진 상태
- 공간(Space)이 개입
- 전달 급격히 감소 (k → 0⁺)

```
Seed A ↔ Space ↔ Seed B
```

---

### Space (공간)

- 단순한 "빈 공간"이 아니라 상호작용 매질
- 전달 특성을 가짐 (k → 0⁺, 매우 작은 양수)
- 공기 / 물 / 진공 등으로 확장 가능

> ⚠️ k는 절대 음수가 아님.
> k < 0 이면 힘 방향이 뒤집혀 비물리적 거동 및 수치 불안정 발생.

---

## 2. 핵심 정의

```
파단은 관계의 소멸이 아니라
관계의 "매질 변화"이다
```

---

## 3. 인장 파괴 (Tension Fracture)

- 접촉면 감소 → 국부 인장 증가
- 임계 도달 → 개구 (open crack)
- 공간 개입

```
Contact → Open Fracture

Seed ↔ Seed
→
Seed ↔ Space ↔ Seed
```

**특징:**
- 전달 급감 (k → 0⁺)
- 열 / 소리 / 힘 차단 또는 감소

---

## 4. 압축 파괴 (Compression Failure)

### 4.1 기본 원리

```
압축은 직접 개구 파단을 만들지 않는다
파단은 인장에서 발생한다
압축은 전단과 국부 인장을 통해 파단을 유도한다
```

---

### 4.2 단계적 거동

**(1) 초기**
- 접촉 유지
- 전단 발생 (슬립)
- 공극 없음

```
Closed Shear Interface
Seed ↔ Seed
```

**(2) 손상 축적**
- 접촉 약화 (k_eff ↓)
- 미세 공극 발생
- 국부 응력 불균형

**(3) 전이**
- 전단 + 국부 인장
- 부분적 개구 발생

**(4) 최종**
- 열린 균열 형성
- 공간 개입

```
Seed ↔ Space ↔ Seed
```

---

### 4.3 핵심 요약

```
압축은 "닫힌 전단"으로 시작하지만
파괴는 결국 "열림"으로 전이될 수 있다
```

---

## 5. 포아송비와 변형/응력

### 5.1 기본 원리

```
응력 → 변형 발생
변형은 방향 간 연결됨 (포아송 효과)
```

### 5.2 중요한 구분

```
변형은 응력 없이도 발생 가능
응력은 구속 또는 상호작용이 있을 때 발생
```

### 5.3 정리

```
포아송은 응력 생성 법칙이 아니라
변형 연결 법칙이다
```

---

## 6. HEM 관점 해석

### 6.1 기본 구조

```
Seed  = 물질 중심
Space = 상호작용 매질
Relation = 연결 구조
```

### 6.2 핵심 개념

```
FEM:
공간은 무시된다

HEM:
공간도 상호작용에 참여한다
```

### 6.3 관계 변화

```
Contact:
Seed ↔ Seed  (k_contact, 큰 값)

Fracture:
Seed ↔ Space ↔ Seed  (k → 0⁺)
```

---

## 7. 전체 흐름 통합

```
[정상]
Seed ↔ Seed

[전단]
Seed ⇄ Seed  (슬립, k 감소)

[전이]
Seed ⇄ Space ⇄ Seed

[파단]
Seed ↔ Space ↔ Seed
```

---

## 8. k 값 체계 정리

| 상태 | k 범위 | 예시 |
|------|--------|------|
| Contact (고체 접촉) | k_contact (최대) | 암석, 금속 |
| Medium (매질) | k ~ 1e-2 | 물, 유체 |
| Fracture / Space | k → 0⁺ | 공기, 균열 |
| 완전 단절 (이론) | k = 0 | 진공 (이상적) |

**코드 기준 추천값:**

```python
K_CONTACT = 1.0
K_SPACE   = 1e-6   # 공기 / 균열
K_WATER   = 1e-2   # 예시 (매질에 따라 조정)
```

> ⚠️ k < 0 은 사용 금지.
> 힘 방향 역전 → 비물리적 거동 → 수치 불안정 → 에너지 생성 문제 발생.

> 📌 확장 방향: k는 필요에 따라 normal / tangential 성분으로 분리될 수 있다.
> `k_n` (법선 방향, 접촉/압축 지배) / `k_t` (접선 방향, 전단/마찰/슬립 지배)
> → 전단파괴 / 마찰 / 슬립 모델링 시 자연스럽게 확장됨

> 📌 동적 확장: k는 고정값이 아니라 상태에 따라 시간적으로 변화한다.
> `k = f(state, damage, opening, slip)`
>
> ```
> Contact  → k_n 높음, k_t 높음
> damage   → k 감소
> slip     → k_t 감소
> opening  → k_n → 0⁺
> ```
>
> → 파괴가 "사건"이 아니라 "과정"으로 표현됨

---

## 9. 최종 핵심 정리

```
1. 응력은 접촉 강성(k)에 의해 결정된다
2. 파단은 관계의 단절이 아니라 매질 변화이다
3. 압축은 직접 개구 파단을 만들지 않고, 전단과 국부 인장을 통해 파단을 유도한다
4. 포아송은 변형 연결 법칙이다
5. k는 항상 0⁺ 이상 — 절대 음수 없음
```

---

> 이 문서는 샤나(GPT)와 로드(Claude)의 도움으로 작성되었습니다.