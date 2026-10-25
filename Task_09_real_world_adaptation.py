import numpy as np

# Student collaboration network
# Each node represents a student.
# A connection means two students have worked together.
# Node order: Alice, Brian, Carol, David, Eva

A = np.array([
    [0., 1., 1., 0., 0.],
    [1., 0., 1., 1., 0.],
    [1., 1., 0., 1., 1.],
    [0., 1., 1., 0., 1.],
    [0., 0., 1., 1., 0.]
])

students = ["Alice", "Brian", "Carol", "David", "Eva"]

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Find the dominant eigenvalue and corresponding eigenvector
index = np.argmax(np.real(eigenvalues))
dominant_value = np.real(eigenvalues[index])
dominant_vector = np.abs(np.real(eigenvectors[:, index]))

# Normalize the eigenvector to estimate student importance
importance = dominant_vector / dominant_vector.sum()

print("STUDENT COLLABORATION NETWORK")
print("Dominant eigenvalue:", round(dominant_value, 4))
print("\nStudent importance scores:")

for student, score in zip(students, importance):
    print(f"{student}: {score:.4f}")

# Verify the eigenvalue equation Av = lambda*v
v = np.real(eigenvectors[:, index])

print("\nVerification:", np.allclose(A @ v, dominant_value * v))