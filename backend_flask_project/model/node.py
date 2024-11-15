
from database.db import db

class Node(db.Model):
    __tablename__ = "node"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)  # FK
    mac_address = db.Column(db.String(17), nullable=False)

    def __init__(self, room_id, mac_address):
        self.room_id = room_id
        self.mac_address = mac_address

