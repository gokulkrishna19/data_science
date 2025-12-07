"""
flask_api_model_prediction.py

Simple Flask API to serve predictions from a trained model.

Steps:
1. First, train and save a model using your 'train_model_save_joblib.py'
   Example: save model as 'model.joblib'
2. Run this file:
       python flask_api_model_prediction.py
3. Send a POST request to /predict with JSON data.

Example JSON body for POST:
{
    "features": [5.1, 3.5, 1.4, 0.2]
}
"""

from flask import Flask, request, jsonify
import numpy as np
import joblib
import os

app = Flask(__name__)

MODEL_PATH = "model.joblib"  # change if needed

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"Model file '{MODEL_PATH}' not found. "
            f"Please train and save a model before running the API."
        )
    model = joblib.load(MODEL_PATH)
    return model

model = None
try:
    model = load_model()
    print("Model loaded successfully from", MODEL_PATH)
except Exception as e:
    print("Error loading model:", e)

@app.route("/")
def home():
    return jsonify({"message": "ML Model Prediction API is running."})

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded on server."}), 500

    data = request.get_json()

    if not data or "features" not in data:
        return jsonify({"error": "Please provide 'features' in JSON body."}), 400

    features = data["features"]

    try:
        # Convert to 2D array for model: [[f1, f2, ...]]
        features_array = np.array(features).reshape(1, -1)
        prediction = model.predict(features_array)
        # If model has predict_proba
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(features_array).tolist()
        else:
            proba = None

        return jsonify({
            "input_features": features,
            "prediction": prediction.tolist(),
            "prediction_proba": proba
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Run Flask development server
    app.run(host="0.0.0.0", port=5000, debug=True)
