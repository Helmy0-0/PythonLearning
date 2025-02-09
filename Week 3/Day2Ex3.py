import numpy as np

A = np.array([[2, 3, 1], [3, 1, 1], [1, 2, 1]])
U, S, Vt = np.linalg.svd(A)
print("U: \n", U)
print("Singular values: \n", S)
print("V Transpose: \n", Vt)

# Recunstruct
Sigma = np.zeros((3, 3))
np.fill_diagonal(Sigma, S)
reconstructed = U @ Sigma @ Vt
print("Reconstructed: \n", reconstructed)
