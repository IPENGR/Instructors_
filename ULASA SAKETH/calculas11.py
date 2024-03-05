#Symbolic Integration with SymPy:
'''SymPy is a symbolic mathematics library in Python that provides
powerful tools for symbolic integration.'''

import sympy as sp

# Define a symbolic variable
x = sp.Symbol('x')

# Define a function to integrate
f = x**2

# Perform symbolic integration
integral = sp.integrate(f, x)

print("Symbolic integral:", integral)
