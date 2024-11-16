# default_routes.py
from flask import Blueprint, jsonify

# Define a blueprint for the default routes
default_bp = Blueprint('default', __name__)

@default_bp.route('/default', methods=['GET'])
def default_route():
    return jsonify({"hello": "world"}), 200
