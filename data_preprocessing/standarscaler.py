from sklearn.preprocessing import StandardScaler
import numpy as np

# data sample
data = np.array([
	[25, 500, 1],
	[30, 700, 3]
])

# create StandardScacler object
std_scaler = StandardScaler()

# Scale the value
scaled_values = std_scaler.fit_transform(data)

# Dispalying
print("Original Data : ", data)
print("Scaled Data : ", scaled_values)
