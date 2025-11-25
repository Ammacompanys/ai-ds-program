import matplotlib.pyplot as plt
import seaborn as sns 

sns.set_style("darkgrid")

x = [2030, 2031, 2032, 2033]
y = [1000, 2500, 3500, 4000]

plt.plot(x, y)
plt.xticks(x, ["2030", "2031", "2032", "2033"])
plt.title("Bluor Country GDP from 2030-2033")
plt.xlabel("Years")
plt.ylabel("Q coins")
plt.show()