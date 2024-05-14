# Batch Image Editor

Batch Image Editor is a Python script that allows you to process multiple images in a folder. It crops the images to a square aspect ratio and adds a customizable watermark to each image.

## Features

- Automatically crops images to a square shape.
- Adds a customizable watermark to each image.
- Supports various image formats like JPG and PNG.

## Requirements

- Python 3
- Pillow (Python Imaging Library)
- OpenCV
- NumPy

## Installation

1. Download or clone this repository to your computer.

2. Install the required dependencies by running the following command:

`pip3 install pillow opencv-python numpy`

3. Place the images you want to process in the `input_images` folder.

## Usage

1. Make sure your images are in the `input_images` folder.

2. Run the script by executing the following command:

`python main.py`

3. The processed images with the watermark and square crop will be saved in the `edited_img` folder.

## Customization

- **Watermark Text**: You can change the text of the watermark by editing the `add_watermark` function in the `main.py` file.

- **Font**: Replace the default font with your preferred font by providing the path to the font file in the `add_watermark` function.

- **Opacity**: Adjust the transparency of the watermark by modifying the `opacity` parameter in the `add_watermark` function.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to submit them.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.