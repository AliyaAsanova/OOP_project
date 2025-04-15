import sqlite3

class ReservationModel:
    def __init__(self, db_name="hotel.db"):
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            guest_name TEXT,
            room_number INTEGER,
            check_in TEXT,
            check_out TEXT
        )
        """)
        self.connection.commit()

    def insert_reservation(self, guest_name, room_number, check_in, check_out):
        cursor = self.connection.cursor()
        cursor.execute("""
        INSERT INTO reservations (guest_name, room_number, check_in, check_out)
        VALUES (?, ?, ?, ?)""", (guest_name, room_number, check_in, check_out))
        self.connection.commit()

    def get_all_reservations(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM reservations")
        return cursor.fetchall()
