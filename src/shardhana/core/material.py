"""
core/material.py
재료 특성 구조

Material definition for Shardhana

Core material structure
"""

class Material:
    """
    Basic material properties
    """

    def __init__(
        self,
        name: str = "material",
        density: float = 0.0,
        young_modulus: float = 0.0,
        poisson_ratio: float = 0.0,
    ):

        # material name
        self.name = name

        # physical properties
        self.density = float(density)

        self.young_modulus = float(young_modulus)
        self.poisson_ratio = float(poisson_ratio)

        # short alias
        self.E = self.young_modulus