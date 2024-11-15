
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
#         data = request.get_json()

#         if not all(key in data for key in ("nim", "signal_strength", "scanned_result")):
#             return jsonify({"error": "Missing required data fields"}), 400
        
#         nim = data['nim']
#         signal_strength = data['signal_strength']
#         scanned_result = data['scanned_result']

#         # get student's id
#         student = Student.query.filter_by(student_nim=nim).first()
#         if not student:
#             return jsonify({"error": "Student not found"}), 404
#         student_id = student.id

#         # process each ESP
#         for esp in scanned_result:
#             mac_address = esp.get("mac_address")

#             # get node's id
#             node = Node.query.filter_by(mac_address=mac_address).first()
#             if not node:
#                 return jsonify({"error": f"Node with MAC address {mac_address} not found"}), 404
#             room_id = node.room_id

#         # AI check
#         if ai_process_signal(signal_strength):
#             return jsonify({"error": "Signal strength too weak"}), 500
        
#         print(student_id)
#         print(room_id)
        
#         transaction = Transaction(student_id=student_id, room_id=room_id, coordinate_x=None, coordinate_y=None)
#         db.session.add(transaction)
#         db.session.commit()

#         return jsonify({"message": "Data processed and inserted into transactions"}), 201

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


from flask import Blueprint, jsonify
from model.transaction import Transaction
from database.db import db
import random

transaction_bp = Blueprint('transaction', __name__)

@transaction_bp.route('/transaction', methods=['POST'])
def process_data():
    try:

        transaction = Transaction(
            student_id=5,
            room_id=1,
            coordinate_x=0.5,
            coordinate_y=0.4
        )
        
        # Add to session and commit
        db.session.add(transaction)
        db.session.commit()

        return jsonify({
            "message": "Random data inserted into transaction table",
            "data": {
                # "student_id": 1,
                "room_id": 1,
                "coordinate_x": 0.5,
                "coordinate_y": 0.4
            }
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

