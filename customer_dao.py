import sqlite3

class CustomerDAO:
    def __init__(self, db_name="hotel_reservation.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def add_customer(self, name, surname, email, mobile):
        self.cursor.execute("""
            INSERT INTO customers (name, surname, email, mobile)
            VALUES (?, ?, ?, ?)
        """, (name, surname, email, mobile))
        self.conn.commit()

    def get_all_customers(self):
        self.cursor.execute("SELECT * FROM customers")
        return self.cursor.fetchall()

    def get_customer_by_email(self, email):
        self.cursor.execute("SELECT * FROM customers WHERE email = ?", (email,))
        return self.cursor.fetchone()

    def update_customer(self, customer_id, name, surname, email, mobile):
        self.cursor.execute("""
            UPDATE customers
            SET name = ?, surname = ?, email = ?, mobile = ?
            WHERE id = ?
        """, (name, surname, email, mobile, customer_id))
        self.conn.commit()

    def delete_customer(self, customer_id):
        self.cursor.execute("DELETE FROM customers WHERE id = ?", (customer_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()
