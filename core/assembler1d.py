# shardhanacore/assembler1d.py
import numpy as np

class Assembler1D:
    def __init__(self, nodes, elements):
        self.nodes = list(nodes)
        self.elements = list(elements)

    def assign_dofs(self):
        # 1 dof per node: u
        for i, nd in enumerate(self.nodes):
            nd.dof_u = i

    def build_KF(self):
        n = len(self.nodes)
        K = np.zeros((n, n), dtype=float)
        F = np.zeros((n,), dtype=float)

        for e in self.elements:
            ke = e.stiffness_matrix()
            idx = e.dof_map()
            # assemble 2x2
            for a in range(2):
                for b in range(2):
                    K[idx[a], idx[b]] += ke[a, b]
        return K, F

    @staticmethod
    def apply_bc(K, F, fixed_dofs, fixed_values=None):
        # eliminate rows/cols (simple and robust for small problems)
        fixed_dofs = list(fixed_dofs)
        if fixed_values is None:
            fixed_values = [0.0] * len(fixed_dofs)

        all_dofs = np.arange(K.shape[0])
        free = np.array([d for d in all_dofs if d not in fixed_dofs], dtype=int)

        # modify RHS for prescribed values: F_free -= K_free,fixed * u_fixed
        u_fixed = np.array(fixed_values, dtype=float)
        K_ff = K[np.ix_(free, free)]
        K_fc = K[np.ix_(free, fixed_dofs)]
        F_f = F[free] - K_fc @ u_fixed

        return K_ff, F_f, free, fixed_dofs, u_fixed

    def solve(self, loads: dict, fixed: dict):
        """
        loads: {node_id: force}  (axial nodal forces)
        fixed: {node_id: displacement_value} (usually 0.0)
        """
        self.assign_dofs()
        K, F = self.build_KF()

        # apply loads
        for nd in self.nodes:
            if nd.id in loads:
                F[nd.dof_u] += float(loads[nd.id])

        # boundary conditions
        fixed_dofs = []
        fixed_vals = []
        for nd in self.nodes:
            if nd.id in fixed:
                fixed_dofs.append(nd.dof_u)
                fixed_vals.append(float(fixed[nd.id]))

        K_ff, F_f, free, fixed_dofs, u_fixed = self.apply_bc(K, F, fixed_dofs, fixed_vals)

        # solve
        u_free = np.linalg.solve(K_ff, F_f)

        # build full displacement vector
        u = np.zeros((len(self.nodes),), dtype=float)
        u[free] = u_free
        for dof, val in zip(fixed_dofs, u_fixed):
            u[dof] = val

        return u, K, F