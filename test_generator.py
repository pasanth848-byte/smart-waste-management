from tensorflow.keras.preprocessing.image import load_img
import os

folder = "dataset/train/battery"

filename = os.listdir(folder)[0]
path = os.path.join(folder, filename)

print("Testing image:", path)

img = load_img(path)

print("Image loaded successfully!")