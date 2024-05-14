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

# Function to add watermark to image with opacity
def add_watermark(image, watermark_text, opacity):
    draw = ImageDraw.Draw(image)
    # Load Open Sans font with size 24
    font_path = "OpenSans-Italic.ttf"  # Replace with the path to your Open Sans font file
    font_size = 24
    font = ImageFont.truetype(font_path, font_size)
    # Calculate text size
    text_width, text_height = draw.textsize(watermark_text, font=font)
    # Calculate text position
    width, height = image.size
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    # Draw text with specified opacity
    fill_color = (255, 255, 255, int(255 * opacity))  # Convert opacity to 0-255 range
    draw.text((x, y), watermark_text, fill=fill_color, font=font)
    return image


# Create the "edited_img" folder if it doesn't exist
output_folder = "edited_img"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process each image in the source folder
source_folder = "input_images"
for filename in os.listdir(source_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Load the image
        image = Image.open(os.path.join(source_folder, filename))

        # Crop image to 1:1 aspect ratio
        cropped_image = crop_image_to_square(image)

        # Add watermark with 50% opacity
        watermarked_image = add_watermark(cropped_image, "bimql.69", opacity=0.1)

        # Save the edited image in the "edited_img" folder
        output_path = os.path.join(output_folder, filename)
        watermarked_image.save(output_path)

print("Editing complete.")
