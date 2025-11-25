# Write a program on dataframe operations and grouping with pandas library

import pandas as pd

# Series
name = pd.Series(["Guru", "Suresh", "Mahesh", "Nithin"])
print(name)

# DataFrame
a = pd.DataFrame({
	"Student Name" : name,
	"regno" : [1, 2, 3, 4],
    "semester" : [2, 4, 6, 2]
})

print("\n", a)

# Datatypes 
print("\nData types")
print(a.dtypes)

# Describe
print("\nDescribe : ")
print(a.describe())

# info
print("\ninfo : ")
print(a.info())

# Column
print("Column")
print(a.columns)

# Column of index
info_col = a.columns
print(info_col[1])

# Index
print("\nIndex : ")
print(a.index)

# Length 
print("\nLength of a : ")
print(len(a))

# Head
print("\nHead of dataframe : ")
print(a.head())

# Tail
print("\nTail of dataframe : ")
print(a.tail())

# Merging column
a["add_columns"] = a["regno"] + a["semester"]
print(a)

# Adding column
print("\n Adding columns : ")
a["Marks"] = [97, 99, 100, 99]
print(a)

# Access value in index 1
print("\nAcess value in index 1 : ")
print(a.iloc[[1]])

# Access value of key 3
print("\nAccess value of key 3 : ")
print(a.loc[[3]])

# Missing values
print("\nMissing value in the dataframe : ")
print(a.isnull())

# Groupby and sum
print("\nGroup sem and add marks : ")
print(a.groupby("semester")["Marks"].sum())

# Group and apply many
print("\nGroup and apply many agg : ")
print(a.groupby("semester")["Marks"].agg(["mean", "sum", "count"]))

# Group sum the marks and reset index
print("\nGroup and reset index : ")
print(a.groupby("semester")["Marks"].sum().reset_index())


