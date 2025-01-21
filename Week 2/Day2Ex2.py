import numpy as np

# Generate random dataset
dataset = np.random.randint(1, 51, size=(5,5))
print("Original: \n", dataset)

# Filter value > 25 and replace with 0
dataset[dataset > 25] = 0
print("Modified Dataset: \n", dataset)

# Calculate summary stats
print("Sum: ", np.sum(dataset))
print("Mean: ", np.mean(dataset))
print("Standar Deviation: ", np.std(dataset))