import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Grid resolution
N = 40

phi   = np.linspace(0, np.pi / 2, N)   # 0 → π/2  (from z-axis downward)
theta = np.linspace(0, np.pi / 2, N)   # 0 → π/2  (around z-axis, first octant)

PHI, THETA = np.meshgrid(phi, theta)

def spherical_to_cartesian(rho, PHI, THETA):
    x = rho * np.sin(PHI) * np.cos(THETA)
    y = rho * np.sin(PHI) * np.sin(THETA)
    z = rho * np.cos(PHI)
    return x, y, z

# ── surface colours ──────────────────────────────────────────────────────────
OUTER_COLOR = "#4a90d9"   # steel-blue  – outer sphere (ρ = 3)
INNER_COLOR = "#f0a500"   # amber       – inner sphere (ρ = 2)
FLAT_COLOR  = "#a8d8a8"   # sage-green  – flat faces (coordinate planes)
ALPHA_SHELL = 0.55
ALPHA_FLAT  = 0.45

fig = plt.figure(figsize=(10, 8))
ax  = fig.add_subplot(111, projection="3d")

# ── 1. Outer spherical surface (ρ = 3) ───────────────────────────────────────
x3, y3, z3 = spherical_to_cartesian(3, PHI, THETA)
ax.plot_surface(x3, y3, z3, color=OUTER_COLOR, alpha=ALPHA_SHELL,
                linewidth=0, label="Outer sphere ρ=3")

# ── 2. Inner spherical surface (ρ = 2) ───────────────────────────────────────
x2, y2, z2 = spherical_to_cartesian(2, PHI, THETA)
ax.plot_surface(x2, y2, z2, color=INNER_COLOR, alpha=ALPHA_SHELL,
                linewidth=0, label="Inner sphere ρ=2")

# ── Flat-face helpers ─────────────────────────────────────────────────────────
rho   = np.linspace(2, 3, N)
angle = np.linspace(0, np.pi / 2, N)
RHO, ANG = np.meshgrid(rho, angle)

# ── 3. Face on the xz-plane  (θ = 0,  y = 0) ─────────────────────────────────
#    x = ρ sinφ,  y = 0,  z = ρ cosφ
ax.plot_surface(
    RHO * np.sin(ANG),          # x
    np.zeros_like(RHO),         # y = 0
    RHO * np.cos(ANG),          # z
    color=FLAT_COLOR, alpha=ALPHA_FLAT, linewidth=0,
)

# ── 4. Face on the yz-plane  (θ = π/2,  x = 0) ───────────────────────────────
#    x = 0,  y = ρ sinφ,  z = ρ cosφ
ax.plot_surface(
    np.zeros_like(RHO),         # x = 0
    RHO * np.sin(ANG),          # y
    RHO * np.cos(ANG),          # z
    color=FLAT_COLOR, alpha=ALPHA_FLAT, linewidth=0,
)

# ── 5. Face on the xy-plane  (φ = π/2,  z = 0) ───────────────────────────────
#    x = ρ cosθ,  y = ρ sinθ,  z = 0
ax.plot_surface(
    RHO * np.cos(ANG),          # x
    RHO * np.sin(ANG),          # y
    np.zeros_like(RHO),         # z = 0
    color=FLAT_COLOR, alpha=ALPHA_FLAT, linewidth=0,
)

# ── Axis labels and limits ────────────────────────────────────────────────────
ax.set_xlabel("x", fontsize=12, labelpad=6)
ax.set_ylabel("y", fontsize=12, labelpad=6)
ax.set_zlabel("z", fontsize=12, labelpad=6)
ax.set_xlim(0, 3.2)
ax.set_ylim(0, 3.2)
ax.set_zlim(0, 3.2)
ax.set_title(
    "Spherical Shell Wedge — First Octant\n"
    r"$2 \leq \rho \leq 3,\quad 0 \leq \varphi \leq \pi/2,\quad 0 \leq \theta \leq \pi/2$",
    fontsize=11, pad=14,
)

# ── Legend (manual patches) ───────────────────────────────────────────────────
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor=OUTER_COLOR, alpha=0.8, label=r"Outer sphere ($\rho = 3$)"),
    Patch(facecolor=INNER_COLOR, alpha=0.8, label=r"Inner sphere ($\rho = 2$)"),
    Patch(facecolor=FLAT_COLOR,  alpha=0.8, label="Flat faces (coordinate planes)"),
]
ax.legend(handles=legend_elements, loc="upper left", fontsize=9)

ax.view_init(elev=20, azim=35)
plt.tight_layout()
plt.savefig("spherical_shell_wedge.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved → spherical_shell_wedge.png")
