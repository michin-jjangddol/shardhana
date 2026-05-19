> Location: `docs/guide/io-file-guidelines.md`

<br>

# Input and Output File Guidelines

---

## Purpose

Shardhana is not simply a GUI application.  
It aims to be a structural analysis platform  
that people, AI, APIs, and programs can all understand and modify together.

Input and output files are not merely storage formats.  
They are the **Source of Truth** for every analysis —  
a record that connects the past to the present.

---

## Core Philosophy

### 1. Text-First

All input and output data in Shardhana  
is based on human-readable, human-editable text formats.

The GUI is not a layer that hides the original data.  
It is an interface for viewing and editing the text source more easily.

```text
TXT file = original source
GUI = viewer / editor
```

---

### 2. GUI ↔ TXT One-to-One Relationship

Changes made in the GUI must be immediately reflected in the text file.  
Edits made directly to the text file must be readable by the GUI without loss.

API tools and AI agents must also be able to read and modify the same files directly.

```text
GUI
API
AI
Human
→ shared source file
```

---

### 3. Preserve the Past

Users must be able to reopen any past input or result file at any time  
and compare it with current results.

Even as versions change,  
past text files should remain readable wherever possible.

```text
Past input + past result
vs
Current input + current result
```

---

### 4. Binary Is Cache

Binary or cache data may be used internally  
for performance and memory optimization.

But binary data is never the source.  
It must always be regenerable from the text-based source file.

```text
Text file = source
Binary = runtime cache
```

---

### 5. Human-Centered Structure

The structure prioritizes what people can understand and verify,  
not what is convenient for the computer.

Input and output files should remain  
as readable, comparable, and traceable as possible.

---

## File Extension Direction

Shardhana uses a role-based file extension structure.

Initial candidates:

```text
.shi   = Shardhana Input
.sho   = Shardhana Output
.shl   = Shardhana Log
```

Extensions may be revised and expanded as the project grows.

---

## Version Information

Input and output files should include the following where possible:

```text
format_version
engine_version
solver_version
created_time
```

These are essential references for result reproduction and comparison.

---

## The One Seed Principle

One Seed is a small example —  
but it is developed in the same direction as the final Shardhana architecture.

Features may be minimal,  
but the structural philosophy must match the full vision.

```text
small feature
same architecture philosophy
```

---

## Future Direction

As Shardhana grows, the same input and output philosophy  
will be maintained across all environments:

- GUI
- CLI
- API
- AI Agent
- Automation Pipeline
- MCP / External Tools

All tools are encouraged to share the same text-based source file whenever practical.

---

*This document was prepared with the assistance of Shana (GPT) and Laude (Claude).*

---
<br>
<br>

# 입출력 파일 지침서

---

## 목적

Shardhana는 단순 GUI 프로그램이 아니라,
사람·AI·API·프로그램이 함께 이해하고 수정 가능한
구조해석 플랫폼을 목표로 한다.

입출력 파일은 단순 저장 형식이 아니라,
해석의 원본(Source of Truth)이며,
과거와 현재를 연결하는 기록이다.

---

## 핵심 철학

### 1. 텍스트 원본 우선

Shardhana의 입력 및 출력 데이터는
사람이 직접 읽고 수정 가능한 텍스트 형식을 기본으로 한다.

GUI는 원본 데이터를 숨기는 존재가 아니라,
텍스트 원본을 쉽게 보고 수정하기 위한 인터페이스이다.

```text
TXT file = original source
GUI = viewer / editor
```

---

### 2. GUI ↔ TXT 1:1 관계

GUI에서 수정한 내용은 즉시 텍스트 파일에 반영될 수 있어야 하며,
텍스트 파일을 직접 수정해도 GUI에서 동일하게 읽을 수 있어야 한다.

또한 API 및 AI 도구도 동일한 파일을 직접 수정 가능해야 한다.

```text
GUI
API
AI
Human
→ same source file
```

---

### 3. 과거 기록 보존

사용자는 언제든지 과거 입력 파일과 결과 파일을 다시 열고,
현재 결과와 비교할 수 있어야 한다.

버전이 변경되더라도 가능한 한
과거 텍스트 파일을 읽을 수 있도록 유지한다.

```text
Past input + past result
vs
Current input + current result
```

---

### 4. 바이너리는 캐시

빠른 계산 및 메모리 최적화를 위해
내부적으로 binary/cache 데이터를 사용할 수 있다.

하지만 binary 데이터는 원본이 아니며,
항상 텍스트 기반 원본 파일로부터 재생성 가능해야 한다.

```text
Text file = source
Binary = runtime cache
```

---

### 5. 사람 중심 구조

컴퓨터의 편의보다,
사람이 이해하고 검증할 수 있는 구조를 우선한다.

입출력 파일은 가능한 한
읽기 쉽고 비교 가능하며 추적 가능한 형태를 유지한다.

---

## 파일 확장자 방향

Shardhana는 역할 기반 확장자 구조를 지향한다.

초기 후보 예시:

```text
.shi   = Shardhana Input
.sho   = Shardhana Output
.shl   = Shardhana Log
```

확장자는 프로젝트 성장에 따라 수정 및 보완될 수 있다.

---

## 버전 정보

입출력 파일에는 가능한 한 다음 정보를 포함한다.

```text
format_version
engine_version
solver_version
created_time
```

이는 결과 재현 및 비교를 위한 중요한 기준이다.

---

## One Seed 원칙

One Seed는 작은 예제이지만,
최종 Shardhana 구조와 동일한 방향으로 개발한다.

기능은 작을 수 있지만,
구조 철학은 완성형과 동일해야 한다.

```text
small feature
same architecture philosophy
```

---

## 향후 방향

향후 Shardhana는 다음 환경에서도
동일한 입출력 철학을 유지한다.

- GUI
- CLI
- API
- AI Agent
- Automation Pipeline
- MCP / External Tools

모든 도구는 가능한 한
동일한 텍스트 원본 파일을 공유하는 방향을 지향한다.

---

*이 문서는 샤나(GPT)와 로드(Claude)의 도움으로 작성되었습니다.*
