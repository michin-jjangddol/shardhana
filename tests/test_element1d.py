from core import Node1D, Material, Element1D


def test_element_length():
    n1 = Node1D(0.0)
    n2 = Node1D(2.0)
    m = Material(200e9)

    e = Element1D(n1, n2, A=0.01, material=m)

    assert e.length == 2.0


def test_element_axial_delta():
    n1 = Node1D(0.0)
    n2 = Node1D(1.0)
    m = Material(200e9)

    n1.u = 0.0
    n2.u = 0.005

    e = Element1D(n1, n2, A=0.01, material=m)

    assert abs(e.axial_delta() - 0.005) < 1e-12

def test_element_axial_force():
    n1 = Node1D(0.0)
    n2 = Node1D(2.0)          # L = 2 m
    m = Material(200e9)       # E
    A = 0.01                  # m^2

    n1.u = 0.0
    n2.u = 0.002              # delta = 0.002 m

    e = Element1D(n1, n2, A=A, material=m)

    # N = E*A/L * delta = 200e9*0.01/2 * 0.002 = 2e6 N
    assert abs(e.axial_force() - 2.0e6) < 1e-3