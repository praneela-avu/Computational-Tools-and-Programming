from scipy.optimize import minimize

def fun(v):
    x, y = v
    return (x-2)**2 + (y-2)**2

initial_guess = [0, 0]

result = minimize(fun, initial_guess)

print("Minimum value of function:", result.fun)
print("Value of x:", result.x[0])
print("Value of y:", result.x[1])