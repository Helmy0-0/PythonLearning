import pandas as pd 

s = pd.Series([10, 20, 30], index = ['a', 'b', 'c'])
# print(s)

data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)
print(df)