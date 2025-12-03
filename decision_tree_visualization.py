from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

X = [[0],[1],[2],[3]]
y = [0,0,1,1]

model = DecisionTreeClassifier().fit(X, y)
plot_tree(model, filled=True)
plt.title("Decision Tree Visualization")
plt.show()
