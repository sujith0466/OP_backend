from flask import Flask, request, jsonify, send_file
from hospital_backend import generate_op_sheet
from datetime import datetime
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        name = data.get("name")
        age = data.get("age")
        mobile = data.get("mobile")
        symptom = data.get("symptom")
        gender = data.get("gender")
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Input validation
        if not name or not age or not mobile:
            return jsonify({"error": "Please fill all fields."}), 400
        
        if not str(age).isdigit() or int(age) <= 0:
            return jsonify({"error": "Age must be a valid positive number."}), 400
        
        if not str(mobile).isdigit() or len(mobile) != 10:
            return jsonify({"error": "Mobile number must be a 10-digit number."}), 400
        
        # Generate OP Sheet
        file_path = generate_op_sheet(name, age, mobile, symptom, gender, date_time)
        logging.info(f"Generated OP sheet for {name}")
        return send_file(file_path, as_attachment=True)
    
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
