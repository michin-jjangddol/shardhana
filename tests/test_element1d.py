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