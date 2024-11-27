#!/usr/bin/env python3
# Import required libraries
import email.message  # For creating email messages
import mimetypes  # For determining file MIME types
import os.path  # For handling file paths
import smtplib  # For sending emails via SMTP

def generate_email(sender, recipient, subject, body, attachment_path):
    """
    Creates an email message with an attachment.
    
    Args:
        sender (str): Email address of the sender.
        recipient (str): Email address of the recipient.
        subject (str): Subject line of the email.
        body (str): Body text of the email.
        attachment_path (str): Path to the attachment file.
    
    Returns:
        email.message.EmailMessage: The email message object.
    """
    # Create a new email message object
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    # Process the attachment and attach it to the email
    attachment_filename = os.path.basename(attachment_path)  # Extract file name
    mime_type, _ = mimetypes.guess_type(attachment_path)  # Guess the MIME type
    mime_type, mime_subtype = mime_type.split('/', 1)  # Split into type and subtype

    # Read the attachment file in binary mode and attach it
    with open(attachment_path, 'rb') as ap:
        message.add_attachment(
            ap.read(),  # File content
            maintype=mime_type,  # MIME type (e.g., "application")
            subtype=mime_subtype,  # MIME subtype (e.g., "pdf")
            filename=attachment_filename  # File name to display in the email
        )

    return message


def generate_error_email(sender, recipient, subject, body):
    """
    Creates an email message without an attachment.
    
    Args:
        sender (str): Email address of the sender.
        recipient (str): Email address of the recipient.
        subject (str): Subject line of the email.
        body (str): Body text of the email.
    
    Returns:
        email.message.EmailMessage: The email message object.
    """
    # Create a new email message object
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    return message


def send_email(message):
    """
    Sends an email message using the local SMTP server.
    
    Args:
        message (email.message.EmailMessage): The email message to send.
    
    Returns:
        None
    """
    # Connect to the local SMTP server
    mail_server = smtplib.SMTP('localhost')
    # Send the email message
    mail_server.send_message(message)
    # Close the connection to the SMTP server
    mail_server.quit()
