# shardhana/core/element.py

from material import Material

class Element:
    """
    기본 Element 클래스
    구조 요소(Element)를 정의하고, Material과 연결
    """
    def __init__(self, name: str, material: Material, nodes: list, area: float = None, length: float = None):
        """
        :param name: 요소 이름
        :param material: Material 객체
        :param nodes: 요소가 연결된 노드 좌표 리스트 [(x1, y1), (x2, y2), ...]
        :param area: 단면적 (m^2)
        :param length: 요소 길이 (m)
        """
        self.name = name
        self.material = material
        self.nodes = nodes
        self.area = area
        self.length = length

    def info(self) -> str:
        """
        요소 정보 출력
        """
        node_str = ', '.join([f"({x},{y})" for x, y in self.nodes])
        return f"Element: {self.name}, Material: {self.material.name}, Nodes: [{node_str}], Area: {self.area}, Length: {self.length}"

    # 향후 stiffness_matrix, force 계산 등 AEM 관련 메서드 추가 가능

# 테스트용 코드
if __name__ == "__main__":
    from material import Material
    steel = Material(name="Steel", density=7850, elasticity=2.1e11)
    elem = Element(name="Beam1", material=steel, nodes=[(0,0), (1,0)], area=0.01, length=1.0)
    print(elem.info())
