# Units – Distance and Scale Domains

Shardhana considers how to define and connect **distance**
between different physical worlds,
ranging from the atomic scale to the cosmic scale.

This document is not a simple unit conversion table.
It records the design philosophy of Shardhana regarding
**the separation and connection of scale domains**.

---

## 0. Distinction Between Length and Distance

In Shardhana, **length** and **distance** are treated as distinct concepts.

### Length
- An intrinsic geometric property of an object or element
- A value attached to the object itself
- Examples:
  - Element length
  - Member length
  - Crack length
- Primary usage:
  - Geometry definition
  - Element properties
  - Reference for stiffness calculation

### Distance
- The separation between two positions
- A relational value defined by positions
- May change depending on state or deformation
- Examples:
  - Distance between two nodes
  - Distance before and after deformation
  - Distance between planets or stars

**This document focuses on distance, not length.**  
It defines the separation between different worlds and scales,
rather than the size of objects.

---

## 1. Concept of Scale Domains

Shardhana does not enforce a single distance unit for all analyses.
Instead, it defines meaningful **scale domains** for different physical worlds.

Each scale domain has:
- A representative distance unit intuitive to humans
- An approximate conversion to meters (m)
- Explicit conversion rules when connecting to other domains

---

## 2. Distance Definition by Scale Domain

### (1) Atomic / Microscopic Scale
- Representative units: Å, nm
- Approximate distances:
  - 1 Å ≈ 1.0 × 10⁻¹⁰ m  
  - 1 nm ≈ 1.0 × 10⁻⁹ m
- Meaning:
  - Material microstructure
  - Theoretical background of fracture mechanisms

---

### (2) Mechanical / Component Scale
- Representative unit: mm
- Approximate distance:
  - 1 mm = 1.0 × 10⁻³ m
- Meaning:
  - Cross-sections
  - Connections and local behavior
  - Structural details

---

### (3) Architectural / Structural Scale  
**(Base Domain of Shardhana)**
- Representative unit: m
- Approximate distance:
  - 1 m = 1.0 × 10⁰ m
- Meaning:
  - Buildings
  - Structural systems
  - AEM-based structural analysis
- **Shardhana starts from this scale**

---

### (4) Civil / Geotechnical / Urban Scale
- Representative units: m, km
- Approximate distance:
  - 1 km = 1.0 × 10³ m
- Meaning:
  - Bridges, tunnels
  - Ground and site-scale structures

---

### (5) Solar System Scale
- Representative unit: AU (Astronomical Unit)
- Approximate distance:
  - 1 AU ≈ 1.496 × 10¹¹ m
- Meaning:
  - Planetary orbits
  - Solar system dynamics

---

### (6) Stellar / Galactic Scale
- Representative units: light-year (ly), parsec
- Approximate distances:
  - 1 light-year ≈ 9.46 × 10¹⁵ m
  - 1 parsec ≈ 3.09 × 10¹⁶ m
- Meaning:
  - Interstellar distances
  - Galactic structures

---

## 3. Principles for Connecting Scale Domains

- Different scale domains are never mixed implicitly
- Transition between domains always requires **explicit distance conversion**
- Distance conversion is treated as a semantic transition,
  not merely a numerical operation

---

## Supplement: Definition of 1 Meter in the SI System

In the modern SI system, one meter (m) is not defined by a physical object,
but by a fundamental constant of nature.

- One meter is defined as  
  **the distance traveled by light in vacuum during
  1 / 299,792,458 of a second.**

Thus, the meter is:
- Not a measuring tool
- A distance fixed by time and the speed of light
- A universally agreed reference for distance

Reference:
- BIPM – SI definition of the meter  
  https://www.bipm.org/en/measurement-units/si-definitions/meter

---

## 4. Declaration of Shardhana

- Shardhana v0.x adopts the
  **architectural / structural scale (meter)** as its base domain
- The internal reference distance unit is **meter (m)**
- Other scale domains are conceptually open,
  but not directly connected in early implementations

---

## Notes
- Distance connects worlds
- Length will be treated separately in geometry and element documents
- This document serves as the distance worldview declaration of Shardhana

---

---

# 단위 – 거리와 스케일 도메인

Shardhana는  
원자 수준부터 우주 스케일까지,  
서로 다른 물리 세계 사이의 **거리(distance)** 를 어떻게 정의하고  
어떻게 연결할 것인가를 고민하는 프로젝트이다.

이 문서는 단순한 단위 환산표가 아니라,  
Shardhana가 다루는 **세계와 세계 사이의 간격**에 대한  
설계 철학을 기록한 문서이다.

---

## 0. Length와 Distance의 구분

Shardhana에서는 **Length(길이)** 와 **Distance(거리)** 를  
서로 다른 개념으로 명확히 구분한다.

