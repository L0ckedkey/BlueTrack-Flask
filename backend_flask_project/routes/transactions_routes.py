
from flask import Blueprint, request, jsonify
from database.db import db
from model.transaction import Transaction
from model.student import Student
from model.node import Node
from classification.classification import PositionPredictor

transaction_bp = Blueprint('transaction', __name__)

@transaction_bp.route('/transaction', methods=['POST'])
def process_data():
    try:
        # get data
        data = request.get_json()
        required_fields = {"student_nim", "rssi_values", "esp_mac_addresses"}
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required data fields"}), 400
        
        # validate data & types
        if not isinstance(data['student_nim'], str):
            return jsonify({"error": "Invalid 'student_nim' format"}), 400
        if not (isinstance(data['rssi_values'], list) and len(data['rssi_values']) == 4 and all(isinstance(val, int) for val in data['rssi_values'])):
            return jsonify({"error": "'rssi_values' must be an array of 4 integers"}), 400
        if not (isinstance(data['esp_mac_addresses'], list) and len(data['esp_mac_addresses']) == 4 and all(isinstance(val, str) for val in data['esp_mac_addresses'])):
            return jsonify({"error": "'esp_mac_addresses' must be an array of 4 strings"}), 400
        
        student_nim = data['student_nim']
        rssi_values = data['rssi_values']
        esp_mac_addresses = data['esp_mac_addresses']

        # check NIM validity
        student = Student.query.filter_by(student_nim=student_nim).first()
        if not student:
            return jsonify({"error": "Student not found"}), 404
        student_id = student.id

        # check & get room
        node = Node.query.filter(Node.mac_address == ','.join(esp_mac_addresses)).first()
        if not node:
            return jsonify({"error": "Room with provided ESP not found"}), 404
        room_id = node.room_id

        # AI
        try:
            predictor = PositionPredictor()
            predicted_position = int(predictor.predict_position(rssi_values))
        except Exception as e:
            return jsonify({"error": f"Prediction error: {str(e)}"}), 500
        
        # add to db
        transaction = Transaction(
            student_id=student_id,
            room_id=room_id,
            position=predicted_position
        )
        db.session.add(transaction)
        db.session.commit()

        # success
        return jsonify({
            "message": "Data successfully inserted",
            "data": {
                "student_id": student_id,
                "room_id": room_id,
                "position": predicted_position
            }
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

