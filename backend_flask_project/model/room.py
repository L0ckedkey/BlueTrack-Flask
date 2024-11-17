
from database.db import db

class Room(db.Model):
    __tablename__ = "room"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    room_number = db.Column(db.String(10), nullable=False)

    # FK destination
    transactions = db.relationship('Transaction', backref='room', lazy=True)
    node = db.relationship('Node', backref='room', lazy=True)

    def __init__(self, room_number):
        self.room_number = room_number

