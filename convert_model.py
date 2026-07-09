import tensorflow as tf

# Load your trained model
model = tf.keras.models.load_model("waste_classifier.h5")

# Convert to TensorFlow Lite
converter = tf.lite.TFLiteConverter.from_keras_model(model)

# Optional optimization (reduces size)
converter.optimizations = [tf.lite.Optimize.DEFAULT]

tflite_model = converter.convert()

# Save the model
with open("waste_classifier.tflite", "wb") as f:
    f.write(tflite_model)

print("Conversion completed successfully!")