
# from flask import Blueprint, request, jsonify
# from model.student import Student
# from model.node import Node
# from model.transaction import Transaction
# from database.db import db

# transaction_bp = Blueprint('transaction', __name__)

# # TODO: load AI
# def ai_process_signal(signal_strength):
#     return signal_strength < 30

# @transaction_bp.route('/transaction', methods=['POST'])
# def process_data():
#     try:
        # data = request.get_json()

        # if not all(key in data for key in ("nim", "signal_strength", "scanned_result")):
        #     return jsonify({"error": "Missing required data fields"}), 400
        
        # nim = data['nim']
        # signal_strength = data['signal_strength']
        # scanned_result = data['scanned_result']

        # # get student's id
        # student = Student.query.filter_by(student_nim=nim).first()
        # if not student:
        #     return jsonify({"error": "Student not found"}), 404
        # student_id = student.id

        # # process each ESP
        # for esp in scanned_result:
        #     mac_address = esp.get("mac_address")

        #     # get node's id
        #     node = Node.query.filter_by(mac_address=mac_address).first()
        #     if not node:
        #         return jsonify({"error": f"Node with MAC address {mac_address} not found"}), 404
        #     room_id = node.room_id

        # # AI check
        # if ai_process_signal(signal_strength):
        #     return jsonify({"error": "Signal strength too weak"}), 500
        
        # print(student_id)
        # print(room_id)
        
#         transaction = Transaction(student_id=student_id, room_id=room_id, coordinate_x=None, coordinate_y=None)
#         db.session.add(transaction)
#         db.session.commit()

#         return jsonify({"message": "Data processed and inserted into transactions"}), 201

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


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

