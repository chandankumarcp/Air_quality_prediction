from pathlib import Path

import joblib
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

FEATURE_KEYS = ["pm25", "pm10", "no2", "so2", "co", "o3"]
MODEL_FILENAMES = ["xgboost_model.pkl", "model.pkl", "best_model.pkl"]
MODEL_DIRS = [
    Path("models"),
    Path("Air-Quality-Index-AQI-Prediction") / "models",
]

model = None
model_error = None


def load_model():
    global model, model_error
    if model is not None:
        return model
    if model_error is not None:
        return None

    for model_dir in MODEL_DIRS:
        for filename in MODEL_FILENAMES:
            model_path = model_dir / filename
            if model_path.exists():
                model = joblib.load(model_path)
                return model

    searched = [str(model_dir / filename) for model_dir in MODEL_DIRS for filename in MODEL_FILENAMES]
    model_error = "Model file not found. Checked: " + ", ".join(searched)
    return None


def get_aqi_details(aqi_value: int):
    """Return AQI category details using CPCB-style breakpoints (0-50, ..., 401-500)."""
    if aqi_value <= 50:
        return "🟢 Good", "good", "Air quality is excellent. Outdoor activities are safe for everyone."
    if aqi_value <= 100:
        return "🟡 Satisfactory", "satisfactory", "Air quality is acceptable. Sensitive groups should monitor symptoms."
    if aqi_value <= 200:
        return "🟠 Moderate", "moderate", "Limit prolonged outdoor exertion if you have breathing conditions."
    if aqi_value <= 300:
        return "🔴 Poor", "poor", "Reduce outdoor activity and consider a mask in polluted areas."
    if aqi_value <= 400:
        return "🟣 Very Poor", "very-poor", "Avoid prolonged exposure outdoors. Keep windows closed when possible."
    return "⚫ Severe", "severe", "Stay indoors as much as possible and use air purification if available."


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    values = {}
    error = None

    try:
        for key in FEATURE_KEYS:
            values[key] = float(request.form[key])
    except (KeyError, TypeError, ValueError):
        error = "Please enter valid numeric values for all six pollutant inputs."
        return render_template("index.html", error=error, form_values=request.form)

    loaded_model = load_model()
    if loaded_model is None:
        return render_template("index.html", error=model_error, form_values=values)

    features = np.array([
        [
            values["pm25"],
            values["pm10"],
            values["no2"],
            values["so2"],
            values["co"],
            values["o3"],
        ]
    ])

    try:
        prediction = float(loaded_model.predict(features)[0])
    except Exception:
        error = "Prediction failed. Please verify model compatibility and input format."
        return render_template("index.html", error=error, form_values=values)

    aqi_value = int(np.clip(round(prediction), 0, 500))
    category, category_class, advisory = get_aqi_details(aqi_value)

    return render_template(
        "index.html",
        prediction=aqi_value,
        category=category,
        category_class=category_class,
        advisory=advisory,
        form_values=values,
    )


if __name__ == "__main__":
    app.run(debug=True)
