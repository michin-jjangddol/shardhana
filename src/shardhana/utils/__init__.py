"""
utils package
Shardhana Utility Layer

This package contains shared utility tools
used throughout the Shardhana platform.

The utils layer is intended to provide:
- reusable helper functions
- mathematical utilities
- logging helpers
- formatting tools
- file utilities
- conversion utilities
- lightweight support systems

The purpose of this package is to prevent:
- duplicated code
- unnecessary dependency coupling
- oversized core modules

Utilities inside this layer should remain:
- simple
- reusable
- lightweight
- solver-independent

Possible future utilities may include:
- unit conversion
- vector operations
- timing tools
- logging systems
- CSV/JSON helpers
- ID generators
- debugging helpers

In Shardhana,
the utils layer acts as a shared toolbox
supporting the overall ecosystem.


이 패키지는 Shardhana 플랫폼 전체에서 사용하는
공용 유틸리티 도구들을 정의한다.

utils 계층은 다음 기능들을 제공하는 것을 목표로 한다:
- 재사용 가능한 보조 함수
- 수학 유틸리티
- 로그 보조 기능
- 형식 처리 도구
- 파일 처리 도구
- 변환 유틸리티
- 경량 지원 시스템

이 패키지의 목적은 다음 문제들을 줄이는 것이다:
- 중복 코드
- 불필요한 의존성 결합
- 비대해진 core 모듈

utils 계층 내부 도구들은 다음 원칙을 유지한다:
- 단순성
- 재사용성
- 경량 구조
- solver 독립성

향후 포함될 수 있는 유틸리티에는 다음 항목들이 있다:
- 단위 변환
- 벡터 연산
- 시간 측정 도구
- 로그 시스템
- CSV/JSON 보조 함수
- ID 생성기
- 디버깅 보조 기능

Shardhana에서 utils 계층은
전체 생태계를 지원하는 공용 도구함 역할을 수행한다.
"""