# shardhana/core/material.py

# class Material:
#    def __init__(self, E: float):
#        self.E = float(E)
        

class Material:

    def __init__(self, name: str, E: float):
        self.name = name
        self.E = float(E)