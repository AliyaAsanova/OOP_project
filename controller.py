from model import ReservationModel

class ReservationController:
    def __init__(self):
        self.model = ReservationModel()

    def create_reservation(self, guest_name, room_number, check_in, check_out):
        self.model.insert_reservation(guest_name, room_number, check_in, check_out)

    def get_reservations(self):
        return self.model.get_all_reservations()
