import os
from PIL import Image

def extract_tif_metadata(directory):
    # Check each file in the directory
    for filename in os.listdir(directory):
        if filename.lower().endswith('.tif') or filename.lower().endswith('.tiff'):
            file_path = os.path.join(directory, filename)
            try:
                # Open the image file
                with Image.open(file_path) as img:
                    print(f"Metadata for {filename}:")
                    print(f"  Format: {img.format}")
                    print(f"  Size: {img.size}")
                    print(f"  Mode: {img.mode}")
                    # Accessing the tag viewer of the TIFF file
                    if img.format == 'TIFF':
                        for tag, value in img.tag.items():
                            print(f"  Tag {tag}: {value}")
                    print("-" * 40)
            except IOError:
                print(f"Cannot open {filename}")
        break

if __name__ == "__main__":
    # Directory containing TIFF images
    directory = 'small_align\extracted'
    extract_tif_metadata(directory)
