#!/usr/bin/env python3

# Import required libraries
import os  # For file system operations
import datetime  # For handling dates
import reports  # For generating PDF reports
import emails  # For sending emails

# Get today's date in the format "Month Day, Year"
dt = datetime.date.today().strftime("%B %d, %Y")
# Create the report title with the current date
date = "Processed Update on " + dt

# Initialize empty lists to store fruit names and weights
names = []
weights = []

# Define the path to the descriptions directory
path = "./supplier-data/descriptions/"

# Process each file in the descriptions directory
for file in os.listdir(path):
    with open(path + file) as f:
        for ln in f:
            # Strip whitespace from the line
            line = ln.strip()
            
            # Check if the line is a fruit name (short text, no "lb")
            if len(line) <= 10 and len(line) > 0 and "lb" not in line:
                fruit_name = "name: " + line
                names.append(fruit_name)
            
            # Check if the line contains weight information
            if "lbs" in line:
                fruit_weight = "weight: " + line
                weights.append(fruit_weight)

# Create a summary string combining names and weights
summary = ""
for name, weight in zip(names, weights):
    summary += name + '<br />' + weight + '<br />' + '<br />'

# Main execution block
if __name__ == "__main__":
    # Generate the PDF report
    reports.generate_report("/tmp/processed.pdf", date, summary)
    
    # Define email details
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))  # Use the system's username
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    
    # Generate and send the email with the PDF report attached
    message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send_email(message)
