import matplotlib.pyplot as plt

languages = ["Python", "C++", "Java", "JavaScript"]
popularity = [90, 75, 80, 85]

plt.barh(languages, popularity)
plt.title("Programming Language Popularity")
plt.xlabel("Popularity Score")
plt.show()
