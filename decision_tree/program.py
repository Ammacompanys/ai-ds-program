import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt
# Step 1: Load the dataset
data = {
'Age': [18, 22, 20, 25, 21, 19, 23, 26, 20, 22, 24, 27, 21],
'Study Hours': [15, 8, 12, 7, 20, 14, 10, 6, 11, 5, 9, 4, 16],
'Grade': ['A', 'B', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'A'],
'Nationality': ['UK', 'USA', 'N', 'USA', 'UK', 'UK', 'N', 'USA', 'N', 'N', 'UK', 'USA', 'N'],
'Pass': ['YES', 'NO', 'YES', 'NO', 'YES', 'YES', 'NO', 'YES', 'YES', 'NO', 'YES', 'NO', 'YES']
}
df = pd.DataFrame(data)
# Step 2: Prepare the data
X = df[['Age', 'Study Hours', 'Grade', 'Nationality']]
y = df['Pass'] # Convert categorical variables to numerical
X = pd.get_dummies(X, drop_first=True)
#Step 3: Create the decision tree classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X, y)
# Step 4: Visualize the decision tree
plt.figure(figsize=(12,8))
tree.plot_tree(clf, feature_names=X.columns, class_names=['NO','YES' ], filled=True)
plt.show()