
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# RC circuit parameters
Vs = 5.0
R = 1000.0
C = 0.001
V0 = 0.0

# Differential equation for capacitor charging
def rc_circuit(t, V):
    return [(Vs - V[0]) / (R * C)]

# Solve the differential equation
t_eval = np.linspace(0, 5, 200)

solution = solve_ivp(
    rc_circuit,
    (0, 5),
    [V0],
    t_eval=t_eval,
    rtol=1e-9,
    atol=1e-11
)

# Exact solution for comparison
exact = Vs * (1 - np.exp(-solution.t / (R * C)))

# Display results
print("RC Circuit Charging Using solve_ivp")
print("Solver success:", solution.success)
print(f"Capacitor voltage at 5 s: {solution.y[0, -1]:.4f} V")
print(
    "Maximum error against exact solution: "
    f"{np.max(np.abs(solution.y[0] - exact)):.3e} V"
)

# Plot and save the results
plt.figure(figsize=(9, 5))
plt.plot(solution.t, solution.y[0], label="solve_ivp numerical solution")
plt.plot(solution.t, exact, "--", label="Exact solution")
plt.xlabel("Time (s)")
plt.ylabel("Capacitor voltage (V)")
plt.title("RC Circuit Charging")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("Task_18_ode_solution.png", dpi=300)
print("Graph saved as Task_18_ode_solution.png")
