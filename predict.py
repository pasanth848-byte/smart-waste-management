import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from config import Config

# Load TensorFlow Lite model
interpreter = tf.lite.Interpreter(model_path=Config.MODEL_PATH)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


def predict_waste(image_path):

    img = image.load_img(
        image_path,
        target_size=Config.IMAGE_SIZE
    )

    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array.astype(np.float32) / 255.0

    interpreter.set_tensor(input_details[0]["index"], img_array)
    interpreter.invoke()

    predictions = interpreter.get_tensor(output_details[0]["index"])[0]

    predicted_index = np.argmax(predictions)

    confidence = float(np.max(predictions) * 100)

    waste_type = Config.CLASS_NAMES[predicted_index]

    recommendation = Config.RECOMMENDATION[waste_type]

    return (
        waste_type.title(),
        round(confidence, 2),
        recommendation
    )