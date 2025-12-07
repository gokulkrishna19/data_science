"""
hyperparameter_tuning_gridsearch.py

Hyperparameter tuning using GridSearchCV with Logistic Regression.
"""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

def main():
    # Load dataset
    data = load_breast_cancer()
    X = data.data
    y = data.target

    # Create pipeline: scaling + model
    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("log_reg", LogisticRegression(max_iter=1000))
    ])

    # Define parameter grid for GridSearchCV
    param_grid = {
        "log_reg__C": [0.01, 0.1, 1, 10],
        "log_reg__penalty": ["l2"],
        "log_reg__solver": ["lbfgs", "liblinear"]
    }

    grid_search = GridSearchCV(
        estimator=pipe,
        param_grid=param_grid,
        cv=5,
        scoring="accuracy",
        n_jobs=-1
    )

    # Train + search best parameters
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    grid_search.fit(X_train, y_train)

    print("Best Cross-Validation Accuracy: {:.4f}".format(grid_search.best_score_))
    print("Best Parameters:", grid_search.best_params_)

    test_score = grid_search.score(X_test, y_test)
    print("Test Set Accuracy with Best Params: {:.4f}".format(test_score))

if __name__ == "__main__":
    main()
