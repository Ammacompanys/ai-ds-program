import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Step 1: Load the dataset
data = {
	"office size (sq. ft)" : [1000, 1500, 2000, 2500, 3000],
	"conference rooms"  : [2, 3, 3, 4, 5],
	"Employee Desks" : [10, 15, 20, 25, 30],
	"Rental Price (prediction)" : [5000, 7000, 9000, 11000, 13000]
}
df = pd.DataFrame(data)

# Step 2: Split the dataset into features and target variable
X = df[["office size (sq. ft)", "conference rooms", "Employee Desks"]]
y = df["Rental Price (prediction)"]

# Step 3: Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the Multiple Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Make predictions
prediction = model.predict(X_test)

# Output the predicted rental prices
print(f"Predicted office Rental Prices : {prediction}")

