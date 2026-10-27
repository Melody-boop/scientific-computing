
import numpy as np
import matplotlib.pyplot as plt

# Hot meal cooling inside a delivery container
ambient_temperature = 24.0
initial_temperature = 85.0
cooling_rate = 0.08
step_size = 1.0
total_time = 30.0

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

print("Food Cooling During Delivery")
print(f"Initial temperature: {temperature[0]:.2f} C")
print(
    f"Temperature after {total_time:.0f} minutes: "
    f"{temperature[-1]:.2f} C"
)

for t, temp in zip(time, temperature):
    if t % 5 == 0:
        print(f"Time={t:.0f} min, Temperature={temp:.2f} C")

plt.figure(figsize=(9, 5))
plt.plot(time, temperature, marker="o", markersize=3)
plt.axhline(
    ambient_temperature,
    linestyle="--",
    label="Ambient temperature"
)
plt.xlabel("Time (minutes)")
plt.ylabel("Meal temperature (C)")
plt.title("Food Cooling During Delivery Using Euler's Method")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("Task_17_real_world_adaptation.png", dpi=300)
print("Graph saved as Task_17_real_world_adaptation.png")
