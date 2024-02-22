
#NumPy is a powerful Python library for numerical computing that provides support for large, multi-dimensional arrays and matrices,
# along with a collection of mathematical functions to operate on these arrays efficiently. It's one of the fundamental libraries in the
# Python data science ecosystem, serving as the foundation for many other libraries such as Pandas, SciPy, and scikit-learn. Here's an in-depth 
# overview of NumPy with examples:

#Importing NumPy:

import numpy as np
#Creating NumPy Arrays:

#NumPy arrays can be created from Python lists or using built-in functions.


# From a Python list
arr1 = np.array([1, 2, 3, 4, 5])

# Using built-in functions
arr2 = np.zeros((3, 3))  # Creates a 3x3 array filled with zeros
arr3 = np.ones((2, 4))   # Creates a 2x4 array filled with ones
arr4 = np.arange(10)     # Creates an array with values from 0 to 9
#Array Attributes:

#NumPy arrays have several attributes such as shape, size, and data type.


print(arr1.shape)  # Shape of the array
print(arr2.size)   # Number of elements in the array
print(arr3.dtype)  # Data type of the array
#Array Indexing and Slicing:

#umPy arrays support advanced indexing and slicing operations.

print(arr1[0])          # Accessing elements
print(arr2[1, 2])       # Accessing elements in multi-dimensional arrays
print(arr3[:, :2])      # Slicing
#Array Operations:

#umPy provides a wide range of mathematical functions for array operations.

print(np.sum(arr1))     # Sum of all elements
print(np.mean(arr2))    # Mean of all elements
print(np.max(arr3))     # Maximum value
#Broadcasting:

#numPy allows arithmetic operations between arrays of different shapes through broadcasting.

arr5 = np.array([[1, 2, 3], [4, 5, 6]])
arr6 = np.array([10, 20, 30])
print(arr5 + arr6)      # Broadcasting the addition operation
#Universal Functions (ufuncs):

#numPy provides universal functions that operate element-wise on arrays.

print(np.sqrt(arr1))    # Square root of each element
print(np.exp(arr2))     # Exponential of each element
#Linear Algebra Operations:

#NumPy offers functions for linear algebra operations.

mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])
print(np.dot(mat1, mat2))   # Matrix multiplication
#Random Number Generation:

#NumPy provides functions to generate arrays of random numbers.

rand_arr = np.random.rand(3, 3)  # 3x3 array of random numbers
#Array Manipulation:

#NumPy offers functions to manipulate array shapes and dimensions.


reshaped_arr = arr1.reshape(5, 1)  # Reshape array
stacked_arr = np.vstack((arr1, arr2))  # Stack arrays vertically
#This is just a brief overview of NumPy's capabilities. It's a vast library with many more features and functions tailored for 
# various numerical computing tasks.





