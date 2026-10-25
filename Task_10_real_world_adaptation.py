
import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

# Real-world scenario:
# Estimate the equilibrium temperature of a room
# when heat supplied balances heat lost.
def room_heat_balance(T):
    heat_supplied = 12 * np.exp(-T / 25)
    heat_lost = T - 20
    return heat_lost - heat_supplied

# Find the root using the bisection method
solution = root_scalar(
    room_heat_balance,
    bracket=[20, 40],
    method="bisect",
    xtol=1e-10
)

# Fixed-point form:
# T = 20 + 12*exp(-T/25)
def g(T):
    return 20 + 12 * np.exp(-T / 25)

T = 25.0
history = [T]

for _ in range(100):
    T_new = g(T)
    history.append(T_new)

    if abs(T_new - T) < 1e-10:
        break

    T = T_new

print(f"Bisection equilibrium room temperature: {solution.root:.6f} C")
print(f"Fixed-point equilibrium room temperature: {history[-1]:.6f} C")
print("Fixed-point iterations:", len(history) - 1)

# Plot the room heat-balance function
temps = np.linspace(20, 40, 300)
plt.plot(temps, room_heat_balance(temps))
plt.axhline(0, linewidth=0.8)
plt.axvline(solution.root, linestyle="--")
plt.xlabel("Room temperature (C)")
plt.ylabel("Heat-balance function")
plt.title("Room Heating System Equilibrium")
plt.grid(True)

plt.savefig(
    "Task_10_real_world_adaptation.png",
    dpi=300,
    bbox_inches="tight"
)
print("Graph saved as Task_10_real_world_adaptation.png")
