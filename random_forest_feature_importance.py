from sklearn.ensemble import RandomForestClassifier
import numpy as np

X = np.array([[1],[2],[3],[4]])
y = [0,0,1,1]

model = RandomForestClassifier().fit(X, y)
print("Feature Importance:", model.feature_importances_)
