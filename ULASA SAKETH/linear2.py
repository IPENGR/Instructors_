import numpy as np

# Define matrices
A = np.array([[1, 2], [3, 4]])  # Creating a 2x2 matrix A
B = np.array([[5, 6], [7, 8]])  # Creating a 2x2 matrix B

# Scalar for scalar multiplication
scalar = 2

# Matrix addition
matrix_sum = A + B  # Adding matrices A and B element-wise

# Scalar multiplication
matrix_scaled = scalar * A  # Multiplying matrix A by a scalar

# Matrix multiplication
matrix_product = np.matmul(A, B)  # Multiplying matrices A and B

# Matrix transpose
matrix_transpose = np.transpose(A)  # Transposing matrix A

# Matrix determinant
matrix_det = np.linalg.det(A)  # Calculating the determinant of matrix A

# Matrix inverse
matrix_inv = np.linalg.inv(A)  # Calculating the inverse of matrix A

# Printing results
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Matrix Addition (A + B):\n", matrix_sum)
print("Scalar Multiplication (scalar * A):\n", matrix_scaled)
print("Matrix Multiplication (A * B):\n", matrix_product)
print("Matrix Transpose (Transpose of A):\n", matrix_transpose)
print("Matrix Determinant (Determinant of A):", matrix_det)
print("Matrix Inverse (Inverse of A):\n", matrix_inv)
