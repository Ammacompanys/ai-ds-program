import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")

x = [2, 4, 6, 7, 8, 10]
y = [17000, 24000, 30000, 40000, 50000, 75000]

plt.scatter(x, y, marker=".")
plt.xticks(x)
plt.title("Comparing The Skills and Salary Using Scatter Plot")
plt.xlabel("Number of Skills")
plt.ylabel("Salary")
plt.show()

