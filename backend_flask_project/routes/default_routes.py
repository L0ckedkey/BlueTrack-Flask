
from flask import Blueprint, jsonify

default_bp = Blueprint('default', __name__)

@default_bp.route('/default', methods=['GET'])
def default_route():
    try:

        return jsonify({
            "hello": "world"
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

