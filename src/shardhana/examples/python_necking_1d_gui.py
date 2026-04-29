"""
necking_1d_gui.py
Shardhana — 1D HEM Prototype with GUI + Graph

Rule-based localization visualization.
No FEM, no stiffness matrix.
Uses tkinter + matplotlib embedded in GUI.

v2:  Seed geometry (length, area, volume, face_left, face_right)
v3:  Seed-level fracture (broken flag per seed)
v3a: Neighbor face freeze on broken seed
v3b: Interface fracture model (binary fractured flag)
v3c: Continuous interface stiffness model.
     Fracture is NOT a boolean event.
     It is a process: Contact → Damage → Opening → Space
     - interface.k replaces interface.fractured
     - k = f(face_right) → decreases as face degrades
     - interaction weighted by k, never fully blocked
     - visualization: k value shown as color intensity
"""

import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# ── Constants ─────────────────────────────────────────────────
K_CONTACT = 1.0    # full contact stiffness
K_SPACE   = 1e-6   # near-zero (air / open crack)
K_VIZ_THRESHOLD = 0.2  # visualization only: mark interface when k < this

# ── Seed ─────────────────────────────────────────────────────

class Seed:
    """
    Represents a single element in the 1D HEM model.

    Fields:
        state      — scalar state value
        length     — seed length
        area       — cross-sectional area
        volume     — length * area
        face_left  — contact area on left face
        face_right — contact area on right face
    """

    def __init__(self, length=1.0, area=1.0):
        self.state      = 0.0
        self.length     = length
        self.area       = area
        self.volume     = length * area
        self.face_left  = area
        self.face_right = area

    def update_geometry(self, state_diff, geo_k=0.1):
        """
        Update geometry based on state change.
        Face reduction is continuous — no binary freeze.
        """
        self.length = max(0.01, self.length + geo_k * self.state)
        self.volume = self.length * self.area

        damage_factor = max(0.0, 1.0 - state_diff)
        self.face_left  = self.area * damage_factor
        self.face_right = self.area * damage_factor


# ── Interface ─────────────────────────────────────────────────

class Interface:
    """
    Represents the contact between seed[i] and seed[i+1].

    v3c: Replaces binary fractured flag with continuous stiffness k.

    k evolves with face degradation:
        k = K_CONTACT  → full contact
        k → K_SPACE    → near-open crack / space

    Fracture is a process, not an event.
    """

    def __init__(self):
        self.k = K_CONTACT  # start fully connected

    def update(self, face_right_i, area):
        """
        Update k based on face_right of seed[i].
        k tracks face degradation smoothly.
        Never drops below K_SPACE.
        """
        normalized = face_right_i / area  # 0.0 ~ 1.0
        self.k = max(K_SPACE, normalized * K_CONTACT)

    @property
    def is_weak(self):
        """Visualization helper: True when k drops below threshold."""
        return self.k < K_VIZ_THRESHOLD


# ── HEM Simulation ───────────────────────────────────────────

