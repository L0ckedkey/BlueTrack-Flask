
from datetime import datetime
from database.db import db

class Transaction(db.Model):
    __tablename__ = "transaction"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer,  nullable=False)  # FK
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)        # FK
    position = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, student_id, room_id, position=None):
        self.student_id = student_id
        self.room_id = room_id
        self.position = position
        self.created_at = datetime.utcnow()

