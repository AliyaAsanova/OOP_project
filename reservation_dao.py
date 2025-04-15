import sqlite3

class ReservationDAO:
    def __init__(self, db_name="hotel_reservation.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_reservation(self, name, surname, email, mobile, room_id, check_in, check_out, cost):
        self.cursor.execute("""
            INSERT INTO reservations (name, surname, email, mobile, room_id, check_in, check_out, cost)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (name, surname, email, mobile, room_id, check_in, check_out, cost))
        self.conn.commit()

    def get_all_reservations(self):
        self.cursor.execute("SELECT * FROM reservations")
        return self.cursor.fetchall()

    def cancel_reservation(self, reservation_id):
        self.cursor.execute("DELETE FROM reservations WHERE id = ?", (reservation_id,))
        self.conn.commit()

    def update_reservation(self, reservation_id, name, surname, email, mobile, room_id, check_in, check_out, cost):
        self.cursor.execute("""
            UPDATE reservations
            SET name = ?, surname = ?, email = ?, mobile = ?, room_id = ?, check_in = ?, check_out = ?, cost = ?
            WHERE id = ?
        """, (name, surname, email, mobile, room_id, check_in, check_out, cost, reservation_id))
        self.conn.commit()


    def get_reservations_by_email(self, email):
        self.cursor.execute("SELECT * FROM reservations WHERE email = ?", (email,))
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
