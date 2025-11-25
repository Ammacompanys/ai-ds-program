import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_style("darkgrid")

data = {
	"tiger" : [3, 6, 7, 8],
	"elephant" : [6, 7, 5, 1],
	"Lion" : [8, 9, 2, 1]
}

df = pd.DataFrame(data, index=["Zota", "Pento", "Zeno", "Quen"])

df.plot(kind="bar", stacked=True, color=["Orange", "black", "Brown"])
plt.xticks(rotation=0)
plt.title("Number Of Animals In Different States Of Bulor Country")
plt.xlabel("States Name")
plt.ylabel("Number Of Animals")
plt.show()
