#!/usr/bin/env python3
# Import necessary libraries
import os  # For file system operations
import requests  # For making HTTP requests

# Initialize an empty dictionary to hold fruit data
fruits = {}

# Define the keys for the dictionary
keys = ["name", "weight", "description", "image_name"]

# Initialize an index to keep track of the current key
index = 0

# Paths to the directories for descriptions and images
path = "./supplier-data/descriptions/"
img_path = "./supplier-data/images/"

# Iterate through each file in the descriptions directory
for file in os.listdir(path):
    # Open and read each file
    with open(path + file) as f:
        for ln in f:
            # Strip whitespace from the line
            line = ln.strip()
            
            # Check if the line contains weight information
            if "lbs" in line:
                # Extract the numeric weight and convert it to an integer
                nline = line.split()
                wght = int(nline[0])
                fruits["weight"] = wght
                index += 1
            else:
                try:
                    # Add other details (name, description) to the dictionary
                    fruits[keys[index]] = line
                    index += 1
                except:
                    # If index is out of range, add the line as the description
                    fruits[keys[2]] = line
        
        # Reset the index for the next file
        index = 0
        
        # Generate the image name corresponding to the current description file
        split_f = file.split(".")
        name = split_f[0] + ".jpeg"
        
        # Find and add the corresponding image file to the dictionary
        for fle in os.listdir(img_path):
            if fle == name:
                fruits["image_name"] = name
        
        # Send a POST request with the fruit data as JSON to the specified endpoint
        response = requests.post("http://<External_IP>/fruits/", json=fruits)
        
        # Clear the dictionary for the next iteration
        fruits.clear()
