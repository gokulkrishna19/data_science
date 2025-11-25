import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(100, 20, 200)

plt.boxplot(data)
plt.title("Boxplot Example")
plt.show()
