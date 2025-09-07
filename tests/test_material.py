import random, math
from core.material import Material

ATTRS = ("name", "E", "density")
N_RANDOM = 3 * len(ATTRS)   # 속성 수의 3배만큼 샘플

def test_material_random_samples():
    random.seed(42)  # 재현 가능하게
    for _ in range(N_RANDOM):
        name = "Rnd"
        E = random.uniform(1e9, 3e11)       # 탄성계수 범위 예시 (1~300 GPa)
        density = random.uniform(500, 8000) # 밀도 범위 예시 (kg/m^3)

        m = Material(name, E=E, density=density)

        # 핵심 속성들 검증 (float은 isclose 권장)
        assert m.name == name
        assert math.isclose(m.E, E, rel_tol=1e-12, abs_tol=0.0)
        assert math.isclose(m.density, density, rel_tol=1e-12, abs_tol=0.0)