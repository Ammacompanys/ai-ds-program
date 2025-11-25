import numpy as np
import scipy.stats as sp
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 1000)
y = 1/(np.sqrt(2*np.pi)) * np.exp(-x**2/2)

print("Skewness for data : ", sp.skew(y))

plt.plot(x, y, "*")
plt.show()

