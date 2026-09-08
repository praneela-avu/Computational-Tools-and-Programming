import numpy as np
from scipy.differentiate import derivative
from scipy.integrate import quad


def f(x):
    return x**2


x = 2

result = derivative(f, x)

integration, error = quad(f, 0, 3)

print("Function: f(x) = x^2")

print("Derivative at x =", x, ":", result.df)

print("Integration from 0 to 3:", integration)