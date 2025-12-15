# tests/test_element1d_matrix.py
import pytest

from core.material import Material
from core.element1d import Node1D, Element1D

def test_local_stiffness_matrix_values():
    # E=200e9 Pa, A=0.01 m^2, L=2.0 m  →  k = EA/L = 1e9
    steel = Material("Steel", 7850,200e9)
    n1, n2 = Node1D(1, 0.0), Node1D(2, 2.0)
    elem = Element1D(n1=n1, n2=n2, area=0.01, material=steel)

    K = elem.local_stiffness_matrix()
    k = 1e9
    expected = [[k, -k],
                [-k,  k]]

    for i in range(2):
        for j in range(2):
            assert K[i][j] == pytest.approx(expected[i][j])

def test_local_stiffness_matrix_symmetry_and_size():
    steel = Material("Steel", 7850, 210e9)
    elem = Element1D(Node1D(1, 0.0), Node1D(2, 3.0), area=0.02, material=steel)

    K = elem.local_stiffness_matrix()

    # 2x2인지
    assert isinstance(K, list) and len(K) == 2 and all(len(row) == 2 for row in K)
    # 대칭성 K[0][1] == K[1][0]
    assert K[0][1] == pytest.approx(K[1][0])
