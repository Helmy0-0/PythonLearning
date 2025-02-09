import numpy as np

dataset = np.random.rand(5)
print("Original: \n", dataset)
normalized_dataset = (dataset - np.min(dataset)) / (np.max(dataset) - np.min(dataset))
print("Min: ", np.min(dataset))
print("Max: ", np.max(dataset))
print("Normalized: \n", normalized_dataset)