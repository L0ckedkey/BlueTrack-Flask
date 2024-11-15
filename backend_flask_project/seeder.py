
from app import app
from database.db import db
from model.msroom import MsRoom
from model.nodes import Nodes
from model.student import Student

rooms = [
    "601", "602", "603", "604", "605", "606", "607", "608", "609", "610",
    "613", "614", "621", "622", "623", "624", "625", "626", "627", "628", "629", "630", "631",
    "706", "708", "710", "721", "722", "723", "725", "727", "729"
]

mac_addresses = [
    f"00:1A:79:{i:02X}:{i:02X}:{i:02X}" for i in range(1, 129)
]

students_nim = [
    "2671234567", "2789876543", "2686781234", "2779876541", "2675556677",
    "2683334444", "2783452342", "2689865432", "2772345432", "2687654321",
    "2671111222", "2785555678", "2776666789", "2679876543", "2685432123",
    "2776543456", "2687654323", "2773456789", "2681234567", "2786543210",
    "2677890123", "2680987654", "2788765432", "2675432198", "2779087654",
    "2682345678", "2776789123", "2689870987", "2673456123", "2780987654"
]

def seed_students_rooms_nodes():
    with app.app_context():
        # delete previous
        MsRoom.query.delete()
        Nodes.query.delete()
        Student.query.delete()
        # seed
        for i, room in enumerate(rooms, start=1):
            new_room = MsRoom(id=i, room_id=room)
            db.session.add(new_room)
            # 4 ESP
            for esp_num in range(1, 5):
                mac_address = mac_addresses[(i - 1) * 4 + (esp_num - 1)]
                new_node = Nodes(id=(i - 1) * 4 + esp_num, room_id=i, mac_address=mac_address)
                db.session.add(new_node)
        # students
        for i, student_nim in enumerate(students_nim, start=1):
            new_student = Student(id=i, student_nim=student_nim, is_registered=True)
            db.session.add(new_student)

        db.session.commit()
        print("Database seeded successfully with rooms, nodes, and students!")

if __name__ == "__main__":
    seed_students_rooms_nodes()

