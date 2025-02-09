grouped = df.groupby("Name")

for name, group in grouped:
    print(name)
    print(group)
    
grouped.mean()
grouped.sum()

df.groupby("category")["numeric"].mean()
df.groupby("category").agg({"numeric": ["mean", "max", "min"]})

pivot = df.pivot_table(
    values = "numeric",
    index = "category",
    aggfunc = "mean"
)
def range_func(x):
    return x.max() - x.min()

df.groupby("category")["numeric"].agg(range_func)

df.groupby("category")["numeric"].mean()
df.groupby("category")["numeric"].max()
df.groupby("category")["numeric"].min()

df.groupby("category").agg({"numeric": ["mean", "max", "min"]})
