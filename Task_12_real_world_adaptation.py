import numpy as np
from scipy.optimize import root


# Real-world adaptation:
# Find where a circular coverage boundary meets a parabolic boundary.
# Circle: x^2 + y^2 = 9  (radius = 3 units)
# Parabola: y = 0.5*x^2 - 1


def equations(z):
    x, y = z

    return [
        x**2 + y**2 - 9,
        y - (0.5 * x**2 - 1)
    ]


# Try two initial guesses to find the intersections
for guess in ([1.0, 2.0], [-1.0, 2.0]):
    solution = root(equations, guess)

    print("Initial guess:", guess)
    print(
        f"Intersection: x={solution.x[0]:.6f}, "
        f"y={solution.x[1]:.6f}"
    )
    print("Residuals:", equations(solution.x))
    print("Converged:", solution.success)
    print()