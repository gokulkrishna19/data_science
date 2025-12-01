from sklearn.neighbors import KNeighborsClassifier

X = [[1],[2],[3],[4]]
y = [0,0,1,1]

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)
print("Prediction:", knn.predict([[2.6]]))
