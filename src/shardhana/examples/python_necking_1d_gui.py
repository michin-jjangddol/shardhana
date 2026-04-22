"""
necking_1d_gui.py
Shardhana — 1D HEM Prototype with GUI + Graph

Rule-based localization visualization.
No FEM, no stiffness matrix.
Uses tkinter + matplotlib embedded in GUI.

v2: Each seed now carries geometric properties (length, area, volume)
    and contact-face values (face_left, face_right).
    State change → geometry update → contact-face update.
"""

import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# ── Seed ─────────────────────────────────────────────────────

class Seed:
    """
    Represents a single element in the 1D HEM model.

    Geometry concept: cuboid-like (expandable toward 2D/3D)
    Contact faces: left / right (1D simplification of face set)

    Fields:
        state      — scalar state value (e.g. damage, strain)
        length     — seed length (deforms with state)
        area       — cross-sectional area (default: 1.0)
        volume     — length * area (updated automatically)
        face_left  — contact area on left face
        face_right — contact area on right face
    """

    def __init__(self, length=1.0, area=1.0):
        self.state      = 0.0
        self.length     = length
        self.area       = area
        self.volume     = length * area
        self.face_left  = area   # default: full contact
        self.face_right = area

    def update_geometry(self, state_diff, geo_k=0.1):
        """
        Update geometry based on state change.

        - length grows slightly when state increases (localization → elongation)
        - volume follows from length * area
        - contact-face area reduces when state gap is large (damage proxy)

        state_diff: abs difference between this seed and neighbor avg
        geo_k:      geometry sensitivity (keep small)
        """
        # Length change: state increase → slight elongation
        self.length = max(0.01, self.length + geo_k * self.state)

        # Volume follows geometry
        self.volume = self.length * self.area

        # Contact face degrades with increasing state gap
        damage_factor = max(0.0, 1.0 - state_diff)
        self.face_left  = self.area * damage_factor
        self.face_right = self.area * damage_factor


# ── HEM Simulation ───────────────────────────────────────────

def run_hem(N, dt, k, steps):
    """
    Run 1D HEM simulation with geometry.
    Returns:
        state_history   — list of state snapshots per step
        volume_history  — list of volume snapshots per step
        face_history    — list of face_right snapshots per step
    """
    # Initialize seeds
    seeds = [Seed(length=1.0, area=1.0) for _ in range(N)]
    seeds[N // 2].state = 0.1  # Seed: small perturbation at center

    def snapshot(attr):
        return [getattr(s, attr) for s in seeds]

    state_history  = [snapshot("state")]
    volume_history = [snapshot("volume")]
    face_history   = [snapshot("face_right")]

    for _ in range(steps):
        new_states = [s.state for s in seeds]  # copy current states

        for i in range(1, N - 1):
            neighbor_avg = (seeds[i - 1].state + seeds[i + 1].state) / 2.0

            # Contact-face weighted interaction
            # face value acts as a conductance between seeds
            face_weight = (seeds[i].face_left + seeds[i].face_right) / (2.0 * seeds[i].area)
            face_weight = max(0.01, face_weight)  # avoid zero

            diff = seeds[i].state - neighbor_avg  # HEM: amplify
            new_states[i] = seeds[i].state + dt * k * face_weight * diff

        # Apply new states and update geometry
        for i in range(1, N - 1):
            seeds[i].state = new_states[i]
            neighbor_avg = (seeds[i - 1].state + seeds[i + 1].state) / 2.0
            state_diff = abs(seeds[i].state - neighbor_avg)
            seeds[i].update_geometry(state_diff)

        state_history.append(snapshot("state"))
        volume_history.append(snapshot("volume"))
        face_history.append(snapshot("face_right"))

    return state_history, volume_history, face_history


# ── GUI ──────────────────────────────────────────────────────

root = tk.Tk()
root.title("Shardhana — 1D HEM Prototype")
root.configure(bg="#1e1e2e")

# ── Header ───────────────────────────────────────────────────
tk.Label(
    root, text="Shardhana · 1D HEM Simulation (v2 — Geometry)",
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

# ── Plot Area (3 subplots: state / volume / face) ────────────
fig, (ax_state, ax_vol, ax_face) = plt.subplots(1, 3, figsize=(14, 4))
fig.patch.set_facecolor("#1e1e2e")
for ax in (ax_state, ax_vol, ax_face):
    ax.set_facecolor("#181825")

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(padx=20, pady=(0, 10), fill="both", expand=True)

# ── Status ───────────────────────────────────────────────────
status_var = tk.StringVar(value="Ready.")
tk.Label(root, textvariable=status_var,
         bg="#1e1e2e", fg="#a6e3a1",
         font=("Arial", 10), pady=4).pack()

# ── Plot Helper ──────────────────────────────────────────────
def plot_panel(ax, history, steps, title, color_final, ylabel):
    step_mid = steps // 2
    x = list(range(len(history[0])))

    ax.clear()
    ax.set_facecolor("#181825")
    ax.plot(x, history[0],        color="#89b4fa", linewidth=1.5,
            marker="o", markersize=3, label="Step 0")
    ax.plot(x, history[step_mid], color="#fab387", linewidth=1.5,
            marker="o", markersize=3, label=f"Step {step_mid}")
    ax.plot(x, history[steps],    color=color_final, linewidth=2.0,
            marker="o", markersize=4, label=f"Step {steps}")
    ax.set_title(title, color="#cdd6f4", fontsize=10)
    ax.set_xlabel("Element Index", color="#a6adc8")
    ax.set_ylabel(ylabel, color="#a6adc8")
    ax.tick_params(colors="#a6adc8")
    ax.spines[:].set_color("#45475a")
    ax.legend(facecolor="#313244", labelcolor="#cdd6f4", fontsize=8)
    ax.grid(True, color="#313244", linestyle="--", linewidth=0.5)

# ── Run ──────────────────────────────────────────────────────
def on_run():
    try:
        N     = int(var_N.get())
        dt    = float(var_dt.get())
        k     = float(var_k.get())
        steps = int(var_steps.get())
    except ValueError:
        status_var.set("⚠ Invalid input. Please check parameters.")
        return

    state_h, vol_h, face_h = run_hem(N, dt, k, steps)

    plot_panel(ax_state, state_h, steps,
               "State (Localization)", "#f38ba8", "State Value")
    plot_panel(ax_vol,   vol_h,   steps,
               "Volume Change",        "#cba6f7", "Volume")
    plot_panel(ax_face,  face_h,  steps,
               "Contact Face (right)", "#a6e3a1", "Face Area")

    fig.tight_layout()
    canvas.draw()

    status_var.set(
        f"✔ Done — N={N}, dt={dt}, k={k}, steps={steps}  |  "
        f"Center: state={state_h[-1][N//2]:.4f}  "
        f"vol={vol_h[-1][N//2]:.4f}  "
        f"face={face_h[-1][N//2]:.4f}"
    )

tk.Button(
    root, text="▶  Run Simulation",
    bg="#89b4fa", fg="#1e1e2e",
    font=("Arial", 11, "bold"),
    relief="flat", padx=20, pady=6,
    cursor="hand2",
    command=on_run
).pack(pady=(0, 16))

root.mainloop()