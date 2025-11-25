import seaborn as sns
import matplotlib.pyplot as plt


# transport expenses of people of one day
expenses = [6, 12, 22, 22, 35, 43, 50, 64, 60, 70, 22, 31, 45, 32, 95, 21, 54, 32, 54, 78, 98, 65, 32]

bins=[0, 20, 40, 60, 80, 100]


sns.histplot(expenses)
plt.xlabel("Total Expenses Of One Day")
plt.ylabel("Number Of Peoples")
plt.title("Transport Expenses Of The Peoples Of One Day")
plt.show()

# 0 - 10   1
# 10 - 20  1
# 20 - 30  4
# 30 - 40  5
# 40 - 50  2
# 50 - 60  
# 60 - 70
# 70 - 80
# 80 - 90
# 90 - 100