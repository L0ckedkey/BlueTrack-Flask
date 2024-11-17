
from flask import Blueprint, request, jsonify
from database.db import db
from sqlalchemy import or_
import numpy as np
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
        required_fields = {"nim", "scannedDevices"}
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required data fields"}), 400
        if not isinstance(data['scannedDevices'], list) or not all(isinstance(device, dict) and "macAddress" in device and "rssi" in device for device in data['scannedDevices']):
            return jsonify({"error": "'scannedDevices' must be a list of objects containing 'macAddress' and 'rssi'"}), 400
        
        # validate data & types
        if not isinstance(data['nim'], str):
            return jsonify({"error": "Invalid 'nim' format"}), 400
        if not isinstance(data['scannedDevices'], list) or not all(isinstance(device, dict) and "macAddress" in device and "rssi" in device for device in data['scannedDevices']):
            return jsonify({"error": "'scannedDevices' must be a list of objects containing 'macAddress' and 'rssi'"}), 400
        
        student_nim = data['nim']
        scanned_devices = data['scannedDevices']

        # check NIM validity
        student = Student.query.filter_by(student_nim=student_nim).first()
        if not student:
            return jsonify({"error": "Student not found"}), 404
        student_id = student.id

        # check & get room
        mac_addresses = [device['macAddress'] for device in scanned_devices]
        result = Node.query.all()
        matching_rows = []
        matching_mac_addresses = []
        rssi_values = []
        room_id = 0
        for row in result:
            db_mac_addresses = row.mac_address.split(',')
            matches = set(mac_addresses).intersection(db_mac_addresses)
            if len(matches) >= 4:
                matching_rows.append(row)
                matching_mac_addresses = db_mac_addresses  # ordering/sorting
                room_id = row.room_id
                ordered_rssi = []
                for mac in matching_mac_addresses:
                    for device in scanned_devices:
                        if device['macAddress'] == mac:
                            ordered_rssi.append(device['rssi'])
                            break
                    else:
                        ordered_rssi.append(None)
                rssi_values.extend(ordered_rssi)

        if not matching_rows:
            return jsonify({"error": "No matching room found with ESPs' mac addresses."}), 404
        if room_id == 0:
            return jsonify({"error": "Error getting room_id from matched row."}), 404

        # AI
        try:
            predictor = PositionPredictor()
            predicted_position = int(predictor.predict_position(np.array(rssi_values)))
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
                # "position": predicted_position
            }
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

