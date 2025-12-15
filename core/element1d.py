from core.node1d import Node1D
from core.material import Material


class Element1D:
    def __init__(self, n1: Node1D, n2: Node1D, A: float, material: Material):
        self.n1 = n1
        self.n2 = n2
        self.A = float(A)
        self.material = material

    @property
    def length(self) -> float:
        return abs(self.n2.x - self.n1.x)

    def axial_delta(self) -> float:
        return self.n2.u - self.n1.u