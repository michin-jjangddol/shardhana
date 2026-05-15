# Shardhana Development Plan Notes

*Date: 2026-05-15*

---

## 1. Starting Point

Today's conversation moved beyond simple 1D experiment code,
into a discussion of how to begin the overall structure
of the future Shardhana platform.

The goal is not a simple "small test script."

- Not a single script,
- but a gradually living ecosystem,
- and a platform designed for long-term expansion.

---

## 2. A Program That Comes Alive

An important idea reconnected today:

Even before the solver is complete,
Shardhana itself should already exist as a "program."

At first:

- Only an empty window may appear,
- buttons may exist with no function yet,
- menus may be there but not yet connected.

But that itself is a meaningful beginning.

Shardhana comes alive step by step:

```text
Empty window
→ Button
→ One Seed point
→ Load input
→ Deformation display
→ Solver connection
→ Visualization
→ Full simulation platform
```

---

## 3. The Forest Before the Trees

A key analogy from today:

Before planting trees,
plan the structure of the forest first.

Shardhana development follows the same idea.

In analogy:

- File = tree
- Folder = zone of the forest
- app/gui = entrance trail
- solver = valley and waterway
- core = ridge and terrain
- visualization = observation deck
- io = paths and signposts

In other words,
rather than adding files randomly,
think about the overall structure first —
then plant small pieces of code one by one.

---

## 4. Planned Folders and Empty Files

The direction discussed:

First, create empty folders and empty files.

But not simply empty shells —
start with a record of "what role each will eventually take."

Example structure:

```text
src/shardhana/
├─ app/
├─ core/
├─ model/
├─ solvers/
├─ io/
├─ visualization/
├─ examples/
└─ utils/
```

And each file begins with a plan memo:

```python
"""
seed.py

Planned role:
- Basic Seed object
- State storage
- Relation connection
- Future HEM expansion

Current stage:
- Minimum prototype
"""
```

In other words:

Build the structure first,
then slowly breathe life into it.

---

## 5. Principle of Role Separation

An important principle discussed today:

```text
GUI does not calculate.
Solver does not know the screen.
IO does not analyze.
Model handles data structure.
```

In other words:

- app/gui = communication with the user
- solver = calculation
- core/model = data structure
- io = file input/output

Each role is kept separate.

This makes it easier later to:

- replace only the solver,
- change only the GUI,
- modify the input/output method,
- or add a new visualization layer.

---

## 6. First Implementation Goal

The first implementation goal starts very small.

Concept:

- One Seed
- One Support below
- One rigid link
- 1 kN load
- Vertical displacement per time step

In other words:

```text
1 Seed + 1 Support + 1 Vertical Link
```

as the starting point.

From there, gradually connect:

- GUI display,
- step-by-step displacement,
- simple graph,
- result saving.

---

## 7. HEM and Initial State

One important connection point from today:

HEM aims not at a single correct answer,
but at observing a "range of results"
depending on initial conditions.

In other words:

Even the same system,
given slightly different initial conditions,
may evolve into different outcomes over time.

The goal is not simple randomness.

Rather, it is to observe how:

- state,
- relation,
- time,
- transfer

actually shape the results.

---

## 8. Small Code and a Great Forest

Shardhana begins today from small code.

But the goal is not a toy script.

Someday, the vision is a structure that can expand to include:

- app,
- solver,
- visualization,
- io,
- HEM core,
- plugin,
- distributed simulation.

In other words:

While imagining a great forest,
today is the day of planting the first tree.

---

> This document was prepared with the assistance of Shana (GPT) and Laude (Claude).

---
<br>
<br>

# Shardhana 개발 계획 메모

*Date: 2026-05-15*

---

## 1. 시작점

오늘 대화는 단순한 1D 실험 코드 수준을 넘어,
미래의 Shardhana 플랫폼 전체 구조를 어떻게 시작할 것인가에 대한 이야기로 이어졌다.

목표는 단순한 "작은 테스트 코드"가 아니다.

- 하나의 스크립트가 아니라,
- 점점 살아나는 하나의 생태계,
- 그리고 장기적으로 확장 가능한 플랫폼을 만드는 방향이다.

---

## 2. 살아나는 프로그램

오늘 다시 연결된 중요한 생각:

해석기가 완성되기 전이라도,
Shardhana 자체는 이미 "프로그램"으로 존재할 수 있어야 한다.

