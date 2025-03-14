#!/usr/bin/env python3
"""
Image Resizer Script
Resizes images to 3000 x 3000 pixels while preserving quality
"""

import os
import sys
import argparse
from PIL import Image

def resize_image(input_path, output_path=None, size=(3000, 3000), preserve_aspect=True):
    """
    Resize an image to the specified size while preserving quality.
    
    Args:
        input_path (str): Path to the input image
        output_path (str, optional): Path to save the resized image. If None, will use input filename with '_resized' suffix
        size (tuple, optional): Target size (width, height). Default is (3000, 3000)
        preserve_aspect (bool, optional): Whether to preserve aspect ratio. Default is True
    
    Returns:
        str: Path to the resized image
    """
    try:
        # Open the image
        img = Image.open(input_path)
        
        # Get original format
        img_format = img.format
        
        # Calculate new dimensions if preserving aspect ratio
        if preserve_aspect:
            # Calculate the ratio of the target size to the original size
            width_ratio = size[0] / img.width
            height_ratio = size[1] / img.height
            
            # Use the smaller ratio to ensure the entire image fits within the target size
            ratio = min(width_ratio, height_ratio)
            
            # Calculate new dimensions
            new_width = int(img.width * ratio)
            new_height = int(img.height * ratio)
            
            # Resize the image
            resized_img = img.resize((new_width, new_height), Image.LANCZOS)
            
            # Create a new blank image with the target size
            new_img = Image.new("RGBA" if img.mode == 'RGBA' else "RGB", size, (255, 255, 255, 0) if img.mode == 'RGBA' else (255, 255, 255))
            
            # Calculate position to paste the resized image (center it)
            paste_position = ((size[0] - new_width) // 2, (size[1] - new_height) // 2)
            
            # Paste the resized image onto the blank canvas
            if img.mode == 'RGBA':
                new_img.paste(resized_img, paste_position, resized_img)
            else:
                new_img.paste(resized_img, paste_position)
            
            final_img = new_img
        else:
            # Resize without preserving aspect ratio
            final_img = img.resize(size, Image.LANCZOS)
        
        # Determine output path if not provided
        if output_path is None:
            filename, ext = os.path.splitext(input_path)
            output_path = f"{filename}_resized{ext}"
        
        # Save the resized image with high quality
        final_img.save(output_path, format=img_format, quality=95)
        print(f"Image resized successfully and saved to: {output_path}")
        return output_path
    
    except Exception as e:
        print(f"Error resizing image: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description='Resize images to 3000x3000 pixels while preserving quality')
    parser.add_argument('input', help='Input image file path')
    parser.add_argument('-o', '--output', help='Output image file path (optional)')
    parser.add_argument('--no-preserve-aspect', action='store_false', dest='preserve_aspect',
                        help='Do not preserve aspect ratio (will stretch image to 3000x3000)')
    
    args = parser.parse_args()
    
    resize_image(args.input, args.output, preserve_aspect=args.preserve_aspect)

if __name__ == "__main__":
    main()
