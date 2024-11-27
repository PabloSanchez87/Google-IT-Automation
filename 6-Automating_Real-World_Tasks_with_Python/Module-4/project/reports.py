#!/usr/bin/env python3
# Import required modules from the ReportLab library
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet  # For styling the document
from reportlab.lib import colors  # For setting colors in the report

# Define a function to generate a PDF report
def generate_report(attachment, title, paragraph):
    """
    Generate a PDF report using ReportLab.
    
    Args:
        attachment (str): The path where the PDF will be saved.
        title (str): The title of the report.
        paragraph (str): The body text of the report.
    
    Returns:
        None
    """
    # Get sample styles for the document
    styles = getSampleStyleSheet()
    
    # Create a PDF document at the specified path
    report = SimpleDocTemplate(attachment)
    
    # Create the title of the report as a styled paragraph
    report_title = Paragraph(title, styles["h1"])
    
    # Create the body text of the report as a styled paragraph
    report_info = Paragraph(paragraph, styles["BodyText"])
    
    # Define a table style (not used in this function but included for future use)
    table_style = [
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Add a grid to the table
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Bold font for the first row
        ('ALIGN', (0, 0), (-1, -1), 'CENTER')  # Center alignment for all cells
    ]
    
    # Add an empty line as a spacer
    empty_line = Spacer(1, 20)
    
    # Build the PDF with the specified elements
    report.build([report_title, empty_line, report_info])
