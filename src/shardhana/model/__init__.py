"""
model package
Shardhana Analysis Model Layer

This package defines the common analysis model structure
used throughout the Shardhana platform.

The model layer represents the analysis target itself,
independent from specific solver implementations.

This layer may contain:
- geometry
- nodes
- supports
- loads
- boundary conditions
- seeds
- spaces
- states
- relations

The purpose of this structure is to allow:
- hand calculation
- FEM
- HEM

to share the same analysis model
under a unified environment.

In Shardhana,
the model layer is intended to become
a bridge between:
- user input
- solver engines
- visualization
- comparison systems

This layer should remain:
- solver-independent
- extensible
- lightweight
- structurally clear


이 패키지는 Shardhana 플랫폼에서 사용하는
공통 해석 모델 구조를 정의한다.

model 계층은 특정 solver 구현과 독립적으로,
해석 대상 자체를 표현하는 역할을 담당한다.

이 계층에는 다음 개념들이 포함될 수 있다:
- 형상 정보
- 절점(node)
- 지점 조건
- 하중
- 경계 조건
- seed
- space
- state
- relation

이 구조의 목적은:
- 수계산
- FEM
- HEM

이 동일한 해석 모델을 공유할 수 있도록 하는 것이다.

Shardhana에서 model 계층은:
- 사용자 입력
- solver 엔진
- 시각화
- 비교 시스템

사이를 연결하는 핵심 구조가 되는 것을 목표로 한다.

이 계층은 다음 원칙을 유지한다:
- solver 독립성
- 확장 가능성
- 경량 구조
- 명확한 구조성
"""