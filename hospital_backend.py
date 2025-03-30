from flask import Flask, request, jsonify, send_file
from back_end import generate_op_sheet
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    
    name = data.get("name")
    age = data.get("age")
    mobile = data.get("mobile")
    symptom = data.get("symptom")
    gender = data.get("gender")
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not name or not age or not mobile:
        return jsonify({"error": "Please fill all fields."}), 400
    
    if not str(age).isdigit() or int(age) <= 0:
        return jsonify({"error": "Age must be a valid positive number."}), 400
    
    if not str(mobile).isdigit() or len(mobile) != 10:
        return jsonify({"error": "Mobile number must be a 10-digit number."}), 400

    # Generate the OP Sheet
    file_path = generate_op_sheet(name, age, mobile, symptom, gender, date_time)
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
