from sklearn.tree import DecisionTreeClassifier

X = [[0],[1],[2],[3]]
y = [0,0,1,1]

model = DecisionTreeClassifier().fit(X, y)
print("Predict:", model.predict([[2.5]]))
