import pandas as pd

df = pd.DataFrame({
    "Age": [20, 25, 22, 23, 21, 30],
    "Salary": [25000, 30000, 27000, 28000, 26000, 35000]
})

print("Head:\n", df.head())
print("\nCorrelation:\n", df.corr())
print("\nSummary:\n", df.describe())
