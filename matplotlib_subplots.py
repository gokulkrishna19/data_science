import matplotlib.pyplot as plt

x = [1, 2, 3, 4]

plt.subplot(1, 2, 1)
plt.plot(x, [1, 4, 9, 16])
plt.title("Plot 1")

plt.subplot(1, 2, 2)
plt.plot(x, [2, 3, 2, 3])
plt.title("Plot 2")

plt.tight_layout()
plt.show()
