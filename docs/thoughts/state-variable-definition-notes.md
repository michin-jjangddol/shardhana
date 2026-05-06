# State Variable Definition Notes

*(Shardhana Thought Archive)*  
*Date: 2026-05-06*

---

## Why Rethink State Variables?

In the early 1D HEM experiments,
state values were designed to propagate between adjacent seeds
in positive (+) / negative (-) form.

This approach was useful for quickly experimenting with
localization and diffusion behavior,

but gradually a question began to emerge:

> "Is State really a value that should be directly manipulated?"

In natural phenomena, it is more common for:

- distance
- volume
- contact
- density
- compression

— geometric and relational changes — to occur first,
and for State to emerge as a result.

In other words, rather than:

```text
State Driven Model
```

the direction of:

```text
Geometry / Relation Driven State Emergence
```

may be more aligned with the philosophy of HEM (Han Element Method).

---

## Is State a Result or a Cause?

In conventional FEM-based thinking,
state values are often results:

- stress
- strain
- displacement

But in HEM, State is not merely a result.
It can also play the role of a time-based causal variable that:

- creates relations
- strengthens relations
- weakens relations
- collapses relations

In other words, the flow:

```text
State → Relation Change → Structure Evolution
```

becomes possible.

---

## Direction of HEM State Variables

In HEM, state variables are not a single number.
They can be divided into several layers:

---

### 1. Geometry State

```text
volume
length
area
density
distance
contact_area
```

Variables directly connected to geometric and positional relationships.

---

### 2. Physical State

```text
velocity
acceleration
pressure
temperature
strain
stress
```

Variables directly connected to physical phenomena.

---

### 3. Material State

```text
damage
hardening
softening
plasticity
moisture
degradation
```

Variables related to internal material change.

---

### 4. Relation State

```text
bond_k
contact
slip
opening
interface_strength
permeability
damping
```

States that are particularly important in HEM.

These define the state between elements (Relation),
rather than the elements themselves.

---

### 5. Environment State

```text
humidity
external_temperature
chemical_exposure
radiation
wind
water
```

Variables representing interaction with the external world.

---

## Dictionary Structure May Be More Suitable for State

HEM may eventually need to connect:

- structural behavior
- heat
- moisture
- chemistry
- contact
- damage
- time evolution

simultaneously.

Therefore, rather than locking state variables into fixed class fields,
managing them as a flexible dictionary structure
may be more appropriate for the early HEM experimental stage.

Example:

```python
state = {
    "volume": 1.0,
    "density": 1000.0,
    "temperature": 20.0,
    "damage": 0.0,
    "bond_k": 0.1,
    "permeability": 1.0,
}
```

---

## Advantages of Dictionary Structure

### Flexibility

New state variables can be added easily:

```python
state["humidity"] = 0.5
state["mold"] = 0.2
```

---

### Experimental Friendliness

HEM is still closer to an exploratory experimental stage
than a fixed theory.

A structure that allows state variables to be freely added or removed
is therefore advantageous.

---

### Connection to CSV and Time History Storage

Dictionary-based state connects naturally to CSV storage:

```text
time,id,volume,density,damage,bond_k
```

This is also advantageous for future:

- Time History tracking
- State change monitoring
- GUI visualization
- Post-processing

---

## Connection to the 1D Initial Model

In the early 1D experiments,
state values were directly manipulated.

But going forward, a flow such as:

```text
distance ↓
→ density ↑
→ interaction ↑
→ relation ↑
```

— where state emerges naturally from geometric and relational changes —
may produce a more physically consistent behavior.

---

## Connection to Self-Amalgamating Tape

The self-amalgamating tape case connects well to the HEM state variable concept:

```text
time ↑
→ bond_k ↑
→ permeability ↓
→ damping ↑
→ unified body formation
```

In other words, State is not merely a stored result —
it is a dynamic variable that changes relations over time.

---

## Closing Thoughts

In HEM, State is not simply a number storing a calculation result.

It may be:

> "A living variable that changes relations."

And the core of HEM may lie not in individual elements themselves,
but in the direction of:

> "How relations are created, strengthened, and collapsed
as state changes over time."

---

> This document was prepared with the assistance of Shana (GPT) and Laude (Claude).

---
<br>
<br>

# 상태 변수(State Variable) 정의 메모
# State Variable Definition Notes

*(Shardhana 생각창고)*  
*Date: 2026-05-06*

---

## 왜 상태 변수(State)를 다시 생각하는가

초기 1D HEM 실험에서는
상태값(State)이 인접 시드(seed) 사이를
양(+)/음(-) 형태로 전달되며 변화하도록 구성되었다.

이 방식은
국부화(localization)와 확산(diffusion)을
빠르게 실험하기에는 유용했지만,

점점 다음과 같은 질문이 생기기 시작했다.

> "상태(State)는 정말 직접 흔들어야 하는 값인가?"

오히려 자연 현상에서는:

- 거리(distance)
- 부피(volume)
- 접촉(contact)
- 밀도(density)
- 압착(compression)

