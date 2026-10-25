
import numpy as np

# x = number of adult tickets sold
# y = number of student tickets sold
#
# Adult ticket price: KSh 500
# Student ticket price: KSh 300
# Total tickets sold: 40
# Total revenue: KSh 15,600

A = np.array([
    [1.0, 1.0],
    [500.0, 300.0]
])

b = np.array([40.0, 15600.0])

solution = np.linalg.solve(A, b)
residual = b - A @ solution

print(f"Adult tickets sold: {solution[0]:.0f}")
print(f"Student tickets sold: {solution[1]:.0f}")
print("Verification A @ solution:", A @ solution)
print("Residual:", residual)
print("Residual norm:", np.linalg.norm(residual))
