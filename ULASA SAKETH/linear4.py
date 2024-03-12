import numpy as np

# Define matrix A
A = np.array([[1, 2], [3, 4]])

# Define vector b
b = np.array([1, 2])

# Solve Ax = b for x
x = np.linalg.solve(A, b)

# Print solution x
print("Solution x:", x)