
from scipy.optimize import minimize

# Cost and capacity per server unit
cost_a = 12.0
cost_b = 18.0
capacity_a = 100.0
capacity_b = 170.0
required_capacity = 1000.0

# Objective: minimize total cost
def total_cost(servers):
    x, y = servers
    return cost_a * x + cost_b * y

# Constraint: total capacity must meet the requirement
def capacity_constraint(servers):
    x, y = servers
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

print("Cloud Server Cost Optimization")
print("Optimization success:", result.success)
print(f"Type A server units: {result.x[0]:.4f}")
print(f"Type B server units: {result.x[1]:.4f}")
print(
    f"Total capacity: "
    f"{capacity_a * result.x[0] + capacity_b * result.x[1]:.2f}"
)
print(f"Minimum cost: {result.fun:.2f} cost units")