def run_hem(N, dt, k_amp, steps):
    """
    Run 1D HEM simulation with continuous interface stiffness (v3c).

    Args:
        k_amp: amplification factor (GUI input 'k')

    Returns:
        state_history     — state snapshots per step
        volume_history    — volume snapshots per step
        face_history      — face_right snapshots per step
        ifc_k_history     — interface k snapshots per step (length N-1)
    """
    seeds      = [Seed(length=1.0, area=1.0) for _ in range(N)]
    interfaces = [Interface() for _ in range(N - 1)]

    seeds[N // 2].state = 0.1  # perturbation at center

    def snap_seeds(attr):
        return [getattr(s, attr) for s in seeds]

    def snap_ifc_k():
        return [ifc.k for ifc in interfaces]

    state_history  = [snap_seeds("state")]
    volume_history = [snap_seeds("volume")]
    face_history   = [snap_seeds("face_right")]
    ifc_k_history  = [snap_ifc_k()]

    for step in range(steps):
        new_states = [s.state for s in seeds]

        # ── Interaction step ─────────────────────────────────
        for i in range(1, N - 1):
            k_left  = interfaces[i - 1].k  # stiffness from left
            k_right = interfaces[i].k       # stiffness from right

            total_k = k_left + k_right
            if total_k < K_SPACE * 2:
                continue  # effectively isolated

            # Weighted neighbor average by interface stiffness
            neighbor_avg = (k_left  * seeds[i - 1].state +
                            k_right * seeds[i + 1].state) / total_k

            # Face weight — how much this seed conducts
            face_weight = (k_left + k_right) / (2.0 * K_CONTACT)
            face_weight = max(K_SPACE, face_weight)

            diff = seeds[i].state - neighbor_avg
            new_states[i] = seeds[i].state + dt * k_amp * face_weight * diff

        # ── Geometry update step ─────────────────────────────
        for i in range(1, N - 1):
            seeds[i].state = new_states[i]

            k_left  = interfaces[i - 1].k
            k_right = interfaces[i].k
            total_k = k_left + k_right

            if total_k > K_SPACE * 2:
                neighbor_avg = (k_left  * seeds[i - 1].state +
                                k_right * seeds[i + 1].state) / total_k
            else:
                neighbor_avg = seeds[i].state

            state_diff = abs(seeds[i].state - neighbor_avg)
            seeds[i].update_geometry(state_diff)

        # ── Interface k update ───────────────────────────────
        # k follows face_right of seed[i] (left seed of interface)
        for i in range(N - 1):
            interfaces[i].update(seeds[i].face_right, seeds[i].area)

        state_history.append(snap_seeds("state"))
        volume_history.append(snap_seeds("volume"))
        face_history.append(snap_seeds("face_right"))
        ifc_k_history.append(snap_ifc_k())

    return state_history, volume_history, face_history, ifc_k_history


# ── GUI ──────────────────────────────────────────────────────

root = tk.Tk()
root.title("Shardhana — 1D HEM Prototype")
root.configure(bg="#1e1e2e")

tk.Label(
    root, text="Shardhana · 1D HEM Simulation (v3c — Continuous Interface k)",
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

# ── Plot Area ────────────────────────────────────────────────
fig, (ax_state, ax_vol, ax_face) = plt.subplots(1, 3, figsize=(14, 4))
fig.patch.set_facecolor("#1e1e2e")
for ax in (ax_state, ax_vol, ax_face):
    ax.set_facecolor("#181825")

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(padx=20, pady=(0, 10), fill="both", expand=True)

status_var = tk.StringVar(value="Ready.")
tk.Label(root, textvariable=status_var,
         bg="#1e1e2e", fg="#a6e3a1",
         font=("Arial", 10), pady=4).pack()

# ── Plot Helpers ─────────────────────────────────────────────
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

def plot_ifc_panel(ax, ifc_k_history, steps):
    """
    Visualize interface stiffness k over element index.
    - x axis: interface position (i + 0.5)
    - y axis: k value
    - color: intensity reflects damage level
    - dashed line: visualization threshold
    """
    step_mid = steps // 2
    N_ifc = len(ifc_k_history[0])
    x = [i + 0.5 for i in range(N_ifc)]

    ax.clear()
    ax.set_facecolor("#181825")

    ax.plot(x, ifc_k_history[0],        color="#89b4fa", linewidth=1.5,
            marker="o", markersize=3, label="Step 0")
    ax.plot(x, ifc_k_history[step_mid], color="#fab387", linewidth=1.5,
            marker="o", markersize=3, label=f"Step {step_mid}")
    ax.plot(x, ifc_k_history[steps],    color="#a6e3a1", linewidth=2.0,
            marker="o", markersize=4, label=f"Step {steps}")

    # Visualization threshold line
    ax.axhline(y=K_VIZ_THRESHOLD, color="#f38ba8", linewidth=1.2,
               linestyle="--", label=f"weak threshold={K_VIZ_THRESHOLD}")

    # Mark weak interfaces at final step
    final_k = ifc_k_history[steps]
    weak_x = [x[i] for i, kv in enumerate(final_k) if kv < K_VIZ_THRESHOLD]
    weak_y = [kv     for kv in final_k              if kv < K_VIZ_THRESHOLD]
    if weak_x:
        ax.scatter(weak_x, weak_y, color="#f38ba8", marker="x",
                   s=100, linewidths=2.5, zorder=5, label="Weak interface")

    ax.set_title("Interface Stiffness k  (Contact → Space)", color="#cdd6f4", fontsize=10)
    ax.set_xlabel("Interface Position (between i and i+1)", color="#a6adc8")
    ax.set_ylabel("k value", color="#a6adc8")
    ax.tick_params(colors="#a6adc8")
    ax.spines[:].set_color("#45475a")
    ax.legend(facecolor="#313244", labelcolor="#cdd6f4", fontsize=8)
    ax.grid(True, color="#313244", linestyle="--", linewidth=0.5)

# ── Run ──────────────────────────────────────────────────────
def on_run():
    try:
        N     = int(var_N.get())
        dt    = float(var_dt.get())
        k_amp = float(var_k.get())
        steps = int(var_steps.get())
    except ValueError:
        status_var.set("⚠ Invalid input. Please check parameters.")
        return

    state_h, vol_h, face_h, ifc_k_h = run_hem(N, dt, k_amp, steps)

    plot_panel(ax_state, state_h, steps,
               "State (Localization)", "#f38ba8", "State Value")
    plot_panel(ax_vol,   vol_h,   steps,
               "Volume Change",        "#cba6f7", "Volume")
    plot_ifc_panel(ax_face, ifc_k_h, steps)

    fig.tight_layout()
    canvas.draw()

    # Find weakest interface at final step
    final_k   = ifc_k_h[steps]
    min_k     = min(final_k)
    min_k_idx = final_k.index(min_k)
    weak_count = sum(1 for kv in final_k if kv < K_VIZ_THRESHOLD)

    status_var.set(
        f"✔ Done — N={N}, dt={dt}, k={k_amp}, steps={steps}  |  "
        f"Center state={state_h[-1][N//2]:.4f}  "
        f"face={face_h[-1][N//2]:.4f}  |  "
        f"Weakest interface: [{min_k_idx}↔{min_k_idx+1}] k={min_k:.4f}  |  "
        f"Weak interfaces (<{K_VIZ_THRESHOLD}): {weak_count}"
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
