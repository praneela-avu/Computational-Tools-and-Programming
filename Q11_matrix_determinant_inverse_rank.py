import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

print("Matrix:")
print(A)

print("\nDeterminant:")
print(np.linalg.det(A))

print("\nInverse:")
print(np.linalg.inv(A))

print("\nRank:")
print(np.linalg.matrix_rank(A))