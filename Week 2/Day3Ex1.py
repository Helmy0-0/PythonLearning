# https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
# print("First 5 rows: \n", df.head())
# print("Last 5 rows: \n", df.tail())

# print(df.describe())

selected_columns = df[["species", "sepal_length"]]
# print("Selected Comuns: \n",selected_columns)

filtered_rows = df[(df["sepal_length"] > 5.0) & (df["species"] == "setosa")]
print("Filtered Rows: \n", filtered_rows)