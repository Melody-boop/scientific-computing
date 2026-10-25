
import numpy as np

# REAL-WORLD APPLICATION:
# Estimating temperatures at five points across a small room.
# One wall is heated to 100°C and the opposite boundary is at 30°C.
# These are simplified illustrative boundary temperatures,
# not recommended real-room operating temperatures.

A = np.array([
    [ 2., -1.,  0.,  0.,  0.],
    [-1.,  2., -1.,  0.,  0.],
    [ 0., -1.,  2., -1.,  0.],
    [ 0.,  0., -1.,  2., -1.],
    [ 0.,  0.,  0., -1.,  2.]
])

b = np.array([100., 0., 0., 0., 30.])


def gauss_seidel(A, b, tol=1e-8, max_iter=500):
    x = np.zeros_like(b)

    for iteration in range(1, max_iter + 1):
        old = x.copy()

        for i in range(len(b)):
            x[i] = (
                b[i]
                - A[i, :i] @ x[:i]
                - A[i, i+1:] @ old[i+1:]
            ) / A[i, i]

        error = np.linalg.norm(x - old, ord=np.inf)

        if error < tol:
            return x, iteration

    return x, max_iter


temperatures, iterations = gauss_seidel(A, b)

print("Estimated room temperatures at five points:")
for i, temperature in enumerate(temperatures, start=1):
    print(f"Point {i}: {temperature:.2f} °C")

print("Iterations to converge:", iterations)
print("Assumption: steady-state, simplified one-dimensional heat distribution.")
