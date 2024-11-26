#! /usr/bin/env python3


import os 
import requests

BASEPATH = '/data/feedback/'

folder = os.listdir(BASEPATH)

list = []

for file in folder:
    with open(BASEPATH + file, 'r') as f:
        list.append({"title":f.readline().rstrip("\n"),
            		"name":f.readline().rstrip("\n"),
            		"date":f.readline().rstrip("\n"),
            		"feedback":f.read().rstrip("\n")})

for item in list:
    resp = requests.post('http://127.0.0.1:80/feedback/', json=item)
    if resp.status_code != 201:
        raise Exception('POST error status={}'.format(resp.status_code))
    print('Created feedback ID: {}'.format(resp.json()["id"]))


'''
The script should now follow the structure:

List all .txt files under /data/feedback directory that contains the actual feedback to be displayed on the company's website.

Hint: Use os.listdir() method for this, which returns a list of all files and directories in the specified path.

You should now have a list that contains all of the feedback files from the path /data/feedback. Traverse over each file and, from the contents of these text files, create a dictionary by keeping title, name, date, and feedback as keys for the content value, respectively.

Now, you need to have a dictionary with keys and their respective values (content from feedback files). This will be uploaded through the Django REST API.

Use the Python requests module to post the dictionary to the company's website. Use the request.post() method to make a POST request to http://<corpweb-external-IP>/feedback. Replace <corpweb-external-IP> with corpweb's external IP address.

Make sure an error message isn't returned. You can print the status_code and text of the response objects to check out what's going on. You can also use the response status_code 201 for created success status response code that indicates the request has succeeded.
'''