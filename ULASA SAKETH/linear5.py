import numpy as np

# Define matrix A
A = np.array([[1, 2], [3, 4]])

# Singular Value Decomposition (SVD)
U, S, VT = np.linalg.svd(A)

# Print the results
print("U:", U)     # Left singular vectors
print("S:", S)     # Singular values (diagonal of Sigma)
print("VT:", VT)   # Right singular vectors transposed