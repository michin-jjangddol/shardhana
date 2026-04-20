"""
necking_1d_gui.py
Shardhana — 1D HEM Prototype with GUI + Graph

Rule-based localization visualization.
No FEM, no stiffness matrix.
Uses tkinter + matplotlib embedded in GUI.
"""

import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# ── HEM Simulation ───────────────────────────────────────────

def run_hem(N, dt, k, steps):
    """Run 1D HEM simulation. Returns full state history."""
    # Initialize: all 0.0, center gets small perturbation (Seed)
    state = [0.0] * N
    state[N // 2] = 0.1

    history = [state.copy()]  # store step 0

    for _ in range(steps):
        new_state = state.copy()  # copy — do not overwrite in-place

        for i in range(1, N - 1):  # skip boundaries
            neighbor_avg = (state[i - 1] + state[i + 1]) / 2.0
            diff = state[i] - neighbor_avg        # difference from neighbors
            new_state[i] = state[i] + dt * k * diff  # amplify, not smooth

        state = new_state
        history.append(state.copy())

    return history

# ── GUI ──────────────────────────────────────────────────────

root = tk.Tk()
root.title("Shardhana — 1D HEM Prototype")
root.configure(bg="#1e1e2e")

# ── Header ───────────────────────────────────────────────────
header = tk.Label(
    root, text="Shardhana · 1D HEM Simulation",
    bg="#1e1e2e", fg="#cdd6f4",
    font=("Arial", 14, "bold"), pady=10
)
header.pack()

# ── Input Panel ──────────────────────────────────────────────
input_frame = tk.Frame(root, bg="#313244", padx=16, pady=12)
input_frame.pack(fill="x", padx=20, pady=(0, 10))

def labeled_entry(parent, label, default):
    frame = tk.Frame(parent, bg="#313244")
    frame.pack(side="left", padx=12)
    tk.Label(frame, text=label, bg="#313244", fg="#a6adc8",
             font=("Arial", 10)).pack()
    var = tk.StringVar(value=str(default))
    entry = tk.Entry(frame, textvariable=var, width=6,
                     bg="#45475a", fg="#cdd6f4",
                     insertbackground="#cdd6f4",
                     font=("Arial", 11), justify="center",
                     relief="flat")
    entry.pack()
    return var

var_N     = labeled_entry(input_frame, "Elements (N)", 20)
var_dt    = labeled_entry(input_frame, "dt", 1.0)
var_k     = labeled_entry(input_frame, "k", 0.5)
var_steps = labeled_entry(input_frame, "Steps", 15)

# ── Plot Area ─────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 4))
fig.patch.set_facecolor("#1e1e2e")
ax.set_facecolor("#181825")

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(padx=20, pady=(0, 10), fill="both", expand=True)

# ── Status Label ─────────────────────────────────────────────
status_var = tk.StringVar(value="Ready.")
status_label = tk.Label(
    root, textvariable=status_var,
    bg="#1e1e2e", fg="#a6e3a1",
    font=("Arial", 10), pady=4
)
status_label.pack()

# ── Run Button ───────────────────────────────────────────────
def on_run():
    try:
        N     = int(var_N.get())
        dt    = float(var_dt.get())
        k     = float(var_k.get())
        steps = int(var_steps.get())
    except ValueError:
        status_var.set("⚠ Invalid input. Please check parameters.")
        return

    # Run simulation
    history = run_hem(N, dt, k, steps)

    # Pick three steps to plot
    step_0   = 0
    step_mid = steps // 2
    step_end = steps

    x = list(range(N))

    ax.clear()
    ax.set_facecolor("#181825")

    ax.plot(x, history[step_0],   color="#89b4fa", linewidth=1.5,
            marker="o", markersize=4, label=f"Step {step_0} (initial)")
    ax.plot(x, history[step_mid], color="#fab387", linewidth=1.5,
            marker="o", markersize=4, label=f"Step {step_mid} (middle)")
    ax.plot(x, history[step_end], color="#f38ba8", linewidth=2.0,
            marker="o", markersize=5, label=f"Step {step_end} (final)")

    ax.set_xlabel("Element Index", color="#a6adc8")
    ax.set_ylabel("State Value", color="#a6adc8")
    ax.set_title("1D HEM — State Localization", color="#cdd6f4", fontsize=12)
    ax.tick_params(colors="#a6adc8")
    ax.spines[:].set_color("#45475a")
    ax.legend(facecolor="#313244", labelcolor="#cdd6f4", fontsize=9)
    ax.grid(True, color="#313244", linestyle="--", linewidth=0.5)

    canvas.draw()
    status_var.set(
        f"✔ Done — N={N}, dt={dt}, k={k}, steps={steps}  |  "
        f"Center final state: {history[-1][N//2]:.4f}"
    )

run_btn = tk.Button(
    root, text="▶  Run Simulation",
    bg="#89b4fa", fg="#1e1e2e",
    font=("Arial", 11, "bold"),
    relief="flat", padx=20, pady=6,
    cursor="hand2",
    command=on_run
)
run_btn.pack(pady=(0, 16))

root.mainloop()