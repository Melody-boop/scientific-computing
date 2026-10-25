
import numpy as np

# x = number of Type A servers
# y = number of Type B servers

# Type A uses 4 CPU units and 8 GB memory
# Type B uses 2 CPU units and 12 GB memory
# Total observed usage: 20 CPU units and 72 GB memory

A = np.array([
    [4.0, 2.0],
    [8.0, 12.0]
])

b = np.array([24.0, 72.0])

# Solve the system of linear equations
solution = np.linalg.solve(A, b)

# Verify the solution
residual = b - A @ solution

print(f"Type A servers: {solution[0]:.0f}")
print(f"Type B servers: {solution[1]:.0f}")
print("Verification A @ solution:", A @ solution)
print("Residual:", residual)
print("Residual norm:", np.linalg.norm(residual))
