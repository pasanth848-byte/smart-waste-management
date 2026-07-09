import os
from PIL import Image

# Dataset path
DATASET_PATH = "dataset"

valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp")

total_images = 0
valid_images = 0
invalid_images = []

print("Checking images...\n")

for root, dirs, files in os.walk(DATASET_PATH):

    for file in files:

        if file.lower().endswith(valid_extensions):

            total_images += 1

            image_path = os.path.join(root, file)

            try:
                with Image.open(image_path) as img:
                    img.verify()

                valid_images += 1

            except Exception:
                invalid_images.append(image_path)

print("=" * 50)
print("Image Verification Report")
print("=" * 50)

print(f"Total Images     : {total_images}")
print(f"Valid Images     : {valid_images}")
print(f"Invalid Images   : {len(invalid_images)}")

if invalid_images:

    print("\nInvalid Image Files:")

    for img in invalid_images:
        print(img)

else:

    print("\nAll images are valid.")

print("=" * 50)