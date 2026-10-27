
import numpy as np
import matplotlib.pyplot as plt

# Delivery motorcycle GPS readings
time = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)
position = np.array([0.0, 7.0, 17.0, 30.0, 46.0, 65.0, 87.0])

speed = np.zeros_like(position)

# Forward difference at the beginning
speed[0] = (position[1] - position[0]) / (time[1] - time[0])

# Central differences for interior points
for i in range(1, len(time) - 1):
    speed[i] = (
        position[i + 1] - position[i - 1]
    ) / (
        time[i + 1] - time[i - 1]
    )

# Backward difference at the end
speed[-1] = (
    position[-1] - position[-2]
) / (
    time[-1] - time[-2]
)

print("Delivery Motorcycle Speed Analysis")
for t, x, v in zip(time, position, speed):
    print(f"t={t:.0f}s, position={x:.1f}m, estimated speed={v:.2f}m/s")

plt.figure(figsize=(9, 5))
plt.plot(time, speed, marker="o")
plt.xlabel("Time (s)")
plt.ylabel("Estimated speed (m/s)")
plt.title("Delivery Motorcycle Speed from GPS Data")
plt.grid(True)
plt.tight_layout()
plt.savefig("Task_15_real_world_adaptation.png", dpi=300)
print("Graph saved as Task_15_real_world_adaptation.png")
