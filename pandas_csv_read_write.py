import pandas as pd

df = pd.DataFrame({
    "City": ["Delhi", "Mumbai", "Kochi"],
    "Population": [19, 20, 7]
})

df.to_csv("cities.csv", index=False)
print("CSV file written")

read_df = pd.read_csv("cities.csv")
print(read_df)
