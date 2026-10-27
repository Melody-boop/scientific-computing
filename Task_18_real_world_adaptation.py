
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Backup-power circuit parameters
Vs = 12.0
R = 2200.0
C = 0.002
V0 = 0.0
total_time = 20.0

def capacitor_charging(t, V):
    return [(Vs - V[0]) / (R * C)]

time_points = np.linspace(0, total_time, 200)

solution = solve_ivp(
    capacitor_charging,
    (0, total_time),
    [V0],
    t_eval=time_points,
    rtol=1e-9,
    atol=1e-11
)

exact = Vs * (1 - np.exp(-solution.t / (R * C)))

print("Backup-Power Capacitor Charging")
print("Solver success:", solution.success)
print(f"Supply voltage: {Vs:.2f} V")
print(f"Capacitance: {C:.4f} F")
print(f"Resistance: {R:.0f} ohms")
print(
    f"Capacitor voltage after {total_time:.0f} s: "
    f"{solution.y[0, -1]:.4f} V"
)
print(
    "Maximum error against exact solution: "
    f"{np.max(np.abs(solution.y[0] - exact)):.3e} V"
)

plt.figure(figsize=(9, 5))
plt.plot(solution.t, solution.y[0], label="solve_ivp numerical solution")
plt.plot(solution.t, exact, "--", label="Exact solution")
plt.axhline(Vs, linestyle=":", label="Supply voltage")
plt.xlabel("Time (s)")
plt.ylabel("Capacitor voltage (V)")
plt.title("Backup-Power Capacitor Charging")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("Task_18_real_world_adaptation.png", dpi=300)
print("Graph saved as Task_18_real_world_adaptation.png")
