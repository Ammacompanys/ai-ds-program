import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22]
y = [100, 95, 88, 75, 60, 50, 55, 40, 35, 30, 25, 20, 15, 10, 15, 20, 45, 65, 70, 80]

model = np.poly1d(np.polyfit(x, y, 3))
myline = np.linspace(1, 22, 100)

plt.scatter(x, y)
plt.plot(myline, model(myline))
plt.show()

