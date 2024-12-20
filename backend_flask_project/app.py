from flask import Flask
from flask_migrate import Migrate
from routes.transactions_routes import transaction_bp
from routes.default_routes import default_bp
from config import Config
from database.db import db

from model.transaction import Transaction
from model.room import Room
from model.node import Node


app = Flask(__name__)
app.config.from_object(Config)

# db
db.init_app(app)
# migrate = Migrate(app, db)

# bp routess
app.register_blueprint(transaction_bp)
app.register_blueprint(default_bp)

if __name__ == '__main__':
    app.run(debug=True)
