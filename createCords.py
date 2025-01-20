import os
from PIL import Image

Image.MAX_IMAGE_PIXELS = None

def create_stitch_files(image_dir, output_dir, root_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Iterate over all TIFF images in the specified directory
    for filename in os.listdir(image_dir):
        if filename.endswith('.tif'):
            # Construct the full path to the image file
            image_path = os.path.join(image_dir, filename)

            # Open the image to get its size
            with Image.open(image_path) as img:
                width, height = img.size

            # Create the coordinate file content
            file_content = f"""
{{ROOT_DIR}}\t{root_dir.replace('\\', '/')}
{{RESOLUTION}}\t4.0
{{TILE_SIZE}}\t{height}\t{width}
{os.path.basename(filename)}\t0\t0
{os.path.basename(filename)}\t0\t0
"""

            # Write the content to a new text file in the output directory
            coord_filename = f"{os.path.splitext(filename)[0]}.txt"
            with open(os.path.join(output_dir, coord_filename), 'w') as file:
                file.write(file_content.strip())

if __name__ == "__main__":
    image_directory = 'feabas\\small_align\\extracted'
    root_dir = 'small_align\\extracted'
    output_directory = 'feabas\\small_align\\stitch\\stitch_coord'
    create_stitch_files(image_directory, output_directory, root_dir)
