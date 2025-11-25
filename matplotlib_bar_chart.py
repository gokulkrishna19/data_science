import matplotlib.pyplot as plt

labels = ["Apple", "Banana", "Cherry", "Grapes"]
values = [30, 45, 10, 25]

plt.bar(labels, values)
plt.title("Bar Chart Example")
plt.xlabel("Fruits")
plt.ylabel("Quantity")
plt.show()
