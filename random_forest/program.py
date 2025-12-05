from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
y = iris.target

Rf = RandomForestClassifier(n_estimators=5)
Rf.fit(X, y)

prediction = Rf.predict(X)

print(prediction)