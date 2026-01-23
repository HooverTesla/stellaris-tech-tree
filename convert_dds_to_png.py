import os
from PIL import Image
import imageio.v2 as imageio  # Use v2 to avoid deprecation warnings
import sys

def convert_dds_to_png(input_folder, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Process each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.dds'):
            dds_path = os.path.join(input_folder, filename)
            png_filename = os.path.splitext(filename)[0] + '.png'
            png_path = os.path.join(output_folder, png_filename)

            try:
                # Read DDS using imageio
                img = imageio.imread(dds_path)
                # Convert and save as PNG using Pillow
                Image.fromarray(img).save(png_path)
                print(f"Converted: {filename} -> {png_filename}")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_dds_to_png.py <input_folder> <output_folder>")
    else:
        input_dir = sys.argv[1]
        output_dir = sys.argv[2]
        convert_dds_to_png(input_dir, output_dir)
