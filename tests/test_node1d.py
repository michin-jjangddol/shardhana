from core import Node1D


def test_node1d_basic():
    n = Node1D(2.5)

    assert n.x == 2.5
    assert n.u == 0.0