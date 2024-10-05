
from flask import Blueprint, request, jsonify
from model.msstudent import MsStudent
from model.nodes import Nodes
from model.transactions import Transactions
from database.db import db

transactions_bp = Blueprint('transactions', __name__)

# TODO: load AI
def ai_process_signal(signal_strength):
    return signal_strength < 30

@transactions_bp.route('/transactions', methods=['POST'])
def process_data():
    try:
        data = request.get_json()

        if not all(key in data for key in ("nim", "signal_strength", "scanned_result")):
            return jsonify({"error": "Missing required data fields"}), 400
        
        nim = data['nim']
        signal_strength = data['signal_strength']
        scanned_result = data['scanned_result']

        # get student's id
        student = MsStudent.query.filter_by(student_nim=nim).first()
        if not student:
            return jsonify({"error": "Student not found"}), 404
        student_id = student.id

        # process each ESP
        for esp in scanned_result:
            mac_address = esp.get("mac_address")

            # get node's id
            node = Nodes.query.filter_by(mac_address=mac_address).first()
            if not node:
                return jsonify({"error": f"Node with MAC address {mac_address} not found"}), 404
            room_id = node.room_id

        # AI check
        if ai_process_signal(signal_strength):
            return jsonify({"error": "Signal strength too weak"}), 500
        
        print(student_id)
        print(room_id)
        
        transaction = Transactions(student_id=student_id, room_id=room_id, coordinate_x=None, coordinate_y=None)
        db.session.add(transaction)
        db.session.commit()

        return jsonify({"message": "Data processed and inserted into transactions"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
