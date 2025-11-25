import matplotlib.pyplot as plt

label = ["Karnataka", "Hyderabad", "Tamil Nadu", "Kerala", "Maharastra"]
colors = ["green", "orange", "yellow", "gray", "pink"]
median_income = [100000, 35000, 50000, 48000, 150000]

plt.pie(median_income, labels=label, colors=colors, shadow=True, explode=(0, 0, 0, 0, 0.2), radius=1.2, autopct="%1.1f%%")
plt.legend()
plt.show()


