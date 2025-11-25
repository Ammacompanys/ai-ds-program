import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# creating a style
sns.set_style("darkgrid")

# Assigning a value for stacked box

df = pd.DataFrame({
	"y1" : [2012, 2015, 2014, 2006, 2018],
	"y2" : [1201, 15021, 2013, 20133, 2206]}, 
	index=["karnataka", "delhi", "hyderabad", "tamil nadu", "maharastra"]
)

df.plot(kind="bar", stacked=True, color=["yellow", "purple"])
'''
df.plot() : plot the data from the dataframe df.
it uses pandas built-in plotting function
kind="bar" :  make a bar chart
stacked=True : stack the bars on top of each other (creates stacked bar chart)
color=["yellow", "purple"] : use yellow for the first column, purple for the second column.
'''
plt.title("Stacked Bar")
plt.xticks(rotation=0)
plt.xlabel("State")
plt.ylabel("median income")
plt.show()


