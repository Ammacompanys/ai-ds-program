import matplotlib.pyplot as plt

median_income = [150000, 200000, 262000, 500000, 660000]
state_name = ["Karnataka", "Hyderabad", "Delhi", "Tamil Nadu", "Kerala"]
colors = ["yellow", "orange", "green", "brown", "pink"]
plt.pie(median_income, labels=state_name, colors=colors, shadow=True, explode=(0, 0, 0, 0, 0.3), radius=1.2, autopct="%1.1f%%")
'''
- median_income : values for the pie slices
- labels = state_name : names for each slice
- colors=colors : colors for each slice
- shadow=True
- explode=(0, 0, 0, 0, 0.3) : pull the last slice out slightly 0.3 to
highlight it
- radius = 1.2 : size of the pie chart
- autopct = "%1.1f%%" : shows the percentage on each slice (like 23.5%)
'''
plt.legend(loc="lower left")
plt.show()


