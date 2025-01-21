import numpy as np

# # Array and scalar broadcasting
# arr = np.array([1, 2, 3])
# print(arr + 10)
# matrix = np.array([[1, 2, 3], [4, 5, 6]])
# vector = np.array([1, 0, 1])
# print(matrix + vector)

# # Aggregation function
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print("Sum:", np.sum(arr))
# print("Mean:", np.mean(arr))
# print("Max:", np.max(arr))
# print("Min:", np.min(arr))
# print("Standard deviation:", np.std(arr))
# print("Sum of rows:", np.sum(arr, axis=1))
# print("Sum of columns:", np.sum(arr, axis=0))

# # Boolean indexing
# arr = np.array([1, 2, 3, 4, 5, 6])
# evens = arr[arr % 2 == 0]
# print("Evens: ", evens)
# arr[arr > 3] = 0
# print("Modified: ", arr)

# # Random number generation
# arr = np.random.rand(3, 3)
# print("Random array: \n", arr)
# randint = np.random.randint(0, 10, size=(2,3))
# print("Random Integer: \n", randint)