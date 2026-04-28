"""
necking_1d_gui.py
Shardhana — 1D HEM Prototype with GUI + Graph

Rule-based localization visualization.
No FEM, no stiffness matrix.
Uses tkinter + matplotlib embedded in GUI.

v2: Each seed now carries geometric properties (length, area, volume)
    and contact-face values (face_left, face_right).
    State change → geometry update → contact-face update.

v3: Fracture logic added.
    - face < face_threshold → broken = True
    - Broken seeds excluded from neighbor interaction
    - Adjacent seeds' faces unchanged (no auto-cascade)
    - Broken seeds shown as red X in contact face plot
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
        state          — scalar state value (e.g. damage, strain)
        length         — seed length (deforms with state)
        area           — cross-sectional area (default: 1.0)
        volume         — length * area (updated automatically)
        face_left      — contact area on left face
        face_right     — contact area on right face
        broken         — True if fracture condition is met
        face_threshold — face area below which fracture triggers
    """

    FACE_THRESHOLD = 0.2  # fixed fracture threshold

    def __init__(self, length=1.0, area=1.0):
        self.state      = 0.0
        self.length     = length
        self.area       = area
        self.volume     = length * area
        self.face_left  = area   # default: full contact
        self.face_right = area
        self.broken     = False  # fracture flag

    def update_geometry(self, state_diff, geo_k=0.1):
        """
        Update geometry based on state change.
        If already broken, skip geometry update (frozen state).

        state_diff: abs difference between this seed and neighbor avg
        geo_k:      geometry sensitivity (keep small)
        """
        if self.broken:
            return  # broken seeds are frozen

        # Length change: state increase → slight elongation
        self.length = max(0.01, self.length + geo_k * self.state)

        # Volume follows geometry
        self.volume = self.length * self.area

        # Contact face degrades with increasing state gap
        damage_factor = max(0.0, 1.0 - state_diff)
        self.face_left  = self.area * damage_factor
        self.face_right = self.area * damage_factor

        # ── Fracture check ──────────────────────────────────
        # If either face drops below threshold → fracture
        if self.face_left < self.FACE_THRESHOLD or \
           self.face_right < self.FACE_THRESHOLD:
            self.broken = True


# ── HEM Simulation ───────────────────────────────────────────

