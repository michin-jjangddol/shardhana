# shardhana/core/material.py

class Material:
    """
    기본 Material 클래스
    재료의 물성치(properties)를 저장
    """
    def __init__(self, name: str,
                 density: float | None = None,
                 elasticity: float | None = None,
                 E: float | None = None):
        """
        :param name: 재료 이름
        :param density: 밀도 (kg/m^3)
        :param elasticity: 탄성계수 (Pa) — 'elasticity' 또는 'E' 중 아무거나 사용 가능
        :param E: 탄성계수 (Pa) — 'elasticity'의 별칭
        """
        self.name = name

        if density is None:
            raise TypeError("Material.__init__ requires 'density' (kg/m^3).")
        self.density = float(density)

        # 'elasticity' 또는 'E' 어느 쪽이든 허용
        if elasticity is None and E is not None:
            elasticity = E
        if elasticity is None:
            raise TypeError("Material.__init__ requires 'elasticity' (or keyword 'E').")

        self.elasticity = float(elasticity)
        self.E = self.elasticity  # 별칭 유지

    def __repr__(self):
        return f"Material(name={self.name}, density={self.density}, elasticity={self.elasticity})"

    def info(self) -> str:
        return f"Material: {self.name}, Density: {self.density}, Elasticity: {self.elasticity}"

if __name__ == "__main__":
    # 간단 점검용
    steel = Material("Steel", 7850, 2.1e11)
    print(steel.info())
