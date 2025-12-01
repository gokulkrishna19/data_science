from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X = [[0],[1],[2],[3]]
y = [0,0,1,1]

model = LogisticRegression().fit(X, y)
pred = model.predict([[1.5]])
print("Prediction:", pred)