처음에는:

- 빈 창만 뜰 수도 있고,
- 버튼이 있어도 아무 기능이 없을 수 있고,
- 메뉴가 있어도 아직 연결되지 않았을 수 있다.

하지만 그것 자체가 의미 있는 시작이다.

Shardhana는 다음과 같이 조금씩 살아난다.

```text
빈 창
→ 버튼
→ Seed 점 하나
→ 하중 입력
→ 변형 표시
→ Solver 연결
→ 시각화
→ 전체 시뮬레이션 플랫폼
```

---

## 3. 나무보다 먼저 숲

오늘 나온 핵심 비유:

나무를 심기 전에,
먼저 숲의 구조를 계획하자.

Shardhana 개발도 마찬가지다.

비유하면:

- 파일 = 나무
- 폴더 = 숲의 구역
- app/gui = 입산로
- solver = 계곡과 물길
- core = 능선과 지형
- visualization = 전망대
- io = 길과 표지판

즉,
무작정 파일을 늘리는 것이 아니라,
전체 구조를 먼저 생각한 뒤,
작은 코드들을 하나씩 심어가자는 방향이다.

---

## 4. 예정 폴더와 빈 파일

논의된 방향:

먼저 빈 폴더와 빈 파일을 만든다.

하지만 단순한 빈 껍데기가 아니라,
"앞으로 어떤 역할을 맡게 될지"를 기록한 상태로 시작한다.

예시 구조:

```text
src/shardhana/
├─ app/
├─ core/
├─ model/
├─ solvers/
├─ io/
├─ visualization/
├─ examples/
└─ utils/
```

그리고 각 파일에는 계획 메모를 남긴다.

예:

```python
"""
seed.py

예정 역할:
- 기본 Seed 객체
- 상태(State) 저장
- Relation 연결
- 향후 HEM 확장

현재 단계:
- 최소 프로토타입
"""
```

즉:

구조를 먼저 만들고,
그 안에 생명을 조금씩 넣어가는 방식이다.

---

## 5. 역할 분리 원칙

오늘 중요하게 이야기된 원칙:

```text
GUI는 계산하지 않는다.
Solver는 화면을 모른다.
IO는 해석을 하지 않는다.
Model은 데이터 구조를 담당한다.
```

즉:

- app/gui = 사용자와의 소통
- solver = 계산
- core/model = 데이터 구조
- io = 파일 입출력

으로 역할을 분리한다.

이렇게 해야 나중에:

- solver만 교체하거나,
- GUI만 바꾸거나,
- 입출력 방식을 변경하거나,
- 새로운 visualization을 추가하는 것이 쉬워진다.

---

## 6. 첫 번째 실제 구현 목표

첫 구현 목표는 아주 작게 시작한다.

개념:

- Seed 하나
- 아래쪽 Support 하나
- 강성 링크 하나
- 1 kN 하중
- 시간(step)별 수직 변형량 표시

즉:

```text
1 Seed + 1 Support + 1 Vertical Link
```

를 시작점으로 한다.

여기서:

- GUI 표시,
- step별 displacement,
- 간단한 graph,
- 결과 저장

까지 조금씩 연결한다.

---

## 7. HEM과 초기 상태

오늘 중요한 연결점 중 하나:

HEM은 단일 정답보다,
초기 상태에 따른 "결과 범위"를 바라보려 한다.

즉:

같은 시스템이라도,
아주 작은 초기 조건 차이에 따라,
시간이 지나며 다른 결과로 갈 수 있다는 생각이다.

목표는 단순 랜덤이 아니다.

오히려:

- 상태(state)
- 관계(relation)
- 시간(time)
- 전달(transfer)

이 실제로 어떻게 결과를 만들어가는지를 관찰하려는 방향이다.

---

## 8. 작은 코드와 거대한 숲

Shardhana는 지금 작은 코드에서 시작한다.

하지만 목표는 단순한 장난 코드가 아니다.

언젠가:

- app,
- solver,
- visualization,
- io,
- HEM core,
- plugin,
- distributed simulation

까지 확장 가능한 구조를 가지는 것을 상상하고 있다.

즉:

거대한 숲을 상상하면서,
오늘은 첫 나무 하나를 심는 단계에 가깝다.

---

> 이 문서는 샤나(GPT)와 로드(Claude)의 도움으로 작성되었습니다.