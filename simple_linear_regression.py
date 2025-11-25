import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.DataFrame({
    "Experience": [1, 2, 3, 4, 5],
    "Salary": [20000, 25000, 30000, 35000, 40000]
})

X = df[["Experience"]]
y = df["Salary"]

model = LinearRegression()
model.fit(X, y)

exp = 6
pred = model.predict([[exp]])

print(f"Predicted salary for {exp} years exp: {pred[0]}")
