import numpy as np

# Define the gradient descent function
def gradient_descent(X, y, theta, learning_rate, iteration):
    m = len(y)
    for _ in range(iteration):
        predictions = np.dot(X, theta)
        errors = predictions - y
        gradients = (1/m) * np.dot(X.T, errors)
        theta -= learning_rate *gradients
    return theta

# Sample data
X = np.array([[1, 1], [1, 2], [1, 3]])
y = np.array([2, 2.5, 3.5])
theta = np.array([0.1, 0.1])
learning_rate = 0.1
iteration = 1000

# Perform gradient descent
optimized_theta = gradient_descent(X, y, theta, learning_rate, iteration)

print("Optimized parameters: ", optimized_theta)