from sklearn.preprocessing import MinMaxScaler
import numpy as np

data = np.array([[10],[20],[30],[40]])
scaler = MinMaxScaler().fit(data)

print("Min-Max Scaled:\n", scaler.transform(data))
