from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(50, 2)

kmeans = KMeans(n_clusters=3).fit(data)
labels = kmeans.labels_

plt.scatter(data[:,0], data[:,1], c=labels)
plt.title("K-Means Clustering")
plt.show()
