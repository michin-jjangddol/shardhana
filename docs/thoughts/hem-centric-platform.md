# HEM-Centric Analysis Platform Concept

*(Shardhana Thoughts)*  
*Date: 2026-04-16*

---

## Purpose

Shardhana is not a single analysis program.  
It aims to be an analysis platform where multiple methods can be directly compared under identical conditions.

---

## Core Concept

Shardhana is structured as follows:

- HEM (Han Element Method) → Main Engine
- FEM (Finite Element Method) → Baseline Analysis
- AEM (Applied Element Method) → Optional Extension

---

## Core Philosophy

Shardhana does not replace any specific analysis method.  
It makes different analysis methods comparable within a single space.

HEM is the central framework that generates phenomena.  
FEM and AEM serve as reference tools for validation and comparison.

> "Not a single analysis — but a comparable analysis environment."

---

## User Goal

For the same model, the user should be able to:

- Apply identical input conditions
- Select different analysis methods (HEM / FEM / AEM)
- Compare results on the same screen

---

## Platform Structure

Shardhana is organized into three layers:

- **Input Layer** → Model definition (geometry, material, condition)
- **Analysis Layer** → Selectable analysis engines
  - HEM
  - FEM
  - AEM (future)
- **Output Layer** → Result visualization and comparison

---

## Development Strategy

### Step 1 — HEM Core Implementation
- Minimal 1D model
- Rule-based behavior generation
- Expression of phenomena such as necking and fracture

### Step 2 — FEM Reference Integration
- Reference existing FEM results
- Build comparison structure under identical conditions

### Step 3 — Unified Interface
- Analysis selection within a single GUI
- Simultaneous result comparison (multi-view)

### Step 4 — Extension
- Add AEM
- Connect multi-scale analysis
- Advanced physics models

---

## Design Principles

- Initial implementation focuses on HEM
- FEM/AEM are conceptually open, introduced incrementally
- Analysis engines remain independent from each other
- Input uses a common structure wherever possible
- Result comparison is performed in the same reference coordinate system
- Each analysis method is a "perspective", not a "replacement"
- This document defines the long-term structural direction of Shardhana

---

## One-line Definition

> Shardhana is an analysis platform centered on HEM,  
> where diverse analysis methods can be compared under identical conditions.

---

> This document was written with the help of Shana (GPT) and Laude (Claude).

---
<br>
<br>

## HEM 중심 해석 플랫폼 개념

*(Shardhana 생각창고)*
*Date: 2026-04-16*

---

## 목적

Shardhana는 단일 해석 프로그램이 아니라,
여러 해석 방법을 하나의 환경에서 비교·검토할 수 있는
해석 플랫폼(Analysis Platform)을 목표로 한다.

---

## 기본 개념

Shardhana의 구조는 다음과 같이 정의된다:

* HEM (Han Element Method) → 본체(Main Engine)
* FEM (Finite Element Method) → 기준 해석(Baseline Analysis)
* AEM (Applied Element Method) → 확장 해석(Optional Extension)

---

## 핵심 철학

Shardhana는 특정 해석 방법을 대체하는 것이 아니라,
서로 다른 해석 방법을 하나의 공간에서 비교 가능하게 만든다.

HEM은 현상을 생성하는 중심 프레임워크이며,
FEM/AEM은 검증 및 비교를 위한 참조 도구로 사용된다.

> “단일 해석이 아니라, 비교 가능한 해석 환경을 만든다.”

---

## 사용자 관점 목표

사용자는 동일한 모델에 대해:

* 동일한 입력 조건
* 서로 다른 해석 방법 선택 (HEM / FEM / AEM)
* 결과를 동일한 화면에서 비교

를 수행할 수 있어야 한다.

---

## 구조 개념

Shardhana는 다음과 같은 구조를 가진다:

* Input Layer → 모델 정의 (geometry, material, condition)

* Analysis Layer → 선택 가능한 해석 엔진

  * HEM
  * FEM
  * AEM (future)

* Output Layer → 결과 시각화 및 비교

---

## 개발 단계 전략

### Step 1 — HEM Core 구현

* 1D 최소 모델
* 상태 기반 거동 생성
* 넥킹, 파단 등 현상 표현

### Step 2 — FEM Reference 연결

* 기존 FEM 결과를 참조
* 동일 조건에서 비교 구조 구성

### Step 3 — 통합 인터페이스

* 단일 GUI에서 해석 선택
* 결과 동시 비교 (multi-view)

### Step 4 — 확장

* AEM 추가
* 다중 스케일 해석 연결
* 고급 물리 모델

---

## 설계 원칙

* 초기 구현에서는 HEM에 집중한다
* FEM/AEM은 개념적으로 열어두되, 단계적으로 도입한다
* 해석 엔진은 서로 독립적으로 유지된다
* 입력은 가능한 한 공통 구조를 사용한다
* 결과 비교는 동일 기준 좌표계에서 수행한다
* 각 해석 방법은 “대체”가 아니라 “관점”이다
* 이 문서는 Shardhana의 장기 구조 방향을 정의한다

---

## 한 줄 정의

Shardhana는 HEM을 중심으로,
다양한 해석 방법을 동일 조건에서 비교할 수 있는 분석 플랫폼이다.

---

> 이 문서는 샤나(GPT)와 로드 Laude(Claude)의 도움으로 작성되었습니다.
