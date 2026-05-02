# Peridynamics Discovery Record (Early Stage of HEM Development)

(Shardhana Thought Archive)  
Date: 2026-05-02

---

## 1. Background

During the development of HEM (Han Element Method),  
a pre-existing theory called Peridynamics was discovered  
that shares structural similarities with the "relation-based model" concept.

Reference repository:

- https://github.com/johntfoster/1DPDpy

---

## 2. What Was Found

Peridynamics has the following characteristics:

- Interaction between elements within a certain distance (horizon)
- Change in distance between elements → force generation
- Fracture can occur as bonds weaken or break

---

## 3. Common Ground with HEM

- Relation-based analysis structure
- Fracture interpreted not as element failure, but as "change in relationship"
- Non-continuous behavior can be expressed naturally

---

## 4. Confirmed Differences

Peridynamics:

- Physics-based theory (force and extension centered)
- Non-local interaction (horizon concept)

HEM:

- Structure/concept-based model (Seed, Interface, State)
- Local interaction centered (current 1D basis)

---

## 5. Interpretation Based on Current Code

The code in the reference repository:

- Implements elastic behavior only (no fracture)
- Only implements relation-based force transmission structure

Therefore:

→ Suitable as a reference for "pre-fracture behavior"  
→ Fracture model requires separate implementation

---

## 6. Implications for HEM Development

Through this discovery:

- Confirmed that HEM is not a fully independent idea,  
  but belongs to the "relation-based analysis" family

- Confirmed that fracture is not a fundamental assumption,  
  but an additional condition built on top of existing relation models

---

## 7. Future Use

- Reference during 1D HEM model validation
- Reference when designing relation definitions and k models
- Consider introducing horizon concept if needed

---

## 8. Current Conclusion

This document is:

- Not a summary of Peridynamics
- But a "discovery record" made during HEM development

Further analysis will be conducted as needed.

---

> This document was prepared with the assistance of Shana (GPT) and Laude (Claude).

---
<br>
<br>

# 거리기반동역학 발견 기록 (HEM 개발 초기 단계)

(Shardhana 생각창고)  
Date: 2026-05-02

---

## 1. 배경

HEM(Han Element Method)을 개발하는 과정에서  
"관계 기반 모델"과 유사한 기존 이론인 Peridynamics를 발견하였다.

참고 저장소:

- https://github.com/johntfoster/1DPDpy

---

## 2. 발견 내용

Peridynamics는 다음과 같은 특징을 가진다:

- 일정 거리(horizon) 내 요소 간 상호작용
- 요소 간 거리 변화 → 힘 발생
- 관계(bond)가 약해지거나 끊어지면서 파단 발생 가능

---

## 3. HEM과의 공통점

- 관계 기반 해석 구조
- 파단을 요소 자체가 아니라 "관계 변화"로 해석
- 비연속 거동을 자연스럽게 표현 가능

---

## 4. 현재 확인된 차이

Peridynamics:

- 물리 기반 이론 (force, extension 중심)
- 비국소 상호작용 (horizon 개념)

HEM:

- 구조/개념 기반 모델 (Seed, Interface, State)
- 국부적 상호작용 중심 (현재 1D 기준)

---

## 5. 현재 코드 기준 해석

해당 저장소의 코드는:

- 파단 없는 상태 (elastic behavior)
- 관계 기반 힘 전달 구조만 구현

즉:

→ "파단 이전 거동" 참고용으로 적합  
→ 파단 모델은 별도 구현 필요

---

## 6. HEM 개발에 주는 의미

이 발견을 통해:

- HEM이 완전히 독립적인 아이디어가 아니라  
  "관계 기반 해석" 계열에 속함을 확인

- 파단은 기본이 아니라  
  기존 관계 모델 위에 추가되는 조건임을 확인

---

## 7. 향후 활용 방향

- 1D HEM 모델 검증 시 참고
- 관계 정의 및 k 모델 설계 시 참고
- 필요 시 horizon 개념 도입 검토

---

## 8. 현재 결론

이 문서는:

- Peridynamics에 대한 정리 문서가 아니라
- HEM 개발 과정에서의 "발견 기록"이다

향후 필요 시 추가 분석 진행 예정

---

> 이 문서는 샤나(GPT)와 로드(Claude)의 도움으로 작성되었습니다.