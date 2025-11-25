import pandas as pd
from sklearn.linear_model import LinearRegression

# sample dataset
data = {
	'size' : [1000, 1500, 2000, 2500, 3000],
	'bedrooms' : [2, 3, 3, 4, 4],
	'price' : [200000, 250000, 300000, 400000, 450000]
}

df = pd.DataFrame(data)
# Independent variable (x) and dependend variable(y)
x = df[['size', 'bedrooms']]
y = df['price']

# create and train model
model = LinearRegression()
model.fit(x, y)

# predict price of a new house (size=2200, bedrooms=3)
prediction = model.predict([[2200, 3]])
print("Predicted Price : ", prediction)