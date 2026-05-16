"""
core package
Shardhana Core Engine Layer

This package contains the fundamental engine systems
used inside the Shardhana platform.

The core layer is responsible for:
- state evolution
- relation dynamics
- interaction processing
- time progression
- damage/fracture behavior
- engine/kernel execution

The core layer is NOT intended to define:
- GUI systems
- visualization logic
- project storage
- input/output handling

In Shardhana:

model
= analysis input and structural configuration

core
= dynamic engine where state, relation,
time, and behavior evolve

The core structure is designed to remain:
- modular
- extensible
- engine-oriented
- method-independent

Future systems may include:
- HEM engine
- FEM-compatible structures
- probabilistic state systems
- emergent interaction models


이 패키지는 Shardhana 플랫폼 내부에서 사용하는
핵심 엔진 시스템(core engine layer)을 정의한다.

core 계층은 다음 역할을 담당한다:
- 상태 변화(state evolution)
- 관계 동역학(relation dynamics)
- 상호작용 처리(interaction processing)
- 시간 흐름(time progression)
- 손상/파괴 거동
- 엔진 및 커널 실행

core 계층은 다음 항목을 담당하지 않는다:
- GUI 시스템
- 시각화 로직
- 프로젝트 저장
- 입출력 처리

Shardhana에서:

model
= 해석 입력 및 구조 구성 정보

core
= 상태·관계·시간·거동 변화가 실제로 발생하는 동적 엔진 계층

core 구조는 다음 원칙을 유지한다:
- 모듈 구조
- 확장 가능성
- 엔진 중심 설계
- 해석 방법 독립성

향후 다음 시스템들이 포함될 수 있다:
- HEM 엔진
- FEM 호환 구조
- 확률 기반 상태 시스템
- 생성적 상호작용 모델
"""