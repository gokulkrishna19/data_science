import pandas as pd

data = {
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [50000, 42000, 52000, 60000, 45000]
}

df = pd.DataFrame(data)

print("Average Salary:\n", df.groupby("Department")["Salary"].mean())
