import pandas as pd
from sklearn import linear_model

df = pd.read_csv("crop_yield.csv")
x = df[["Crop Yield"]]
y = df["Rainfall"]

model = linear_model.LinearRegression()
model.fit(x, y)

predicted1 = model.predict([[90]])
predicted2 = model.predict([[90]])
predicted3 = model.predict([[93]])

print(predicted1)
print(predicted2)
print(predicted3)
