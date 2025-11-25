import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
y = [90, 80, 85, 60, 55, 60, 65, 70, 70, 76, 78, 85, 90]

# fit ploynominal regression model of degree 3
model = np.poly1d(np.polyfit(x, y, 3))

# Generate smooth x - values for the curve
myline = np.linspace(1, 22, 100)

# Plot
plt.scatter(x, y)
plt.plot(myline, model(myline))
plt.show()

