import scipy.stats as sp
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 1000)
y = 1/(np.sqrt(2*np.pi)) * np.exp(-x**2/2)

print("Kurtosis for normal distribution : ", sp.kurtosis(y))
print("Kurtosis for normal distribution : ", sp.kurtosis(y, fisher=True))
print("Kurtosis for normal distribution : ", sp.kurtosis(y, fisher=False))

plt.plot(x, y, "*")
plt.show()