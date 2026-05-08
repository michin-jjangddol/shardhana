# Shardhana Research Lab (Let’s see how far it goes…)
*(Draft – Internal Operation Rule)*
**Date:** 2026-05-05

---

## 1. Purpose

Shardhana Research Lab maintains a clear separation between  
Concept → Code → Data flows,  
providing an experiment-based verification structure for HEM (Han Element Method).

---

## 2. Role Definitions

### ■ Lead Designer – 짱똘

- Sets overall direction
- Defines physical concepts and standards
- Determines experiment objectives
- Makes final decisions

👉 Core: Decides **what to verify**

---

### ■ Design Assistant – Shana (ChatGPT)

- Organizes concepts
- Structures and documents ideas
- Guides implementation direction
- Detects design errors

👉 Core: **Turns thoughts into structure**

---

### ■ Implementation – Lord Laude (Claude)

- Writes code
- Implements features
- Improves with minimal changes
- Produces executable results

👉 Core: **Turns ideas into code**

---

### ■ Validator – Gemi (Gemini)

- Analyzes CSV data
- Extracts patterns
- Verifies consistency
- Detects anomalies

👉 Core: **Judges whether results are correct**

---

### ■ Local Patch Assistant – Gico (GitHub Copilot)

- Fast file-level modifications
- Understands current repository/file context
- Executes quick patch-style fixes
- Connects code and documentation

👉 Core: **Fast local improvement** (file-oriented)

> Gico is strong at current repository/file context,
> but does not determine long-term philosophy or overall project direction.
>
> Final decisions always belong to the user.

---

## 3. Workflow

```
[Design] → [Implement] → [Run] → [Generate Data] → [Validate]
    ↓            ↓          ↓            ↓               ↓
  짱똘     Laude / Gico    짱똘          CSV             Gemi
  Shana
```

> Shana assists at the design stage — not an implementer, but a design collaborator.

---

## 4. Operating Principles

1. **Separate concept from verification**
   - Judge by data, not by feeling

2. **Keep code changes minimal**
   - No full rewrites
   - Patch-style only

3. **Data is not pushed to Git**
   - CSV files managed locally

4. **Validation must be format-based**
   - No impressions
   - Results only

5. **Validation output must follow a defined format**
   - failure_step
   - consistency
   - pattern
   - anomaly

---

## 5. Current Status

- v3d: CSV logging complete
- Status: Experiment phase initiated

---

## 6. Future Direction

- Accumulate multi-run data
- Pattern analysis
- HEM internal consistency verification

---

This document defines the internal operating standards of Shardhana Research Lab.  
All future development and experimentation shall follow this structure.

---

> This document was prepared with the assistance of Shana (GPT) and Laude (Claude).


---
<br>
<br>

# 샤드하나 연구소 (어디까지 갈 수 있을지…)
*(Draft – Internal Operation Rule)*
**Date:** 2026-05-05

---

## 1. 목적

Shardhana Research Lab은 개념(Concept) → 구현(Code) → 검증(Data)의 흐름을 명확히 분리하여  
HEM(Han Element Method)을 실험 기반으로 검증하는 구조를 갖는다.

---

## 2. 역할 정의

### ■ 설계자 – 짱똘

- 전체 방향 설정
- 물리 개념 및 기준 정의
- 실험 목표 결정
- 최종 판단

👉 핵심: **무엇을 검증할 것인가**를 결정하는 역할

---

### ■ 보조 설계자 – 샤나 (ChatGPT)

- 개념 정리
- 구조화 및 문서화
- 구현 방향 가이드
- 설계 오류 감지

👉 핵심: **생각을 구조로 바꾸는** 역할

---

### ■ 구현 담당 – 로드 (Laude / Claude)

- 코드 작성
- 기능 구현
- 최소 수정 기반 개선
- 실행 가능한 결과 생성

👉 핵심: **아이디어를 코드로 만드는** 역할

---

### ■ 검증관 – 제미 (Gemi / Gemini)

- CSV 데이터 분석
- 패턴 추출
- 일관성 검증
- 이상치 탐지

👉 핵심: **결과가 맞는지 판단하는** 역할

---

### ■ 현장 패치 담당 – 기코 (Gico / GitHub Copilot)

- 빠른 파일 단위 수정
- 현재 저장소/파일 문맥 파악
- 신속한 patch 기반 수정
- 코드와 문서 연결

👉 핵심: **빠른 현장 개선** (파일 중심)

> 기코는 현재 파일/저장소 문맥에는 강하지만,
> 장기 철학 및 전체 방향 판단은 하지 않는다.
>
> 최종 결정권은 항상 사용자에게 있다.

---

## 3. 작업 흐름 (Workflow)

```
[설계] → [구현] → [실행] → [데이터 생성] → [검증]
   ↓          ↓         ↓         ↓           ↓
 짱똘     로드 / 기코   짱똘      CSV         제미
 샤나
```

> 샤나는 설계 단계 보조 — 구현 담당이 아닌 방향 설계자

---

## 4. 운영 원칙

1. **개념과 검증을 분리한다**
   - 느낌이 아닌 데이터로 판단

2. **코드는 최소 변경으로 진행한다**
   - 전체 수정 금지
   - patch 방식 유지

3. **데이터는 Git에 올리지 않는다**
   - CSV는 로컬 관리

4. **검증은 형식 기반으로 수행한다**
   - 감상 금지
   - 결과 중심

5. **검증 결과는 반드시 정해진 형식으로 출력한다**
   - failure_step
   - consistency
   - pattern
   - anomaly

---

## 5. 현재 단계

- v3d: CSV logging 완료
- 상태: 실험 단계 진입

---

## 6. 향후 방향

- 다회 실행 데이터 확보
- 패턴 분석
- HEM 내부 일관성 검증

---

이 문서는 Shardhana Research Lab의 내부 운영 기준을 정의하며,  
이후 모든 개발 및 실험은 본 구조를 따른다.

---

> 이 문서는 샤나(GPT)와 로드(Claude)의 도움으로 작성되었습니다.