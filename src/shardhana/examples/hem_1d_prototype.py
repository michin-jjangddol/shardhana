"""
necking_1d_demo.py
Shardhana — Minimal 1D HEM Prototype

Rule-based localization demo.
No FEM, no stiffness matrix.
A small perturbation grows into necking-like concentration over time.
"""

# ── Parameters ───────────────────────────────────────────────
N = 10        # number of elements
dt = 1.0      # time increment
k = 0.5       # amplification factor
steps = 10    # number of time steps

# ── Initial State ────────────────────────────────────────────
# All elements start at 0.0
# Center element gets a small perturbation (Seed)
state = [0.0] * N
state[N // 2] = 0.1   # small perturbation at center

print("=== Shardhana 1D HEM Prototype ===")
print(f"Elements: {N}, dt: {dt}, k: {k}, steps: {steps}")
print()
print(f"Step 0 : {[round(s, 4) for s in state]}")

# ── Time Stepping ────────────────────────────────────────────
t = 0.0

for step in range(1, steps + 1):
    t += dt
    new_state = state.copy()   # copy — do not overwrite in-place

    for i in range(1, N - 1):  # skip boundaries
        neighbor_avg = (state[i - 1] + state[i + 1]) / 2.0
        diff = state[i] - neighbor_avg          # difference from neighbors
        new_state[i] = state[i] + dt * k * diff  # amplify, not smooth

    state = new_state
    print(f"Step {step:2d} (t={t:.1f}): {[round(s, 4) for s in state]}")

print()
print("=== Done ===")
print("Localization (necking-like behavior) observed at center element.")