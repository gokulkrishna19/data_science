import pandas as pd

data = {
    "Name": ["Aju", "Riya", "Kiran"],
    "Age": [22, 24, 21],
    "Marks": [88, 92, 85]
}

df = pd.DataFrame(data)
print(df)
print("\nDescribe:\n", df.describe())
