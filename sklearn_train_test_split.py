from sklearn.model_selection import train_test_split
import numpy as np

X = np.array([[1],[2],[3],[4],[5],[6]])
y = np.array([2,4,6,8,10,12])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

print("Train Data:", X_train, y_train)
print("Test Data:", X_test, y_test)
