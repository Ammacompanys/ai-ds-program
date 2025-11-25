import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")

x1 = np.random.normal(-2, 2, 1000)
'''
-2 = mean (center of the distribution)
2 = standard deviation (spread)
1000 = genearate 1000 random numbers

np.random.normal(-2, 2, 1000) it creates 1000 random values
centered around -2 with a spread of + or - 2

'''
y2 = np.random.normal(2, 2, 1000)

sns.histplot(x1)
# create a histogram of the data in x1
sns.histplot(y2)
# create a histogram of the data in y2

plt.title("Histogram")
plt.legend(['x1', 'y2'])
plt.show()


