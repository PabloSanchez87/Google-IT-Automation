#!/usr/bin/env python3
# Import the required libraries
import requests  # For making HTTP requests
import os  # For interacting with the file system

# Define the URL of the server endpoint where files will be uploaded
url = "http://localhost/upload/"

# Loop through each file in the directory "./supplier-data/images"
for f in os.listdir("./supplier-data/images"):
    # Check if the file has a '.jpeg' extension
    if f.endswith(".jpeg"):
        # Open the file in binary read mode ('rb') for upload
        with open('./supplier-data/images/' + f, 'rb') as opened:
            # Send an HTTP POST request to upload the file
            # The file is sent as form data under the key 'file'
            r = requests.post(url, files={'file': opened})

            # (Optional) Print the status code to confirm successful upload
            print(f"Uploaded {f} with status code {r.status_code}")
