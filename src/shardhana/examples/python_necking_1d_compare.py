"""
necking_1d_compare.py
Shardhana — 1D HEM: Localization vs Smoothing Comparison

Same initial condition, same parameters.
Only the update rule changes.
Left: Localization (HEM) / Right: Smoothing (diffusion-like)
"""

import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# ── HEM Simulation ───────────────────────────────────────────

def run_simulation(N, dt, k, steps, mode="localize"):
    """
    Run 1D simulation.
    mode = "localize" → amplify difference (HEM)
    mode = "smooth"   → reduce difference (diffusion)
    """
    state = [0.0] * N
    state[N // 2] = 0.1  # Seed: small perturbation at center

    history = [state.copy()]

    for _ in range(steps):
        new_state = state.copy()

        for i in range(1, N - 1):
            neighbor_avg = (state[i - 1] + state[i + 1]) / 2.0

            if mode == "localize":
                diff = state[i] - neighbor_avg   # amplify: HEM
            else:
                diff = neighbor_avg - state[i]   # reduce: smoothing

            new_state[i] = state[i] + dt * k * diff

        state = new_state
        history.append(state.copy())

    return history

# ── GUI ──────────────────────────────────────────────────────

root = tk.Tk()
root.title("Shardhana — Localization vs Smoothing")
root.configure(bg="#1e1e2e")

# ── Header ───────────────────────────────────────────────────
tk.Label(
    root, text="Shardhana · Localization vs Smoothing",
    bg="#1e1e2e", fg="#cdd6f4",
    font=("Arial", 14, "bold"), pady=10
).pack()

# ── Input Panel ──────────────────────────────────────────────
input_frame = tk.Frame(root, bg="#313244", padx=16, pady=12)
input_frame.pack(fill="x", padx=20, pady=(0, 10))

def labeled_entry(parent, label, default):
    frame = tk.Frame(parent, bg="#313244")
    frame.pack(side="left", padx=12)
    tk.Label(frame, text=label, bg="#313244", fg="#a6adc8",
             font=("Arial", 10)).pack()
    var = tk.StringVar(value=str(default))
    tk.Entry(frame, textvariable=var, width=6,
             bg="#45475a", fg="#cdd6f4",
             insertbackground="#cdd6f4",
             font=("Arial", 11), justify="center",
             relief="flat").pack()
    return var

var_N     = labeled_entry(input_frame, "Elements (N)", 20)
var_dt    = labeled_entry(input_frame, "dt", 1.0)
var_k     = labeled_entry(input_frame, "k", 0.5)
var_steps = labeled_entry(input_frame, "Steps", 15)

# ── Plot Area (side by side) ──────────────────────────────────
fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(12, 4))
fig.patch.set_facecolor("#1e1e2e")

for ax in (ax_left, ax_right):
    ax.set_facecolor("#181825")

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(padx=20, pady=(0, 10), fill="both", expand=True)

# ── Status ───────────────────────────────────────────────────
status_var = tk.StringVar(value="Ready.")
tk.Label(root, textvariable=status_var,
         bg="#1e1e2e", fg="#a6e3a1",
         font=("Arial", 10), pady=4).pack()

# ── Plot Helper ──────────────────────────────────────────────
def plot_history(ax, history, N, steps, title, color_final):
    step_0   = 0
    step_mid = steps // 2
    step_end = steps
    x = list(range(N))

    ax.clear()
    ax.set_facecolor("#181825")
    ax.plot(x, history[step_0],   color="#89b4fa", linewidth=1.5,
            marker="o", markersize=4, label=f"Step {step_0}")
    ax.plot(x, history[step_mid], color="#fab387", linewidth=1.5,
            marker="o", markersize=4, label=f"Step {step_mid}")
    ax.plot(x, history[step_end], color=color_final, linewidth=2.0,
            marker="o", markersize=5, label=f"Step {step_end}")

    ax.set_title(title, color="#cdd6f4", fontsize=11)
    ax.set_xlabel("Element Index", color="#a6adc8")
    ax.set_ylabel("State Value", color="#a6adc8")
    ax.tick_params(colors="#a6adc8")
    ax.spines[:].set_color("#45475a")
    ax.legend(facecolor="#313244", labelcolor="#cdd6f4", fontsize=9)
    ax.grid(True, color="#313244", linestyle="--", linewidth=0.5)

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

    hist_loc   = run_simulation(N, dt, k, steps, mode="localize")
    hist_smooth = run_simulation(N, dt, k, steps, mode="smooth")

    plot_history(ax_left,  hist_loc,    N, steps,
                 "Localization (HEM)", "#f38ba8")
    plot_history(ax_right, hist_smooth, N, steps,
                 "Smoothing (Diffusion)", "#a6e3a1")

    fig.tight_layout()
    canvas.draw()

    status_var.set(
        f"✔ Done — N={N}, dt={dt}, k={k}, steps={steps}  |  "
        f"Center final: Localize={hist_loc[-1][N//2]:.3f}  "
        f"Smooth={hist_smooth[-1][N//2]:.3f}"
    )

tk.Button(
    root, text="▶  Run Comparison",
    bg="#89b4fa", fg="#1e1e2e",
    font=("Arial", 11, "bold"),
    relief="flat", padx=20, pady=6,
    cursor="hand2",
    command=on_run
).pack(pady=(0, 16))

root.mainloop()