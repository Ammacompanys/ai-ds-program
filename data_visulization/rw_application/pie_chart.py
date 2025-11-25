import matplotlib.pyplot as plt

college_name = ["SSP Engg", "RV Engg", "PES Engg", "AIT Engg", "VT Engg"]
colors = ["yellow", "green", "red", "pink", "orange"]
college_fee = [50000, 75000, 150000, 70000, 85000]

plt.pie(college_fee, labels=college_name, colors=colors, shadow=True, explode=(0, 0, 0.3, 0, 0), radius=1.2, autopct="%1.1f%%")
plt.legend(loc="lower left")
plt.show()
