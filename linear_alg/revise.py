import numpy as np

# Difine the Matrix A
A = np.array([
	[5, 4],
	[1, 2]
])

# Display the Matrix A
print("Matrix A : ", A)

# Find the eigen value and vector of matrix A
eigen_value, eigen_vector = np.linalg.eig(A)

# Display the eigen value
print("Eigen Value : ", eigen_value)

# Display the eigen vector
print("Eigen Vector : ", eigen_vector)
