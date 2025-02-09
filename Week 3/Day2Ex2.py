import numpy as np

A = np.array([[2, 3], [4, 5]])
eigval, eigvec = np.linalg.eig(A)
print("Eigenvalues: ", eigval)
print("Eigenvectors\n: ", eigvec)