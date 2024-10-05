
from database.db import db

class MsStudent(db.Model):
    __tablename__ = "msstudent"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_nim = db.Column(db.String(15), nullable=False)

    # FK destination
    transactions = db.relationship('Transactions', backref='student', lazy=True)

    def __init__(self, student_nim, is_registered):
        self.student_nim = student_nim
        self.is_registered = is_registered

