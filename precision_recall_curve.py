from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt

y_true = [0, 0, 1, 1, 1, 0]
y_scores = [0.1, 0.3, 0.8, 0.6, 0.4, 0.2]

precision, recall, thresholds = precision_recall_curve(y_true, y_scores)

plt.plot(recall, precision)
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title("Precision-Recall Curve")
plt.show()
