# Shardhana: 1차원 막대 요소 기본 예제

# 노드 클래스 (id와 좌표만 가짐)
class Node1D:
    def __init__(self, id, x):
        self.id = id
        self.x = x

# 재료 클래스 (이름과 탄성계수 E)
class Material:
    def __init__(self, name, E):
        self.name = name
        self.E = E

# 요소 클래스 (두 노드, 단면적, 재료)
class Element1D:
    def __init__(self, n1, n2, A, material):
        self.n1 = n1
        self.n2 = n2
        self.A = A
        self.material = material

    # 요소 길이
    def length(self):
        return abs(self.n2.x - self.n1.x)

    # 축강성 k = EA/L
    def stiffness(self):
        L = self.length()
        return self.material.E * self.A / L

    # 변형 δ = PL / (EA)
    def deformation(self, P):
        L = self.length()
        return P * L / (self.material.E * self.A)


# ---------------- 실행 ----------------
if __name__ == "__main__":
    n1 = Node1D(1, 0.0)
    n2 = Node1D(2, 2.0)  # 길이 L = 2.0 m
    steel = Material("Steel", 200e9)  # 탄성계수 E
    bar = Element1D(n1, n2, A=0.01, material=steel)

    print("길이 L =", bar.length())
    print("강성 k =", bar.stiffness())
    print("변형 δ(1000N) =", bar.deformation(1000))
