"""
results package
Shardhana Result Layer

This package contains structures related to
analysis results generated inside Shardhana.

The results layer is intended to manage:
- solver outputs
- displacement results
- stress results
- state evolution
- fracture behavior
- simulation history
- comparison-ready data

The goal is to provide a common result structure
that can be shared across:
- hand calculation
- FEM
- HEM

This layer may later support:
- visualization-ready datasets
- logging systems
- statistical analysis
- probabilistic response tracking
- time-history simulation outputs

The results layer should remain:
- solver-independent
- lightweight
- extensible
- comparison-oriented


이 패키지는 Shardhana 내부에서 생성되는
해석 결과 구조를 정의한다.

results 계층은 다음 항목들을 관리하는 것을 목표로 한다:
- solver 출력 결과
- 변위 결과
- 응력 결과
- 상태 변화
- 파괴 거동
- 시뮬레이션 이력
- 비교 가능한 데이터 구조

이 계층의 목적은:
- 수계산
- FEM
- HEM

사이에서 공통으로 사용할 수 있는
결과 구조를 제공하는 것이다.

향후 이 계층은 다음 기능들을 지원할 수 있다:
- 시각화용 데이터셋
- 로그 시스템
- 통계 분석
- 확률 기반 응답 추적
- 시간이력 시뮬레이션 출력

results 계층은 다음 원칙을 유지한다:
- solver 독립성
- 경량 구조
- 확장 가능성
- 비교 중심 구조
"""