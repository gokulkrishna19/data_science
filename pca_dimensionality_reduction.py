from sklearn.decomposition import PCA
import numpy as np

data = np.random.rand(10, 5)
pca = PCA(n_components=2).fit(data)

print("Reduced shape:", pca.transform(data).shape)
