import numpy as np

A = np.array([[2, 3], [1, 4]])
determinant = np.linalg.det(A)
# print("Determinant: ", determinant)
inverse = np.linalg.inv(A)
# print("Inverse: \n", inverse)

U, S, Vt = np.linalg.svd(A)
print("U: \n", U)
print("Singular values: \n", S)
print("V Transpose: \n", Vt)

eigenvalues, eigenvectors = np.linalg.eig(A)
# print("Eigenvalues: ", eigenvalues)
# print("Eigenvectors\n: ", eigenvectors)

B = np.array([[4, 2], [1, 1]])
eigval, eigvec = np.linalg.eig(B)
# print("Eigenvalues: ", eigval)
# print("Eigenvectors\n: ", eigvec)