import matplotlib.pyplot as plt

x = [1, 2, 3, 4]

plt.plot(x, [1, 4, 9, 16], label="Squares")
plt.plot(x, [1, 8, 27, 64], label="Cubes")

plt.title("Multiple Line Plot")
plt.legend()
plt.show()
