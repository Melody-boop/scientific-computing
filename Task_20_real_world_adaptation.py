
import numpy as np
import matplotlib.pyplot as plt

# Simulate delivery times for a delivery service
np.random.seed(42)
num_simulations = 10000
mean_delivery_time = 25.0
std_delivery_time = 5.0
delivery_deadline = 30.0

delivery_times = np.random.normal(
    mean_delivery_time,
    std_delivery_time,
    num_simulations
)

# Avoid impossible negative delivery times
delivery_times = np.maximum(delivery_times, 0)

on_time = delivery_times <= delivery_deadline
on_time_count = np.sum(on_time)
on_time_probability = on_time_count / num_simulations

print("Monte Carlo Delivery Reliability Simulation")
print(f"Total simulated deliveries: {num_simulations}")
print(f"Average simulated delivery time: {np.mean(delivery_times):.2f} minutes")
print(f"Deliveries within 30 minutes: {on_time_count}")
print(f"Deliveries exceeding 30 minutes: {num_simulations - on_time_count}")
print(f"Estimated on-time delivery probability: {on_time_probability:.4f}")
print(f"Estimated on-time delivery percentage: {on_time_probability * 100:.2f}%")

# Plot the simulated delivery-time distribution
plt.figure(figsize=(9, 5))
plt.hist(delivery_times, bins=40, edgecolor="black")
plt.axvline(
    delivery_deadline,
    linestyle="--",
    linewidth=2,
    label="30-minute deadline"
)
plt.xlabel("Delivery time (minutes)")
plt.ylabel("Number of simulated deliveries")
plt.title("Monte Carlo Simulation of Delivery Times")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("Task_20_real_world_adaptation.png", dpi=300)
print("Graph saved as Task_20_real_world_adaptation.png")
