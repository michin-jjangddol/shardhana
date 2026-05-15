"""
comparison package
Shardhana Comparison Layer

This package contains tools for comparing
different analysis approaches inside Shardhana.

The comparison layer is intended to evaluate:
- hand calculation
- FEM
- HEM

under the same model and boundary conditions.

The goal is not to replace one method with another,
but to observe:
- differences
- similarities
- limitations
- emergent behavior

within a shared analysis environment.

Future comparison targets may include:
- displacement
- stress
- fracture behavior
- state evolution
- probabilistic response
- visualization differences


이 패키지는 Shardhana 내부에서
서로 다른 해석 접근법을 비교하기 위한 구조를 정의한다.

비교 계층은 다음 해석 방법들을
동일 모델 및 동일 경계조건 아래에서 비교하는 것을 목표로 한다:
- 수계산
- FEM
- HEM

목표는 특정 방법을 대체하는 것이 아니라,
공통 해석 환경 안에서:
- 차이점
- 유사점
- 한계
- 생성적 거동(emergent behavior)

을 관찰하는 것이다.

향후 비교 대상에는 다음 항목들이 포함될 수 있다:
- 변위
- 응력
- 파괴 거동
- 상태 변화
- 확률 기반 응답
- 시각화 차이
"""