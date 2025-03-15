# Image Resizer

A Python script to resize images to 3000 x 3000 pixels while preserving quality.

## Features

- Resizes images to 3000 x 3000 pixels
- Preserves aspect ratio by default (centers the image on a 3000 x 3000 canvas)
- Option to stretch images to fill the entire 3000 x 3000 area
- Uses high-quality Lanczos resampling for the best possible quality
- Maintains transparency for PNG images

## Installation

1. Make sure you have Python 3.6+ installed
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```bash
python resize_image.py path/to/your/image.jpg
```

This will create a new file with "_resized" added to the original filename.

### Specify Output Path

```bash
python resize_image.py path/to/your/image.jpg -o path/to/output/image.jpg
```

### Stretch Image (Don't Preserve Aspect Ratio)

```bash
python resize_image.py path/to/your/image.jpg --no-preserve-aspect
```

## How It Works

The script uses the Pillow library to:
1. Open the source image
2. Calculate the appropriate dimensions to maintain aspect ratio
3. Resize the image using high-quality Lanczos resampling
4. Center the resized image on a 3000 x 3000 canvas
5. Save the result with high quality settings (95% quality for JPEG)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
