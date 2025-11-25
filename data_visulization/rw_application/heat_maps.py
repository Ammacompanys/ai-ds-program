import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

data = {
	"Monday" : [5, 6, 7],
	"Tuesday" : [7, 18, 2],
	"Wednesday" : [32, 1, 13]
}

df = pd.DataFrame(data, index=["Blue Pen", "Note Book", "Scale"])
plt.figure(figsize=(6, 4))
# the blue pen , note book are placed in index because to name or label the row and 
# heatmaps need the numeric values not character
sns.heatmap(df, annot=True, cmap="autumn")
# in heatmap annot = True means all the dataframe cell value are display in the boxs 
plt.title("Stationary Store Sells in 3 days")
plt.tight_layout()
plt.show()