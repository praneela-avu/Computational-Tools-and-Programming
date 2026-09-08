import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("Using NumPy")

print("\nAddition:")
print(A + B)

print("\nSubtraction:")
print(A - B)

print("\nMultiplication:")
print(A @ B)

print("\nTranspose:")
print(A.T)


print("\nWithout NumPy")

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

addition = []
subtraction = []

for i in range(2):
    add_row = []
    sub_row = []

    for j in range(2):
        add_row.append(A[i][j] + B[i][j])
        sub_row.append(A[i][j] - B[i][j])

    addition.append(add_row)
    subtraction.append(sub_row)

print("Addition:", addition)
print("Subtraction:", subtraction)

multiplication = []

for i in range(2):
    row = []

    for j in range(2):
        value = 0

        for k in range(2):
            value += A[i][k] * B[k][j]

        row.append(value)

    multiplication.append(row)

print("Multiplication:", multiplication)

transpose = []

for j in range(2):
    row = []

    for i in range(2):
        row.append(A[i][j])

    transpose.append(row)

print("Transpose:", transpose)