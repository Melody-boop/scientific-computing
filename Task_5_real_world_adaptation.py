
import numpy as np

# Coordinates of a square: each column represents one point
points = np.array([
    [1, 2, 2, 1],
    [1, 1, 2, 2]
])

# Scaling matrix: doubles the size of the square
scaling_matrix = np.array([
    [2, 0],
    [0, 2]
])

# Rotation matrix: rotates points 90 degrees counterclockwise
rotation_matrix = np.array([
    [0, -1],
    [1,  0]
])

# Combine scaling and rotation
transformation_matrix = rotation_matrix @ scaling_matrix

# Apply the transformation to all four points
transformed_points = transformation_matrix @ points

print("Original square coordinates:")
print(points)

print("\nCombined transformation matrix:")
print(transformation_matrix)

print("\nTransformed square coordinates:")
print(transformed_points)
