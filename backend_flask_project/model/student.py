
from database.db import db

class Student(db.Model):
    __tablename__ = "student"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_nim = db.Column(db.String(10), nullable=False)

    # FK destination
    # transactions = db.relationship('Transaction', backref='student', lazy=True)

    def __init__(self, student_nim):
        self.student_nim = student_nim
