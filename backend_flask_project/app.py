from flask import Flask
from flask_migrate import Migrate
from routes.transactions_routes import transaction_bp
from routes.default_routes import default_bp
from config import Config
from database.db import db

from model.transaction import Transaction
from model.room import Room
from model.node import Node

from classification.classification import PositionPredictor

app = Flask(__name__)
app.config.from_object(Config)

# db
db.init_app(app)
# migrate = Migrate(app, db)

# bp routess
app.register_blueprint(transaction_bp)
app.register_blueprint(default_bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

predictor = PositionPredictor()
val = [
    [{'bname': '621-1', 'position': 24, 'rssi': -88}, {'bname': '621-2', 'position': 24, 'rssi': -74}, {'bname': '621-3', 'position': 24, 'rssi': -79}, {'bname': '621-4', 'position': 24, 'rssi': -83}],
    [{'bname': '621-1', 'position': 25, 'rssi': -89}, {'bname': '621-2', 'position': 25, 'rssi': -87}, {'bname': '621-3', 'position': 25, 'rssi': -79}, {'bname': '621-4', 'position': 25, 'rssi': -87}],
    [{'bname': '621-1', 'position': 26, 'rssi': -91}, {'bname': '621-2', 'position': 26, 'rssi': -89}, {'bname': '621-3', 'position': 26, 'rssi': -82}, {'bname': '621-4', 'position': 26, 'rssi': -66}],
    [{'bname': '621-1', 'position': 26, 'rssi': -93}, {'bname': '621-2', 'position': 26, 'rssi': -88}, {'bname': '621-3', 'position': 26, 'rssi': -79}, {'bname': '621-4', 'position': 26, 'rssi': -75}],
    [{'bname': '621-1', 'position': 26, 'rssi': -91}, {'bname': '621-2', 'position': 26, 'rssi': -81}, {'bname': '621-3', 'position': 26, 'rssi': -77}, {'bname': '621-4', 'position': 26, 'rssi': -77}],
    [{'bname': '621-1', 'position': 27, 'rssi': -84}, {'bname': '621-2', 'position': 27, 'rssi': -91}, {'bname': '621-3', 'position': 27, 'rssi': -78}, {'bname': '621-4', 'position': 27, 'rssi': -62}],
    [{'bname': '621-1', 'position': 27, 'rssi': -82}, {'bname': '621-2', 'position': 27, 'rssi': -81}, {'bname': '621-3', 'position': 27, 'rssi': -85}, {'bname': '621-4', 'position': 27, 'rssi': -76}],
    [{'bname': '621-1', 'position': 27, 'rssi': -84}, {'bname': '621-2', 'position': 27, 'rssi': -81}, {'bname': '621-3', 'position': 27, 'rssi': -78}, {'bname': '621-4', 'position': 27, 'rssi': -76}],
    [{'bname': '621-1', 'position': 28, 'rssi': -91}, {'bname': '621-2', 'position': 28, 'rssi': -84}, {'bname': '621-3', 'position': 28, 'rssi': -81}, {'bname': '621-4', 'position': 28, 'rssi': -69}],
    [{'bname': '621-1', 'position': 28, 'rssi': -86}, {'bname': '621-2', 'position': 28, 'rssi': -77}, {'bname': '621-3', 'position': 28, 'rssi': -78}, {'bname': '621-4', 'position': 28, 'rssi': -79}],
    [{'bname': '621-1', 'position': 28, 'rssi': -89}, {'bname': '621-2', 'position': 28, 'rssi': -74}, {'bname': '621-3', 'position': 28, 'rssi': -78}, {'bname': '621-4', 'position': 28, 'rssi': -70}],
    [{'bname': '621-1', 'position': 28, 'rssi': -81}, {'bname': '621-2', 'position': 28, 'rssi': -79}, {'bname': '621-3', 'position': 28, 'rssi': -77}, {'bname': '621-4', 'position': 28, 'rssi': -59}],
    [{'bname': '621-1', 'position': 29, 'rssi': -79}, {'bname': '621-2', 'position': 29, 'rssi': -79}, {'bname': '621-3', 'position': 29, 'rssi': -89}, {'bname': '621-4', 'position': 29, 'rssi': -62}],
    [{'bname': '621-1', 'position': 29, 'rssi': -86}, {'bname': '621-2', 'position': 29, 'rssi': -82}, {'bname': '621-3', 'position': 29, 'rssi': -79}, {'bname': '621-4', 'position': 29, 'rssi': -64}],
    [{'bname': '621-1', 'position': 29, 'rssi': -86}, {'bname': '621-2', 'position': 29, 'rssi': -81}, {'bname': '621-3', 'position': 29, 'rssi': -80}, {'bname': '621-4', 'position': 29, 'rssi': -82}],
    [{'bname': '621-1', 'position': 30, 'rssi': -91}, {'bname': '621-2', 'position': 30, 'rssi': -86}, {'bname': '621-3', 'position': 30, 'rssi': -85}, {'bname': '621-4', 'position': 30, 'rssi': -69}],
    [{'bname': '621-1', 'position': 30, 'rssi': -92}, {'bname': '621-2', 'position': 30, 'rssi': -73}, {'bname': '621-3', 'position': 30, 'rssi': -78}, {'bname': '621-4', 'position': 30, 'rssi': -89}],
    [{'bname': '621-1', 'position': 30, 'rssi': -92}, {'bname': '621-2', 'position': 30, 'rssi': -85}, {'bname': '621-3', 'position': 30, 'rssi': -85}, {'bname': '621-4', 'position': 30, 'rssi': -77}],
    [{'bname': '621-1', 'position': 30, 'rssi': -87}, {'bname': '621-2', 'position': 30, 'rssi': -78}, {'bname': '621-3', 'position': 30, 'rssi': -88}, {'bname': '621-4', 'position': 30, 'rssi': -79}],
    [{'bname': '621-1', 'position': 30, 'rssi': -88}, {'bname': '621-2', 'position': 30, 'rssi': -80}, {'bname': '621-3', 'position': 30, 'rssi': -79}, {'bname': '621-4', 'position': 30, 'rssi': -77}],
    [{'bname': '621-1', 'position': 31, 'rssi': -88}, {'bname': '621-2', 'position': 31, 'rssi': -89}, {'bname': '621-3', 'position': 31, 'rssi': -83}, {'bname': '621-4', 'position': 31, 'rssi': -88}],
    [{'bname': '621-1', 'position': 31, 'rssi': -85}, {'bname': '621-2', 'position': 31, 'rssi': -79}, {'bname': '621-3', 'position': 31, 'rssi': -71}, {'bname': '621-4', 'position': 31, 'rssi': -93}],
    [{'bname': '621-1', 'position': 31, 'rssi': -85}, {'bname': '621-2', 'position': 31, 'rssi': -85}, {'bname': '621-3', 'position': 31, 'rssi': -74}, {'bname': '621-4', 'position': 31, 'rssi': -81}],
    [{'bname': '621-1', 'position': 31, 'rssi': -80}, {'bname': '621-2', 'position': 31, 'rssi': -77}, {'bname': '621-3', 'position': 31, 'rssi': -69}, {'bname': '621-4', 'position': 31, 'rssi': -76}],
    [{'bname': '621-1', 'position': 32, 'rssi': -89}, {'bname': '621-2', 'position': 32, 'rssi': -90}, {'bname': '621-3', 'position': 32, 'rssi': -74}, {'bname': '621-4', 'position': 32, 'rssi': -95}],
    [{'bname': '621-1', 'position': 32, 'rssi': -86}, {'bname': '621-2', 'position': 32, 'rssi': -82}, {'bname': '621-3', 'position': 32, 'rssi': -68}, {'bname': '621-4', 'position': 32, 'rssi': -85}],
    [{'bname': '621-1', 'position': 32, 'rssi': -81}, {'bname': '621-2', 'position': 32, 'rssi': -83}, {'bname': '621-3', 'position': 32, 'rssi': -58}, {'bname': '621-4', 'position': 32, 'rssi': -80}],
    [{'bname': '621-1', 'position': 33, 'rssi': -93}, {'bname': '621-2', 'position': 33, 'rssi': -83}, {'bname': '621-3', 'position': 33, 'rssi': -58}, {'bname': '621-4', 'position': 33, 'rssi': -85}],
    [{'bname': '621-1', 'position': 33, 'rssi': -84}, {'bname': '621-2', 'position': 33, 'rssi': -81}, {'bname': '621-3', 'position': 33, 'rssi': -60}, {'bname': '621-4', 'position': 33, 'rssi': -74}],
    [{'bname': '621-1', 'position': 33, 'rssi': -84}, {'bname': '621-2', 'position': 33, 'rssi': -79}, {'bname': '621-3', 'position': 33, 'rssi': -58}, {'bname': '621-4', 'position': 33, 'rssi': -87}],
    [{'bname': '621-1', 'position': 33, 'rssi': -79}, {'bname': '621-2', 'position': 33, 'rssi': -74}, {'bname': '621-3', 'position': 33, 'rssi': -58}, {'bname': '621-4', 'position': 33, 'rssi': -81}]
    ]

predicted_position = predictor.predict_position([-93, -83, -58, -85])
print(f"Predicted Position: {predicted_position}")


# rssi_values = [[entry['rssi'] for entry in group] for group in val]
# for rssi_input in rssi_values:
#     print("Predict:",rssi_input)
#     predicted_position = predictor.predict_position(rssi_input)
#     print(f"Predicted Position: {predicted_position}")
