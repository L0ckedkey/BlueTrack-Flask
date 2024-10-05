from flask import Flask
from flask_migrate import Migrate
from routes.transactions_routes import transactions_bp
from config import Config
from database.db import db

from model.transactions import Transactions
from model.msroom import MsRoom
from model.nodes import Nodes

app = Flask(__name__)
app.config.from_object(Config)

# db
db.init_app(app)
migrate = Migrate(app, db)

# bp routes
app.register_blueprint(transactions_bp)

if __name__ == '__main__':
    app.run(debug=True)
    
