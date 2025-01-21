import numpy as np

def normalize_array(arr):
    arr_min = np.min(arr)
    arr_max = np.max(arr)
    normalized_arr = (arr - arr_min) / (arr_max - arr_min)
    return normalized_arr

# Example usage
array = np.array([1, 2, 3, 4, 5])
normalized_array = normalize_array(array)
print("Original array:", array)
print("Normalized array:", normalized_array)