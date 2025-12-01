from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X = [[1],[2],[3],[4]]
y = [0,0,1,1]

model = LogisticRegression().fit(X, y)
pred = model.predict([[1],[4]])
print("Accuracy:", accuracy_score([0,1], pred))
