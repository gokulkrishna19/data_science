from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1],[2],[3],[4]])
y = np.array([3,6,8,11])

model = LinearRegression().fit(X, y)

print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)
print("Prediction for 5:", model.predict([[5]]))
