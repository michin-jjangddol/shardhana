# Shardhana Development Vision
*Core Philosophy & Architecture | Date: 2026-04-21*

---

## 1. Purpose

Shardhana is a structural analysis engine that does not depend on the cloud.

- Runs on a personal PC
- Works without internet access
- Users have full control over their data
- Extensible only when needed — not by default

---

## 2. Core Principle

**Local-first, Cloud-optional**

The default is local execution.
The cloud is an option, not a prerequisite.

---

## 3. Architecture

### 3.1 Local Core (Required)

The core engine must satisfy the following:

- Perform structural analysis locally
- Implement core concepts of HEM / FEM
- Support debugging and visualization
- Run on low-spec environments

This is the body of Shardhana.

---

### 3.2 Cloud Extension (Optional)

The cloud is used only in the following cases:

- Large-scale analysis
- High-performance computation
- Parallel processing
- Remote execution

The cloud does not replace the core.
It is simply a tool that extends its capabilities.

---

### 3.3 System Structure

```
Shardhana
├─ core/        # Local analysis engine (required)
├─ solver/      # Analysis logic
├─ plugins/     # Extended features
└─ cloud/       # Optional remote execution
```

This structure is designed to protect the local core while keeping extensions separate.

---

## 4. Philosophy

Modern software is moving toward subscription-based pricing, cloud dependency, and reduced user control.
Shardhana deliberately takes a different path.

> Shardhana is a tool, not a service.

---

## 5. Long-term Vision

- Centered on a stable local core
- Extensible through a plugin-based architecture
- Execution mode is selectable: Local by default, Cloud when needed

---

## 6. One-line Definition

Shardhana is a structural analysis platform that is complete locally, with the cloud used only when necessary.

---

*This document serves as the design standard for Shardhana.
All future feature additions and structural changes shall be evaluated against these principles.*

---

> This document was prepared with the assistance of Shana (GPT) and Laude (Claude).

<br>
<br>

# 샤드하나 개발 방향성  
핵심 철학 및 구조 | 작성일: 2026-04-21

---

## 1. 목적

샤드하나는 클라우드에 종속되지 않는 구조해석 엔진이다.

- 개인 PC에서 실행 가능
- 인터넷 없이 동작
- 사용자가 데이터를 완전히 통제
- 필요할 때만 확장 — 의존하지 않음

---

## 2. 핵심 원칙

**Local-first, Cloud-optional**

기본은 로컬 실행이다.  
클라우드는 선택지이지, 전제 조건이 아니다.

---

## 3. 설계 방향

### 3.1 로컬 코어 (필수)

코어 엔진의 조건:

- 로컬에서 구조해석 수행
- HEM / FEM 기본 개념 구현
- 디버깅 및 시각화 가능
- 저사양 환경에서도 동작

이것이 샤드하나의 본체다.

---

### 3.2 클라우드 확장 (선택)

클라우드는 다음 상황에서만 쓴다:

- 대형 해석
- 고성능 계산
- 병렬 처리
- 원격 실행

클라우드는 코어를 대체하지 않는다.  
능력을 확장하는 도구일 뿐이다.

---

### 3.3 시스템 구조

```
Shardhana

├─ core/        # 로컬 해석 엔진 (필수)
├─ solver/      # 해석 로직
├─ plugins/     # 확장 기능
└─ cloud/       # 선택적 원격 실행
```

이 구조는 로컬 코어를 보호하면서 확장을 분리하기 위한 것이다.

---

## 4. 철학

현대 소프트웨어는 구독 과금, 클라우드 의존, 사용자 통제 약화 쪽으로 흘러가고 있다.  
Shardhana는 반대 방향을 선택한다.

> 샤드하나는 서비스가 아니라 도구다.

---

## 5. 장기 비전

- 안정적인 로컬 코어를 중심으로
- 플러그인을 통해 기능을 확장하고
- 실행 방식은 Local에서 Cloud로 선택적으로 확장된다

---

## 6. 한 줄 정의

샤드하나는 로컬에서 완성되고, 클라우드는 필요할 때만 쓰는 구조해석 플랫폼이다.

---

이 문서는 Shardhana의 설계 기준으로 사용되며,  
향후 모든 기능 추가 및 구조 변경은 이 원칙을 기준으로 판단한다.

---

> 이 문서는 샤나(GPT)와 로드 Laude(Claude)의 도움으로 작성되었습니다.