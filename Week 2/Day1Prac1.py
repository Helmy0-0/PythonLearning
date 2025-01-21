import numpy as np

# Create a 4x4 matrix
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])

# Calculate the sum of its rows
row_sums = np.sum(matrix, axis=1)

# Calculate the sum of its columns
col_sums = np.sum(matrix, axis=0)

print("Matrix:")
print(matrix)
print("\nSum of rows:", row_sums)
print("Sum of columns:", col_sums)