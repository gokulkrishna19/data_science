"""
handle_class_imbalance_smote.py

Handling imbalanced data using SMOTE (Synthetic Minority Over-sampling Technique).
Requires:
    pip install imbalanced-learn
"""

from collections import Counter

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

from imblearn.over_sampling import SMOTE

def main():
    # Create an imbalanced dataset
    X, y = make_classification(
        n_samples=2000,
        n_features=20,
        n_informative=3,
        n_redundant=1,
        n_clusters_per_class=1,
        weights=[0.9, 0.1],  # 90% of class 0, 10% of class 1
        random_state=42
    )

    print("Original class distribution:", Counter(y))

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    # Apply SMOTE on training data only
    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

    print("Resampled class distribution:", Counter(y_resampled))

    # Train a classifier on resampled data
    clf = LogisticRegression(max_iter=1000)
    clf.fit(X_resampled, y_resampled)

    # Evaluate on test data
    y_pred = clf.predict(X_test)
    print("\nClassification Report (after SMOTE):")
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    main()
