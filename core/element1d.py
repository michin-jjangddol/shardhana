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
    
    def axial_force(self) -> float:
        L = self.length
        return self.material.E * self.A / L * self.axial_delta()
    
    def summary(self) -> str:
        return (
            "=== Element1D Summary ===\n"
            f"x1     = {self.n1.x}\n"
            f"u1     = {self.n1.u}\n"
            f"x2     = {self.n2.x}\n"
            f"u2     = {self.n2.u}\n"
            f"L      = {self.length}\n"
            f"delta  = {self.axial_delta()}\n"
            f"E      = {self.material.E}\n"
            f"A      = {self.A}\n"
            f"N      = {self.axial_force()}\n"
    )