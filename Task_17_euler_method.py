
import numpy as np
import matplotlib.pyplot as plt

# Cooling object parameters
ambient_temperature = 25.0
initial_temperature = 90.0
cooling_rate = 0.15
step_size = 1.0
total_time = 20.0

time = np.arange(0, total_time + step_size, step_size)
temperature = np.zeros(len(time))
temperature[0] = initial_temperature

# Euler's method
for i in range(len(time) - 1):
    rate_of_change = -cooling_rate * (
        temperature[i] - ambient_temperature
    )
    temperature[i + 1] = (
        temperature[i] + step_size * rate_of_change
    )

print("Object Cooling Using Euler's Method")
print(f"Initial temperature: {temperature[0]:.2f} C")
print(f"Temperature after {total_time:.0f} minutes: {temperature[-1]:.2f} C")

for t, temp in zip(time, temperature):
    print(f"Time={t:.0f} min, Temperature={temp:.2f} C")

plt.figure(figsize=(9, 5))
plt.plot(time, temperature, marker="o", markersize=3)
plt.xlabel("Time (minutes)")
plt.ylabel("Temperature (C)")
plt.title("Object Cooling Using Euler's Method")
plt.grid(True)
plt.tight_layout()
plt.savefig("Task_17_euler_method.png", dpi=300)
print("Graph saved as Task_17_euler_method.png")
