"""
train_test_split_visual_scatter.py

Visualizing train-test split using a scatter plot.
"""

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

def main():
    # Load dataset
    iris = load_iris()
    X = iris.data[:, :2]  # use first 2 features for plotting
    y = iris.target

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    # Plot train data
    plt.scatter(X_train[:, 0], X_train[:, 1], c="blue", label="Train Data", alpha=0.6)

    # Plot test data
    plt.scatter(X_test[:, 0], X_test[:, 1], c="red", label="Test Data", alpha=0.6)

    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.title("Train-Test Split Visualization")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