def run_hem(N, dt, k, steps):
    """
    Run 1D HEM simulation with geometry + fracture.

    Returns:
        state_history   — list of state snapshots per step
        volume_history  — list of volume snapshots per step
        face_history    — list of face_right snapshots per step
        broken_history  — list of broken-flag snapshots per step
        fracture_step   — step index when first fracture occurred (or None)
    """
    # Initialize seeds
    seeds = [Seed(length=1.0, area=1.0) for _ in range(N)]
    seeds[N // 2].state = 0.1  # perturbation at center

    def snapshot(attr):
        return [getattr(s, attr) for s in seeds]

    state_history  = [snapshot("state")]
    volume_history = [snapshot("volume")]
    face_history   = [snapshot("face_right")]
    broken_history = [snapshot("broken")]

    fracture_step = None  # track when first fracture happens

    for step in range(steps):
        new_states = [s.state for s in seeds]  # copy

        for i in range(1, N - 1):
            # ── Skip broken seeds entirely ──────────────────
            if seeds[i].broken:
                continue

            # Build neighbor average, also skip broken neighbors
            left_state  = seeds[i - 1].state if not seeds[i - 1].broken else seeds[i].state
            right_state = seeds[i + 1].state if not seeds[i + 1].broken else seeds[i].state
            neighbor_avg = (left_state + right_state) / 2.0

            # Contact-face weighted interaction
            face_weight = (seeds[i].face_left + seeds[i].face_right) / (2.0 * seeds[i].area)
            face_weight = max(0.01, face_weight)

            diff = seeds[i].state - neighbor_avg
            new_states[i] = seeds[i].state + dt * k * face_weight * diff

        # Apply new states + update geometry
        for i in range(1, N - 1):
            if seeds[i].broken:
                continue  # frozen — don't update

            seeds[i].state = new_states[i]

            # Neighbor avg for geometry (broken neighbors ignored)
            left_state  = seeds[i - 1].state if not seeds[i - 1].broken else seeds[i].state
            right_state = seeds[i + 1].state if not seeds[i + 1].broken else seeds[i].state
            neighbor_avg = (left_state + right_state) / 2.0

            state_diff = abs(seeds[i].state - neighbor_avg)
            seeds[i].update_geometry(state_diff)

        # Track first fracture step
        if fracture_step is None and any(s.broken for s in seeds):
            fracture_step = step + 1

        state_history.append(snapshot("state"))
        volume_history.append(snapshot("volume"))
        face_history.append(snapshot("face_right"))
        broken_history.append(snapshot("broken"))

    return state_history, volume_history, face_history, broken_history, fracture_step


# ── GUI ──────────────────────────────────────────────────────

root = tk.Tk()
root.title("Shardhana — 1D HEM Prototype")
root.configure(bg="#1e1e2e")

# ── Header ───────────────────────────────────────────────────
tk.Label(
    root, text="Shardhana · 1D HEM Simulation (v3 — Fracture)",
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

# ── Plot Helper (state / volume) ─────────────────────────────
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

# ── Contact Face Plot (with threshold line + broken markers) ─
def plot_face_panel(ax, face_history, broken_history, steps):
    step_mid = steps // 2
    x = list(range(len(face_history[0])))

    ax.clear()
    ax.set_facecolor("#181825")

    # Plot face curves
    ax.plot(x, face_history[0],        color="#89b4fa", linewidth=1.5,
            marker="o", markersize=3, label="Step 0")
    ax.plot(x, face_history[step_mid], color="#fab387", linewidth=1.5,
            marker="o", markersize=3, label=f"Step {step_mid}")
    ax.plot(x, face_history[steps],    color="#a6e3a1", linewidth=2.0,
            marker="o", markersize=4, label=f"Step {steps}")

    # Threshold line
    ax.axhline(y=Seed.FACE_THRESHOLD, color="#f38ba8", linewidth=1.2,
               linestyle="--", label=f"threshold={Seed.FACE_THRESHOLD}")

    # Mark broken seeds at final step with red X
    final_broken = broken_history[steps]
    final_face   = face_history[steps]
    broken_x     = [i for i, b in enumerate(final_broken) if b]
    broken_y     = [final_face[i] for i in broken_x]
    if broken_x:
        ax.scatter(broken_x, broken_y, color="#f38ba8", marker="x",
                   s=80, linewidths=2, zorder=5, label="Broken")

    ax.set_title("Contact Face (right) + Fracture", color="#cdd6f4", fontsize=10)
    ax.set_xlabel("Element Index", color="#a6adc8")
    ax.set_ylabel("Face Area", color="#a6adc8")
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

    state_h, vol_h, face_h, broken_h, fracture_step = run_hem(N, dt, k, steps)

    plot_panel(ax_state, state_h, steps,
               "State (Localization)", "#f38ba8", "State Value")
    plot_panel(ax_vol,   vol_h,   steps,
               "Volume Change",        "#cba6f7", "Volume")
    plot_face_panel(ax_face, face_h, broken_h, steps)

    fig.tight_layout()
    canvas.draw()

    # Count broken seeds at final step
    broken_count = sum(broken_h[steps])
    broken_ids   = [i for i, b in enumerate(broken_h[steps]) if b]

    frac_info = (f"First fracture @ step {fracture_step}"
                 if fracture_step else "No fracture")

    status_var.set(
        f"✔ Done — N={N}, dt={dt}, k={k}, steps={steps}  |  "
        f"Center: state={state_h[-1][N//2]:.4f}  "
        f"vol={vol_h[-1][N//2]:.4f}  "
        f"face={face_h[-1][N//2]:.4f}  |  "
        f"{frac_info}  |  Broken seeds: {broken_count} {broken_ids}"
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