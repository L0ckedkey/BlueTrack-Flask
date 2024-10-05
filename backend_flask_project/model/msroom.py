
from database.db import db

class MsRoom(db.Model):
    __tablename__ = "msroom"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    room_id = db.Column(db.String(10), nullable=False)

    # FK destination
    transactions = db.relationship('Transactions', backref='room', lazy=True)
    nodes = db.relationship('Nodes', backref='room', lazy=True)

    def __init__(self, room_id):
        self.room_id = room_id

