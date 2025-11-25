import matplotlib.pyplot as plt
import seaborn as sns 

sns.set_style("darkgrid")

x = ["PVP", "MEI", "SJP", "JSP", "MKT"]
y = [500, 321, 135, 91, 1000]

colors = ["yellow", "green", "blue", "orange", "pink"]

plt.bar(x, y, color=colors)
plt.title("Number Of Student In Different Colleges")
plt.xlabel("Polytechnic College Names")
plt.ylabel("Number of Students")
plt.show()