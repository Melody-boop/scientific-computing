
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson

# Household electricity readings every two hours
time_hours = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)
power_kw = np.array([0.3, 0.5, 1.2, 1.8, 1.4, 0.8, 0.4])

# Numerical integration estimates energy consumption
energy_trapezoid = np.trapezoid(power_kw, time_hours)
energy_simpson = simpson(power_kw, x=time_hours)

print("Household Electricity Consumption")
print(f"Energy using trapezoidal rule: {energy_trapezoid:.3f} kWh")
print(f"Energy using Simpson's rule:   {energy_simpson:.3f} kWh")
print(
    f"Difference between estimates: "
    f"{abs(energy_simpson - energy_trapezoid):.3f} kWh"
)

plt.figure(figsize=(9, 5))
plt.plot(time_hours, power_kw, marker="o")
plt.fill_between(time_hours, power_kw, alpha=0.2)
plt.xlabel("Time (hours)")
plt.ylabel("Power consumption (kW)")
plt.title("Household Power Consumption Over 12 Hours")
plt.grid(True)
plt.tight_layout()
plt.savefig("Task_16_real_world_adaptation.png", dpi=300)
print("Graph saved as Task_16_real_world_adaptation.png")