### Length (길이)
- 물체나 요소가 가지는 **고유한 기하학적 속성**
- 대상(object)에 붙어 있는 값
- 예:
  - 부재 길이
  - 요소 길이
  - 균열 길이
- 주요 용도:
  - 요소 정의
  - 기하 속성
  - 강성 계산의 기준

### Distance (거리)
- 두 위치 사이의 **떨어진 정도**
- 관계(relationship)에 의해 정의되는 값
- 상태에 따라 변할 수 있음
- 예:
  - 두 노드 사이의 거리
  - 변형 전·후 위치 간 거리
  - 행성, 항성, 은하 사이의 거리

**이 문서는 Length가 아니라 Distance를 다룬다.**  
즉, 물체의 크기가 아니라  
**서로 다른 세계와 스케일 사이의 간격**을 정의한다.

---

## 1. 스케일 도메인 개념

모든 해석을 하나의 거리 단위로 강제하지 않는다.  
대신, 의미 있는 물리 세계별로 **스케일 도메인(scale domain)** 을 정의한다.

각 스케일 도메인은 다음을 가진다.

- 사람이 직관적으로 사용하는 대표 거리 단위
- 미터(m)를 기준으로 한 근사 환산값
- 다른 도메인과의 연결은 **명시적인 단위 변환**을 통해서만 수행

---

## 2. 스케일 도메인별 거리 정의

### (1) 원자 / 미시 스케일
- 대표 단위: Å, nm
- 거리 근사치:
  - 1 Å ≈ 1.0 × 10⁻¹⁰ m  
  - 1 nm ≈ 1.0 × 10⁻⁹ m
- 적용 의미:
  - 재료 미시 구조
  - 파괴 메커니즘의 이론적 배경

---

### (2) 기계 / 부재 스케일
- 대표 단위: mm
- 거리 근사치:
  - 1 mm = 1.0 × 10⁻³ m
- 적용 의미:
  - 단면 치수
  - 접합부, 국부 거동
  - 구조 요소 상세

---

### (3) 건축 / 구조 스케일  **(Shardhana 기본 도메인)**
- 대표 단위: m
- 거리 근사치:
  - 1 m = 1.0 × 10⁰ m
- 적용 의미:
  - 건축물
  - 구조 시스템
  - AEM 기반 구조 해석
- **Shardhana는 이 스케일을 출발점으로 삼는다**

---

### (4) 토목 / 지반 / 도시 스케일
- 대표 단위: m, km
- 거리 근사치:
  - 1 km = 1.0 × 10³ m
- 적용 의미:
  - 교량, 터널
  - 지반, 단지 규모 구조물

---

### (5) 태양계 스케일
- 대표 단위: AU (Astronomical Unit)
- 거리 근사치:
  - 1 AU ≈ 1.496 × 10¹¹ m
- 적용 의미:
  - 행성 궤도
  - 태양계 동역학

---

### (6) 항성 / 은하 스케일
- 대표 단위: light-year (ly), parsec
- 거리 근사치:
  - 1 light-year ≈ 9.46 × 10¹⁵ m
  - 1 parsec ≈ 3.09 × 10¹⁶ m
- 적용 의미:
  - 항성 간 거리
  - 은하 구조

---

## 3. 스케일 간 연결 원칙

- 서로 다른 스케일 도메인은 자동으로 섞이지 않는다
- 도메인 간 이동은 항상 **명시적인 거리 변환**을 거친다
- 거리 변환은 단순 환산이 아니라,
  해석 세계가 바뀌는 **의미적 이동**으로 간주한다

---

## 보충: 현대 SI 단위계에서의 1 m 정의

현재 인류가 정의한 1 미터(m)는  
물리적 막대가 아니라 자연 상수에 기반한 정의이다.

- 1 m는  
  **진공에서 빛이 1 / 299,792,458 초 동안 이동한 거리**로 정의된다.

즉, 미터는:
- 측정 도구가 아니라
- 시간과 빛의 속도에 의해 고정된 거리 기준이며
- 인류가 합의한 가장 보편적인 기준 거리이다.

참고:
- BIPM (국제도량형국) SI 미터 정의  
  https://www.bipm.org/en/measurement-units/si-definitions/meter

---

## 4. Shardhana의 선언

- Shardhana v0.x는  
  **건축 / 구조 스케일(m)** 을 기본 거리 도메인으로 시작한다
- 내부 계산의 기준 거리 단위는 **미터(m)** 이다
- 다른 스케일 도메인은  
  개념적으로 열어 두되,  
  초기 구현에서는 직접 연결하지 않는다

---

## 메모
- Distance는 세계와 세계를 잇는 개념
- Length는 이후 요소/기하 문서에서 별도로 다룬다
- 이 문서는 Shardhana의 거리 세계관 선언문이다