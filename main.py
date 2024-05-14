import os
from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np

# Function to crop image to 1:1 aspect ratio
def crop_image_to_square(image):
    width, height = image.size
    min_dim = min(width, height)
    left = (width - min_dim) / 2
    top = (height - min_dim) / 2
    right = (width + min_dim) / 2
    bottom = (height + min_dim) / 2
    return image.crop((left, top, right, bottom))

# Function to apply LUT to image
def apply_lut(image, lut):
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    result_image = cv2.LUT(image, lut)
    return Image.fromarray(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB))

# Function to add watermark to image
def add_watermark(image, watermark_text):
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    text_width, text_height = draw.textsize(watermark_text, font=font)
    width, height = image.size
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    draw.text((x, y), watermark_text, fill=(255, 255, 255, 128), font=font)
    return image

# Create the "edited_img" folder if it doesn't exist
output_folder = "edited_img"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Load the LUT
lut = np.loadtxt('your_lut_file.cube', dtype='f', comments='#', delimiter='\t')

# Process each image in the source folder
source_folder = "input_images"
for filename in os.listdir(source_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Load the image
        image = Image.open(os.path.join(source_folder, filename))

        # Crop image to 1:1 aspect ratio
        cropped_image = crop_image_to_square(image)

        # Apply LUT to the cropped image
        lut_applied_image = apply_lut(cropped_image, lut)

        # Add watermark to the image
        watermarked_image = add_watermark(lut_applied_image, "bimql.69")

        # Save the edited image in the "edited_img" folder
        output_path = os.path.join(output_folder, filename)
        watermarked_image.save(output_path)

print("Editing complete.")