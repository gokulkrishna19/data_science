import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(200)
sns.distplot(data)
plt.title("Distribution Plot")
plt.show()