같은 형상 및 관계 변화가 먼저 발생하고,

그 결과로 상태(State)가 나타나는 경우가 많다.

즉:

```text
State Driven Model
```

보다,

```text
Geometry / Relation Driven State Emergence
```

방향이
HEM(Han Element Method)의 철학과
더 가까울 가능성이 있다.

---

## 상태(State)는 결과인가, 원인인가

기존 FEM 기반 사고에서는
상태값이 결과(Result)인 경우가 많다.

예:

- 응력(stress)
- 변형률(strain)
- 변위(displacement)

하지만 HEM에서는
상태(State)가 단순 결과값이 아니라,

- 관계를 생성하고
- 관계를 강화하고
- 관계를 약화시키고
- 관계를 붕괴시키는

시간 기반 원인 변수 역할까지 수행할 수 있다.

즉:

```text
State → Relation Change → Structure Evolution
```

이라는 흐름이 가능하다.

---

## HEM 상태 변수의 방향성

HEM에서 상태 변수는
단순 수치 하나가 아니라,

다음과 같은 여러 층(layer)으로 나눌 수 있다.

---

### 1. 형상 기반 상태 (Geometry State)

```text
volume
length
area
density
distance
contact_area
```

형상 및 위치 관계와 직접 연결되는 변수들.

---

### 2. 물리 상태 (Physical State)

```text
velocity
acceleration
pressure
temperature
strain
stress
```

물리 현상과 직접 연결되는 변수들.

---

### 3. 재료 상태 (Material State)

```text
damage
hardening
softening
plasticity
moisture
degradation
```

재료 내부 변화와 관련된 변수들.

---

### 4. 관계 상태 (Relation State)

```text
bond_k
contact
slip
opening
interface_strength
permeability
damping
```

HEM에서 특히 중요할 가능성이 있는 상태들.

요소(Element) 자체보다,
요소 사이(Relation)의 상태를 정의한다.

---

### 5. 환경 상태 (Environment State)

```text
humidity
external_temperature
chemical_exposure
radiation
wind
water
```

외부 세계와의 상호작용 변수들.

---

## 상태(State)는 딕셔너리(Dictionary) 구조가 적합할 수 있다

HEM은 향후:

- 구조
- 열
- 수분
- 화학
- 접촉
- 손상
- 시간 변화

등이 동시에 연결될 가능성이 있다.

따라서 상태 변수를 고정 클래스 변수로 제한하기보다,
유연한 딕셔너리(Dictionary) 구조로 관리하는 것이
초기 HEM 실험 단계에서는 더 적합할 수 있다.

예시:

```python
state = {
    "volume": 1.0,
    "density": 1000.0,
    "temperature": 20.0,
    "damage": 0.0,
    "bond_k": 0.1,
    "permeability": 1.0,
}
```

---

## 딕셔너리 방식의 장점

### 유연성

새로운 상태 변수를 쉽게 추가 가능.

```python
state["humidity"] = 0.5
state["mold"] = 0.2
```

---

### 실험성

HEM은 아직 고정된 이론보다
실험적 탐색 단계에 가깝다.

따라서 상태 변수도
자유롭게 추가/삭제 가능한 구조가 유리하다.

---

### CSV 및 시간이력 저장과의 연결

딕셔너리 기반 상태는
CSV 저장 구조와도 자연스럽게 연결될 수 있다.

예:

```text
time,id,volume,density,damage,bond_k
```

이는 향후:

- 시간이력(Time History)
- 상태 변화 추적
- GUI 시각화
- 후처리(Post-processing)

에도 유리하다.

---

## 1D 초기 모델과의 연결 가능성

초기 1D 실험에서는
상태값 자체를 직접 변화시키는 방식이 많았다.

하지만 향후에는:

```text
distance ↓
→ density ↑
→ interaction ↑
→ relation ↑
```

처럼,

형상 및 관계 변화로부터
상태가 자연스럽게 발생하는 방향이
더 물리적인 흐름을 만들 수 있다.

---

## 자가융착테이프와의 연결

자가융착테이프 사례는
HEM 상태 변수 개념과 잘 연결된다.

예:

```text
time ↑
→ bond_k ↑
→ permeability ↓
→ damping ↑
→ unified body formation
```

즉 상태(State)는
단순한 결과값이 아니라,

시간 속에서 관계를 변화시키는
동적 변수(Dynamic Variable) 역할을 한다.

---

## 마무리 생각

HEM에서 상태(State)는
단순 계산 결과를 저장하는 숫자가 아니라,

> "관계를 변화시키는 살아있는 변수"

일 수 있다.

그리고 HEM의 핵심은
개별 요소(Element) 자체보다,

> "상태 변화에 따라 관계가 어떻게 생성되고,
강화되며,
붕괴되는가"

를 다루는 방향일지도 모른다.

---

> 이 문서는 샤나(GPT)와 로드(Claude)의 도움으로 작성되었습니다.