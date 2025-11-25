import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["Aju", "Riya", None, "Kiran"],
    "Score": [88, None, 90, 82]
})

print("Original:\n", df)

df["Name"] = df["Name"].fillna("Unknown")
df["Score"] = df["Score"].fillna(df["Score"].mean())

print("\nCleaned:\n", df)
