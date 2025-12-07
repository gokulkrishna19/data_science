"""
feature_selection_chi2.py

Feature selection using Chi-Square test on a classification dataset.
"""

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.preprocessing import MinMaxScaler

def main():
    # Load Iris dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    feature_names = iris.feature_names

    # Chi-square requires non-negative features → scale to [0, 1]
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    # Select top 2 features based on chi2 score
    selector = SelectKBest(score_func=chi2, k=2)
    X_new = selector.fit_transform(X_scaled, y)

    scores = selector.scores_

    # Create a DataFrame with feature names and scores
    scores_df = pd.DataFrame({
        "feature": feature_names,
        "chi2_score": scores
    }).sort_values(by="chi2_score", ascending=False)

    print("Chi-Square Feature Scores:")
    print(scores_df)
    print("\nTop 2 selected features (transformed X shape):", X_new.shape)

if __name__ == "__main__":
    main()
