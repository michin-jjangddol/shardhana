# run_bar1d.py (프로젝트 루트에)

from core.node1d import Node1D
from core.material import Material
from core.element1d import Element1D
from core.assembler1d import Assembler1D

if __name__ == "__main__":
    # --- model ---
    n1 = Node1D(1, 0.0)
    n2 = Node1D(2, 2.0)

    steel = Material("Steel", 200e9)
    e1 = Element1D(n1, n2, A=0.01, material=steel)

    asm = Assembler1D(nodes=[n1, n2], elements=[e1])

    # --- loads / BC (사용자 입력 지점) ---
    loads = {2: 1000.0}   # node_id : N
    fixed = {1: 0.0}      # node_id : m

    # --- solve ---
    u, K, F = asm.solve(loads=loads, fixed=fixed)

    print("u =", u)
    print("K =\n", K)
    print("F =", F)
    print("u2 (mm) =", u[1] * 1000)

    # --- post (중복 없이 모델/loads에서 끌어오기) ---
    L = e1.length()
    A = e1.A
    P = loads.get(2, 0.0)   # 여기서는 node2에만 하중 준 케이스라 단순히 가져옴

    delta = u[1] - u[0]
    eps = delta / L
    sigma = P / A

    print("\n--- Post ---")
    print("L (m)      =", L)
    print("A (m^2)    =", A)
    print("P (N)      =", P)
    print("delta (mm) =", delta * 1000)
    print("strain ε   =", eps)
    print("stress σ (MPa) =", sigma / 1e6)