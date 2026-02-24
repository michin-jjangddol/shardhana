# Memo on Grain in HEM Elements

This document is not a finalized paper.
It is a memo that records thoughts that emerged while considering HEM.

---

## Initial Thought

Most natural materials possess grain (directionality).
Wood is the obvious example, but rolled steel may also exhibit process-induced directionality or residual stress patterns.

If so, in HEM elements,
can “grain” be treated not merely as a material constant,
but as a function or a state variable?

This question triggered the line of thinking.

---

## Possible Considerations

- Can grain be represented as a local axis of the element?
- Can grain be defined as a spatially varying directional function?
- Can inspection data from existing buildings be mapped into element states?
- Should uncertain grain orientation be expressed probabilistically?
- Can grain be interpreted as a result of formation history (growth, manufacturing)?

There are no conclusions yet.
This is only a list of possibilities.

---

## Connection to Existing Structures

In the evaluation of existing wooden structures,
grain direction may relate to:

- Crack propagation direction
- Vulnerability in compression perpendicular to grain
- Shear failure paths
- Splitting behavior near connections

However, it is still unclear whether a refined anisotropic analysis
would produce a meaningful difference in actual safety assessment.

---

## Note from the Perspective of Generative / Partition-Based Elements

Various alternative computational approaches (DEM, Peridynamics, MPM, Phase-field, etc.)
show strengths in fracture and fragmentation.

However, a simple and practical framework that integrates
“formation history + directionality + structural judgment”
has not yet been clearly organized.

Whether HEM can contribute in this domain remains a question for future consideration.

---

## Questions to Leave Open

- Should grain belong to the core, or be implemented as a plugin?
- Is grain a material constant, or an internal state?
- Does incorporating grain meaningfully influence design decisions?

---
> This document was prepared with the assistance of Shana (GPT).


<br>
<br>


# HEM 요소에서 결(Grain)에 대한 메모

이 문서는 정리 문서가 아니라,
HEM을 고민하던 중 떠오른 생각을 기록해 두는 메모이다.

---

## 출발 생각

자연 재료는 대부분 결(방향성)을 가진다.
목재는 물론이고, 압연강재도 공정에 따른 방향성이나 잔류응력이 존재할 수 있다.

그렇다면 HEM 요소에서도 “결”을 단순한 재료 상수가 아니라
어떤 함수나 상태(state)로 다룰 수 있을까?

---

## 떠오른 가능성들

- 결을 요소의 로컬 축으로 둘 수 있을까?
- 결을 공간적으로 변하는 방향 함수로 정의할 수 있을까?
- 기존 건물 조사 시 결 방향을 요소 상태로 매핑할 수 있을까?
- 불확실한 결을 확률적으로 표현해야 할까?
- 결을 생성 이력(성장, 가공)의 결과로 해석할 수 있을까?


---

## 기존 건물과의 연결

기존 목조건물 검토 시 결 방향은 다음과 관계될 수 있다:

- 균열 진행 방향
- 결 직각 압축 취약성
- 전단 파괴 경로
- 접합부 쪼개짐

그러나 정교한 이방성 해석이
실제 안전 판단에 의미 있는 차이를 만드는지는 아직 판단하지 못했다.

---

## 생성/분할 요소 관점 메모

현재의 다양한 해석법(DEM, Peridynamics, MPM, Phase-field 등)은
파괴나 분절에는 강점을 보인다.

그러나 “형성 이력 + 방향성 + 구조 판단”을
단순하고 실용적으로 통합한 체계는 아직 정리되지 않은 상태다.

HEM이 이 영역에서 어떤 역할을 할 수 있을지는 추후 다시 생각해 볼 문제다.

---

## 남겨둘 질문

- 결은 코어에 들어가야 하는가, 플러그인인가?
- 결은 재료 상수인가, 내부 상태인가?
- 결 반영이 실제 설계 판단에 영향을 줄 정도로 의미가 있는가?

---

> 이 문서는 샤나(GPT)의 도움으로 작성된 문서입니다

