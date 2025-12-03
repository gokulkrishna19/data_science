from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt

y_true = [0, 0, 1, 1]
y_scores = [0.1, 0.4, 0.35, 0.8]

fpr, tpr, _ = roc_curve(y_true, y_scores)

plt.plot(fpr, tpr)
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.show()
