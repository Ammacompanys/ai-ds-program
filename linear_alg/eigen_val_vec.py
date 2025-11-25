import numpy as np

# Define the matrix A
A = np.array([[5, 4], [1, 2]])

# Display the Matrix A
print("Matrix A : ", A)

# Find the Eigen value and vector of Matrix A
eigen_value, eigen_vector = np.linalg.eig(A)

# Display eigen value
print("Eigen Value : ", eigen_value)

# Display eigen vector
print("Eigen Vector : ", eigen_vector)
