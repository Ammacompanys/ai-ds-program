import pandas as pd
import scipy.stats as sp

# Create a sample DataFrame
data = {
	"A" : [1, 2, 3, 1]
}

df = pd.DataFrame(data)

# Display the DataFrame
print("\nDataFrame : ")
print(df)

# Variance
print("\nVariance of each column : ")
print(df.var())

# Standard Deviation
print("\nStandard deviation of each column : ")
print(df.std())

# Zscore
print("\nZscore of each value : ")
print(sp.zscore(df))

