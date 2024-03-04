#partial derivatives

#g(x,y)=x**2 . y+sin(y)

import sympy as sp
# Define multiple variables
x, y = sp.symbols('x y')

# Define a multivariable function
g = x**2 * y + sp.sin(y)

# Compute the partial derivative of g with respect to x
a = sp.diff(g, x)

# Compute the partial derivative of g with respect to y
b = sp.diff(g, y)

# Print the partial derivatives
print("Partial derivative of g with respect to x:", a)
print("Partial derivative of g with respect to y:", b)
