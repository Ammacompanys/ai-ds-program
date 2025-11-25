# import the necessary libraries
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

# load the iris dataset
iris = load_iris()
x = iris.data
y = iris.target

# create the random forest classifer
Rf = RandomForestClassifier(n_estimators=5)

# train the model
Rf.fit(x, y)

# make prediction
prediction = Rf.predict(x)

# print the predictions
print(prediction)