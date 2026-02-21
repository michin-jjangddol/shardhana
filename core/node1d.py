# shardhana/core/node1d.py

#class Node1D:
#    def __init__(self, x: float):
#        self.x = float(x)
#        self.u = 0.0  # displacement
        

class Node1D:
    """
    1D bar node: only axial displacement u (1 dof)
    """
    def __init__(self, id: int, x: float):
        self.id = id
        self.x = float(x)
        self.dof_u = None  # assigned by assembler