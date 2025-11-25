from sklearn.preprocessing import Normalizer
import numpy as np

# data samples
data = np.array([
	[25, 500, 1],
	[30, 600, 3]
])

# create the normalizer object
norm = Normalizer(norm="l2")

# fit and transform values
scaled_value = norm.fit_transform(data)

# display the values
print("Original value : ", data)
print("Scaled value : ", scaled_value)


