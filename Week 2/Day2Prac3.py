import numpy as np

def create_binary_mask(data, threshold):
    """
    Create a binary mask of values above a given threshold.

    Parameters:
    data (numpy array): Input data array.
    threshold (float): Threshold value.

    Returns:
    numpy array: Binary mask array.
    """
    binary_mask = np.where(data > threshold, 1, 0)
    return binary_mask

# Example usage
data = np.array([1, 5, 8, 3, 7, 2, 9])
threshold = 5
binary_mask = create_binary_mask(data, threshold)
print(binary_mask)