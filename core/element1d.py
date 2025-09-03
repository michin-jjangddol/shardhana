"""
Shardhana: 1차원 막대 요소 (축강성)
"""

# 노드(Node1D) 클래스를 dataclass로 정의한다. (id: int, x: float)

from dataclasses import dataclass
import math
from material import Material
@dataclass
class Node1D:
    id: int
    x: float

    def coords(self) -> float:
        return self.x
    # __repr__(): 노드 번호와


# 좌표를 반환하는 메서드 포함
    def __repr__(self) -> str:
        return f"Node1D(id={self.id}, x={self.x})"  
    

# 재료(Material) 클래스를 정의한다. (이름, 탄성계수 E)
class Material:
    def __init__(self, name: str, elasticity: float):
        self.name = name
        self.elasticity = elasticity  # 탄성계수 E (Pa)

    def __repr__(self) -> str:
        return f"Material(name={self.name}, E={self.elasticity} Pa)"


# Element1D 클래스를 정의한다.

class Element1D:
    def __init__(self, n1: Node1D, n2: Node1D, area: float, material: Material):
        if n1.id == n2.id:
            raise ValueError("두 노드는 서로 달라야 합니다.")
        self.n1 = n1
        self.n2 = n2
        self.area = area  # 단면적 A (m^2)
        self.material = material  # 재료(Material) 객체

    def length(self) -> float:
        return abs(self.n2.x - self.n1.x)

    def stiffness(self) -> float:
        L = self.length()
        if L == 0:
            raise ValueError("길이가 0인 요소는 허용되지 않습니다.")
        E = self.material.elasticity
        A = self.area
        k = E * A / L  # 축강성 k = E*A/L
        return k

    def deformation(self, P: float) -> float:
        L = self.length()
        E = self.material.elasticity
        A = self.area
        if E * A == 0:
            raise ValueError("재료의 탄성계수와 단면적은 0이 될 수 없습니다.")
        delta = P * L / (E * A)  # 변형 δ = P*L/(E*A)
        return delta

    def __repr__(self) -> str:
        return (f"Element1D(n1={self.n1.id}, n2={self.n2.id}, A={self.area} m^2, "
                f"E={self.material.elasticity} Pa, L={self.length()} m, k={self.stiffness()} N/m)")
        
# 1D 막대(Bar1D) 클래스를 정의한다.
# - 두 노드(Node1D)로 구성
# - 속성: 두 노드(n1, n2), 단면적 A, 재료
# - 재료(Material) 객체 포함

# - 메서드:
#   - length(): 두 노드 간 거리 (절댓값)

#   - stiffness(): 축강성 k = E*A/L

#   - deformation(P): 하중 P에 대한 변형 δ = P*L/(E*A)
# - 예외 처리:
# - 두 노드가 같을 경우 예외(ValueError) 발생

# - 길이가 0일 경우 예외(ValueError) 발생
# - __repr__(): 노드 번호, A, E, L, k 출력

if __name__ == "__main__":
    n1 = Node1D(1, 0.0)
    n2 = Node1D(2, 2.0)  # L = 2.0
    steel = Material("steel", 200e9)
    bar = Element1D(n1, n2, area=0.01, material=steel)

    print("길이 L =", bar.length())                 # 2.0
    print("강성 k =", bar.stiffness())              # 1.0e9
    print("변형 δ(1000N) =", bar.deformation(1000)) # 1.0e-6