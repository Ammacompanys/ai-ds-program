# Write a program to find Variance, Standard Deviation, and Zscore

import pandas as pd
import scipy.stats as sp

# Create a sample Dataframe
data = {
	"A" : [1, 4, 5, 6, 8]
}
df = pd.DataFrame(data)

# Display the DataFrame
print("\nDataFrame : ")
print(df)

# Variance
print("\nVariance of each column : ")
print(df.var())

# Standard Deviation
print("\nStandard Deviation of each column : ")
print(df.std())

# Zscore
print("\nZscore of each value : ")
print(sp.zscore(df))

