
import numpy as np
from scipy.linalg import lu_factor, lu_solve

# Simplified electricity network model.
# Unknowns represent voltage-related quantities at three nodes.
# The coefficient matrix represents the fixed network relationships.

A = np.array([
    [4.0, -1.0, 0.0],
    [-1.0, 4.0, -1.0],
    [0.0, -1.0, 3.0]
])

# Different measurement sets from the network
measurement_sets = [
    np.array([12.0, 8.0, 6.0]),
    np.array([14.0, 9.0, 7.0]),
    np.array([10.0, 7.0, 8.0])
]

# Factor the network matrix once
lu, piv = lu_factor(A)

for i, b in enumerate(measurement_sets, start=1):
    solution = lu_solve((lu, piv), b)
    residual = b - A @ solution

    print(f"Network measurement set {i}")
    print("Calculated node values:", solution)
    print("Verification A @ solution:", A @ solution)
    print("Residual norm:", np.linalg.norm(residual))
    print()
