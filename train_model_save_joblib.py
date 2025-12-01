from sklearn.ensemble import RandomForestClassifier
import joblib

X = [[1],[2],[3],[4]]
y = [0,0,1,1]

model = RandomForestClassifier().fit(X, y)
joblib.dump(model, "rf_model.joblib")

print("Model saved as rf_model.joblib")
