df = df.dropna() # Drop rows with NaN values
df = df.dropna(axis = 1) # Drop columns with NaN values

df["column_name"] = df["column_name"].fillna("0") # Replace NaN with 0

df.fillna(method = "ffill") # Replace NaN with previous value
df.fillna(method = "bfill") # Replace NaN with next value

df["column_name"] = df["column_name".interpolate()] # Replace NaN with interpolated value

df = df.rename(columns = {"old_name": "new_name"}) # Rename column

df["column_name"] = df["column_name"].astype("float") # Change data type
df["column_name"] = pd.to_datetime(df["column_name"]) # Change data type to datetime

df["new_column"] = df[existing_column] * 2 # Create new column

combined = pd.concat([df1, df2], axis = 0) # Combine rows
combined = pd.concat([df1, df2], axis = 1) # Combine columns

merged = pd.merge(df1, df2, on = "column_name") # Merge dataframes
merged = pd.merge(df1, df2, how = "left", on = "column_name") # Left join
merged = pd.merge(df1, df2, how = "right", on = "column_name") # Right join
merged = pd.merge(df1, df2, how = "outer", on = "column_name") # Outer join
merged = pd.merge(df1, df2, how = "inner", on = "column_name") # Inner join

joined = df1.join(df2, how = "inner") # Join dataframes
