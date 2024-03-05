''' an integral is a mathematical concept that represents the accumulation of quantities.
It is used to find the area under a curve or the total accumulation of a quantity over an interval. 
Integrals are fundamental to various branches of mathematics, including calculus, physics, 
engineering, and statistics'''

#Numerical Integration with NumPy:
#NumPy provides the numpy.trapz function for numerical integration using the trapezoidal rule.

import numpy as np

# Define a function to integrate
def f(x):
    return x**2

# Define the interval [a, b] and the number of points
a = 0
b = 1
n = 100  # Number of points

# Generate evenly spaced points in the interval [a, b]
x = np.linspace(a, b, n)

# Evaluate the function at these points
y = f(x)

# Perform numerical integration using the trapezoidal rule
integral = np.trapz(y, x)

print("Numerical integral:", integral)
