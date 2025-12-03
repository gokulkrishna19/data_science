import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(10, 5)
sns.heatmap(np.corrcoef(data, rowvar=False), annot=True)
plt.title("Correlation Matrix")
plt.show()
