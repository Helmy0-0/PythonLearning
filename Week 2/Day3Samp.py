import pandas as pd 

s = pd.Series([10, 20, 30], index = ['a', 'b', 'c'])
# print(s)

data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)
print(df)

df = pd.read_csv("data.csv")
df.to_csv("data.csv", index = False)
df = pd.read_excel("data.xlsx")

# Viewing Data
print(df.head())
print(df.tail(3))
print(df.info())
print(df.describe())
print(df["Name"]) 
print(df[["Name", "Age"]])
print(df[df["Age"] > 25])
print(df.iloc[0]) # First row
print(df.iloc[:, 0]) # First column
print(df.loc[0]) # First row
print(df.loc[:, "Name"]) # First column