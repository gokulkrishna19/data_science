"""
ml_pipeline_example.py

End-to-end ML pipeline with StandardScaler and RandomForestClassifier.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

def main():
    # Load Iris dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Create a pipeline: scaling + Random Forest
    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("rf", RandomForestClassifier(
            n_estimators=100,
            random_state=42
        ))
    ])

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Fit the pipeline
    pipeline.fit(X_train, y_train)

    # Evaluate on test set
    test_accuracy = pipeline.score(X_test, y_test)
    print("Test Accuracy:", round(test_accuracy, 4))

    # Cross-validation scores
    cv_scores = cross_val_score(pipeline, X, y, cv=5)
    print("Cross-Validation Scores:", cv_scores)
    print("Mean CV Score:", round(cv_scores.mean(), 4))

if __name__ == "__main__":
    main()
