from sklearn.linear_model import LinearRegression
import pandas as pd

df = pd.read_csv("student_dataset.csv")

x = df[["CIE-1", "CIE-2", "CIE-3"]]
y = df["SEE"]

# Create the LinearRegression object
model = LinearRegression()

# fit the values to model
model.fit(x, y)

# predicting the value
predicted1 = model.predict([[30, 27, 26]])
predicted2 = model.predict([[27, 24, 26]])
predicted3 = model.predict([[25, 23, 26]])
predicted4 = model.predict([[26, 24, 28]])
predicted5 = model.predict([[25, 24, 23]])

print(predicted1)
print(predicted2)
print(predicted3)
print(predicted4)
print(predicted5)

