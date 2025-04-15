from room_dao import RoomDAO
from reservation_dao import ReservationDAO
from customer_dao import CustomerDAO

class ReservationController:
    def __init__(self, db_name="hotel_reservation.db"):
        self.room_dao = RoomDAO(db_name)
        self.reservation_dao = ReservationDAO(db_name)
        self.customer_dao = CustomerDAO(db_name)

    # ─────────── ROOMS ───────────
    def get_available_rooms(self):
        return self.room_dao.get_available_rooms()

    def get_all_rooms(self):
        return self.room_dao.get_all_rooms()

    def add_room(self, room_id, room_type, price):
        self.room_dao.add_room_with_id(room_id, room_type, price)


    def update_room_availability(self, room_id, available):
        self.room_dao.update_room_availability(room_id, available)

    def get_room_price(self, room_id):
        rooms = self.room_dao.get_all_rooms()
        for room in rooms:
            if room[0] == room_id:
                return room[2]  
        return None

    # ─────────── RESERVATIONS ───────────
    def make_reservation(self, name, surname, email, mobile, room_id, check_in, check_out, cost):
        self.reservation_dao.create_reservation(name, surname, email, mobile, room_id, check_in, check_out, cost)
        self.room_dao.update_room_availability(room_id, 0)

    def get_all_reservations(self):
        return self.reservation_dao.get_all_reservations()

    def cancel_reservation(self, reservation_id, room_id):
        self.reservation_dao.cancel_reservation(reservation_id)
        self.room_dao.update_room_availability(room_id, 1)

    def update_reservation(self, reservation_id, name, surname, email, mobile, room_id, check_in, check_out, cost):
        self.reservation_dao.update_reservation(reservation_id, name, surname, email, mobile, room_id, check_in, check_out, cost)

    # ─────────── CUSTOMERS ───────────
    def add_customer(self, name, surname, email, mobile):
        self.customer_dao.add_customer(name, surname, email, mobile)

    def get_customer_by_email(self, email):
        return self.customer_dao.get_customer_by_email(email)

    def get_all_customers(self):
        return self.customer_dao.get_all_customers()
