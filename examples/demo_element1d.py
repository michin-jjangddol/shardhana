# UNIT SYSTEM (Shardhana core demo)
# x, u : m
# E    : Pa (N/m^2)
# A    : m^2
# N    : N

# --- UNITS ---
X_UNIT = "m"
U_UNIT = "m"
E_UNIT = "Pa"
A_UNIT = "m^2"
N_UNIT = "N"

from core import Node1D, Material, Element1D

def main():
    # ---- INPUT ----
    n1 = Node1D(0.0)          # x [m]
    n2 = Node1D(3.0)          # x [m]
    n1.u = 0.0                # u [m]
    n2.u = 0.002              # u [m]

    mat = Material(200e9)     # E [Pa]= 200 GPa
    A = 0.02                  # A [m^2]

    e = Element1D(n1, n2, A=A, material=mat)

    # ---- OUTPUT ----
    print("=== INPUT ===")
    print(f"x1 = {n1.x} [{X_UNIT}], u1 = {n1.u} [{U_UNIT}]")
    print(f"x2 = {n2.x} [{X_UNIT}], u2 = {n2.u} [{U_UNIT}]")
    print(f"E  = {mat.E*1e-9:,.2f} [G{E_UNIT}]")
    print(f"A  = {e.A} [{A_UNIT}]")

    print("\n=== OUTPUT ===")
    print(f"L           = {e.length}[{X_UNIT}]")
    print(f"delta       = {e.axial_delta()}[{U_UNIT}]")
    print(f"Axial Force = {e.axial_force()*1e-3:,.2f}[k{N_UNIT}]")

if __name__ == "__main__":
    main()
