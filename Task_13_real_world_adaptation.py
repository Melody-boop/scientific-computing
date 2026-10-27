
import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

# Simulated hourly temperature readings from a greenhouse sensor
hours = np.array([6, 7, 8, 9, 10, 11, 12], dtype=float)
temperature = np.array([16.0, 17.5, 20.0, 23.0, 26.0, 28.0, 29.0])

# Create interpolation functions
linear = interp1d(hours, temperature, kind="linear")
cubic = CubicSpline(hours, temperature)

# Estimate temperatures every 10 minutes
times = np.linspace(6, 12, 37)
linear_values = linear(times)
cubic_values = cubic(times)

# Estimate temperature at 8:30 AM
target_time = 8.5
print(f"Linear estimate at 8:30 AM: {float(linear(target_time)):.2f} C")
print(f"Cubic estimate at 8:30 AM: {float(cubic(target_time)):.2f} C")

# Plot results
plt.figure(figsize=(10, 6))
plt.scatter(hours, temperature, label="Hourly sensor readings")
plt.plot(times, linear_values, label="Linear interpolation")
plt.plot(times, cubic_values, label="Cubic spline interpolation")
plt.xlabel("Hour of day")
plt.ylabel("Temperature (C)")
plt.title("Greenhouse Temperature Interpolation")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("Task_13_real_world_adaptation.png", dpi=300)
print("Graph saved as Task_13_real_world_adaptation.png")
