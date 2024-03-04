#derivative 

#f(x)=x**2+3x+2

import sympy as sp

# Define the variable
x = sp.Symbol('x')

# Define a function
f = x**2 + 3*x + 2

# Compute the derivative of the function with respect to x
y= sp.diff(f, x)

# Print the derivative
print(y)
