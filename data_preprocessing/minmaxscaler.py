from sklearn.preprocessing import MinMaxScaler
import numpy as np

# data sample
data = np.array([
	[25, 500, 1],
	[30, 600, 3]
])

# create the MinMaxScaler Object
minmax_scaler = MinMaxScaler()

# fit and transfrom values
scaled_values = minmax_scaler.fit_transform(data)

# Display the content
print("Original values : ", data)
print("Scaled values : ", scaled_values)
