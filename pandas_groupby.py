import pandas as pd

df = pd.DataFrame({
    "Team": ["A", "A", "B", "B"],
    "Score": [85, 90, 78, 92]
})

print(df.groupby("Team")["Score"].mean())
