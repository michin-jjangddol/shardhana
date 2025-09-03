# Shardhana 교재 예제 1: 1차원 막대 축변형

이 예제에서는 **1차원 막대(Bar)** 에 축방향 하중이 작용할 때 발생하는 변형량과 응력을 계산합니다.  

---

## 문제

- 재질: 강(steel), 탄성계수 \( E = 200 \, \text{GPa} = 200 \times 10^9 \, \text{Pa} \)  
- 막대 길이: \( L = 2.0 \, \text{m} \)  
- 단면적: \( A = 0.0001 \, \text{m}^2 \) (10mm × 10mm 정사각형 단면)  
- 인장하중: \( P = 1.0 \, \text{kN} = 1000 \, \text{N} \)

---

## 해석 개념

1. **변형량**  
\[
\delta = \frac{P \cdot L}{E \cdot A}
\]

2. **응력**  
\[
\sigma = \frac{P}{A}
\]

---

## 계산

- 변형량  
\[
\delta = \frac{1000 \times 2.0}{200 \times 10^9 \times 0.0001} 
= 1.0 \times 10^{-4} \, \text{m} = 0.1 \, \text{mm}
\]

- 응력  
\[
\sigma = \frac{1000}{0.0001} = 10 \, \text{MPa}
\]

---

## 결과

- 변형량: **0.1 mm**  
- 응력: **10 MPa**

---

## 그림

아래 그림은 문제 조건을 나타낸 단순화된 도식입니다.

![Bar under axial load](img/ex1_bar_axial.svg)

---

## Python 코드 예시

```python
from dataclasses import dataclass

@dataclass
class Node1D:
    id: int
    x: float

class Material:
    def __init__(self, name: str, E: float):
        self.name = name
        self.E = E

class Element1D:
    def __init__(self, n1, n2, A, material):
        self.n1, self.n2 = n1, n2
        self.A, self.material = A, material

    def length(self):
        return abs(self.n2.x - self.n1.x)

    def deformation(self, P):
        L = self.length()
        return P * L / (self.material.E * self.A)

    def stress(self, P):
        return P / self.A

if __name__ == "__main__":
    n1, n2 = Node1D(1, 0.0), Node1D(2, 2.0)
    steel = Material("Steel", 200e9)
    bar = Element1D(n1, n2, 0.0001, steel)

    P = 1000  # N
    print("변형량 δ =", bar.deformation(P), "m")
    print("응력 σ =", bar.stress(P), "Pa")