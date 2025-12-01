from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

X = np.array([[1],[2],[3],[4]])
y = [2,8,18,32]

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

model = LinearRegression().fit(X_poly, y)
print("Prediction for x=5:", model.predict(poly.fit_transform([[5]])))
