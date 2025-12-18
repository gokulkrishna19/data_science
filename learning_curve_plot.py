"""
learning_curve_plot.py

Plot learning curve for a machine learning model.
"""

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import learning_curve
from sklearn.svm import SVC

def main():
    # Load dataset
    iris = load_iris()
    X, y = iris.data, iris.target

    model = SVC(kernel="linear")

    train_sizes, train_scores, test_scores = learning_curve(
        model, X, y, cv=5, scoring="accuracy",
        train_sizes=[0.1, 0.3, 0.5, 0.7, 1.0]
    )

    train_mean = train_scores.mean(axis=1)
    test_mean = test_scores.mean(axis=1)

    plt.plot(train_sizes, train_mean, label="Training Accuracy")
    plt.plot(train_sizes, test_mean, label="Validation Accuracy")
    plt.xlabel("Training Size")
    plt.ylabel("Accuracy")
    plt.title("Learning Curve")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
