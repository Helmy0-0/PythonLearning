#https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
del df['species']

# Calculate correlation matrix
corr = df.corr()

# Plot heatmap
sns.heatmap(corr, annot = True, cmap = "coolwarm")
plt.title("Correlation Heatmap")
plt.show()