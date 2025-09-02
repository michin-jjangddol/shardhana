# shardhana/core/material.py

class Material:
    """
    기본 Material 클래스
    재료의 물성치(properties)를 저장하고,
    필요시 관련 계산 메서드를 포함
    """
    def __init__(self, name: str, density: float = None, elasticity: float = None):
        """
        :param name: 재료 이름
        :param density: 밀도 (kg/m^3)
        :param elasticity: 탄성계수 (Pa)
        """
        self.name = name
        self.density = density
        self.elasticity = elasticity

    def info(self) -> str:
        """
        재료 정보 출력
        """
        return f"Material: {self.name}, Density: {self.density}, Elasticity: {self.elasticity}"

    # 필요시 여기에 재료 관련 계산 메서드 추가
    # 예: stress, strain 계산 등

# 테스트용 코드
if __name__ == "__main__":
    steel = Material(name="Steel", density=7850, elasticity=2.1e11)
    print(steel.info())
