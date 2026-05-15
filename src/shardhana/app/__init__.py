"""
app package
Shardhana Application Layer

This package contains the user-facing application layer
of the Shardhana platform.

The app layer is responsible for:
- application entry points
- GUI windows
- user interaction
- visualization connection
- workflow coordination
- result view selection

This layer should remain independent from
the internal solver implementation whenever possible.

The goal is to allow:
- Hand Calculation
- FEM
- HEM

to be selected, executed, visualized, and compared
within a common user environment.


이 패키지는 Shardhana 플랫폼의
사용자 응용 계층(app layer)을 정의한다.

app 계층은 다음 역할을 담당한다:
- 프로그램 실행 진입점
- GUI 창 구성
- 사용자 상호작용
- 시각화 연결
- 작업 흐름 제어
- 결과 보기 선택

이 계층은 가능한 한
내부 solver 구현과 분리된 상태를 유지한다.

목표는:
- 수계산
- FEM
- HEM

결과를 사용자가 선택하고,
실행하고,
시각화하고,
비교할 수 있는 공통 사용자 환경을 만드는 것이다.
"""