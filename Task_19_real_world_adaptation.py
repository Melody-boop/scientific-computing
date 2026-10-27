
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Cloud resources for a small business
cost_a = 10.0
cost_b = 16.0
capacity_a = 80.0
capacity_b = 150.0
required_capacity = 900.0

def total_cost(resources):
    x, y = resources
    return cost_a * x + cost_b * y

def capacity_constraint(resources):
    x, y = resources
    return capacity_a * x + capacity_b * y - required_capacity

result = minimize(
    total_cost,
    [5.0, 5.0],
    method="SLSQP",
    bounds=[(0, None), (0, None)],
    constraints={
        "type": "ineq",
        "fun": capacity_constraint
    },
    options={"ftol": 1e-9, "maxiter": 1000}
)

x, y = result.x
total_capacity = capacity_a * x + capacity_b * y

print("Small Business Cloud Resource Optimization")
print("Optimization success:", result.success)
print(f"Type A resource units: {x:.4f}")
print(f"Type B resource units: {y:.4f}")
print(f"Required capacity: {required_capacity:.2f}")
print(f"Total capacity: {total_capacity:.2f}")
print(f"Minimum cost: {result.fun:.2f} cost units")

# Visualize the selected resource allocation
labels = ["Type A", "Type B"]
units = [x, y]

plt.figure(figsize=(8, 5))
plt.bar(labels, units)
plt.xlabel("Cloud resource type")
plt.ylabel("Allocated units")
plt.title("Optimized Cloud Resource Allocation")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("Task_19_real_world_adaptation.png", dpi=300)
print("Graph saved as Task_19_real_world_adaptation.png")
