import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [3, 8, 1, 10, 5]

plt.fill_between(x, y)
plt.title("Area Plot Example")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
