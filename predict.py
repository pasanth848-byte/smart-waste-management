import os
import gdown
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from config import Config

MODEL_URL = "https://drive.google.com/uc?id=1pj9311xhC79w2-Ah_CF8GpNq1F2a2zoj"

if not os.path.exists(Config.MODEL_PATH):
    print("Downloading AI model...")
    gdown.download(MODEL_URL, Config.MODEL_PATH, quiet=False)

model = load_model(Config.MODEL_PATH)

def predict_waste(image_path):
    """
    Predict the waste category from an image.

    Parameters:
        image_path (str): Path to the uploaded image.

    Returns:
        tuple:
            waste_type (str)
            confidence (float)
            recommendation (str)
    """

    # Load image
    img = image.load_img(
        image_path,
        target_size=Config.IMAGE_SIZE
    )

    # Convert image to array
    img_array = image.img_to_array(img)

    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)

    # Normalize image
    img_array = img_array / 255.0

    # Predict
    predictions = model.predict(img_array, verbose=0)

    predicted_index = np.argmax(predictions)

    confidence = float(np.max(predictions) * 100)

    waste_type = Config.CLASS_NAMES[predicted_index]

    recommendation = Config.RECOMMENDATION[waste_type]

    return (
        waste_type.title(),
        round(confidence, 2),
        recommendation
    )