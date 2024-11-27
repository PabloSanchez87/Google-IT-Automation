#!/usr/bin/env python3
# Import required libraries
from PIL import Image  # For working with images
import os  # For file system operations

# Define the directory containing the images
path = "./supplier-data/images/"

# Loop through each file in the specified directory
for f in os.listdir(path):
    # Check if the file has a '.tiff' extension
    if f.endswith(".tiff"):
        # Split the file name to remove the extension
        split_f = f.split(".")
        # Create the new file name with a '.jpeg' extension
        name = split_f[0] + ".jpeg"
        
        # Open the image with PIL and convert it to RGB mode
        im = Image.open(path + f).convert("RGB")
        
        # Resize the image to 600x400 pixels
        im.resize((600, 400)).save(path + name, "JPEG")
