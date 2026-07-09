import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import Sequential, Input
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Dataset paths
train_path = "dataset/train"
test_path = "dataset/test"

# Check dataset folders
if not os.path.exists(train_path):
    print("Error: dataset/train folder not found!")
    exit()

if not os.path.exists(test_path):
    print("Error: dataset/test folder not found!")
    exit()

# Image preprocessing
train_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

# Load training dataset
train_generator = train_datagen.flow_from_directory(
    train_path,
    target_size=(224, 224),
    batch_size=32,
    class_mode="categorical"
)

# Load testing dataset
test_generator = test_datagen.flow_from_directory(
    test_path,
    target_size=(224, 224),
    batch_size=32,
    class_mode="categorical"
)

print("Classes Found:")
print(train_generator.class_indices)

# CNN Model
model = Sequential([
    Input(shape=(224, 224, 3)),

    Conv2D(32, (3, 3), activation="relu"),
    MaxPooling2D(pool_size=(2, 2)),

    Conv2D(64, (3, 3), activation="relu"),
    MaxPooling2D(pool_size=(2, 2)),

    Flatten(),

    Dense(128, activation="relu"),

    Dense(10, activation="softmax")
])

# Compile Model
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

print("\nTraining Started...\n")

# Train Model
history = model.fit(
    train_generator,
    validation_data=test_generator,
    epochs=10
)

# Create model folder if it doesn't exist
os.makedirs("model", exist_ok=True)

# Save model
model.save("waste_classifier.h5")

print("\nModel saved successfully!")
print("Location: waste_classifier.h5")