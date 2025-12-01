from sklearn.ensemble import RandomForestClassifier

X = [[0],[1],[2],[3]]
y = [0,0,1,1]

model = RandomForestClassifier().fit(X, y)
print("Predict:", model.predict([[2.2]]))
