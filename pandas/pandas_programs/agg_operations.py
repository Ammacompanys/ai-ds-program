# Write a program on aggregate opearations with pandas library 

import pandas as pd

# Create the a sample DataFrame
data = {
	"A" : [2, 4, 5, 6, 7, 2]
}
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame : ")
print(df)

# Sum
print("\nSum of each column")
print(df.sum())

# Mean
print("\nMean of each column")
print(df.mean())
# the Means tells the average of the number in the particular list
# it varies when data with outliers (very big or small values)

# Median
print("\nMedian of each column")
print(df.median())
# the median give the middle most value
# it does not varies when the outliers are big or small

# Mode
print("\nMode of each column")
print(df.mode())

# Mininum
print("\nMinium value of the each column")
print(df.min())

# Maximum
print("Maximum value of each column")
print(df.max())

# Count
print("\nCount of the non-null entries of each column")
print(df.count()) # return number of non-null values, care about missing value
print(len(df)) # return number of rows , does not care about missing value

# Variance
print("\nVariance of each column")
print(df.var())

# Standard Deviation
print("\nStandard deviation of each column")
print(df.std())
