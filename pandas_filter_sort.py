import pandas as pd

df = pd.DataFrame({
    "Name": ["Alex", "Bob", "Chris"],
    "Marks": [90, 72, 85]
})

print("Sorted Data:\n", df.sort_values("Marks"))
print("\nFilter Marks > 80:\n", df[df["Marks"] > 80])
