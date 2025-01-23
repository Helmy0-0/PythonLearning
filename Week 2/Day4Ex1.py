import pandas as pd
import numpy as np

# Create a sample dataset
data = {
    "Name": ["Alice", "Bob", np.nan, "David"],
    "Age": [25, np.nan, 30, 35],
    "Score": [85, 90, np.nan, 88]
}
df = pd.DataFrame(data)
print("Original: \n", df)

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Score"] = df["Score"].interpolate()

print("Modified: \n", df)

df = df.rename(columns={"Name": "Student_Name", "Score": "Exam:Score"})
print("Renamed: \n", df)