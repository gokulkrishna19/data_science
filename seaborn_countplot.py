import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
sns.countplot(x="day", data=data)
plt.title("Countplot Example")
plt.show()
