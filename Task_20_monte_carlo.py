
import numpy as np
import matplotlib.pyplot as plt

# Monte Carlo estimation of pi
np.random.seed(42)
num_points = 10000

x = np.random.uniform(0, 1, num_points)
y = np.random.uniform(0, 1, num_points)

inside = x**2 + y**2 <= 1
inside_count = np.sum(inside)

pi_estimate = 4 * inside_count / num_points
absolute_error = abs(np.pi - pi_estimate)

print("Monte Carlo Estimation of Pi")
print(f"Total points: {num_points}")
print(f"Points inside quarter-circle: {inside_count}")
print(f"Estimated pi: {pi_estimate:.6f}")
print(f"Actual pi: {np.pi:.6f}")
print(f"Absolute error: {absolute_error:.6f}")

# Plot the sampled points
plt.figure(figsize=(7, 7))
plt.scatter(x[inside], y[inside], s=4, label="Inside quarter-circle")
plt.scatter(x[~inside], y[~inside], s=4, label="Outside quarter-circle")

theta = np.linspace(0, np.pi / 2, 200)
plt.plot(np.cos(theta), np.sin(theta), linewidth=2, label="Quarter-circle boundary")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Monte Carlo Estimation of Pi")
plt.axis("equal")
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("Task_20_monte_carlo.png", dpi=300)
print("Graph saved as Task_20_monte_carlo.png")
