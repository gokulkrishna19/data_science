import numpy as np

random_numbers = np.random.randint(1, 100, size=10)
print("Random Integers:", random_numbers)

normal_dist = np.random.normal(50, 10, 100)
print("Normal Distribution Mean:", np.mean(normal_dist))
