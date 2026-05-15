"""
seed.py
Shardhana Core Seed Definition

This file defines the fundamental Seed object used in the Shardhana core engine.

A Seed is not simply a finite element.
It is a minimal unit that may contain:
- state
- relation
- interaction
- transformation possibility

The Seed structure is intended to evolve gradually
as HEM (Han Element Method) concepts become clearer.

This file should remain:
- lightweight
- extensible
- engine-oriented

Future expansion may include:
- geometry
- state variables
- neighbor relations
- damage/fracture behavior
- space interaction
- probabilistic transition rules


이 파일은 Shardhana 코어 엔진에서 사용하는
기본 Seed 객체를 정의한다.

Seed는 단순한 유한요소(Finite Element)가 아니다.

Seed는 다음과 같은 개념을 담을 수 있는
최소 단위 구조이다:
- 상태(state)
- 관계(relation)
- 상호작용(interaction)
- 변화 가능성(transformation possibility)

이 구조는 앞으로
HEM(Han Element Method) 개념이 구체화됨에 따라
점진적으로 확장될 예정이다.

이 파일은 다음 원칙을 유지한다:
- 경량 구조
- 확장 가능성
- 엔진 중심 설계

향후 확장 가능 항목:
- 형상 정보
- 상태 변수
- 이웃 관계
- 손상/파괴 거동
- 공간 상호작용
- 확률 기반 변화 규칙
"""