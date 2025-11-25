from sklearn import linear_model
import pandas as pd

df = pd.read_csv("student_dataset.csv")

x = df[["CIE-1"]]
y = df["SEE"]

model = linear_model.LinearRegression()
model.fit(x, y)

predict1 = model.predict([[30]])
predict2 = model.predict([[27]])
predict3 = model.predict([[25]])
predict4 = model.predict([[26]])
predict5 = model.predict([[25]])

print(predict1)
print(predict2)
print(predict3)
print(predict4)
print(predict5)
