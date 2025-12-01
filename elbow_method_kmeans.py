from sklearn.cluster import KMeans
import numpy as np

data = np.random.rand(50, 2)
inertia = []

for i in range(1, 8):
    kmeans = KMeans(n_clusters=i).fit(data)
    inertia.append(kmeans.inertia_)

print("Inertia values:", inertia)
