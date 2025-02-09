import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
# print("Add: \n", A+B)
# print("Sub: \n", A-B)

C = 2*A
# print("Scalar Multiplication: \n", C)

result = np.dot(A, B)
# print("Matrix Multiplication: \n", result)

I = np.eye(3)
# print("Identity Matrix: \n", I)

Z = np.zeros((3, 3))
# print("Zero Matrix: \n", Z)

D = np.diag([1, 2, 3])
print("Diagonal Matrix: \n", D)