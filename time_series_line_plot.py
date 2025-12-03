import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1, 31)
values = np.random.randint(50, 100, size=30)

plt.plot(days, values)
plt.xlabel("Days")
plt.ylabel("Value")
plt.title("Time Series Line Plot Example")
plt.show()
