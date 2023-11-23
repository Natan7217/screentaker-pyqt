import os
import pathlib


folder_path = f"{f'{os.path.sep}'.join(str(pathlib.Path(__file__).parent.absolute()).split(os.path.sep)[:-1])}" \
              f"\\images\\screens"

# List of common image file extensions
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

# Get a list of all files in the folder
all_files = os.listdir(folder_path)

# Filter out only the image files
image_files = [file for file in all_files if os.path.splitext(file)[-1].lower() in image_extensions]

# Create a list of full paths to the image files
image_paths = [os.path.join(folder_path, file) for file in image_files]

# Print the list of image paths
print(image_paths)

