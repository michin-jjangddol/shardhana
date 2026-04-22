# Shardhana Input Philosophy
*Input & State History Design | Date: 2026-04-22*

---

## 1. Purpose

In most existing analysis programs, an input file represents a single point in time.
Shardhana, however, is built around state changes and relationship changes as its core.

Therefore, the input file in Shardhana is not simply a static bundle of values —
it aims to be a structure capable of managing the flow of states that change over time.

---

## 2. Core Idea

In Shardhana, analysis is understood as follows:

- Not a process of throwing one complete input file and being done
- But starting from an initial state
- Where state changes accumulate
- Where returning to a specific point in time is possible when needed
- And where analysis can continue in a different direction

In other words, the input is not a fixed document separate from the result —
it becomes the starting point of a state history.

---

## 3. Core Principles

### 3.1 An input file is not "a single file" but "a flow of states"

Shardhana extends the concept of input to include:

- Initial model definition
- Analysis conditions
- State change records
- Relationship change records
- Checkpoints for rollback when needed

---

### 3.2 Saves must include messages, not just timestamps

A timestamp alone makes it difficult to understand
why something was saved or what changed.

Therefore, each checkpoint should carry the following:

- Save time
- Save message
- Key changes made
- Difference from the previous state

Examples:

- initial seed state definition
- start of interaction between neighboring seeds
- deformation accumulation stage
- onset of contact-face reduction
- state just before relation break

---

### 3.3 Returning to a past state is part of the analysis process

During analysis, situations like the following often arise:

- State becomes tangled
- Break condition is too aggressive
- Relationship update behaves abnormally
- Need to re-run from a specific point

Shardhana treats these not as exceptions,
but as a natural part of the analysis process.

---

## 4. Target Structure

Long-term, the Shardhana input system may aim for a structure like this:

```text
model/
├─ initial_state.json
├─ history/
│  ├─ step_0001.json
│  ├─ step_0002.json
│  ├─ step_0003.json
│  └─ ...
└─ messages/
   ├─ step_0001.txt
   ├─ step_0002.txt
   └─ ...
```

Alternatively, the history structure may be embedded within a single file.

What matters is not the file format itself —
but the philosophy of managing state changes and save messages together.

---

## 5. Similarity to Git

Just as Git tracks changes in code,
Shardhana tracks changes in analysis state.
Both arise from the same structural way of thinking.

- Save the current state
- Review past states
- Return to a specific point in time
- Record the reason for each change
- Continue in a different direction

Git manages code.
Shardhana manages analysis models and state flow.
The purpose is different, but the way of seeing the problem is the same.

---

## 6. One-line Definition

The input file in Shardhana is not a static input document —
it aims to be an analysis record system that carries both the flow of state changes and the possibility of rollback.

---

*This document serves as a reference standard for designing Shardhana's input file and state management system.*

---

> This document was prepared with the assistance of Shana (GPT) and Laude (Claude).

---
<br>
<br>


# 샤드하나 입력파일 방향성
입력파일과 상태 이력 관리 방향성 | 작성일: 2026-04-22

---

## 1. 목적

기존 해석 프로그램의 입력파일은 대체로 하나의 시점만 표현한다.  
하지만 샤드하나는 상태 변화와 관계 변화를 핵심으로 다루는 구조를 지향한다.

따라서 샤드하나의 입력파일은 단순한 정적 입력값 묶음이 아니라,  
시간에 따라 변화하는 상태의 흐름을 관리할 수 있는 구조를 목표로 한다.

---

## 2. 기본 생각

샤드하나에서 해석은 다음과 같이 본다.

- 하나의 완성된 입력파일을 던지고 끝나는 방식이 아니라
- 초기 상태에서 출발하여
- 상태 변화가 누적되고
- 필요하면 특정 시점으로 돌아가고
- 다른 방향으로 다시 진행할 수 있는 방식

즉, 입력은 결과와 분리된 고정 문서가 아니라  
상태 이력의 시작점이 된다.

---

## 3. 핵심 원칙

### 3.1 입력파일은 “한 장의 파일”이 아니라 “상태의 흐름”이다

샤드하나는 입력을 다음과 같이 확장해서 본다.

- 초기 모델 정의
- 해석 조건
- 상태 변화 기록
- 관계 변화 기록
- 필요 시 복귀 가능한 저장점

---

### 3.2 저장은 날짜뿐 아니라 메시지를 포함해야 한다

단순 날짜 저장만으로는  
왜 저장했는지, 어떤 변화가 있었는지 파악하기 어렵다.

따라서 각 저장점에는 다음 정보가 함께 남아야 한다.

- 저장 시각
- 저장 메시지
- 주요 변경 내용
- 이전 상태와의 차이

예:

- 초기 시드 상태 정의
- 인접 시드 간 상호작용 시작
- 변형 누적 단계
- 접촉면 감소 시작
- 관계 단절 직전 상태

---

### 3.3 과거 상태 복귀는 해석 흐름의 일부다

해석 중에는 종종 다음과 같은 상황이 생긴다.

- 상태가 꼬임
- 파단 조건이 과도함
- 관계 업데이트가 비정상적임
- 특정 시점부터 다시 실험하고 싶음

샤드하나는 이런 상황을 예외가 아니라  
자연스러운 해석 과정의 일부로 본다.

---

## 4. 지향 구조

샤드하나 입력 시스템은 장기적으로 다음과 같은 구조를 지향할 수 있다.

```text
model/
├─ initial_state.json
├─ history/
│  ├─ step_0001.json
│  ├─ step_0002.json
│  ├─ step_0003.json
│  └─ ...
└─ messages/
   ├─ step_0001.txt
   ├─ step_0002.txt
   └─ ...
```

또는 하나의 파일 안에 이력 구조를 포함하는 방식도 가능하다.

핵심은 파일 형식 자체보다  
상태 변화와 저장 메시지를 함께 관리하는 철학이다.

---

## 5. Git과의 유사성

Git이 코드의 변화를 추적하듯,  
샤드하나는 해석 상태의 변화를 추적한다.  
둘은 같은 구조적 사고에서 출발한다.

- 현재 상태 저장
- 과거 상태 열람
- 특정 시점 복귀
- 변경 이유 기록
- 다른 방향으로 다시 진행

다만 Git은 코드를 관리하고,  
샤드하나는 해석 모델과 상태 흐름을 관리한다.  
목적은 다르지만, 문제를 보는 방식은 같다.

---

## 6. 한 줄 정의

샤드하나의 입력파일은 단순한 정적 입력 문서가 아니라,  
상태 변화의 흐름과 복귀 가능성을 함께 담는 해석 기록 시스템을 지향한다.

---

이 문서는 샤드하나의 입력파일 및 상태 저장 시스템 설계 시 참고 기준으로 사용한다.

---

> 이 문서는 샤나(GPT)와 로드(Claude)의 도움으로 작성되었습니다.