from flask import Flask, render_template, request, redirect
import os
import json
from datetime import datetime
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename

app = Flask(__name__)

# -----------------------------
# Configuration
# -----------------------------
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# -----------------------------
# History File
# -----------------------------

HISTORY_FILE = "history.json"


def load_history():

    if not os.path.exists(HISTORY_FILE):

        return []

    with open(HISTORY_FILE, "r") as file:

        return json.load(file)


def save_history(history):

    with open(HISTORY_FILE, "w") as file:

        json.dump(history, file, indent=4)

# -----------------------------
# Load Trained Model
# -----------------------------
import gdown

MODEL_PATH = "waste_classifier.h5"
MODEL_URL = "https://drive.google.com/uc?id=1pj9311xhC79w2-Ah_CF8GpNq1F2a2zoj"

if not os.path.exists(MODEL_PATH):
    print("Downloading AI model...")
    gdown.download(MODEL_URL, MODEL_PATH, quiet=False)

model = load_model(MODEL_PATH)

# Class Names (same order as your training dataset)
class_names = [
    "battery",
    "biological",
    "cardboard",
    "clothes",
    "glass",
    "metal",
    "paper",
    "plastic",
    "shoes",
    "trash"
]

# Disposal Recommendation
recommendation = {
    "battery": "Hazardous Waste Bin",
    "biological": "Brown Organic Bin",
    "cardboard": "Blue Recycling Bin",
    "clothes": "Reuse / Donation Bin",
    "glass": "Green Recycling Bin",
    "metal": "Grey Recycling Bin",
    "paper": "Blue Recycling Bin",
    "plastic": "Blue Recycling Bin",
    "shoes": "Reuse / Donation Bin",
    "trash": "Black Waste Bin"
}

# Description
description = {
    "battery": "Dispose of batteries at an authorized hazardous waste collection center.",
    "biological": "Organic waste can be composted into natural fertilizer.",
    "cardboard": "Cardboard can be recycled after removing food contamination.",
    "clothes": "Donate or recycle wearable clothes whenever possible.",
    "glass": "Glass can be recycled many times without losing quality.",
    "metal": "Metal waste should be recycled to conserve natural resources.",
    "paper": "Paper should be kept dry and clean before recycling.",
    "plastic": "Plastic should be cleaned before placing it in a recycling bin.",
    "shoes": "Reusable shoes can be donated to charity organizations.",
    "trash": "General waste should be disposed of in a black waste bin."
}

# Environmental Tips
tips = {
    "battery": "Never throw batteries into regular household waste.",
    "biological": "Convert food waste into compost whenever possible.",
    "cardboard": "Flatten cardboard boxes before recycling.",
    "clothes": "Donate old clothes instead of throwing them away.",
    "glass": "Separate glass by color if your recycling center requires it.",
    "metal": "Recycle aluminum cans to save energy.",
    "paper": "Avoid mixing wet paper with recyclable paper.",
    "plastic": "Reduce single-use plastics whenever possible.",
    "shoes": "Repair or donate shoes before discarding them.",
    "trash": "Reduce landfill waste through proper segregation."
}


# -----------------------------
# Routes
# -----------------------------

@app.route("/")
def home():

    history = load_history()

    total_predictions = len(history)

    if total_predictions > 0:
        average_confidence = round(
            sum(item["confidence"] for item in history) / total_predictions,
            2
        )
    else:
        average_confidence = 0

    return render_template(
        "index.html",
        total_predictions=total_predictions,
        average_confidence=average_confidence
    )


@app.route("/about")
def about():
    return render_template("about.html")



@app.route("/history")
def history():

    history_data = load_history()

    total_predictions = len(history_data)

    average_confidence = (
        round(sum(item["confidence"] for item in history_data) / total_predictions, 2)
        if total_predictions > 0 else 0
    )

    return render_template(
        "history.html",
        history=history_data,
        total_predictions=total_predictions,
        average_confidence=average_confidence
    )


@app.route("/dashboard")
def dashboard():

    history_data = load_history()

    total_predictions = len(history_data)

    # Average Confidence
    if total_predictions > 0:

        average_confidence = round(

            sum(item["confidence"] for item in history_data)
            / total_predictions,

            2

        )

    else:

        average_confidence = 0

    this_month = total_predictions

    # Waste Category Count
    category_counts = {

        "Battery":0,
        "Biological":0,
        "Cardboard":0,
        "Clothes":0,
        "Glass":0,
        "Metal":0,
        "Paper":0,
        "Plastic":0,
        "Shoes":0,
        "Trash":0

    }

    # Daily Prediction Count
    daily_predictions = {}

    for item in history_data:

        waste = item["waste"]

        if waste in category_counts:

            category_counts[waste] += 1

        # Example date: 2026-07-07
        day = item["datetime"][:10]

        if day in daily_predictions:

            daily_predictions[day] += 1

        else:

            daily_predictions[day] = 1

    daily_labels = list(daily_predictions.keys())

    daily_counts = list(daily_predictions.values())

    print("Daily Labels:", daily_labels)
    print("Daily Counts:", daily_counts)

    return render_template(

        "dashboard.html",

        history=history_data[::-1],

        total_predictions=total_predictions,

        average_confidence=average_confidence,

        this_month=this_month,

        category_counts=category_counts,

        daily_labels=daily_labels,

        daily_counts=daily_counts

    )


@app.route("/report")
def report():
    return render_template("report.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():

    if request.method == "POST":

        # Check image
        if "image" not in request.files:
            return "No file uploaded."

        file = request.files["image"]

        if file.filename == "":
            return "No image selected."

        # Save uploaded image
        filename = secure_filename(file.filename)

        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)

        file.save(filepath)

        # -----------------------------
        # Image Preprocessing
        # -----------------------------
        img = image.load_img(filepath, target_size=(224, 224))

        img_array = image.img_to_array(img)

        img_array = np.expand_dims(img_array, axis=0)

        img_array = img_array / 255.0

        # -----------------------------
        # Prediction
        # -----------------------------
        prediction = model.predict(img_array)

        predicted_index = np.argmax(prediction)

        confidence = round(float(np.max(prediction) * 100), 2)

        waste_type = class_names[predicted_index]

        # -----------------------------
        # Save Prediction to History
        # -----------------------------
        history = load_history()

        history.append({

            "image": filepath.replace("\\", "/").replace("static/", ""),

            "waste": waste_type.title(),

            "confidence": confidence,

            "recommendation": recommendation[waste_type],

            "datetime": datetime.now().strftime("%d-%m-%Y %I:%M %p")

        })

        save_history(history)

        # -----------------------------
        # Show Result
        # -----------------------------
        return render_template(
            "predict.html",
            image_path="/" + filepath.replace("\\", "/"),
            prediction=waste_type.title(),
            confidence=confidence,
            recommendation=recommendation[waste_type],
            description=description[waste_type],
            tip=tips[waste_type]
)

    return render_template("predict.html")


# -----------------------------
# Run Flask
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)