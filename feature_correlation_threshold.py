"""
feature_correlation_threshold.py

Remove highly correlated features using a correlation threshold.
"""

import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer

def main():
    # Load dataset
    data = load_breast_cancer()
    df = pd.DataFrame(data.data, columns=data.feature_names)

    # Compute correlation matrix
    corr_matrix = df.corr().abs()

    # Select upper triangle of correlation matrix
    upper = corr_matrix.where(
        np.triu(np.ones(corr_matrix.shape), k=1).astype(bool)
    )

    # Set correlation threshold
    threshold = 0.9

    # Find features with correlation greater than threshold
    to_drop = [
        column for column in upper.columns
        if any(upper[column] > threshold)
    ]

    print("Highly correlated features to drop:")
    print(to_drop)

    df_reduced = df.drop(columns=to_drop)
    print("\nOriginal shape:", df.shape)
    print("Reduced shape:", df_reduced.shape)

if __name__ == "__main__":
    main()
