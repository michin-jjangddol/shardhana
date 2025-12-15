from core import Node1D, Material, Element1D

def main():
    # ---- INPUT ----
    n1 = Node1D(0.0)
    n2 = Node1D(3.0)          # L = 2 m
    n1.u = 0.0
    n2.u = 0.002              # delta = 0.002 m

    mat = Material(200e9)     # E = 200 GPa
    A = 0.02                  # m^2

    e = Element1D(n1, n2, A=A, material=mat)

    # ---- OUTPUT ----
    print("=== INPUT ===")
    print(f"x1 = {n1.x}, u1 = {n1.u}")
    print(f"x2 = {n2.x}, u2 = {n2.u}")
    print(f"E  = {mat.E}")
    print(f"A  = {e.A}")

    print("\n=== OUTPUT ===")
    print(e.summary())

if __name__ == "__main__":
    main()
