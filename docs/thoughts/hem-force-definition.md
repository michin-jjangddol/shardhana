# On the Difference Between Force Definitions in FEM and HEM

## 1. Motivation

In conventional structural analysis (FEM), axial force, shear force, and bending moment are defined based on infinitesimal cross-sections (dA).  
This approach assumes a continuum and derives forces by first defining a stress field and then integrating it over a cross-section.

In contrast, HEM does not define force as the result of stress integration.  
Instead, force is defined as the transfer of force between Seeds.

This document records the conceptual difference between force definitions in FEM and HEM.

---

## 2. Force Definition in FEM

### 2.1 Fundamental Assumptions

- The material is a continuum.
- A cross-section can be divided into infinitesimal areas (dA).
- The stress field is defined first.

### 2.2 Definition of Forces

Axial force:

N = ∫A σ dA

Shear force:

V = ∫A τ dA

Bending moment:

M = ∫A yσ dA

### 2.3 Characteristics

- Force is the result of integrating the stress field.
- The concept of cross-section is essential.
- It relies on infinitesimal (limit) concepts.
- Force is defined as a derived quantity.

---

## 3. Force Definition in HEM

### 3.1 Basic Concept

- A Seed is a finite-volume mass entity.
- A Seed receives external force.
- The received force is either translated or transferred to neighboring Seeds.
- In statics, the sum of incoming and outgoing forces at each Seed is zero.

An external force acts directly on a specific Seed,  
which becomes the primary starting point of force transfer.  
The force is then distributed throughout the structure via transfer relations between Seeds.

---

## 4. Transfer-Based Force Definition

For two Seeds i and j, define:

Initial distance: L₀  
Current distance: L  

Distance change:

ΔL = L − L₀

Transfer force:

Tᵢⱼ = k · ΔL · eᵢⱼ

Here, k is the transfer stiffness between the two Seeds,  
and eᵢⱼ is the unit vector connecting the two Seeds.

---

## 5. Axial, Shear, and Moment in HEM

Axial force:

The component of the transfer force along the unit vector connecting two Seeds.

Shear force:

The component of the transfer force excluding the axial direction.

Moment:

If the force acts away from the Seed center,  
M = r × F can be defined.

In HEM Stage 1, the system can begin without rotational degrees of freedom,  
similar to truss analysis.

---

## 6. Philosophical Difference Between FEM and HEM

FEM:  
“Define stress first, then integrate stress to obtain force.”

HEM:  
“Define force transfer first, and construct structural behavior from transfer relations.”

FEM is continuum-based.  
HEM is discrete-entity-based.

The final results may appear similar,  
but the starting point of force definition and the underlying conceptual framework are fundamentally different.

---

## 7. HEM Stage 1 Declaration

- A Seed is a finite-volume mass entity.
- Force is a transfer quantity proportional to the distance change between Seeds.
- Static equilibrium is defined by force balance at each Seed.

---

## 8. Initial Seed and Automatic Refinement Concept

### 8.1 Initial Seed Definition

HEM begins analysis not from infinitesimal elements,  
but from finite-sized Seeds defined by the user.

- The initial Seed size is user-defined according to analysis purpose.
- Examples: 1000 mm cube, 1 mm cube, 1 μm cube.
- Each Seed is treated as an independent entity with mass and state.

Thus, the analysis starts from a finite reference entity,  
not from an infinitesimal element.

---

### 8.2 Seed State and Neighbor Relations

Each Seed contains:

- Position
- Mass
- External force
- Displacement
- Transfer relations with neighboring Seeds
- Current transfer force value

A Seed’s behavior is not determined independently.  
It is always defined by its relations with neighboring Seeds  
(distance change, relative state variation, etc.).

---

### 8.3 Automatic Refinement (Generational Evolution)

During analysis, a Seed is automatically subdivided into smaller Seeds  
if the following conditions are met:

- State difference with neighboring Seeds exceeds a threshold.
- Distance change or transfer force variation becomes significant.
- User-defined tolerance is exceeded.

When subdivision occurs:

- The original Seed becomes the parent.
- Newly generated smaller Seeds become children.
- Child Seeds inherit the parent’s state as initial conditions.

This is not a method that expands from micro to macro scale.  
Rather, it starts from a macro-scale analysis and refines into smaller Seeds when necessary.

---

### 8.4 Termination of Refinement

Subdivision does not continue indefinitely.

- Refinement stops when the minimum Seed size defined by the user is reached.
- Or when state variation falls below the tolerance.

Thus, the minimum Seed size determines the maximum generational depth of the analysis.

---

### 8.5 Iterative Analysis Procedure

1. Generate initial finite Seeds.
2. Perform global static analysis.
3. Evaluate state differences between Seeds.
4. Subdivide Seeds exceeding criteria.
5. Reanalyze with the updated Seed structure.
6. Stop when minimum size or tolerance condition is satisfied.

This process is not merely mesh refinement,  
but a process in which existence itself evolves according to state.

---

> This document was prepared with the assistance of Shana (GPT).

<br>
<br>



# FEM과 HEM에서의 힘 정의 차이에 대한 정리

## 1. 문제의식

기존 구조해석(FEM)은 미소단면(dA)을 기반으로 축력, 전단력, 모멘트를 정의한다.  
이는 연속체 가정을 전제로 하며, 응력장을 먼저 정의한 뒤 단면 적분을 통해 힘을 도출하는 방식이다.

그러나 HEM에서는 힘을 단면 적분의 결과로 정의하기보다,  
시드(Seed) 간의 “힘 전달(transfer)” 자체를 힘의 정의로 삼고자 한다.

