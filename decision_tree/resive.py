from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("D:\\folders\\ai_ds_programs\\decison_tree\\dataset.csv")

n_encode = {"UK" : 0, "USA" : 1, "N" : 2}
df["Nationality"] = df["Nationality"].map(n_encode)

go_encode = {"YES" : 1, "NO" : 0}
df["Go"] = df["Go"].map(go_encode)

features = ["Age", "Experience", "Rank", "Nationality"]

x = df[features]
y = df["Go"]

dtree = DecisionTreeClassifier()
dtree.fit(x, y)

plt.figure(figsize=(8, 6))
tree.plot_tree(dtree, feature_names=features, class_names=['NO', 'YES'], filled=True)
plt.show()