# Necking — HEM Implementation Direction

*(Shardhana Thoughts)*  
*Date: 2026-04-16*

---

## Purpose

This document outlines the initial direction for implementing necking behavior in Shardhana.

The goal is not to replicate conventional FEM,  
but to build a structure where necking and fracture behavior  
emerge naturally through HEM (Han Element Method).

---

## Reference Paper

Cho et al. (2024)  
High-temperature Properties and Constitutive Model of FR355 Fire-resistant Steel for Fire-resistant Structure Simulation

DOI: https://doi.org/10.7781/kjoss.2024.36.1.091

---

## Key Observations

Main points confirmed from the paper:

- At high temperatures, necking occurs before large deformation
- After yielding, deformation is not uniform — it concentrates locally
- Post-necking behavior cannot be explained by simple 1D assumptions
- Therefore, separate modeling is needed for:
  - Pre-necking
  - Post-necking
  - Ductile fracture

---

## Shardhana Interpretation

Necking is not simply a reduction in cross-section.  
It is interpreted as:

- **State** — concentration of state
- **Relation** — imbalance between element relations
- **Space** — collapse of uniform deformation

---

## Target Behavior (1D)

Starting from a simple 1D bar model, the following flow is implemented:

| Stage | Behavior |
|-------|----------|
| Initial | Entire bar stretches uniformly |
| Middle | Deformation begins to concentrate at a specific location |
| Late | Concentrated zone grows rapidly (necking) |
| Final | Fracture occurs |

---

## HEM Concept Connection

> Element = Seed + Space + State + Relation

Necking initiation conditions (conceptual):

- Increasing State difference between adjacent elements
- Load transfer imbalance
- Deformation concentration in specific elements

---

## Development Strategy

> At this stage, the focus is on rule-based behavior generation, not equation-based formulation.

- Step 1 — Implement minimal 1D model without GUI
- Step 2 — Visualize deformation over time
- Step 3 — Compare with FEM behavior
- Step 4 — Expand to 3-panel GUI structure

---

## Future Extensions

- Add temperature dependency
- Introduce damage accumulation model
- Compare with actual experimental behavior

---

## State Interpretation

> Necking is not a force problem —  
> it is the moment when the state distribution collapses.

---

## One-line Definition

> Necking is not a reduction in cross-section —  
> it is a phenomenon that emerges naturally from state concentration and relational imbalance.

---

> This document was written with the help of Shana (GPT) and Laude (Claude).

---
<br>
<br>

# 넥킹(Necking) — HEM 구현 방향 노트

*(Shardhana 생각창고)*  
*Date: 2026-04-16*

---

## 목적

Shardhana에서 넥킹(Necking) 현상을 구현하기 위한 시작 방향을 정리한다.

목표는 기존 FEM을 그대로 재현하는 것이 아니라,  
HEM(Han Element Method)을 이용하여  
넥킹과 파괴 거동이 자연스럽게 생성되는 구조를 만드는 것이다.

---

## 참고 논문

Cho et al. (2024)  
내화구조 시뮬레이션을 위한 FR355 내화강의 고온특성 및 구성모델

DOI: https://doi.org/10.7781/kjoss.2024.36.1.091

---

## 핵심 관찰

논문에서 확인되는 주요 포인트:

- 고온에서는 큰 변형 전에 넥킹이 발생한다
- 항복 이후 변형이 균일하지 않고 국부적으로 집중된다
- 넥킹 이후 거동은 단순 1D 가정으로 설명 불가
- 따라서 구간을 나누어 모델링 필요:
  - 넥킹 이전 (Pre-necking)
  - 넥킹 이후 (Post-necking)
  - 연성 파괴 (Ductile fracture)

---

## Shardhana 관점 해석

넥킹은 단순한 단면 감소가 아니다:

- **State** — 상태의 집중
- **Relation** — 요소 간 관계의 불균형
- **Space** — 균일 변형의 붕괴

으로 해석한다.

---

## 목표 거동 (1D)

단순한 1D 막대 모델에서 다음 흐름을 구현한다:

| 단계 | 거동 |
|------|------|
| 초기 | 전체가 균일하게 늘어남 |
| 중기 | 특정 위치에 변형 집중 시작 |
| 후기 | 집중 구간 급격히 증가 (넥킹) |
| 최종 | 파단 발생 |

---

## HEM 개념 연결

> Element = Seed + Space + State + Relation

넥킹 발생 조건 (개념):

- 인접 요소 간 State 차이 증가
- 하중 전달 불균형 발생
- 특정 요소에 변형 집중

---

## 개발 전략

> 본 단계에서는 수식 기반이 아닌, 규칙 기반 거동 생성에 집중한다.

- Step 1 — GUI 없이 1D 최소 모델 구현
- Step 2 — 시간에 따른 변형 시각화
- Step 3 — FEM 거동과 비교
- Step 4 — 3단 GUI 구조로 확장

---

## 향후 확장

- 온도 의존성 추가
- 손상 누적 모델 도입
- 실제 실험 거동과 비교

---

## 상태 해석 핵심

> 넥킹은 힘의 문제가 아니라, 상태 분포가 무너지는 순간이다.

---

## 한 줄 정의

> 넥킹은 단면 감소가 아니라,  
> 상태 집중과 관계 불균형으로부터 자연스럽게 생성되는 현상이다.

---

> 이 문서는 샤나(GPT)와 로드 Laude(Claude)의 도움으로 작성되었습니다.
