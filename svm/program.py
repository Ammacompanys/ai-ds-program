from scipy import stats
import matplotlib.pyplot as plt

x = [7, 11, 12, 17, 20, 21, 27, 30, 34, 37, 41, 8]
y = [91, 85, 101, 100, 112, 76, 78, 79, 82, 120, 122, 90]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept

model = list(map(myfunc, x))
plt.scatter(x, y)
plt.plot(x, model)
plt.show()