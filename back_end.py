from reportlab.pdfgen import canvas  # Import the canvas module from ReportLab for PDF generation
import random  # Import the random module for generating random numbers
import os  # Import the os module for interacting with the operating system (e.g., creating directories)
from datetime import datetime  # Import the datetime module for handling dates and times

# Disease to department mapping
disease_map = {
    "Fever": "General Medicine",
    "Chest Pain": "Cardiology",
    "Stomach Pain": "Gastroenterology",
    "Headache": "Neurology",
    "Skin Rash": "Dermatology"
}

# Doctors for each department
doctors_map = {
    "General Medicine": ["Dr. Smith", "Dr. Johnson", "Dr. Lee"],
    "Cardiology": ["Dr. Brown", "Dr. Davis", "Dr. Wilson"],
    "Gastroenterology": ["Dr. Taylor", "Dr. Anderson", "Dr. Thomas"],
    "Neurology": ["Dr. Jackson", "Dr. White", "Dr. Harris"],
    "Dermatology": ["Dr. Martin", "Dr. Thompson", "Dr. Garcia"]
}

# Generate a random room number
def get_room(department):
    return random.randint(100, 199)

# Function to generate OP sheet PDF
def generate_op_sheet(name, age, mobile, symptom, gender, date_time):
    department = disease_map.get(symptom, "General Medicine")
    doctor = random.choice(doctors_map[department])
    room = get_room(department)
    
    # Create folder for patient data
    folder = "patient_data"
    os.makedirs(folder, exist_ok=True)
    
    # File path with timestamp
    file_name = f"{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}_OP.pdf"
    file_path = os.path.join(folder, file_name)
    c = canvas.Canvas(file_path)
    
    # Header
    c.setFont("Helvetica-Bold", 16)
    c.drawString(180, 780, "Hospital OP Receipt")
    c.setFont("Helvetica", 10)
    c.drawString(400, 785, date_time)
    
    # Patient Details
    c.setFont("Helvetica", 12)
    c.drawString(50, 740, f"Name: {name}     Age: {age}     Gender: {gender}")
    c.drawString(50, 720, f"Mobile No: {mobile}")
    
    # Doctor & Room
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, 700, f"Doctor: {doctor}")
    c.drawString(250, 700, f"Room No: {room}")
    
    # Table Header
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, 670, "Medication")
    c.drawString(200, 670, "Morning")
    c.drawString(270, 670, "Afternoon")
    c.drawString(350, 670, "Night")
    
    # Table Rows
    y_position = 630
    for _ in range(5):
        c.drawString(50, y_position, "__________________")
        c.drawString(200, y_position, "_____")
        c.drawString(270, y_position, "_____")
        c.drawString(350, y_position, "_____")
        y_position -= 30
    
    # Signature Field
    c.setFont("Helvetica", 12)
    c.drawString(50, 470, "Signature: __________________________")
    
    # Save PDF
    c.save()
    return file_path
