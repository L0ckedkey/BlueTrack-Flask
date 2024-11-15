
from datetime import datetime
from database.db import db

class Transaction(db.Model):
    __tablename__ = "transaction"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer,  nullable=False)  # FK
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)        # FK
    coordinate_x = db.Column(db.Float, nullable=True)
    coordinate_y = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, student_id, room_id, coordinate_x=None, coordinate_y=None):
        self.student_id = student_id
        self.room_id = room_id
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.created_at = datetime.utcnow()

