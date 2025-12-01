import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

X = np.arange(1, 21)
y = X * 2

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

plt.scatter(X_train, y_train, label="Train Data")
plt.scatter(X_test, y_test, marker="x", label="Test Data")
plt.title("Train-Test Split Visualization")
plt.legend()
plt.show()
