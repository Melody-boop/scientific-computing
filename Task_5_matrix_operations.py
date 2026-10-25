
import numpy as np

# Define a matrix and a vector
A = np.array([
    [1, 2],
    [3, 5]
])

x = np.array([5, 6])

# Matrix-vector multiplication
result = A @ x

# Matrix addition
B = np.array([
    [2, 1],
    [1, 2]
])

addition = A + B

# Calculate determinant and inverse
determinant = np.linalg.det(A)
inverse = np.linalg.inv(A)

print("Matrix A:")
print(A)

print("\nVector x:")
print(x)

print("\nMatrix-vector multiplication (Ax):")
print(result)

print("\nMatrix addition (A + B):")
print(addition)

print(f"\nDeterminant of A: {determinant:.2f}")

print("\nInverse of A:")
print(inverse)
