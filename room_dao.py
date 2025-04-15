import sqlite3

class RoomDAO:
    def __init__(self, db_name="hotel_reservation.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    

    def add_room_with_id(self, room_id, room_type, price, available=True):
        self.cursor.execute("""
            INSERT INTO rooms (id, type, price, available)
            VALUES (?, ?, ?, ?)
        """, (room_id, room_type, price, int(available)))
        self.conn.commit()


    def get_all_rooms(self):
        self.cursor.execute("SELECT * FROM rooms")
        return self.cursor.fetchall()

    def get_available_rooms(self):
        self.cursor.execute("SELECT id,type,price FROM rooms WHERE available = 1")
        return self.cursor.fetchall()

    def update_room_availability(self, room_id, available):
        self.cursor.execute("""
            UPDATE rooms
            SET available = ?
            WHERE id = ?
        """, (available, room_id))
        self.conn.commit()

    def close(self):
        self.conn.close()
