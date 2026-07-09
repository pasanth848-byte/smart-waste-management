import os

class Config:

    # Secret Key
    SECRET_KEY = "AI_WASTE_CLASSIFICATION_SECRET_KEY"

    # Upload Folder
    UPLOAD_FOLDER = os.path.join("static", "uploads")

    # Allowed Image Extensions
    ALLOWED_EXTENSIONS = {
        "png",
        "jpg",
        "jpeg",
        "gif",
        "bmp",
        "webp"
    }

    # Maximum Upload Size (16 MB)
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    # Model Path
    MODEL_PATH = "waste_classifier.tflite"

    # Image Size (same as training)
    IMAGE_SIZE = (224, 224)

    # Class Names
    CLASS_NAMES = [
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

    # Recommendation for Each Waste Type
    RECOMMENDATION = {
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