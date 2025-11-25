import pandas as pd

df = pd.read_csv("sample_data.csv")  # Create your own CSV
print("First 5 rows:\n", df.head())
print("Columns:", df.columns)
print("Shape:", df.shape)
