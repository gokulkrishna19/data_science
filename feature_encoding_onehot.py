import pandas as pd
from sklearn.preprocessing import OneHotEncoder

df = pd.DataFrame({"City": ["Kochi", "Delhi", "Kochi", "Mumbai"]})
encoder = OneHotEncoder(sparse_output=False)

encoded = encoder.fit_transform(df[["City"]])
print("One Hot Encoding:\n", encoded)
print("Categories:", encoder.categories_)