이 문서는 FEM과 HEM의 힘 정의 방식의 차이를 정리하기 위한 사고 기록이다.

---

## 2. FEM에서의 힘 정의

### 2.1 기본 가정

- 재료는 연속체이다.
- 단면은 무한히 작은 면적(dA)으로 나눌 수 있다.
- 응력장이 먼저 정의된다.

### 2.2 힘의 정의

축력:

N = ∫A σ dA

전단력:

V = ∫A τ dA

모멘트:

M = ∫A yσ dA

### 2.3 특징

- 힘은 응력장의 적분 결과이다.
- 단면 개념이 필수적이다.
- 무한소(극한) 개념에 기반한다.
- 힘은 “결과값”으로 정의된다.

---

## 3. HEM에서의 힘 정의

### 3.1 기본 개념

- Seed는 유한한 부피를 가진 질량 덩어리이다.
- Seed는 외력을 받는다.
- 받은 힘은 이동하거나 인접 Seed로 전달된다.
- 정역학에서는 각 Seed에서 들어온 힘과 나간 힘의 합이 0이 된다.

외력은 특정 Seed에 직접 작용하며,
해당 Seed는 전달의 1차 기점이 된다.
이후 힘은 Seed 간 전달 관계를 통해 구조 내부로 분산된다.

---

## 4. 전달 기반 힘 정의

두 Seed i, j 사이의 초기 거리 L₀와 현재 거리 L을 정의한다.

거리 변화:

ΔL = L − L₀

전달력:

Tᵢⱼ = k · ΔL · eᵢⱼ
여기서 k는 두 Seed 간 전달 강성이고, 
eᵢⱼ는 두 Seed를 잇는 방향 단위 벡터이다.

---

## 5. HEM에서의 축력, 전단, 모멘트

축력:

두 Seed를 잇는 방향 단위 벡터에 대한 전달력의 성분

전단력:

전달력 중 축 방향을 제외한 성분

모멘트:

힘의 작용 위치가 Seed 중심에서 벗어날 경우  
M = r × F 로 정의 가능

단, HEM 1단계에서는 트러스 해석처럼 회전 자유도 없이 시작할 수 있다.

---

## 6. FEM과 HEM의 철학적 차이

FEM은  
“응력을 정의하고, 그 응력을 적분하여 힘을 얻는다.”

HEM은  
“힘의 전달을 정의하고, 그 전달 관계로 구조 거동을 만든다.”

FEM은 연속체 기반,  
HEM은 이산 집합체 기반이다.

결과는 유사할 수 있으나,
힘을 정의하는 출발점과 해석을 구성하는 사고 체계는 근본적으로 다르다.

---

## 7. HEM 1단계 선언

- Seed는 유한 부피를 가진 질량 존재이다.
- 힘은 Seed 간 거리 변화에 선형 비례하는 전달량이다.
- 정역학은 각 Seed에서 전달력의 평형으로 정의된다.

---

## 8. 해석 시작 시드와 자동 분할 개념

### 8.1 초기 시드의 정의

HEM에서 해석은 무한소 요소가 아니라,  
사용자가 정의한 유한 크기의 Seed로 시작한다.

- 초기 Seed 크기는 해석 목적에 따라 사용자가 지정한다.
- 예: 1000mm 입방체, 1mm 입방체, 1μm 입방체 등
- 각 Seed는 질량과 상태(state)를 가진 독립적 존재로 취급된다.

즉, 해석의 출발점은 “무한히 작은 요소”가 아니라  
“유한 크기를 가진 기준 존재”이다.

---

### 8.2 시드 상태와 인접 관계

각 Seed는 다음 정보를 가진다.

- 위치
- 질량
- 외력
- 변위
- 인접 Seed와의 전달 관계
- 현재 전달력 값

Seed의 거동은 단독으로 결정되지 않는다.  
항상 인접 Seed와의 관계(거리 변화, 상대 상태 변화 등)에 의해 정의된다.

---

### 8.3 자동 분할(세대 진화) 개념

HEM에서는 해석 과정 중 다음 조건이 만족되면  
Seed는 더 작은 Seed로 자동 분할된다.

- 인접 Seed와의 상태 차이가 기준값을 초과하는 경우
- 거리 변화 또는 전달력 변화가 급격한 경우
- 사용자가 설정한 허용 오차를 초과하는 경우

이때:

- 기존 Seed는 부모(Parent)가 되고
- 새로 생성된 작은 Seed들은 자식(Child)이 된다.
- 자식 Seed는 부모의 상태를 초기값으로 상속받는다.

이는 미소 단위에서 거시적 단위로 확장하는 방식이 아니라,
거시적 단위 해석을 수행하다가 필요 시 더 작은 Seed로 세분화하는 해석 방식이다.

---

### 8.4 분할의 종료 조건

자동 분할은 무한히 진행되지 않는다.

- 사용자가 정의한 최소 Seed 크기에 도달하면 분할 중지
- 또는 상태 변화가 허용 오차 이하가 되면 종료

즉, 사용자가 정의한 최소 단위 크기가  
해석의 최대 세대 깊이를 결정한다.

---

### 8.5 해석의 반복 구조

1. 초기 유한 크기 Seed 생성
2. 전역 정역학 해석 수행
3. Seed 간 상태 차이 평가
4. 기준 초과 시 해당 Seed 분할
5. 새로운 Seed 구조로 재해석
6. 최소 크기 또는 허용 오차 만족 시 종료

이 과정은 단순한 메쉬 세분화가 아니라,

상태에 의해 존재가 분화되는 과정으로 정의된다.

---

> 이 문서는 샤나(GPT)의 도움으로 작성된 문서입니다
