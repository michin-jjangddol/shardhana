

from core import Material


def test_material_E():
    m = Material(200e9)
    assert m.E == 200e9