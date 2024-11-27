#!/usr/bin/env python3

# Import required libraries
import shutil  # For checking disk usage
import psutil  # For checking CPU and memory usage
import socket  # For checking hostname resolution
import emails  # Custom module for sending emails
import os  # For accessing environment variables

# Define the sender and recipient email addresses
sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))  # Uses the system's username

# Common email body for alerts
body = "Please check your system and resolve the issue as soon as possible."

# Check disk usage and send an email if available space is less than 20%
du = shutil.disk_usage("/")  # Get disk usage statistics for the root directory
du_prsnt = du.free / du.total * 100  # Calculate the percentage of free space
if du_prsnt < 20:
    subject = "Error - Available disk space is less than 20%"
    message = emails.generate_error_email(sender, receiver, subject, body)
    emails.send_email(message)

# Check CPU usage and send an email if usage exceeds 80%
cpu_prsnt = psutil.cpu_percent(1)  # Measure CPU usage over a 1-second interval
if cpu_prsnt > 80:
    subject = "Error - CPU usage is over 80%"
    message = emails.generate_error_email(sender, receiver, subject, body)
    emails.send_email(message)

# Check available memory and send an email if less than 100 MB is available
mem = psutil.virtual_memory()  # Get memory usage statistics
trs = 100 * 1024 * 1024  # Define the threshold (100 MB in bytes)
if mem.available < trs:
    subject = "Error - Available memory is less than 100MB"
    message = emails.generate_error_email(sender, receiver, subject, body)
    emails.send_email(message)

# Check if localhost resolves to 127.0.0.1 and send an email if it does not
hostname = socket.gethostbyname('localhost')  # Resolve 'localhost' to an IP address
if hostname != '127.0.0.1':
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    message = emails.generate_error_email(sender, receiver, subject, body)
    emails.send_email(message)
