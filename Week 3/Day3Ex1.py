import sympy as sp

# Define a function
x = sp.Symbol('x')
f = x**3 - 5*x + 7 

# Compute the derivative
derivative = sp.diff(f, x)
print("function: ", f)
print("Derivative: ", derivative)