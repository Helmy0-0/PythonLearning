import numpy as np

# Create a 3D random array with shape (3, 4, 5)
array_3d = np.random.rand(3, 4, 5)

# Compute the mean along the first axis (axis=0)
mean_axis_0 = np.mean(array_3d, axis=0)

# Compute the sum along the second axis (axis=1)
sum_axis_1 = np.sum(array_3d, axis=1)

# Compute the standard deviation along the third axis (axis=2)
std_axis_2 = np.std(array_3d, axis=2)

print("3D Random Array:\n", array_3d)
print("\nMean along the first axis:\n", mean_axis_0)
print("\nSum along the second axis:\n", sum_axis_1)
print("\nStandard Deviation along the third axis:\n", std_axis_2)