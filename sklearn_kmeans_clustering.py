from sklearn.cluster import KMeans
import numpy as np

data = np.array([[1,2],[1,4],[1,0],[4,2],[4,4],[4,0]])

kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

print("Cluster Centers:\n", kmeans.cluster_centers_)
print("Labels:", kmeans.labels_)
