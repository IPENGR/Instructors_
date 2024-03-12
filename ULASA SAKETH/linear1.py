import numpy as np  # Importing the numpy library and aliasing it as np

# Define vectors
v1 = np.array([1, 2, 3])  # Creating a numpy array representing the first vector [1, 2, 3]
v2 = np.array([4, 5, 6])  # Creating a numpy array representing the second vector [4, 5, 6]

# Vector addition
v_sum = v1 + v2  # Adding the two vectors element-wise

# Scalar multiplication
scalar = 2  # Defining a scalar value
v_scaled = scalar * v1  # Multiplying the first vector by the scalar

# Dot product
dot_product = np.dot(v1, v2)  # Calculating the dot product of the two vectors

# Cross product
cross_product = np.cross(v1, v2)  # Calculating the cross product of the two vectors

# Printing the results
print("Vector Addition:", v_sum)  # Printing the result of vector addition
print("Scalar Multiplication:", v_scaled)  # Printing the result of scalar multiplication
print("Dot Product:", dot_product)  # Printing the result of dot product
print("Cross Product:", cross_product)  # Printing the result of cross product



