from reportlab.pdfgen import canvas  # Import the canvas module from ReportLab for PDF generation
import random  # Import the random module for generating random numbers
import os  # Import the os module for interacting with the operating system (e.g., creating directories)
from datetime import datetime  # Import the datetime module for handling dates and times

# Disease to department mapping (dictionary to store disease-department relationships)
disease_map = {
    "Fever": "General Medicine",
    "Chest Pain": "Cardiology",
    "Stomach Pain": "Gastroenterology",
    "Headache": "Neurology",
    "Skin Rash": "Dermatology"
}

# Doctors for each department (dictionary to store department-doctor relationships)
doctors_map = {
    "General Medicine": ["Dr. Smith", "Dr. Johnson", "Dr. Lee"],
    "Cardiology": ["Dr. Brown", "Dr. Davis", "Dr. Wilson"],
    "Gastroenterology": ["Dr. Taylor", "Dr. Anderson", "Dr. Thomas"],
    "Neurology": ["Dr. Jackson", "Dr. White", "Dr. Harris"],
    "Dermatology": ["Dr. Martin", "Dr. Thompson", "Dr. Garcia"]
}

# Generate a random room number (function to generate a random room number within a specific range)
def get_room(department):
    return random.randint(100, 199)  # Returns a random integer between 100 and 199 (inclusive)

# Function to generate OP sheet PDF (function to create a PDF document with patient information)
def generate_op_sheet(name, age, mobile, symptom, gender, date_time):
    department = disease_map.get(symptom, "General Medicine")  # Get the department based on the symptom (default to General Medicine)
    doctor = random.choice(doctors_map[department])  # Randomly select a doctor from the department's list
    room = get_room(department)  # Generate a random room number for the department

    # Create folder for patient data (create a directory to store patient PDFs)
    folder = "patient_data"
    os.makedirs(folder, exist_ok=True)  # Create the directory if it doesn't exist

    # Create PDF file (generate the PDF file)
    file_path = os.path.join(folder, f"{name}_OP_Sheet.pdf")  # Construct the file path
    c = canvas.Canvas(file_path)  # Create a canvas object for drawing on the PDF

    # Header (add the header to the PDF)
    c.setFont("Helvetica-Bold", 16)  # Set the font and size for the header
    c.drawString(180, 780, "Hospital OP Receipt")  # Draw the header text

    # Date & Time (add the date and time to the PDF)
    c.setFont("Helvetica", 10)  # Set the font and size for the date/time
    c.drawString(400, 785, date_time)  # Draw the date/time text

    # Patient Details (add patient details to the PDF)
    c.setFont("Helvetica", 12)  # Set the font and size for patient details
    c.drawString(50, 740, f"Name: {name}     Age: {age}     Gender: {gender}")  # Draw patient name, age, gender
    c.drawString(50, 720, f"Mobile No: {mobile}")  # Draw patient mobile number

    # Highlighted Doctor & Room (add doctor and room information to the PDF)
    c.setFont("Helvetica-Bold", 12)  # Set the font and size for doctor/room
    c.drawString(50, 700, f"Doctor: {doctor}")  # Draw the doctor's name
    c.drawString(250, 700, f"Room No: {room}")  # Draw the room number

    # Table Header (add table headers for medication)
    c.setFont("Helvetica-Bold", 12)  # Set the font and size for table headers
    c.drawString(50, 670, "Medication")  # Draw the "Medication" header
    c.drawString(200, 670, "Morning")  # Draw the "Morning" header
    c.drawString(270, 670, "Afternoon")  # Draw the "Afternoon" header
    c.drawString(350, 670, "Night")  # Draw the "Night" header

    # Vertical Lines for Table (draw vertical lines to create table columns)
    c.line(45, 660, 45, 500)  # Leftmost line
    c.line(195, 660, 195, 500)  # Morning Column
    c.line(265, 660, 265, 500)  # Afternoon Column
    c.line(345, 660, 345, 500)  # Night Column
    c.line(450, 660, 450, 500)  # Rightmost line

    # Empty rows for medication input (add blank rows for medication input)
    y_position = 630
    for _ in range(5):  # Loop to create 5 rows
        c.drawString(50, y_position, "__________________")  # Draw a line for medication name
        c.drawString(200, y_position, "_____")  # Draw a line for morning dosage
        c.drawString(270, y_position, "_____")  # Draw a line for afternoon dosage
        c.drawString(350, y_position, "_____")  # Draw a line for night dosage
        y_position -= 30  # Move to the next row

    # Signature Field (Moved Up) (add a signature field)
    c.setFont("Helvetica", 12)  # Set the font and size for the signature field
    c.drawString(50, 470, "Signature: __________________________")  # Draw the signature field

    # Save PDF (save the PDF document)
    c.save()  # Save the PDF file
    return file_path  # Return the file path of the generated PDF