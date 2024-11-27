#!/usr/bin/env python3
# Import the necessary library
import requests  # For making HTTP requests

# Define the URL of the server endpoint where the file will be uploaded
url = "http://localhost/upload/"

# Open the file to be uploaded in binary read mode
# Replace the file path with the path to your desired file
with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
    # Use the `post` method to upload the file
    # The file is sent as a multipart form-data request under the key 'file'
    r = requests.post(url, files={'file': opened})

    # (Optional) You can check the response from the server
    print(r.status_code)  # Print the HTTP status code to verify success
    print(r.text)  # Print the server's response message
