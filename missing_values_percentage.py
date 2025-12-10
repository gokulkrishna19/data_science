"""
missing_values_percentage.py

Calculate missing value percentage in each column.
"""

import pandas as pd

def main():
    # Sample dataset with missing values
    data = {
        "name": ["A", "B", None, "D"],
        "age": [20, None, 25, 30],
        "city": ["Kochi", "TVM", "Kollam", None]
    }

    df = pd.DataFrame(data)

    print("Dataset:")
    print(df, "\n")

    # Calculate percentage of missing values
    missing_percentage = df.isnull().mean() * 100

    print("Missing Value Percentage:")
    print(missing_percentage)

if __name__ == "__main__":
    main()
