"""
io package
Shardhana Input/Output Layer

This package contains the data input/output layer
used throughout the Shardhana platform.

The io layer is responsible for:
- model input
- file loading
- file saving
- result export
- simulation logging
- data serialization

The goal of this layer is to provide
a stable and extensible interface
between:
- user input
- solvers
- visualization
- external tools

Possible future formats may include:
- CSV
- JSON
- structured logging
- visualization data
- external application interfaces

This layer is expected to become
one of the major connection gateways
inside the Shardhana ecosystem.


이 패키지는 Shardhana 플랫폼에서 사용하는
입력/출력 계층(io layer)을 정의한다.

io 계층은 다음 역할을 담당한다:
- 모델 입력
- 파일 불러오기
- 파일 저장
- 결과 내보내기
- 시뮬레이션 로그 기록
- 데이터 직렬화

이 계층의 목표는 다음 구성 요소 사이의
안정적이고 확장 가능한 연결 인터페이스를 제공하는 것이다:
- 사용자 입력
- solver
- 시각화
- 외부 도구

향후 지원 가능한 형식에는 다음이 포함될 수 있다:
- CSV
- JSON
- 구조화 로그
- 시각화 데이터
- 외부 프로그램 인터페이스

이 계층은 앞으로
Shardhana 생태계 내부의 주요 연결 관문 중 하나가 될 예정이다.
"""