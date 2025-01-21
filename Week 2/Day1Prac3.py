import numpy as np


random_array = np.random.randint(1, 100, 10) 
print(random_array)
arr_min = np.min(random_array)
arr_max = np.max(random_array)

print("Minimum value:", arr_min)
print("Maximum value:", arr_max)